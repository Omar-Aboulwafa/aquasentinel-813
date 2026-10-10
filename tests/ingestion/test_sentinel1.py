from __future__ import annotations

import struct
from dataclasses import replace

from aquasentinel.catalog.stac import CatalogResult
from aquasentinel.config import SARConfig
from aquasentinel.ingestion import sentinel1 as s1
from aquasentinel.ingestion import sentinel1_resolver as resolver


def _properties(policy):
    return {
        "start_datetime": policy.acquisition_start.isoformat().replace("+00:00", "Z"),
        "end_datetime": policy.acquisition_end.isoformat().replace("+00:00", "Z"),
        "platform": "sentinel-1a",
        "sar:instrument_mode": "IW",
        "sar:polarizations": ["VV", "VH"],
        "sat:orbit_state": "ascending",
        "sat:relative_orbit": 101,
        "sat:absolute_orbit": policy.absolute_orbit,
        "s1:product_type": "GRD",
        "s1:product_identifier": policy.native_source_product_id,
        "sar:pixel_spacing_range": 10,
        "sar:pixel_spacing_azimuth": 10,
    }


def _item(policy, provider: str):
    item_id = policy.cdse_item_id if provider == "cdse" else policy.pc_item_id
    collection = "sentinel-1-grd"
    item = {
        "type": "Feature",
        "id": item_id,
        "collection": collection,
        "properties": _properties(policy),
        "geometry": {
            "type": "Polygon",
            "coordinates": [[[49.5, 28.5], [50.8, 28.5], [50.8, 29.7], [49.5, 29.7], [49.5, 28.5]]],
        },
        "bbox": [49.5, 28.5, 50.8, 29.7],
        "links": [{"rel": "self", "href": f"https://example.test/{provider}/{item_id}"}],
        "assets": {},
    }
    if provider == "pc":
        root = f"https://sentinel1euwest.blob.core.windows.net/s1-grd/{policy.native_source_product_id}.SAFE"
        item["assets"] = {
            "vv": {
                "href": root + "/measurement/iw-vv.tiff",
                "type": "image/tiff; application=geotiff; profile=cloud-optimized",
                "roles": ["data"],
            },
            "vh": {
                "href": root + "/measurement/iw-vh.tiff",
                "type": "image/tiff; application=geotiff; profile=cloud-optimized",
                "roles": ["data"],
            },
            "schema-product-vv": {
                "href": root + "/annotation/rfi/rfi-iw-vv.xml",
                "type": "application/xml",
            },
        }
    return item


def _all_items(provider: str):
    return tuple(_item(policy, provider) for policy in s1.FROZEN_SOURCES)


def test_exact_frozen_six_resolve_with_stable_order_and_no_pixel_processing():
    retrieval = s1.build_retrieval_set(_all_items("cdse"), _all_items("pc"), SARConfig())
    assert [group.role for group in retrieval.groups] == list(s1.ROLE_ORDER)
    assert len(retrieval.slices) == 6
    assert all(source.availability == "RESOLVED_NOT_ACCESSED" for source in retrieval.slices)
    orders = [source.policy.slice_order for group in retrieval.groups for source in group.slices]
    assert orders == [1, 2, 1, 2, 1, 2]
    assert not retrieval.ready
    assert len(retrieval.fingerprint) == 64
    for source in retrieval.slices:
        assert source.representation == "RAW_GRD_AMPLITUDE"
        assert source.asset("measurement_vv").href.endswith("/measurement/iw-vv.tiff")
        assert source.asset("product_vv").href.endswith("/annotation/iw-vv.xml")
        assert "rfi" not in source.asset("product_vv").href
        assert all("?" not in asset.href for asset in source.assets)


def test_mislabelled_vv_asset_key_does_not_override_measurement_identity():
    pc = list(_all_items("pc"))
    pc[0]["assets"]["vv"]["href"] = pc[0]["assets"]["vh"]["href"]
    retrieval = s1.build_retrieval_set(_all_items("cdse"), tuple(pc), SARConfig())
    assert retrieval.slices[0].availability == "UNAVAILABLE"
    assert retrieval.slices[0].reason == "PC_IDENTITY_OR_ASSET_CONTRACT_INVALID"


def test_vv_vh_must_share_same_product_root():
    pc = list(_all_items("pc"))
    pc[0]["assets"]["vh"]["href"] = (
        "https://sentinel1euwest.blob.core.windows.net/s1-grd/OTHER.SAFE/measurement/iw-vh.tiff"
    )
    retrieval = s1.build_retrieval_set(_all_items("cdse"), tuple(pc), SARConfig())
    assert retrieval.slices[0].availability == "UNAVAILABLE"
    assert retrieval.slices[0].reason == "PC_IDENTITY_OR_ASSET_CONTRACT_INVALID"


def test_missing_source_retains_required_slot_without_substitution():
    missing = s1.FROZEN_SOURCES[2]
    cdse = tuple(item for item in _all_items("cdse") if item["id"] != missing.cdse_item_id)
    retrieval = s1.build_retrieval_set(cdse, _all_items("pc"), SARConfig())
    source = retrieval.groups[1].slices[0]
    assert source.policy == missing
    assert source.availability == "UNAVAILABLE"
    assert source.reason == "DISCOVERY_SOURCE_MISSING"
    assert len(retrieval.slices) == 6


def test_wrong_orbit_fails_closed_for_that_slice():
    pc = list(_all_items("pc"))
    pc[0]["properties"]["sat:relative_orbit"] = 102
    retrieval = s1.build_retrieval_set(_all_items("cdse"), tuple(pc), SARConfig())
    assert retrieval.slices[0].availability == "UNAVAILABLE"
    assert retrieval.slices[0].reason == "PC_IDENTITY_OR_ASSET_CONTRACT_INVALID"
    assert all(source.availability == "RESOLVED_NOT_ACCESSED" for source in retrieval.slices[1:])


def test_fingerprint_is_independent_of_catalog_result_order():
    a = s1.build_retrieval_set(_all_items("cdse"), _all_items("pc"), SARConfig())
    b = s1.build_retrieval_set(
        tuple(reversed(_all_items("cdse"))),
        tuple(reversed(_all_items("pc"))),
        SARConfig(),
    )
    assert a.fingerprint == b.fingerprint
    assert [source.fingerprint for source in a.slices] == [
        source.fingerprint for source in b.slices
    ]


def test_search_path_omits_sentinel2_cloud_query(monkeypatch):
    calls = []

    def search(settings, **kwargs):
        calls.append((settings, kwargs))
        items = _all_items("cdse") if len(calls) == 1 else _all_items("pc")
        return CatalogResult(items, "proprietary")

    monkeypatch.setattr(resolver, "search_catalog", search)
    retrieval = s1.search_sentinel1(SARConfig())
    assert len(retrieval.slices) == 6
    assert len(calls) == 2
    assert all(call[1]["query"] is None for call in calls)
    assert all("max_cloud_cover_percent" not in call[1] for call in calls)


def _ifd_entry(tag, field_type, count, value):
    if field_type == 3 and count == 1:
        raw = struct.pack("<H", value) + b"\x00\x00"
    elif field_type in {4, 13} and count == 1:
        raw = struct.pack("<I", value)
    elif field_type == 2 and count <= 4:
        raw = value.ljust(4, b"\x00")
    else:
        raw = struct.pack("<I", 4096)
    return struct.pack("<HHI", tag, field_type, count) + raw


def _tiff_blob(policy):
    blob = bytearray(16384)
    offsets = [8 + 256 * i for i in range(7)]
    blob[:8] = b"II*\x00" + struct.pack("<I", offsets[0])
    for level, offset in enumerate(offsets):
        entries = [
            _ifd_entry(256, 4, 1, policy.width // 2**level),
            _ifd_entry(257, 4, 1, policy.height // 2**level),
            _ifd_entry(258, 3, 1, 16),
            _ifd_entry(259, 3, 1, 50000),
            _ifd_entry(277, 3, 1, 1),
            _ifd_entry(322, 4, 1, 1024),
            _ifd_entry(323, 4, 1, 1024),
            _ifd_entry(339, 3, 1, 1),
            _ifd_entry(324, 4, 1, 1000000 + 2000 * level),
            _ifd_entry(325, 4, 1, 1000),
        ]
        if level == 0:
            entries.extend(
                [
                    struct.pack("<HHII", 33922, 12, 6, 4096),
                    struct.pack("<HHII", 34735, 3, 12, 4200),
                    _ifd_entry(42113, 2, 2, b"0\x00"),
                ]
            )
        ifd = (
            struct.pack("<H", len(entries))
            + b"".join(entries)
            + struct.pack("<I", offsets[level + 1] if level < 6 else 0)
        )
        blob[offset : offset + len(ifd)] = ifd
    blob[4096:4144] = struct.pack("<6d", 0, 0, 0, 50, 29, 0)
    blob[4200:4224] = struct.pack("<12H", 1, 1, 0, 2, 1024, 0, 1, 2, 2048, 0, 1, 4326)
    return bytes(blob)


def _tiff_ranges(policy):
    blob = _tiff_blob(policy)
    count = struct.unpack("<H", blob[8:10])[0]
    return blob[:8], blob[8 : 8 + 2 + 12 * count + 4]


def test_header_reader_uses_only_structural_ranges():
    policy = s1.FROZEN_SOURCES[0]
    blob = _tiff_blob(policy)
    requests = []

    def reader(url, *, timeout, start, end):
        requests.append((start, end))
        assert end < 1000000  # no image-block span is requested
        return blob[start : end + 1]

    summary = s1.read_tiff_header(
        "https://example.test/fake", policy, timeout=1, range_reader=reader
    )
    assert (summary.width, summary.height) == (policy.width, policy.height)
    assert summary.compression == 50000
    assert summary.tiepoint_count == 1
    assert summary.overview_count == 6
    assert len(requests) == 17  # header, 7 IFD count/body pairs, tiepoints and GeoKeys


def _ads(policy):
    start = policy.acquisition_start.isoformat().replace("+00:00", "Z")
    stop = policy.acquisition_end.isoformat().replace("+00:00", "Z")
    return f"""
      <adsHeader>
        <missionId>S1A</missionId><productType>GRD</productType>
        <polarisation>VV</polarisation><mode>IW</mode>
        <startTime>{start}</startTime><stopTime>{stop}</stopTime>
        <absoluteOrbitNumber>{policy.absolute_orbit}</absoluteOrbitNumber>
      </adsHeader>
    """


def _xml_bundle(policy):
    start = policy.acquisition_start.isoformat()
    product = f"""<product>{_ads(policy)}<imageAnnotation><imageInformation>
      <numberOfSamples>{policy.width}</numberOfSamples><numberOfLines>{policy.height}</numberOfLines>
      <thermalNoiseCorrectionPerformed>false</thermalNoiseCorrectionPerformed>
      <rangePixelSpacing>10</rangePixelSpacing><azimuthPixelSpacing>10</azimuthPixelSpacing>
    </imageInformation></imageAnnotation><geolocationGridPointList count="1"><geolocationGridPoint>
      <line>0</line><pixel>0</pixel><latitude>29</latitude><longitude>50</longitude>
      <height>0</height><incidenceAngle>35</incidenceAngle>
    </geolocationGridPoint></geolocationGridPointList></product>""".encode()
    calibration = f"""<calibration>{_ads(policy)}<calibrationVectorList count="1"><calibrationVector>
      <azimuthTime>{start}</azimuthTime><line>0</line><pixel count="2">0 40</pixel>
      <betaNought>1 2</betaNought><sigmaNought>1 2</sigmaNought><gamma>1 2</gamma><dn>1 2</dn>
    </calibrationVector></calibrationVectorList></calibration>""".encode()
    noise = f"""<noise>{_ads(policy)}<noiseRangeVectorList count="1"><noiseRangeVector>
      <azimuthTime>{start}</azimuthTime><line>0</line><pixel>0 40</pixel><noiseRangeLut>0 1</noiseRangeLut>
    </noiseRangeVector></noiseRangeVectorList><noiseAzimuthVectorList count="1"><noiseAzimuthVector>
      <firstAzimuthLine>0</firstAzimuthLine><lastAzimuthLine>1</lastAzimuthLine>
      <firstRangeSample>0</firstRangeSample><lastRangeSample>40</lastRangeSample>
      <line>0 1</line><noiseAzimuthLut>0 1</noiseAzimuthLut>
    </noiseAzimuthVector></noiseAzimuthVectorList></noise>""".encode()
    parts = policy.native_source_product_id.lower().split("_")
    name = f"s1a-iw-grd-vv-{parts[4]}-{parts[5]}-{parts[6]}-{parts[7]}-001.tiff"
    manifest = f"""<xfdu:XFDU xmlns:xfdu="urn:ccsds:schema:xfdu:1"><platform>
      <familyName>Sentinel-1</familyName><number>A</number></platform><mode>IW</mode>
      <pass>ASCENDING</pass><relativeOrbitNumber>101</relativeOrbitNumber><productType>GRD</productType>
      <startTime>{start}</startTime><stopTime>{policy.acquisition_end.isoformat()}</stopTime>
      <fileLocation href="./measurement/{name}"/></xfdu:XFDU>""".encode()
    return manifest, product, calibration, noise


def test_xml_contract_validates_identity_noise_state_and_luts():
    policy = s1.FROZEN_SOURCES[0]
    header_bytes, ifd = _tiff_ranges(policy)
    header = s1._parse_tiff_ifd(header_bytes, ifd, policy, overview_count=6)
    manifest, product, calibration, noise = _xml_bundle(policy)
    summary = s1.validate_metadata_xml(
        manifest=manifest,
        product=product,
        calibration=calibration,
        noise=noise,
        expected=policy,
        header=header,
    )
    assert summary.thermal_noise_correction_performed is False
    assert summary.calibration_has_sigma0
    assert summary.noise_has_range and summary.noise_has_azimuth


def test_access_validation_never_persists_signed_urls():
    retrieval = s1.build_retrieval_set(_all_items("cdse"), _all_items("pc"), SARConfig())
    source = retrieval.slices[0]
    blob = _tiff_blob(source.policy)
    manifest, product, calibration, noise = _xml_bundle(source.policy)

    def signer(href, settings):
        return href + "?sv=fake&sig=fake-only"

    def range_reader(url, *, timeout, start, end):
        assert "sig=fake-only" in url
        return blob[start : end + 1]

    def byte_reader(url, *, timeout, max_bytes):
        if url.endswith("manifest.safe?sv=fake&sig=fake-only"):
            return manifest
        if "calibration-iw-vv.xml" in url:
            return calibration
        if "noise-iw-vv.xml" in url:
            return noise
        return product

    validated = s1.validate_slice_access(
        source,
        SARConfig(),
        signer=signer,
        range_reader=range_reader,
        byte_reader=byte_reader,
    )
    assert validated.availability == "AVAILABLE"
    assert validated.metadata.thermal_noise_correction_performed is False
    assert "sig=" not in repr(validated)
    assert "fake-only" not in repr(validated)
    assert validated.fingerprint != source.fingerprint


def test_representation_double_processing_guard_is_still_raw_only():
    retrieval = s1.build_retrieval_set(_all_items("cdse"), _all_items("pc"), SARConfig())
    assert {source.representation for source in retrieval.slices} == {"RAW_GRD_AMPLITUDE"}
    tampered = replace(retrieval.slices[0], representation="RTC_GAMMA0")
    assert tampered.representation != s1.REPRESENTATION
