"""Small bounded HTTP/signing transport; signed URLs never cross persistence boundaries."""

from __future__ import annotations

import json
from urllib.parse import urlencode, urlsplit
from urllib.request import HTTPRedirectHandler, Request, build_opener

from aquasentinel.config import OpticalConfig


class AssetAccessError(RuntimeError):
    """Sanitized transport failure, deliberately without provider URL diagnostics."""


def validate_asset_href(href: str, settings: OpticalConfig, *, signed: bool = False) -> None:
    try:
        parsed = urlsplit(href)
        valid = (
            isinstance(href, str)
            and not any(c.isspace() for c in href)
            and parsed.scheme == "https"
            and parsed.hostname in settings.allowed_asset_hosts
            and parsed.port in (None, 443)
            and parsed.username is None
            and parsed.password is None
            and not parsed.fragment
            and bool(parsed.path)
            and (signed or not parsed.query)
        )
    except (TypeError, ValueError, AttributeError):
        valid = False
    if not valid:
        raise AssetAccessError("Asset URL is not an allowed unsigned/signed HTTPS reference.")


class _SameHostRedirect(HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        try:
            old, new = urlsplit(req.full_url), urlsplit(newurl)
            valid = (
                isinstance(newurl, str)
                and not any(c.isspace() for c in newurl)
                and all(
                    parsed.scheme == "https"
                    and bool(parsed.hostname)
                    and parsed.port in (None, 443)
                    and parsed.username is None
                    and parsed.password is None
                    and not parsed.fragment
                    for parsed in (old, new)
                )
                and new.hostname == old.hostname
            )
        except (TypeError, ValueError, AttributeError):
            valid = False
        if not valid:
            raise AssetAccessError("Unsafe or cross-host HTTPS redirect refused.") from None
        return super().redirect_request(req, fp, code, msg, headers, newurl)


def read_bytes(url: str, *, timeout: float, max_bytes: int) -> bytes:
    """Bound response length and strip all raw/chained transport exception text."""
    try:
        request = Request(url, headers={"User-Agent": "AquaSentinel813/as102-v1"})
        with build_opener(_SameHostRedirect()).open(request, timeout=timeout) as response:
            body = response.read(max_bytes + 1)
        if len(body) > max_bytes:
            raise AssetAccessError("HTTP response exceeds the bounded metadata size.")
        return body
    except (OSError, ValueError, TypeError, KeyError, AssetAccessError):
        # HTTP library exceptions can contain SAS queries. Never propagate their strings.
        pass
    raise AssetAccessError(
        "Bounded HTTPS metadata request failed or exceeded size limit."
    ) from None


def sign_asset(href: str, settings: OpticalConfig) -> str:
    settings.validate()
    validate_asset_href(href, settings)
    url = settings.signing_endpoint + "?" + urlencode({"href": href})
    try:
        payload = json.loads(read_bytes(url, timeout=settings.timeout_seconds, max_bytes=16384))
        signed = payload["href"]
        validate_asset_href(signed, settings, signed=True)
        original, returned = urlsplit(href), urlsplit(signed)
        if (original.scheme, original.hostname, original.port or 443, original.path) != (
            returned.scheme,
            returned.hostname,
            returned.port or 443,
            returned.path,
        ) or not returned.query:
            raise ValueError
        return signed
    except (OSError, ValueError, TypeError, KeyError, AssetAccessError):
        pass
    raise AssetAccessError("Signing response is invalid or unavailable.") from None
