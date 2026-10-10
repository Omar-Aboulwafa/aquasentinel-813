"""AS-201 offline/adversarial source contract; no provider or pixel access."""

import copy
import json
import struct
from dataclasses import replace
from datetime import UTC, datetime, timedelta
from hashlib import sha256

import pytest
from pystac_client import Client
from test_sentinel1 import _all_items, _item, _tiff_blob, _xml_bundle

from aquasentinel.catalog.stac import CatalogResult
from aquasentinel.config import SARConfig
from aquasentinel.ingestion import planetary_computer as pc
from aquasentinel.ingestion import sentinel1 as s1
from aquasentinel.ingestion import sentinel1_metadata as metadata
from aquasentinel.ingestion import sentinel1_policy as policy
from aquasentinel.ingestion import sentinel1_resolver as resolver
from aquasentinel.ingestion.sentinel1_coverage import canonical_geometry
from aquasentinel.provenance import ProvenanceRegistry


@pytest.fixture(autouse=True)
def no_network(monkeypatch):
    import socket

    monkeypatch.setattr(
        socket.socket, "connect", lambda *a: pytest.fail("External network forbidden")
    )


def retrieval():
    return s1.build_retrieval_set(_all_items("cdse"), _all_items("pc"), SARConfig())


def test_search_geometry_is_independent_plain_json_for_both_providers(monkeypatch):
    expected = {
        "type": "Polygon",
        "coordinates": [
            [[49.60, 28.60], [50.70, 28.60], [50.70, 29.60], [49.60, 29.60], [49.60, 28.60]]
        ],
    }
    original = json.dumps(policy.ENVELOPE_GEOMETRY, allow_nan=False)
    calls = []

    def assert_plain(value):
        assert not isinstance(value, (policy.FrozenJSON, tuple))
        if type(value) is dict:
            assert all(type(key) is str for key in value)
            for child in value.values():
                assert_plain(child)
        elif type(value) is list:
            for child in value:
                assert_plain(child)
        else:
            assert type(value) in (str, int, float, bool, type(None))

    def search(settings, **kwargs):
        geometry = kwargs["intersects"]
        assert type(geometry) is dict
        assert_plain(geometry)
        assert geometry == expected
        assert json.dumps(geometry, allow_nan=False) == original
        assert geometry is not policy.ENVELOPE_GEOMETRY
        assert kwargs["query"] is None
        assert "eo:cloud_cover" not in repr(kwargs)
        calls.append((settings.endpoint, geometry))
        return CatalogResult(items=(), license_name="fixture-license")

    monkeypatch.setattr(resolver, "search_catalog", search)
    settings = SARConfig()
    s1.search_sentinel1(settings)
    assert [endpoint for endpoint, _ in calls] == [
        settings.discovery_endpoint,
        settings.access_endpoint,
    ]
    for _, geometry in calls:
        geometry["coordinates"][0][0][0] = 0
        geometry["type"] = "Changed"
    assert json.dumps(policy.ENVELOPE_GEOMETRY, allow_nan=False) == original
    with pytest.raises(TypeError, match="AS-201 metadata is immutable"):
        policy.ENVELOPE_GEOMETRY["type"] = "Point"
    with pytest.raises(TypeError):
        policy.ENVELOPE_GEOMETRY["coordinates"][0][0][0] = 0


def test_search_geometry_real_client_construction_and_pagination_offline(stac_server):
    responses, calls = stac_server
    fixture_endpoint = next(iter(responses))
    root = responses[fixture_endpoint]
    collection = responses[fixture_endpoint + "collections/sentinel-2-l2a"]
    settings = SARConfig()
    for provider, endpoint in (
        ("cdse", settings.discovery_endpoint),
        ("pc", settings.access_endpoint),
    ):
        responses[endpoint] = json.loads(json.dumps(root).replace(fixture_endpoint, endpoint))
        responses[endpoint + "collections/sentinel-1-grd"] = {
            **collection,
            "id": "sentinel-1-grd",
        }
        items = _all_items(provider)
        for index in range(3):
            url = endpoint + ("search" if index == 0 else f"page{index}")
            responses[url] = {
                "type": "FeatureCollection",
                "features": list(items[index * 2 : (index + 1) * 2]),
                "links": (
                    [{
                        "rel": "next",
                        "href": endpoint + f"page{index + 1}",
                        "method": "POST",
                        "merge": True,
                        "body": {"cursor": str(index + 1)},
                    }]
                    if index < 2
                    else []
                ),
            }

    # Reproduce the exact library construction failure, with synthetic root metadata.
    client = Client.open(settings.discovery_endpoint)
    with pytest.raises(TypeError, match="AS-201 metadata is immutable"):
        client.search(intersects=policy.ENVELOPE_GEOMETRY)
    calls.clear()

    # Only the HTTP request layer is replaced: real Client.search/deepcopy and IO run.
    result = s1.search_sentinel1(settings)
    assert len(result.slices) == 6
    assert all(source.availability == "RESOLVED_NOT_ACCESSED" for source in result.slices)
    expected = json.loads(json.dumps(policy.ENVELOPE_GEOMETRY))
    for endpoint in (settings.discovery_endpoint, settings.access_endpoint):
        assert [href for href, _, _, _ in calls if href.startswith(endpoint)] == [
            endpoint,
            endpoint + "collections/sentinel-1-grd",
            endpoint + "search",
            endpoint + "page1",
            endpoint + "page2",
        ]
    parameters = [kwargs for _, _, kwargs, _ in calls if kwargs]
    assert len(parameters) == 6
    assert all(kwargs["intersects"] == expected for kwargs in parameters)
    assert all("query" not in kwargs and "eo:cloud_cover" not in repr(kwargs) for kwargs in parameters)


@pytest.mark.parametrize(
    "field,value",
    [
        ("start_datetime", "2026-04-24T14:42:05Z"),
        ("end_datetime", "2026-04-24T14:42:30Z"),
        ("start_datetime", "2026-04-24T14:42:05.150515"),
        ("platform", "sentinel-1b"),
        ("platform", None),
        ("sar:instrument_mode", "EW"),
        ("s1:product_type", "SLC"),
        ("sat:orbit_state", "descending"),
        ("sat:relative_orbit", 102),
        ("sat:relative_orbit", True),
        ("sat:absolute_orbit", 1),
        ("sar:polarizations", ["VV"]),
        ("sar:polarizations", ["VV", "VV"]),
        ("sar:polarizations", "VV/VH"),
        ("s1:product_identifier", "another-product"),
        ("sar:pixel_spacing_range", True),
        ("sar:pixel_spacing_azimuth", 20),
    ],
)
@pytest.mark.parametrize("provider", ["cdse", "pc"])
def test_source_contract_rejects_each_incompatible_field(provider, field, value):
    inputs = {p: list(_all_items(p)) for p in ("cdse", "pc")}
    inputs[provider][0]["properties"][field] = value
    result = s1.build_retrieval_set(tuple(inputs["cdse"]), tuple(inputs["pc"]), SARConfig())
    assert result.slices[0].availability == "UNAVAILABLE"
    assert len(result.slices) == 6 and not result.ready


def test_zero_and_multiple_PC_matches_preserve_slots_no_nearest_fallback():
    items = list(_all_items("pc"))
    absent = s1.build_retrieval_set(_all_items("cdse"), tuple(items[1:]), SARConfig())
    assert absent.slices[0].reason == "PC_SOURCE_MISSING"
    for duplicate in (copy.deepcopy(items[0]), {**copy.deepcopy(items[0]), "id": "another-id"}):
        ambiguous = s1.build_retrieval_set(_all_items("cdse"), (*items, duplicate), SARConfig())
        assert ambiguous.slices[0].reason == "PC_SOURCE_AMBIGUOUS"
        assert len(ambiguous.slices) == 6


def test_duplicate_discovery_is_unavailable():
    result = s1.build_retrieval_set(
        (*_all_items("cdse"), _item(s1.FROZEN_SOURCES[0], "cdse")), _all_items("pc"), SARConfig()
    )
    assert result.slices[0].reason == "DISCOVERY_SOURCE_AMBIGUOUS"


@pytest.mark.parametrize(
    "collection,properties,expected",
    [
        ("sentinel-1-grd", {}, "RAW_GRD_AMPLITUDE"),
        ("sentinel-1-rtc", {}, "RTC_GAMMA0"),
        ("sentinel-1-grd", {"s1:calibrated": True}, "PROVIDER_CALIBRATED_BACKSCATTER"),
        ("sentinel-1-grd", {"representation": "unknown"}, "UNKNOWN_REPRESENTATION"),
        ("other", {}, "UNKNOWN_REPRESENTATION"),
    ],
)
def test_representation_classification(collection, properties, expected):
    assert (
        resolver.classify_representation({"collection": collection, "properties": properties})
        == expected
    )


@pytest.mark.parametrize(
    "representation", ["RTC_GAMMA0", "PROVIDER_CALIBRATED_BACKSCATTER", "UNKNOWN_REPRESENTATION"]
)
def test_nonraw_product_cannot_enter_handoff(representation):
    items = list(_all_items("pc"))
    items[0]["properties"]["representation"] = representation
    assert (
        s1.build_retrieval_set(_all_items("cdse"), tuple(items), SARConfig()).slices[0].availability
        == "UNAVAILABLE"
    )


@pytest.mark.parametrize(
    "href",
    [
        "http://sentinel1euwest.blob.core.windows.net/s1-grd/x/measurement/vv.tiff",
        "https://evil.test/s1-grd/x/measurement/vv.tiff",
        "https://sentinel1euwest.blob.core.windows.net/s1-grd/x/measurement/vv.tiff?sv=1&se=2030&sp=r&sig=secret",
        "https://user:password@sentinel1euwest.blob.core.windows.net/s1-grd/x/measurement/vv.tiff",
        "https://sentinel1euwest.blob.core.windows.net:444/s1-grd/x/measurement/vv.tiff",
    ],
)
def test_unsafe_assets_are_sanitized_unavailable(href):
    items = list(_all_items("pc"))
    items[0]["assets"]["vv"]["href"] = href
    result = s1.build_retrieval_set(_all_items("cdse"), tuple(items), SARConfig())
    assert result.slices[0].availability == "UNAVAILABLE"
    serialized = json.dumps(result.to_dict())
    assert href not in serialized and "secret" not in serialized and "password" not in serialized


def test_no_assets_from_other_native_product_even_when_STAC_identity_matches():
    items = list(_all_items("pc"))
    items[0]["assets"]["vv"]["href"] = items[1]["assets"]["vv"]["href"]
    assert (
        s1.build_retrieval_set(_all_items("cdse"), tuple(items), SARConfig()).slices[0].availability
        == "UNAVAILABLE"
    )


def test_coverage_retains_gaps_and_common_intersection_not_bbox_union():
    items = list(_all_items("pc"))
    for i, item in enumerate(items):
        west, east = (49.60, 50.10) if i < 2 else (49.90, 50.40)
        item["geometry"] = {
            "type": "Polygon",
            "coordinates": [
                [[west, 28.60], [east, 28.60], [east, 29.60], [west, 29.60], [west, 28.60]]
            ],
        }
        item["bbox"] = [west, 28.60, east, 29.60]
    result = s1.build_retrieval_set(_all_items("cdse"), tuple(items), SARConfig())
    common = result.common_support_metadata["source_support"]
    points = [p for part in common["coordinates"] for ring in part for p in ring]
    assert min(p[0] for p in points) == 49.9 and max(p[0] for p in points) == 50.1
    assert result.common_support_metadata["coverage_gaps"]["coordinates"]
    assert all(
        g.coverage_metadata["support_semantics"].startswith("METADATA") for g in result.groups
    )
    assert all(g.missingness for g in result.groups)  # resolved is not yet access-validated
    assert result.envelope_bbox == (49.60, 28.60, 50.70, 29.60)


def test_all_missing_retains_three_groups_and_six_slots_no_fabricated_sources():
    result = s1.build_retrieval_set((), (), SARConfig())
    result.validate()
    assert len(result.groups) == 3 and len(result.slices) == 6
    assert result.provenance is None and result.common_support_metadata["is_lower_bound"]
    assert result.common_support_metadata["source_support"]["coordinates"] == ()


def test_groups_and_retrieval_are_deeply_immutable_no_input_aliases():
    inputs = list(_all_items("pc"))
    result = s1.build_retrieval_set(_all_items("cdse"), tuple(inputs), SARConfig())
    previous = result.fingerprint
    inputs[0]["geometry"]["coordinates"][0][0][0] = 0
    inputs[0]["properties"]["proj:shape"] = [1, 2]
    assert result.fingerprint == previous
    for action in (
        lambda: result.envelope_geometry.__setitem__("type", "Point"),
        lambda: result.groups[0].coverage_metadata.clear(),
        lambda: result.slices[0].provider_metadata.update({"x": 1}),
        lambda: result.provenance.parameters.pop("decision"),
    ):
        with pytest.raises(TypeError):
            action()
    with pytest.raises(TypeError):
        result.slices[0].footprint["coordinates"][0][0][0][0] = 0


def test_slice_group_set_identity_determinism_and_creation_time_exclusion():
    a = retrieval()
    b = s1.build_retrieval_set(
        tuple(reversed(_all_items("cdse"))), tuple(reversed(_all_items("pc"))), SARConfig()
    )
    assert a.fingerprint == b.fingerprint
    assert [g.fingerprint for g in a.groups] == [g.fingerprint for g in b.groups]
    later = policy.assemble_retrieval(
        a.slices, created_at=a.provenance.created_at + timedelta(days=1)
    )
    assert (
        later.product_id == a.product_id and later.processing_parameters == a.processing_parameters
    )
    independently = sha256(policy._stable_json(a.processing_parameters)).hexdigest()
    assert independently == a.fingerprint


def test_derived_registry_references_distinct_CDSE_and_PC_sources():
    result = retrieval()
    registry = ProvenanceRegistry()
    result.register(registry)
    assert len(registry.sources) == 12
    assert result.provenance.product_type == "sentinel1_retrieval"
    assert result.provenance.processing_version == "as201-v1"
    expected = tuple(r.source_id for s in result.slices for r in (s.discovery_source, s.source))
    assert result.provenance.source_ids == expected
    assert registry.get_lineage(result.product_id) == (*expected, result.product_id)
    result.register(registry)  # same instance registration is idempotent
    assert result.provenance.parameters == result.processing_parameters


@pytest.mark.parametrize(
    "change", ["fingerprint", "source_ids", "parameters", "processing_version"]
)
def test_retrieval_provenance_tampering_is_rejected(change):
    result = retrieval()
    if change == "fingerprint":
        changed = replace(result, fingerprint="0" * 64)
    else:
        value = {
            "source_ids": (result.slices[0].source.source_id,),
            "parameters": {},
            "processing_version": "bad",
        }[change]
        changed = replace(result, provenance=replace(result.provenance, **{change: value}))
    with pytest.raises(s1.Sentinel1RetrievalError):
        changed.validate()


@pytest.mark.parametrize(
    "value",
    [
        {
            "href": "https://sentinel1euwest.blob.core.windows.net/s1-grd/x?sv=1&se=2030&sp=r&sig=synthetic"
        },
        {"token": "synthetic"},
        {"Authorization": "Bearer synthetic"},
        {"note": "sv=2023&se=2030&sp=r&sig=synthetic"},
        {"x": float("nan")},
        {"x": float("inf")},
    ],
)
def test_stable_cache_serialization_rejects_SAS_and_nonfinite(value):
    with pytest.raises(s1.Sentinel1RetrievalError):
        policy._stable_json(value)


def header(policy_source):
    blob = _tiff_blob(policy_source)
    return s1.read_tiff_header(
        "synthetic",
        policy_source,
        timeout=1,
        range_reader=lambda url, timeout, start, end: blob[start : end + 1],
    )


@pytest.mark.parametrize(
    "index,old,new",
    [
        (0, b"<number>A</number>", b"<number>B</number>"),
        (0, b"<relativeOrbitNumber>101", b"<relativeOrbitNumber>102"),
        (1, b"<product>", b"<rfi>"),
        (1, b"<numberOfSamples>", b"<invalidSamples>"),
        (1, b"<incidenceAngle>35", b"<incidenceAngle>NaN"),
        (2, b"<sigmaNought>1 2", b"<sigmaNought>1"),
        (2, b"<betaNought>1 2", b"<betaNought>NaN 2"),
        (2, b"<polarisation>VV", b"<polarisation>VH"),
        (3, b'<noiseRangeVectorList count="1">', b'<noiseRangeVectorList count="0">'),
        (3, b"<noiseAzimuthLut>0 1", b"<noiseAzimuthLut>0"),
    ],
)
def test_required_XML_role_identity_and_structure_tampering_fails(index, old, new):
    source = s1.FROZEN_SOURCES[0]
    bundle = list(_xml_bundle(source))
    bundle[index] = bundle[index].replace(old, new)
    with pytest.raises(s1.Sentinel1MetadataError):
        s1.validate_metadata_xml(
            manifest=bundle[0],
            product=bundle[1],
            calibration=bundle[2],
            noise=bundle[3],
            expected=source,
            header=header(source),
        )


@pytest.mark.parametrize("state", [True, False, None])
def test_each_slice_thermal_noise_state_is_preserved_without_correction(state):
    source = s1.FROZEN_SOURCES[0]
    m, p, c, n = _xml_bundle(source)
    replacement = (
        b""
        if state is None
        else f"<thermalNoiseCorrectionPerformed>{str(state).lower()}</thermalNoiseCorrectionPerformed>".encode()
    )
    p = p.replace(
        b"<thermalNoiseCorrectionPerformed>false</thermalNoiseCorrectionPerformed>", replacement
    )
    summary = s1.validate_metadata_xml(
        manifest=m, product=p, calibration=c, noise=n, expected=source, header=header(source)
    )
    assert summary.thermal_noise_correction_performed is state


@pytest.mark.parametrize("role", ["manifest", "product_vv", "calibration_vv", "noise_vv"])
def test_missing_required_metadata_is_unavailable_and_signed_errors_do_not_escape(role):
    source = retrieval().slices[0]
    blob = _tiff_blob(source.policy)
    bundle = _xml_bundle(source.policy)
    payloads = dict(zip(("manifest", "product_vv", "calibration_vv", "noise_vv"), bundle))

    def reader(url, **kwargs):
        for purpose, payload in payloads.items():
            if url.startswith(source.asset(purpose).href):
                if purpose == role:
                    raise OSError(url + "&sig=synthetic-secret")
                return payload
        pytest.fail("Unexpected asset")

    result = s1.validate_slice_access(
        source,
        SARConfig(),
        signer=lambda h, s: h + "?sv=fake&sig=synthetic",
        range_reader=lambda url, timeout, start, end: blob[start : end + 1],
        byte_reader=reader,
    )
    assert result.availability == "UNAVAILABLE" and result.reason == "ACCESS_BLOCKED"
    assert "sig=" not in repr(result) and "synthetic-secret" not in repr(result)


def test_validate_all_slices_rebuilds_group_coverage_and_provenance_no_raster_API(monkeypatch):
    import rasterio

    monkeypatch.setattr(rasterio, "open", lambda *a, **k: pytest.fail("Raster API forbidden"))

    def validate(source, settings, **kwargs):
        blob = _tiff_blob(source.policy)
        bundle = _xml_bundle(source.policy)

        def reader(url, **kwargs):
            return next(
                body
                for purpose, body in zip(
                    ("manifest", "product_vv", "calibration_vv", "noise_vv"), bundle
                )
                if url.startswith(source.asset(purpose).href)
            )

        return s1.validate_slice_access(
            source,
            settings,
            signer=lambda h, s: h + "?sig=synthetic",
            range_reader=lambda url, timeout, start, end: blob[start : end + 1],
            byte_reader=reader,
        )

    monkeypatch.setattr(metadata, "validate_slice_access", validate)
    original = retrieval()
    result = s1.validate_retrieval_access(original, SARConfig())
    result.validate()
    assert result.ready and all(not g.missingness for g in result.groups)
    assert result.product_id != original.product_id
    assert all(s.asset("measurement_vh") for s in result.slices)
    assert "sig=" not in json.dumps(result.to_dict())


@pytest.mark.parametrize(
    "url",
    [
        "http://sentinel1euwest.blob.core.windows.net/s1-grd/x",
        "https://u:p@sentinel1euwest.blob.core.windows.net/s1-grd/x",
        "https://sentinel1euwest.blob.core.windows.net:444/s1-grd/x",
        "https://sentinel1euwest.blob.core.windows.net/s1-grd/x#fragment",
        "https://other.test/s1-grd/x",
    ],
)
def test_SAR_transport_rejects_unsafe_host_scheme_port_userinfo_fragment(url):
    with pytest.raises(pc.AssetAccessError):
        pc.validate_asset_href(url, SARConfig())


def test_signing_reuses_existing_PC_token_subsystem_with_SAR_settings(monkeypatch):
    now = datetime(2026, 10, 11, tzinfo=UTC)
    calls = []
    monkeypatch.setattr(pc, "_utc_now", lambda: now)
    monkeypatch.setattr(pc, "_TOKEN_CACHE", {})

    def request(url, settings):
        calls.append(url)
        return json.dumps(
            {
                "token": "sv=2023&se=2030&sp=r&sig=synthetic",
                "msft:expiry": (now + timedelta(hours=1)).isoformat(),
            }
        ).encode()

    monkeypatch.setattr(pc, "_request_token", request)
    for source in retrieval().slices:
        for asset in source.assets:
            assert "sig=synthetic" in pc.sign_asset(asset.href, SARConfig())
    assert calls == [
        "https://planetarycomputer.microsoft.com/api/sas/v1/token/sentinel1euwest/s1-grd"
    ]


@pytest.mark.parametrize("modify", ["cycle", "big_endian", "image_overlap", "truncated"])
def test_TIFF_directory_adversarial_cases_rejected(modify):
    source = s1.FROZEN_SOURCES[0]
    blob = bytearray(_tiff_blob(source))
    if modify == "big_endian":
        blob[:2] = b"MM"
    if modify == "cycle":
        count = struct.unpack("<H", blob[8:10])[0]
        end = 8 + 2 + 12 * count
        blob[end : end + 4] = struct.pack("<I", 8)
    if modify == "image_overlap":
        count = struct.unpack("<H", blob[8:10])[0]
        for i in range(count):
            off = 10 + 12 * i
            if struct.unpack("<H", blob[off : off + 2])[0] == 324:
                blob[off + 8 : off + 12] = struct.pack("<I", 8)
    if modify == "truncated":
        blob = blob[:12]
    with pytest.raises(s1.Sentinel1MetadataError):
        s1.read_tiff_header(
            "synthetic",
            source,
            timeout=1,
            range_reader=lambda url, timeout, start, end: bytes(blob[start : end + 1]),
        )


def test_canonical_footprint_rotations_and_holes_are_equivalent():
    original = _item(s1.FROZEN_SOURCES[0], "pc")["geometry"]
    ring = original["coordinates"][0][:-1]
    rotated = ring[2:] + ring[:2]
    assert canonical_geometry(original) == canonical_geometry(
        {"type": "Polygon", "coordinates": [rotated + [rotated[0]]]}
    )


def test_proj_shape_defect_does_not_define_native_dimensions():
    items = list(_all_items("pc"))
    items[0]["properties"]["proj:shape"] = [1, 999]
    result = s1.build_retrieval_set(_all_items("cdse"), tuple(items), SARConfig())
    assert result.slices[0].availability == "RESOLVED_NOT_ACCESSED"
    native = header(result.slices[0].policy)
    assert (native.width, native.height) == (25835, 16732)


@pytest.mark.parametrize(
    "newurl",
    [
        "http://sentinel1euwest.blob.core.windows.net/container/a",
        "https://other.test/container/a",
        "https://user@sentinel1euwest.blob.core.windows.net/container/a",
        "https://user:password@sentinel1euwest.blob.core.windows.net/container/a",
        "https://sentinel1euwest.blob.core.windows.net:444/container/a",
        "https://sentinel1euwest.blob.core.windows.net/container/a#fragment",
        "https://[malformed/container/a",
    ],
)
def test_sar_redirect_rejects_unsafe_targets(newurl):
    from urllib.request import Request

    with pytest.raises(pc.AssetAccessError):
        pc._SameHostRedirect().redirect_request(
            Request("https://sentinel1euwest.blob.core.windows.net/container/a"),
            None,
            302,
            "redirect",
            {},
            newurl,
        )


@pytest.mark.parametrize(
    "code,span,body",
    [
        (200, "bytes 0-7/100", b"12345678"),
        (206, "bytes 1-8/100", b"12345678"),
        (206, "bytes 0-7/*", b"12345678"),
        (206, "bytes 0-7/7", b"12345678"),
        (206, "bytes 0-7/100", b"short"),
        (206, "bytes 0-7/100", b"123456789"),
    ],
)
def test_bounded_range_refuses_full_or_malformed_responses(monkeypatch, code, span, body):
    class Response:
        def __init__(self):
            self.headers = {"Content-Range": span}

        def __enter__(self):
            return self

        def __exit__(self, *args):
            pass

        def getcode(self):
            return code

        def read(self, size):
            assert size == 9
            return body

    class Opener:
        def open(self, request, timeout):
            assert request.get_header("Range") == "bytes=0-7"
            return Response()

    monkeypatch.setattr(metadata, "build_opener", lambda *args: Opener())
    with pytest.raises(pc.AssetAccessError) as caught:
        metadata._safe_range_bytes(
            retrieval().slices[0].asset("measurement_vv").href + "?sv=synthetic&sig=never-persist",
            timeout=30,
            start=0,
            end=7,
        )
    assert "never-persist" not in str(caught.value)
    assert caught.value.__context__ is None


def test_bounded_range_success_and_sanitized_failure(monkeypatch):
    class Response:
        def __init__(self):
            self.headers = {"Content-Range": "bytes 0-7/100"}

        def __enter__(self):
            return self

        def __exit__(self, *args):
            pass

        def getcode(self):
            return 206

        def read(self, size):
            return b"II*\x00\x08\x00\x00\x00"

    class Opener:
        def open(self, request, timeout):
            return Response()

    monkeypatch.setattr(metadata, "build_opener", lambda *args: Opener())
    url = retrieval().slices[0].asset("measurement_vv").href + "?sv=test&sig=never-persist"
    assert metadata._safe_range_bytes(url, timeout=30, start=0, end=7) == b"II*\x00\x08\x00\x00\x00"

    def fail(*args):
        raise OSError(url)

    monkeypatch.setattr(metadata, "build_opener", fail)
    with pytest.raises(pc.AssetAccessError) as caught:
        metadata._safe_range_bytes(url, timeout=30, start=0, end=7)
    assert "never-persist" not in str(caught.value) and caught.value.__context__ is None


@pytest.mark.parametrize(
    "href",
    [
        "https://[malformed/path",
        "http://example.test/item",
        "https://user@example.test/item",
        "https://example.test:444/item",
        "https://example.test/item?sig=private",
    ],
)
def test_invalid_catalog_self_link_is_sanitized_unavailability(href):
    items = list(_all_items("pc"))
    items[0]["links"] = [{"rel": "self", "href": href}]
    source = s1.build_retrieval_set(_all_items("cdse"), tuple(items), SARConfig()).slices[0]
    assert source.availability == "UNAVAILABLE"
    assert href not in repr(source)


@pytest.mark.parametrize("href", [[], None, "https://[malformed/path"])
def test_malformed_measurement_href_never_escapes_native_parser_error(href):
    items = list(_all_items("pc"))
    items[0]["assets"]["vv"]["href"] = href
    source = s1.build_retrieval_set(_all_items("cdse"), tuple(items), SARConfig()).slices[0]
    assert source.availability == "UNAVAILABLE"


def test_header_summary_cannot_claim_available_with_violated_contract():
    source = retrieval().slices[0]
    modified = policy._with_fingerprint(
        replace(source, header=replace(header(source.policy), width=1))
    )
    with pytest.raises(s1.Sentinel1RetrievalError):
        modified.validate()


def test_measurement_polarization_is_validated_independently_of_asset_key():
    items = list(_all_items("pc"))
    items[0]["assets"]["vv"]["href"] = items[0]["assets"]["vh"]["href"]
    assert (
        s1.build_retrieval_set(_all_items("cdse"), tuple(items), SARConfig()).slices[0].availability
        == "UNAVAILABLE"
    )


def test_rehashed_source_cannot_bypass_asset_host_allowlist():
    source = retrieval().slices[0]
    assets = list(source.assets)
    assets[0] = replace(assets[0], href="https://other.test/source/measurement/iw-vv.tiff")
    source = policy._with_fingerprint(replace(source, assets=tuple(assets)))
    with pytest.raises(s1.Sentinel1RetrievalError):
        source.validate()


def test_registry_reload_accepts_same_semantics_with_later_creation_time(tmp_path):
    from aquasentinel.provenance import load_registry, save_registry

    result = retrieval()
    registry = ProvenanceRegistry()
    result.register(registry)
    path = save_registry(registry, tmp_path / "registry.json")
    restored = load_registry(path)
    before = path.read_bytes()
    later = policy.assemble_retrieval(
        result.slices, created_at=result.provenance.created_at + timedelta(days=1)
    )
    later.register(restored)
    assert later.product_id == result.product_id
    assert restored.derived_products[result.product_id].created_at == result.provenance.created_at
    assert len(restored.sources) == 12 and len(restored.derived_products) == 1
    assert path.read_bytes() == before
    altered = replace(restored.derived_products[result.product_id], processing_version="wrong")
    restored.derived_products[result.product_id] = altered
    with pytest.raises(s1.Sentinel1RetrievalError):
        later.register(restored)
