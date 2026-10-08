import json
from dataclasses import replace
from urllib.parse import parse_qs, urlsplit

import pytest

from aquasentinel.config import OpticalConfig
from aquasentinel.ingestion import planetary_computer as pc
from aquasentinel.preprocessing.cache import cache_identity, canonical_json
from aquasentinel.provenance.serialization import source_record_to_dict

HREF = "https://sentinel2l2a01.blob.core.windows.net/test/B02.tif"
# Synthetic SAS fields only; these are not usable credentials.
SAS_QUERY = "sv=2023-11-03&se=2030-01-01T00%3A00%3A00Z&sp=r&sig=fake%2Bsignature%2Fonly%3D"
SIGNED_HREF = HREF + "?" + SAS_QUERY


def test_transient_signing_response(monkeypatch):
    calls = []

    def response(url, **kwargs):
        calls.append(url)
        return json.dumps({"href": HREF + "?temporary=fake-only"}).encode()

    monkeypatch.setattr(pc, "read_bytes", response)
    signed = pc.sign_asset(HREF, OpticalConfig())
    assert signed.endswith("?temporary=fake-only")
    assert calls[0].startswith(OpticalConfig().signing_endpoint + "?href=")
    assert parse_qs(urlsplit(calls[0]).query) == {"href": [HREF]}
    for value in (signed, signed.replace("https://", "HTTPS://")):
        with pytest.raises(ValueError, match="stable"):
            canonical_json({"asset": value})
    assert b"temporary" not in canonical_json({"asset": HREF})


@pytest.mark.parametrize(
    "payload",
    [
        b"no-json",
        b"{}",
        b'{"href":null}',
        json.dumps({"href": HREF}).encode(),
        json.dumps({"href": "https://other.test/B02.tif?temporary=fake-only"}).encode(),
        json.dumps({"href": HREF.replace("B02", "B03") + "?temporary=fake-only"}).encode(),
    ],
)
def test_malformed_signing_response_sanitized(monkeypatch, payload):
    monkeypatch.setattr(pc, "read_bytes", lambda *a, **k: payload)
    with pytest.raises(pc.AssetAccessError) as error:
        pc.sign_asset(HREF, OpticalConfig())
    assert "fake-only" not in str(error.value)
    assert error.value.__suppress_context__
    assert error.value.__context__ is None


def test_http_failure_sanitized(monkeypatch):
    def failed(*args, **kwargs):
        raise OSError(HREF + "?temporary=do-not-leak")

    monkeypatch.setattr(pc, "build_opener", failed)
    with pytest.raises(pc.AssetAccessError) as error:
        pc.read_bytes(HREF + "?temporary=do-not-leak", timeout=1, max_bytes=10)
    assert "do-not-leak" not in str(error.value)
    assert error.value.__suppress_context__
    assert error.value.__context__ is None


def test_response_bounded(monkeypatch):
    class Response:
        def __enter__(self):
            return self

        def __exit__(self, *args):
            pass

        def read(self, count):
            assert count == 11
            return b"X" * 11

    class Opener:
        def open(self, *args, **kwargs):
            return Response()

    monkeypatch.setattr(pc, "build_opener", lambda *a: Opener())
    with pytest.raises(pc.AssetAccessError):
        pc.read_bytes(HREF, timeout=1, max_bytes=10)


def test_cross_host_redirect_refused():
    request = pc.Request(HREF + "?temporary=fake-only")
    with pytest.raises(pc.AssetAccessError):
        pc._SameHostRedirect().redirect_request(request, None, 302, "", {}, "https://other.test/x")


@pytest.mark.parametrize(
    "destination",
    [
        HREF.replace("https://", "http://"),
        HREF.replace(".net/", ".net:80/"),
        HREF.replace(".net/", ".net:444/"),
    ],
    ids=["same-host-http-downgrade", "port-80", "port-444"],
)
def test_insecure_same_host_redirect_refused(destination):
    request = pc.Request(SIGNED_HREF)
    with pytest.raises(pc.AssetAccessError) as error:
        pc._SameHostRedirect().redirect_request(
            request, None, 302, "", {}, destination + "?" + SAS_QUERY
        )
    for key, value in parse_qs(SAS_QUERY).items():
        assert key + "=" + value[0] not in str(error.value)
        if key != "sp":
            assert value[0] not in str(error.value)


@pytest.mark.parametrize("original_explicit_port", [False, True])
@pytest.mark.parametrize("destination_explicit_port", [False, True])
def test_redirect_accepts_normal_https_port_semantics(
    original_explicit_port, destination_explicit_port
):
    original = HREF.replace(".net/", ".net:443/") if original_explicit_port else HREF
    destination = HREF.replace(".net/", ".net:443/") if destination_explicit_port else HREF
    redirected = pc._SameHostRedirect().redirect_request(
        pc.Request(original), None, 302, "", {}, destination
    )
    assert redirected.full_url == destination


@pytest.mark.parametrize(
    "returned",
    [
        SIGNED_HREF.replace("https://", "http://"),
        SIGNED_HREF.replace("https://", "https://fake-user@"),
        SIGNED_HREF.replace("https://", "https://fake-user:fake-password@"),
    ],
    ids=["http", "username", "username-password"],
)
def test_signing_rejects_insecure_returned_url_without_leaking_sas(monkeypatch, returned):
    monkeypatch.setattr(pc, "read_bytes", lambda *a, **k: json.dumps({"href": returned}).encode())
    with pytest.raises(pc.AssetAccessError) as error:
        pc.sign_asset(HREF, OpticalConfig())
    assert str(error.value) == "Signing response is invalid or unavailable."
    assert error.value.__context__ is None
    for key, value in parse_qs(SAS_QUERY).items():
        assert key + "=" + value[0] not in str(error.value)
        if key != "sp":
            assert value[0] not in str(error.value)
    assert "fake-password" not in str(error.value)


def test_signing_query_round_trips_encoded_unsigned_href(monkeypatch):
    # Encoded blob path components must not be decoded or double-decoded by signing.
    original = HREF.replace("/test/", "/test%20folder/a%2Bb%26c%23d%25/")

    def response(url, **kwargs):
        assert parse_qs(urlsplit(url).query) == {"href": [original]}
        return json.dumps({"href": original + "?" + SAS_QUERY}).encode()

    monkeypatch.setattr(pc, "read_bytes", response)
    assert pc.sign_asset(original, OpticalConfig()) == original + "?" + SAS_QUERY


def test_realistic_sas_rejected_at_stable_metadata_boundaries(resolved):
    payloads = [
        {"asset": SIGNED_HREF},
        {"nested": [{"href": SIGNED_HREF}]},
        source_record_to_dict(replace(resolved.source, source_url=SIGNED_HREF)),
    ]
    for payload in payloads:
        for helper in (canonical_json, cache_identity):
            with pytest.raises(ValueError, match="stable") as error:
                helper(payload)
            for key, value in parse_qs(SAS_QUERY).items():
                assert key + "=" + value[0] not in str(error.value)
                if key != "sp":
                    assert value[0] not in str(error.value)


def test_http_sas_failure_sanitized_without_exception_chain(monkeypatch):
    def failed(*args, **kwargs):
        raise OSError(SIGNED_HREF)

    monkeypatch.setattr(pc, "build_opener", failed)
    with pytest.raises(pc.AssetAccessError) as error:
        pc.read_bytes(SIGNED_HREF, timeout=1, max_bytes=10)
    assert error.value.__context__ is None
    assert error.value.__cause__ is None
    for key, value in parse_qs(SAS_QUERY).items():
        assert key + "=" + value[0] not in str(error.value)
        if key != "sp":
            assert value[0] not in str(error.value)
    assert SAS_QUERY not in str(error.value)


@pytest.mark.parametrize("original_explicit_port", [False, True])
@pytest.mark.parametrize("returned_explicit_port", [False, True])
def test_signing_accepts_canonical_https_identity(
    monkeypatch, original_explicit_port, returned_explicit_port
):
    original = HREF.replace(".net/", ".net:443/") if original_explicit_port else HREF
    returned = HREF.replace(".net/", ".net:443/") if returned_explicit_port else HREF
    # Host case is immaterial, while the asset path is compared exactly.
    returned = returned.replace("sentinel2l2a01", "SENTINEL2L2A01") + "?" + SAS_QUERY
    monkeypatch.setattr(pc, "read_bytes", lambda *a, **k: json.dumps({"href": returned}).encode())
    assert pc.sign_asset(original, OpticalConfig()) == returned


@pytest.mark.parametrize(
    "destination",
    [
        SIGNED_HREF.replace("https://", "https://fake-user@"),
        SIGNED_HREF.replace("https://", "https://fake-user:fake-password@"),
        SIGNED_HREF + "#fake-fragment",
        SIGNED_HREF.replace(".net/", ".net:not-a-port/"),
        SIGNED_HREF.replace(".net/", ".net:65536/"),
        "https://[malformed/?" + SAS_QUERY,
        SIGNED_HREF.replace("/test/", "/test folder/"),
        None,
    ],
    ids=["userinfo", "password", "fragment", "invalid-port", "port-range",
         "malformed-ipv6", "whitespace", "non-string"],
)
def test_redirect_rejects_unsafe_or_malformed_url_safely(destination):
    with pytest.raises(pc.AssetAccessError) as error:
        pc._SameHostRedirect().redirect_request(
            pc.Request(SIGNED_HREF), None, 302, "", {}, destination
        )
    assert str(error.value) == "Unsafe or cross-host HTTPS redirect refused."
    assert error.value.__context__ is None
    assert error.value.__cause__ is None
    assert "fake" not in str(error.value)
