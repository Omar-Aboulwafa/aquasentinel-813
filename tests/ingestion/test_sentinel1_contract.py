"""AS-201 offline/adversarial source contract; no provider or pixel access."""

import copy
import json
import struct
from dataclasses import replace
from datetime import UTC, datetime, timedelta, timezone
from hashlib import sha256
from xml.etree import ElementTree as ET

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


def _cdse_product_type_item(source):
    """Synthetic exact source with the product-type field shape observed in M51."""
    item = _item(source, "cdse")
    item["properties"].pop("s1:product_type")
    item["properties"]["product:type"] = "IW_GRDH_1S"
    assert "sar:product_type" not in item["properties"]
    return item


@pytest.mark.parametrize("source", s1.FROZEN_SOURCES, ids=lambda source: source.cdse_item_id)
def test_cdse_m51_product_type_normalizes_each_exact_frozen_source(source):
    item = _cdse_product_type_item(source)
    original = copy.deepcopy(item)
    settings = SARConfig()
    record, _, _, properties = resolver._normalize_item(
        item, source, endpoint=settings.discovery_endpoint,
        collection=settings.discovery_collection, expected_item_id=source.cdse_item_id,
        license_name=None,
    )
    assert record.product_id == source.cdse_item_id
    assert record.acquired_at == source.acquisition_start
    assert properties["product:type"] == "IW_GRDH_1S"
    assert item == original


def test_cdse_m51_product_type_resolves_all_six_without_changing_normalized_identity():
    cdse = tuple(_cdse_product_type_item(source) for source in s1.FROZEN_SOURCES)
    result = s1.build_retrieval_set(cdse, _all_items("pc"), SARConfig())
    expected = retrieval()
    assert [source.policy for source in result.slices] == list(s1.FROZEN_SOURCES)
    assert all(source.availability == "RESOLVED_NOT_ACCESSED" for source in result.slices)
    assert all(source.discovery_source and source.source for source in result.slices)
    assert result.to_dict()["parameters"] == expected.to_dict()["parameters"]
    assert result.fingerprint == expected.fingerprint
    assert result.product_id == expected.product_id
    assert not result.ready  # Synthetic normalization does not establish live asset access.


@pytest.mark.parametrize("field", ["sar:product_type", "s1:product_type", "product:type"])
@pytest.mark.parametrize("product", ["GRD", "GRDH"])
def test_pc_existing_grd_product_type_representations_remain_accepted(field, product):
    source = s1.FROZEN_SOURCES[0]
    item = _item(source, "pc")
    item["properties"].pop("s1:product_type")
    item["properties"][field] = product
    settings = SARConfig()
    record, _, _, _ = resolver._normalize_item(
        item, source, endpoint=settings.access_endpoint,
        collection=settings.access_collection, expected_item_id=source.pc_item_id,
        license_name=None,
    )
    assert record.product_id == source.pc_item_id


@pytest.mark.parametrize("product", [
    "EW_GRDH_1S", "IW_GRDM_1S", "IW_SLC__1S", "GRDM", "SLC", "unknown",
    "OTHER_GRDH_1S", "IW_GRDH_1S_extra", "prefix_IW_GRDH_1S", "iw_grdh_1s", "",
])
def test_cdse_product_type_alias_does_not_accept_other_strings(product):
    source = s1.FROZEN_SOURCES[0]
    item = _cdse_product_type_item(source)
    item["properties"]["product:type"] = product
    settings = SARConfig()
    with pytest.raises(s1.Sentinel1RetrievalError, match="not GRDH-compatible"):
        resolver._normalize_item(
            item, source, endpoint=settings.discovery_endpoint,
            collection=settings.discovery_collection, expected_item_id=source.cdse_item_id,
            license_name=None,
        )


@pytest.mark.parametrize("explicit", [
    {"sar:product_type": "SLC"},
    {"s1:product_type": "SLC"},
    {"sar:product_type": "SLC", "s1:product_type": "GRD"},
    {"sar:product_type": None},
    {"s1:product_type": None},
    {"sar:product_type": "EW_GRDH_1S"},
    {"s1:product_type": "IW_GRDM_1S"},
])
def test_cdse_product_type_alias_cannot_rescue_incompatible_explicit_metadata(explicit):
    items = list(_all_items("cdse"))
    items[0] = _cdse_product_type_item(s1.FROZEN_SOURCES[0])
    items[0]["properties"].update(explicit)
    result = s1.build_retrieval_set(tuple(items), _all_items("pc"), SARConfig())
    assert result.slices[0].availability == "UNAVAILABLE"
    assert result.slices[0].reason == "DISCOVERY_IDENTITY_INVALID"
    assert len(result.slices) == 6 and not result.ready


@pytest.mark.parametrize("field,value", [
    ("id", "different-CDSE-product"),
    ("collection", "sentinel-1-rtc"),
    ("start_datetime", "2026-04-24T14:42:05Z"),
    ("end_datetime", "2026-04-24T14:42:30Z"),
    ("platform", "sentinel-1b"),
    ("sar:instrument_mode", "EW"),
    ("sar:polarizations", ["VV"]),
    ("sat:orbit_state", "descending"),
    ("sat:relative_orbit", 102),
    ("sat:absolute_orbit", 1),
])
def test_cdse_product_type_alias_preserves_exact_identity_guards(field, value):
    source = s1.FROZEN_SOURCES[0]
    item = _cdse_product_type_item(source)
    if field in {"id", "collection"}:
        item[field] = value
    else:
        item["properties"][field] = value
    settings = SARConfig()
    with pytest.raises(s1.Sentinel1RetrievalError):
        resolver._normalize_item(
            item, source, endpoint=settings.discovery_endpoint,
            collection=settings.discovery_collection, expected_item_id=source.cdse_item_id,
            license_name=None,
        )


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


def _manifest_time_bundle(source, start, stop):
    bundle = list(_xml_bundle(source))
    for name, original, value in (
        ("startTime", source.acquisition_start.isoformat(), start),
        ("stopTime", source.acquisition_end.isoformat(), stop),
    ):
        old = f"<{name}>{original}</{name}>".encode()
        assert old in bundle[0]
        bundle[0] = bundle[0].replace(old, f"<{name}>{value}</{name}>".encode())
    return dict(zip(("manifest", "product", "calibration", "noise"), bundle))


def _manifest_platform_bundle(
    source, families=("SENTINEL-1",), instrument_family="Synthetic Aperture Radar"
):
    """Synthetic M56 platform structure with M54's naive exact UTC interval."""
    bundle = _manifest_time_bundle(
        source, source.acquisition_start.replace(tzinfo=None).isoformat(),
        source.acquisition_end.replace(tzinfo=None).isoformat(),
    )
    root = metadata._parse_xml(bundle["manifest"], "manifest")
    platform = next(e for e in root.iter() if metadata._local(e.tag) == "platform")
    for child in list(platform):
        if metadata._local(child.tag) == "familyName":
            platform.remove(child)
    platform.insert(0, ET.Element("nssdcIdentifier"))
    for index, value in enumerate(families, start=1):
        child = ET.Element("familyName")
        child.text = value
        platform.insert(index, child)
    if instrument_family is not None:
        instrument = ET.SubElement(platform, "instrument")
        ET.SubElement(instrument, "familyName", {"abbreviation": "SAR"}).text = instrument_family
    bundle["manifest"] = ET.tostring(root)
    return bundle


@pytest.mark.parametrize("source", s1.FROZEN_SOURCES, ids=lambda source: source.pc_item_id)
@pytest.mark.parametrize("family", ["SENTINEL-1", "Sentinel-1", "sentinel-1", " \nSENTINEL-1\t "])
def test_manifest_direct_platform_family_case_preserves_complete_six_source_metadata(source, family):
    bundle = _manifest_platform_bundle(source, families=(family,))
    original = dict(zip(("manifest", "product", "calibration", "noise"), _xml_bundle(source)))
    summary = s1.validate_metadata_xml(**bundle, expected=source, header=header(source))
    assert summary == s1.validate_metadata_xml(**original, expected=source, header=header(source))
    assert summary.thermal_noise_correction_performed is False


@pytest.mark.parametrize("instrument_family", [
    None, "", "Synthetic Aperture Radar", "OTHER", "SENTINEL-2", "Sentinel-1",
])
def test_nested_instrument_family_does_not_contaminate_platform_identity(instrument_family):
    source = s1.FROZEN_SOURCES[0]
    bundle = _manifest_platform_bundle(source, instrument_family=instrument_family)
    summary = s1.validate_metadata_xml(**bundle, expected=source, header=header(source))
    assert summary.thermal_noise_correction_performed is False


@pytest.mark.parametrize("families", [
    (), (None,), ("",), (" \n\t ",),
    ("SENTINEL-1", "SENTINEL-1"), ("SENTINEL-1", "SENTINEL-2"),
    ("SENTINEL-1", ""), ("SENTINEL-1", None),
    ("SENTINEL-2",), ("Synthetic Aperture Radar",), ("SENTINEL",),
    ("Sentinel_1",), ("Sentinel-1A",), ("prefix-Sentinel-1",),
    ("Sentinel-1-suffix",), ("Sentinel-10",), ("Sentinel -1",),
    ("Sentinel- 1",), ("Sentinel 1",), ("SENTINEL\n-1",),
])
def test_nested_valid_family_cannot_rescue_invalid_direct_platform_family(families):
    source = s1.FROZEN_SOURCES[0]
    bundle = _manifest_platform_bundle(
        source, families=families, instrument_family="Sentinel-1"
    )
    with pytest.raises(s1.Sentinel1MetadataError, match="Required XML metadata contract"):
        s1.validate_metadata_xml(**bundle, expected=source, header=header(source))


def test_manifest_family_fix_does_not_change_recursive_shared_helpers():
    source = s1.FROZEN_SOURCES[0]
    bundle = _manifest_platform_bundle(source)
    root = metadata._parse_xml(bundle["manifest"], "manifest")
    platform = next(e for e in root.iter() if metadata._local(e.tag) == "platform")
    assert metadata._texts(platform, "familyName") == ["SENTINEL-1", "Synthetic Aperture Radar"]
    with pytest.raises(s1.Sentinel1MetadataError, match="one consistent familyName"):
        metadata._unique_text(platform, "familyName")
    assert metadata._unique_text(platform, "number") == "A"
    metadata._validate_manifest(root, source)


@pytest.mark.parametrize("source", s1.FROZEN_SOURCES, ids=lambda source: source.pc_item_id)
@pytest.mark.parametrize("serialization", ["naive", "Z", "+00:00", "+04:00"])
def test_manifest_time_serializations_preserve_exact_six_source_metadata(source, serialization):
    def serialize(value):
        if serialization == "naive":
            return value.replace(tzinfo=None).isoformat()
        if serialization == "Z":
            return value.isoformat().replace("+00:00", "Z")
        if serialization == "+04:00":
            return value.astimezone(timezone(timedelta(hours=4))).isoformat()
        return value.isoformat()

    bundle = _manifest_time_bundle(
        source, serialize(source.acquisition_start), serialize(source.acquisition_end)
    )
    summary = s1.validate_metadata_xml(**bundle, expected=source, header=header(source))
    original = dict(zip(("manifest", "product", "calibration", "noise"), _xml_bundle(source)))
    assert summary == s1.validate_metadata_xml(**original, expected=source, header=header(source))
    assert summary.thermal_noise_correction_performed is False


@pytest.mark.parametrize("field", ["start", "stop"])
@pytest.mark.parametrize("delta", [timedelta(microseconds=1), timedelta(seconds=1)])
def test_manifest_time_mismatch_fails_without_tolerance(field, delta):
    source = s1.FROZEN_SOURCES[0]
    start, stop = source.acquisition_start, source.acquisition_end
    start += delta if field == "start" else timedelta(0)
    stop += delta if field == "stop" else timedelta(0)
    bundle = _manifest_time_bundle(
        source, start.replace(tzinfo=None).isoformat(), stop.replace(tzinfo=None).isoformat()
    )
    with pytest.raises(s1.Sentinel1MetadataError, match="Required XML metadata contract"):
        s1.validate_metadata_xml(**bundle, expected=source, header=header(source))


def test_manifest_time_swapped_interval_fails():
    source = s1.FROZEN_SOURCES[0]
    bundle = _manifest_time_bundle(
        source, source.acquisition_end.replace(tzinfo=None).isoformat(),
        source.acquisition_start.replace(tzinfo=None).isoformat(),
    )
    with pytest.raises(s1.Sentinel1MetadataError, match="Required XML metadata contract"):
        s1.validate_metadata_xml(**bundle, expected=source, header=header(source))


@pytest.mark.parametrize("field", ["start", "stop"])
@pytest.mark.parametrize("invalid", [
    "malformed", "empty", "spaces_only", "leading_space", "trailing_space",
    "impossible_date", "impossible_time", "extra_fraction_digits",
])
def test_manifest_time_invalid_serialization_fails(field, invalid):
    source = s1.FROZEN_SOURCES[0]
    values = {
        "start": source.acquisition_start.replace(tzinfo=None).isoformat(),
        "stop": source.acquisition_end.replace(tzinfo=None).isoformat(),
    }
    value = values[field]
    values[field] = {
        "malformed": "not-a-timestamp", "empty": "", "spaces_only": "  ",
        "leading_space": " " + value, "trailing_space": value + " ",
        "impossible_date": "2026-02-30T14:42:05.150515",
        "impossible_time": "2026-04-24T25:42:05.150515",
        "extra_fraction_digits": value + "1",
    }[invalid]
    bundle = _manifest_time_bundle(source, values["start"], values["stop"])
    with pytest.raises(s1.Sentinel1MetadataError):
        s1.validate_metadata_xml(**bundle, expected=source, header=header(source))


@pytest.mark.parametrize("field", ["startTime", "stopTime"])
def test_generic_time_parser_remains_strict_for_naive_inputs(field):
    source = s1.FROZEN_SOURCES[0]
    value = source.acquisition_start if field == "startTime" else source.acquisition_end
    with pytest.raises(s1.Sentinel1RetrievalError, match="must be timezone-aware"):
        policy._parse_time(value.replace(tzinfo=None).isoformat(), field)


@pytest.mark.parametrize("role", ["product", "calibration", "noise"])
@pytest.mark.parametrize("field", ["startTime", "stopTime"])
def test_ads_time_parser_remains_strict_after_manifest_utc_normalization(role, field):
    source = s1.FROZEN_SOURCES[0]
    bundle = _manifest_time_bundle(
        source, source.acquisition_start.replace(tzinfo=None).isoformat(),
        source.acquisition_end.replace(tzinfo=None).isoformat(),
    )
    value = source.acquisition_start if field == "startTime" else source.acquisition_end
    aware = value.isoformat().replace("+00:00", "Z")
    original = f"<{field}>{aware}</{field}>".encode()
    assert original in bundle[role]
    bundle[role] = bundle[role].replace(
        original, f"<{field}>{value.replace(tzinfo=None).isoformat()}</{field}>".encode()
    )
    with pytest.raises(s1.Sentinel1MetadataError, match="Required XML metadata contract"):
        s1.validate_metadata_xml(**bundle, expected=source, header=header(source))


@pytest.mark.parametrize("role", ["calibration", "noise"])
def test_lut_time_parser_remains_strict_after_manifest_utc_normalization(role):
    source = s1.FROZEN_SOURCES[0]
    bundle = _manifest_time_bundle(
        source, source.acquisition_start.replace(tzinfo=None).isoformat(),
        source.acquisition_end.replace(tzinfo=None).isoformat(),
    )
    original = f"<azimuthTime>{source.acquisition_start.isoformat()}</azimuthTime>".encode()
    assert original in bundle[role]
    bundle[role] = bundle[role].replace(
        original, f"<azimuthTime>{source.acquisition_start.replace(tzinfo=None).isoformat()}</azimuthTime>".encode()
    )
    with pytest.raises(s1.Sentinel1MetadataError, match="Required XML metadata contract"):
        s1.validate_metadata_xml(**bundle, expected=source, header=header(source))


@pytest.mark.parametrize("role,old,new", [
    ("manifest", b"<number>A", b"<number>B"),
    ("manifest", b"<familyName>Sentinel-1", b"<familyName>OTHER"),
    ("manifest", b"<mode>IW", b"<mode>EW"),
    ("manifest", b"<pass>ASCENDING", b"<pass>DESCENDING"),
    ("manifest", b"<relativeOrbitNumber>101", b"<relativeOrbitNumber>102"),
    ("manifest", b"<productType>GRD", b"<productType>SLC"),
    ("manifest", b"./measurement/", b"./wrong/"),
    ("product", b"<missionId>S1A", b"<missionId>S1B"),
    ("product", b"<mode>IW", b"<mode>EW"),
    ("product", b"<polarisation>VV", b"<polarisation>VH"),
    ("product", b"<absoluteOrbitNumber>64223", b"<absoluteOrbitNumber>64224"),
    ("product", b"<numberOfSamples>25835", b"<numberOfSamples>25836"),
    ("product", b"<incidenceAngle>35", b"<incidenceAngle>NaN"),
    ("product", b"<latitude>29", b"<latitude>999"),
    ("calibration", b"<sigmaNought>1 2", b"<sigmaNought>1"),
    ("noise", b"<noiseAzimuthLut>0 1", b"<noiseAzimuthLut>0"),
    ("noise", b'<noiseRangeVectorList count="1">', b'<noiseRangeVectorList count="0">'),
    ("product", b"<thermalNoiseCorrectionPerformed>false", b"<thermalNoiseCorrectionPerformed>unknown"),
])
@pytest.mark.parametrize("nested_instrument", [False, True], ids=["original", "M56-nested"])
def test_manifest_utc_boundary_does_not_bypass_later_guards(role, old, new, nested_instrument):
    source = s1.FROZEN_SOURCES[0]
    bundle = _manifest_time_bundle(
        source, source.acquisition_start.replace(tzinfo=None).isoformat(),
        source.acquisition_end.replace(tzinfo=None).isoformat(),
    )
    if nested_instrument:
        bundle = _manifest_platform_bundle(source, families=("Sentinel-1",))
    assert old in bundle[role]
    bundle[role] = bundle[role].replace(old, new)
    with pytest.raises(s1.Sentinel1RetrievalError):
        s1.validate_metadata_xml(**bundle, expected=source, header=header(source))


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
