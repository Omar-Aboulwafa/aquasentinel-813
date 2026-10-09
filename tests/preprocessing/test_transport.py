import errno
import inspect
import json
import socket
from dataclasses import replace
from datetime import UTC, datetime, timedelta
from urllib.error import HTTPError, URLError
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
NOW = datetime(2026, 10, 9, tzinfo=UTC)


def token_body(*, material=SAS_QUERY, expiry=None):
    return json.dumps({
        "token": material,
        "msft:expiry": expiry or (NOW + timedelta(hours=1)).isoformat(),
    }).encode()


@pytest.fixture(autouse=True)
def isolated_token_cache(monkeypatch):
    pc._TOKEN_CACHE.clear()
    monkeypatch.setattr(pc, "_utc_now", lambda: NOW)
    monkeypatch.setattr(pc, "sleep", lambda delay: pytest.fail("Unexpected retry sleep"))
    yield
    pc._TOKEN_CACHE.clear()


def fake_token(monkeypatch):
    monkeypatch.setattr(pc, "_request_token", lambda *a: token_body())


def assert_sanitized(error):
    assert error.__context__ is None
    assert error.__cause__ is None
    assert error.__suppress_context__
    assert SAS_QUERY not in str(error)
    assert SIGNED_HREF not in str(error)
    assert "fake" not in str(error)


def test_transient_signing_response(monkeypatch):
    calls = []

    def response(url, settings):
        calls.append(url)
        return token_body()

    monkeypatch.setattr(pc, "_request_token", response)
    signed = pc.sign_asset(HREF, OpticalConfig())
    assert signed == SIGNED_HREF
    assert calls == [
        "https://planetarycomputer.microsoft.com/api/sas/v1/token/sentinel2l2a01/test"
    ]
    assert not urlsplit(calls[0]).query
    for value in (signed, signed.replace("https://", "HTTPS://")):
        with pytest.raises(ValueError, match="stable"):
            canonical_json({"asset": value})
    assert b"sig=" not in canonical_json({"asset": HREF})


@pytest.mark.parametrize(
    "payload",
    [
        b"no-json",
        b"{}",
        b'{"token":null}',
        b'[]',
        b"[" * 1100 + b"]" * 1100,
        token_body(material=""),
        token_body(expiry="not-a-date"),
    ],
)
def test_malformed_signing_response_sanitized(monkeypatch, payload):
    calls = []
    monkeypatch.setattr(pc, "_request_token", lambda *a: calls.append(a) or payload)
    with pytest.raises(pc.AssetAccessError) as error:
        pc.sign_asset(HREF, OpticalConfig())
    assert "fake-only" not in str(error.value)
    assert error.value.__suppress_context__
    assert error.value.__context__ is None
    assert len(calls) == 1
    assert not pc._TOKEN_CACHE


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
    fake_token(monkeypatch)
    monkeypatch.setattr(pc, "_signed_href", lambda *a: returned)
    with pytest.raises(pc.AssetAccessError) as error:
        pc.sign_asset(HREF, OpticalConfig())
    assert str(error.value) == "Signing response is invalid or unavailable."
    assert error.value.__context__ is None
    for key, value in parse_qs(SAS_QUERY).items():
        assert key + "=" + value[0] not in str(error.value)
        if key != "sp":
            assert value[0] not in str(error.value)
    assert "fake-password" not in str(error.value)


def test_signing_preserves_encoded_unsigned_blob_path(monkeypatch):
    # Encoded blob path components must not be decoded or double-decoded by signing.
    original = HREF.replace("/test/", "/test/test%20folder/a%2Bb%26c%23d%25/")

    def response(url, settings):
        assert url.endswith("/token/sentinel2l2a01/test")
        assert not urlsplit(url).query
        return token_body()

    monkeypatch.setattr(pc, "_request_token", response)
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
    fake_token(monkeypatch)
    monkeypatch.setattr(pc, "_signed_href", lambda *a: returned)
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


def test_eleven_assets_and_second_scene_reuse_one_token(monkeypatch):
    calls = []
    monkeypatch.setattr(pc, "_request_token", lambda *a: calls.append(a) or token_body())
    settings = OpticalConfig()
    keys = ("B02", "B03", "B04", "B05", "B06", "B07", "B08", "B8A", "B11",
            "SCL", "product-metadata")
    for scene in ("scene-one", "scene-two"):
        for key in keys:
            original = HREF.replace("B02.tif", f"{scene}/{key}.tif")
            assert pc.sign_asset(original, settings) == original + "?" + SAS_QUERY
    assert len(calls) == 1
    assert len(pc._TOKEN_CACHE) == 1


@pytest.mark.parametrize("scope", ["account", "container", "issuer", "issuer-port"])
def test_distinct_scope_never_reuses_token(monkeypatch, scope):
    calls = []
    monkeypatch.setattr(pc, "_request_token", lambda *a: calls.append(a) or token_body())
    settings = OpticalConfig()
    pc.sign_asset(HREF, settings)
    if scope == "account":
        second = HREF.replace("sentinel2l2a01", "sentinel2l2a02")
        settings = replace(settings, allowed_asset_hosts=(urlsplit(second).hostname,))
    elif scope == "container":
        second = HREF.replace("/test/", "/another/")
    else:
        second = HREF
        issuer = ("https://another.test" if scope == "issuer" else
                  "https://planetarycomputer.microsoft.com:444")
        settings = replace(settings, signing_endpoint=issuer + "/api/sas/v1/sign")
    pc.sign_asset(second, settings)
    assert len(calls) == len(pc._TOKEN_CACHE) == 2
    assert calls[0][0] != calls[1][0]


def test_canonical_issuer_and_asset_host_share_scope(monkeypatch):
    calls = []
    monkeypatch.setattr(pc, "_request_token", lambda *a: calls.append(a) or token_body())
    pc.sign_asset(HREF, OpticalConfig())
    settings = replace(OpticalConfig(), signing_endpoint=(
        "https://PLANETARYCOMPUTER.MICROSOFT.COM:443/api/sas/v1/sign/"
    ))
    original = HREF.replace("sentinel2l2a01", "SENTINEL2L2A01").replace(".net/", ".net:443/")
    assert pc.sign_asset(original, settings) == original + "?" + SAS_QUERY
    assert len(calls) == 1


@pytest.mark.parametrize("remaining", [61, 60, 59, 0, -1])
def test_cached_token_refresh_boundary(monkeypatch, remaining):
    calls = []
    settings = OpticalConfig()
    key = pc._token_url(HREF, settings)
    pc._TOKEN_CACHE[key] = pc._SASToken(
        "sig=old-fake", NOW + timedelta(seconds=remaining)
    )
    monkeypatch.setattr(pc, "_request_token", lambda *a: calls.append(a) or token_body())
    signed = pc.sign_asset(HREF, settings)
    if remaining > 60:
        assert signed == HREF + "?sig=old-fake"
        assert not calls
    else:
        assert signed == SIGNED_HREF
        assert len(calls) == 1


@pytest.mark.parametrize("remaining", [60, 59, 0, -1])
def test_new_near_expiry_token_never_returned_or_cached(monkeypatch, remaining):
    calls = []
    body = token_body(expiry=(NOW + timedelta(seconds=remaining)).isoformat())
    monkeypatch.setattr(pc, "_request_token", lambda *a: calls.append(a) or body)
    with pytest.raises(pc.AssetAccessError) as error:
        pc.sign_asset(HREF, OpticalConfig())
    assert_sanitized(error.value)
    assert len(calls) == 1
    assert not pc._TOKEN_CACHE


@pytest.mark.parametrize("payload", [
    {"msft:expiry": "2030-01-01T00:00:00Z"},
    {"token": SAS_QUERY},
    {"token": SAS_QUERY, "msft:expiry": None},
    {"token": SAS_QUERY, "msft:expiry": "2030-01-01T00:00:00"},
    {"token": SAS_QUERY, "msft:expiry": True},
    {"token": True, "msft:expiry": "2030-01-01T00:00:00Z"},
])
def test_incomplete_token_response_rejected_once(monkeypatch, payload):
    calls = []
    monkeypatch.setattr(pc, "_request_token",
                        lambda *a: calls.append(a) or json.dumps(payload).encode())
    with pytest.raises(pc.AssetAccessError) as error:
        pc.sign_asset(HREF, OpticalConfig())
    assert_sanitized(error.value)
    assert len(calls) == 1
    assert not pc._TOKEN_CACHE


@pytest.mark.parametrize("material", [
    "", "?" + SAS_QUERY, SAS_QUERY + "#fragment", SAS_QUERY + " ",
    SAS_QUERY + "\n", "sig=", "sig=fake&sig=other", "sv=only",
    "sig=fake%ZZ", "sig=fake%0Asecret", "sig=fake&broken", "sig=fake&=empty-key",
    "https://other.test/?sig=fake", SAS_QUERY + "&sp=", "sig=fake\x00secret",
])
def test_unsafe_token_material_never_cached_or_retried(monkeypatch, material):
    calls = []
    monkeypatch.setattr(pc, "_request_token",
                        lambda *a: calls.append(a) or token_body(material=material))
    with pytest.raises(pc.AssetAccessError) as error:
        pc.sign_asset(HREF, OpticalConfig())
    assert_sanitized(error.value)
    assert len(calls) == 1
    assert not pc._TOKEN_CACHE


def test_read_and_list_permission_is_not_invented_as_invalid(monkeypatch):
    # Actual provider SAS can include read/list; do not impose sp == 'r'.
    material = SAS_QUERY.replace("sp=r", "sp=rl")
    monkeypatch.setattr(pc, "_request_token", lambda *a: token_body(material=material))
    assert pc.sign_asset(HREF, OpticalConfig()) == HREF + "?" + material


@pytest.mark.parametrize("status", [429, 500, 502, 503, 504])
def test_retryable_status_then_success_is_cached_once(monkeypatch, status):
    calls, delays = [], []

    def request(url, settings):
        calls.append(url)
        if len(calls) == 1:
            raise HTTPError(SIGNED_HREF, status, SAS_QUERY, {}, None)
        return token_body()

    monkeypatch.setattr(pc, "_request_token", request)
    monkeypatch.setattr(pc, "sleep", delays.append)
    assert pc.sign_asset(HREF, OpticalConfig()) == SIGNED_HREF
    pc.sign_asset(HREF.replace("B02", "B03"), OpticalConfig())
    assert len(calls) == 2
    assert delays == [0.8]
    assert len(pc._TOKEN_CACHE) == 1


@pytest.mark.parametrize("status", [429, 500, 502, 503, 504])
def test_five_retryable_failures_bounded_sanitized(monkeypatch, status):
    calls, delays = [], []

    def request(*args):
        calls.append(args)
        raise HTTPError(SIGNED_HREF, status, SAS_QUERY, {}, None)

    monkeypatch.setattr(pc, "_request_token", request)
    monkeypatch.setattr(pc, "sleep", delays.append)
    with pytest.raises(pc.AssetAccessError) as error:
        pc.sign_asset(HREF, OpticalConfig())
    assert_sanitized(error.value)
    assert len(calls) == 5
    assert delays == [0.8, 1.6, 3.2, 6.4]
    assert not pc._TOKEN_CACHE


@pytest.mark.parametrize("status", [400, 401, 403, 404, 408, 501])
def test_terminal_http_failure_never_retried(monkeypatch, status):
    calls = []

    def request(*args):
        calls.append(args)
        raise HTTPError(SIGNED_HREF, status, SAS_QUERY, {}, None)

    monkeypatch.setattr(pc, "_request_token", request)
    with pytest.raises(pc.AssetAccessError) as error:
        pc.sign_asset(HREF, OpticalConfig())
    assert_sanitized(error.value)
    assert len(calls) == 1
    assert not pc._TOKEN_CACHE


@pytest.mark.parametrize("failure", [
    TimeoutError(SIGNED_HREF), ConnectionResetError(SIGNED_HREF),
    URLError(TimeoutError(SIGNED_HREF)), URLError(ConnectionRefusedError(SIGNED_HREF)),
    URLError(socket.gaierror(socket.EAI_AGAIN, SIGNED_HREF)),
    OSError(errno.ECONNRESET, SIGNED_HREF),
])
def test_typed_transient_failures_have_bounded_retries(monkeypatch, failure):
    calls, delays = [], []

    def request(*args):
        calls.append(args)
        raise failure

    monkeypatch.setattr(pc, "_request_token", request)
    monkeypatch.setattr(pc, "sleep", delays.append)
    with pytest.raises(pc.AssetAccessError) as error:
        pc.sign_asset(HREF, OpticalConfig())
    assert_sanitized(error.value)
    assert len(calls) == 5
    assert delays == [0.8, 1.6, 3.2, 6.4]


@pytest.mark.parametrize("failure", [
    URLError(SIGNED_HREF), URLError(socket.gaierror(socket.EAI_NONAME, SIGNED_HREF)),
    OSError(SIGNED_HREF), TypeError(SIGNED_HREF), ValueError(SIGNED_HREF),
    KeyError(SIGNED_HREF), pc.AssetAccessError(SIGNED_HREF),
])
def test_unclassified_permanent_or_programming_failures_not_retried(monkeypatch, failure):
    calls = []

    def request(*args):
        calls.append(args)
        raise failure

    monkeypatch.setattr(pc, "_request_token", request)
    with pytest.raises(pc.AssetAccessError) as error:
        pc.sign_asset(HREF, OpticalConfig())
    assert_sanitized(error.value)
    assert len(calls) == 1


def test_success_on_last_attempt_has_no_final_sleep(monkeypatch):
    calls, delays = [], []

    def request(*args):
        calls.append(args)
        if len(calls) < 5:
            raise TimeoutError(SIGNED_HREF)
        return token_body()

    monkeypatch.setattr(pc, "_request_token", request)
    monkeypatch.setattr(pc, "sleep", delays.append)
    assert pc.sign_asset(HREF, OpticalConfig()) == SIGNED_HREF
    assert len(calls) == 5
    assert delays == [0.8, 1.6, 3.2, 6.4]
    assert len(pc._TOKEN_CACHE) == 1


@pytest.mark.parametrize("href", [
    SIGNED_HREF, HREF + "?", HREF + "#",
    HREF.replace("https://", "http://"), HREF + "#fragment",
    HREF.replace("https://", "https://user@"),
    HREF.replace("https://", "https://user:password@"),
    HREF.replace(".net/", ".net:444/"), HREF.replace(".net/", ".net:bad/"),
    HREF.replace("/test/", "/test folder/"), "https://other.test/test/x",
    "https://[malformed/test/x", None,
])
def test_unsigned_validation_precedes_token_request(monkeypatch, href):
    monkeypatch.setattr(pc, "_request_token", lambda *a: pytest.fail("Must not acquire"))
    with pytest.raises(pc.AssetAccessError) as error:
        pc.sign_asset(href, OpticalConfig())
    assert_sanitized(error.value)


@pytest.mark.parametrize("path", [
    "/", "/test", "//test/x", "/test%2Fother/x", "/test%20folder/x",
    "/a/x", "/bad--container/x", "/-bad/x", "/bad-/x", "/test/",
])
def test_unsafe_container_scope_fails_without_acquisition(monkeypatch, path):
    monkeypatch.setattr(pc, "_request_token", lambda *a: pytest.fail("Must not acquire"))
    href = "https://sentinel2l2a01.blob.core.windows.net" + path
    with pytest.raises(pc.AssetAccessError) as error:
        pc.sign_asset(href, OpticalConfig())
    assert_sanitized(error.value)


@pytest.mark.parametrize("endpoint", [
    "https://planetarycomputer.microsoft.com/other/sign",
    "https://planetarycomputer.microsoft.com/api/sas/v1/sign?query=bad",
    "https://planetarycomputer.microsoft.com/api/sas/v1/sign#fragment",
    "https://user@planetarycomputer.microsoft.com/api/sas/v1/sign",
    "http://planetarycomputer.microsoft.com/api/sas/v1/sign",
    "https://planetarycomputer.microsoft.com:bad/api/sas/v1/sign",
])
def test_unmappable_issuer_fails_before_acquisition(monkeypatch, endpoint):
    monkeypatch.setattr(pc, "_request_token", lambda *a: pytest.fail("Must not acquire"))
    with pytest.raises(pc.AssetAccessError) as error:
        pc.sign_asset(HREF, replace(OpticalConfig(), signing_endpoint=endpoint))
    assert_sanitized(error.value)


def test_allowlisted_non_azure_host_does_not_get_guessed_scope(monkeypatch):
    monkeypatch.setattr(pc, "_request_token", lambda *a: pytest.fail("Must not acquire"))
    with pytest.raises(pc.AssetAccessError):
        pc.sign_asset("https://other.test/test/B02.tif",
                      replace(OpticalConfig(), allowed_asset_hosts=("other.test",)))


@pytest.mark.parametrize("returned", [
    SIGNED_HREF.replace("sentinel2l2a01", "otheraccount"),
    SIGNED_HREF.replace("B02", "B03"), SIGNED_HREF + "#fragment",
    SIGNED_HREF.replace(".net/", ".net:444/"),
    SIGNED_HREF.replace(".net/", ".net:bad/"),
    SIGNED_HREF.replace("/test/", "/test folder/"), HREF,
    "https://[bad/test/x?" + SAS_QUERY, None,
])
def test_final_signed_resource_validation_is_preserved(monkeypatch, returned):
    fake_token(monkeypatch)
    monkeypatch.setattr(pc, "_signed_href", lambda *a: returned)
    with pytest.raises(pc.AssetAccessError) as error:
        pc.sign_asset(HREF, OpticalConfig())
    assert_sanitized(error.value)


@pytest.mark.parametrize("size", [16384, 16385])
def test_token_request_bounded_timeout_and_no_subscription_key(monkeypatch, size):
    class Response:
        def __enter__(self):
            return self

        def __exit__(self, *args):
            pass

        def read(self, count):
            assert count == 16385
            return b"X" * size

    class Opener:
        def open(self, request, timeout):
            assert timeout == 1.25
            assert request.get_method() == "GET"
            assert not urlsplit(request.full_url).query
            assert set(dict(request.header_items())) == {"User-agent"}
            return Response()

    monkeypatch.setattr(pc, "build_opener", lambda handler: Opener())
    settings = replace(OpticalConfig(), timeout_seconds=1.25)
    key = pc._token_url(HREF, settings)
    if size == 16385:
        with pytest.raises(ValueError):
            pc._request_token(key, settings)
    else:
        assert len(pc._request_token(key, settings)) == size


def test_transport_token_does_not_change_stable_source_metadata(monkeypatch, resolved):
    before = canonical_json(source_record_to_dict(resolved.source))
    identity = cache_identity({"source": source_record_to_dict(resolved.source)})
    fake_token(monkeypatch)
    pc.sign_asset(HREF, OpticalConfig())
    key = pc._token_url(HREF, OpticalConfig())
    first = pc._TOKEN_CACHE[key]
    second = pc._SASToken("sig=another-fake", first.expires_at)
    assert first == second  # Credential content is excluded from equality/repr.
    assert "sig" not in repr(first)
    pc._TOKEN_CACHE[key] = second
    assert pc.sign_asset(HREF, OpticalConfig()) != SIGNED_HREF
    assert canonical_json(source_record_to_dict(resolved.source)) == before
    assert cache_identity({"source": source_record_to_dict(resolved.source)}) == identity
    signature = inspect.signature(pc.sign_asset)
    assert tuple(signature.parameters) == ("href", "settings")
    assert signature.parameters["href"].annotation == "str"
    assert signature.parameters["settings"].annotation == "OpticalConfig"
    assert signature.return_annotation == "str"
