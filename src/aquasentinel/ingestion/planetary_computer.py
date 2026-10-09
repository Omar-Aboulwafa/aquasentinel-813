"""Small bounded HTTP/signing transport; signed URLs never cross persistence boundaries."""

from __future__ import annotations

import errno
import json
import re
import socket
from dataclasses import dataclass, field
from datetime import UTC, datetime
from time import sleep
from urllib.error import HTTPError, URLError
from urllib.parse import parse_qs, quote, urlsplit, urlunsplit
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


@dataclass(frozen=True)
class _SASToken:
    material: str = field(repr=False, compare=False)
    expires_at: datetime


# Transport state only: never persisted or added to source/processing metadata.
_TOKEN_CACHE: dict[str, _SASToken] = {}
_REFRESH_MARGIN_SECONDS = 60
_MAX_TOKEN_ATTEMPTS = 5
_RETRYABLE_STATUSES = frozenset((429, 500, 502, 503, 504))
_TRANSIENT_ERRNOS = frozenset((
    errno.ECONNRESET, errno.ECONNABORTED, errno.ECONNREFUSED,
    errno.ETIMEDOUT, errno.ENETRESET, errno.ENETUNREACH, errno.EHOSTUNREACH,
))


def _utc_now() -> datetime:
    return datetime.now(UTC)


def _token_url(href: str, settings: OpticalConfig) -> str:
    """Derive one canonical credential-free issuer/account/container scope."""
    asset = urlsplit(href)  # Caller has already enforced the asset allowlist.
    # Even an empty delimiter would make appending query authorization ambiguous.
    if "?" in href or "#" in href:
        raise ValueError
    suffix = ".blob.core.windows.net"
    hostname = asset.hostname or ""
    if not hostname.endswith(suffix):
        raise ValueError
    account = hostname[:-len(suffix)]
    segments = asset.path.split("/")
    container = segments[1] if len(segments) > 2 else ""
    if (
        not re.fullmatch(r"[a-z0-9]{3,24}", account)
        or not re.fullmatch(r"[a-z0-9](?:[a-z0-9-]{1,61})[a-z0-9]", container)
        or "--" in container
        or not any(segments[2:])
    ):
        raise ValueError
    issuer = urlsplit(settings.signing_endpoint)
    if (
        issuer.scheme != "https"
        or not issuer.hostname
        or issuer.username is not None
        or issuer.password is not None
        or issuer.query
        or issuer.fragment
        or any(c.isspace() for c in settings.signing_endpoint)
        or issuer.path not in ("/api/sas/v1/sign", "/api/sas/v1/sign/")
    ):
        raise ValueError
    port = 443 if issuer.port is None else issuer.port
    if port == 0:
        raise ValueError
    authority = issuer.hostname if port == 443 else f"{issuer.hostname}:{port}"
    path = "/api/sas/v1/token/" + quote(account, safe="") + "/" + quote(container, safe="")
    return urlunsplit(("https", authority, path, "", ""))


def _request_token(url: str, settings: OpticalConfig) -> bytes:
    """One bounded acquisition; retain typed HTTP errors only inside this module."""
    request = Request(url, headers={"User-Agent": "AquaSentinel813/as102-v1"})
    with build_opener(_SameHostRedirect()).open(
        request, timeout=settings.timeout_seconds
    ) as response:
        body = response.read(16385)
    if len(body) > 16384:
        raise ValueError
    return body


def _parse_token(body: bytes) -> _SASToken:
    payload = json.loads(body)
    if not isinstance(payload, dict):
        raise TypeError
    material, expiry = payload.get("token"), payload.get("msft:expiry")
    if (
        not isinstance(material, str)
        or not material
        or any(ord(c) <= 32 or ord(c) >= 127 or c in "?#" for c in material)
        or re.search(r"%(?![0-9a-fA-F]{2})", material)
        or not isinstance(expiry, str)
    ):
        raise ValueError
    fields = parse_qs(material, keep_blank_values=True, strict_parsing=True)
    if (
        not fields.get("sig")
        or any(
            not key or len(values) != 1 or not values[0]
            or any(ord(c) < 32 or ord(c) == 127 for c in key + values[0])
            for key, values in fields.items()
        )
    ):
        raise ValueError
    expires_at = datetime.fromisoformat(expiry)
    if (
        expires_at.tzinfo is None
        or (expires_at - _utc_now()).total_seconds() <= _REFRESH_MARGIN_SECONDS
    ):
        raise ValueError
    return _SASToken(material, expires_at.astimezone(UTC))


def _is_transient(error: OSError) -> bool:
    reason = error.reason if isinstance(error, URLError) else error
    if isinstance(reason, socket.gaierror):
        return reason.errno == socket.EAI_AGAIN
    return isinstance(reason, (TimeoutError, ConnectionError)) or (
        isinstance(reason, OSError) and reason.errno in _TRANSIENT_ERRNOS
    )


def _acquire_token(url: str, settings: OpticalConfig) -> _SASToken:
    for attempt in range(_MAX_TOKEN_ATTEMPTS):
        retry = False
        try:
            return _parse_token(_request_token(url, settings))
        except HTTPError as error:
            retry = error.code in _RETRYABLE_STATUSES
        except OSError as error:
            retry = _is_transient(error)
        except (ValueError, TypeError, KeyError, AttributeError, RecursionError, AssetAccessError):
            pass
        if not retry or attempt == _MAX_TOKEN_ATTEMPTS - 1:
            break
        sleep(0.8 * 2 ** attempt)
    # Raise outside the handler: neither raw text nor a credential-bearing chain.
    raise AssetAccessError("Token acquisition is invalid or unavailable.") from None


def _get_token(url: str, settings: OpticalConfig) -> _SASToken:
    cached = _TOKEN_CACHE.get(url)
    if cached is not None and (
        cached.expires_at - _utc_now()
    ).total_seconds() > _REFRESH_MARGIN_SECONDS:
        return cached
    _TOKEN_CACHE.pop(url, None)
    token = _acquire_token(url, settings)
    _TOKEN_CACHE[url] = token
    return token


def _signed_href(href: str, token: _SASToken) -> str:
    return href + "?" + token.material


def sign_asset(href: str, settings: OpticalConfig) -> str:
    """Stable unsigned HREF in, ephemeral signed HREF out; no caller API change."""
    try:
        settings.validate()
        validate_asset_href(href, settings)
        token = _get_token(_token_url(href, settings), settings)
        signed = _signed_href(href, token)
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
    except (OSError, ValueError, TypeError, KeyError, AttributeError, AssetAccessError):
        pass
    raise AssetAccessError("Signing response is invalid or unavailable.") from None
