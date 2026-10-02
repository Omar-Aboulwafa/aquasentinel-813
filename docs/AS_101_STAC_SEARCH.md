# AS-101 — Sentinel-2 STAC Search

Implemented and validated on 2 October 2026 on `feature/as-101-sentinel2-stac`, based on `origin/main` at `51f4ede37e46e6d4a0ac568b90f316f60e1277ba`. Changes remain uncommitted for review.

## Scope and setup

AS-101 discovers candidate Sentinel-2 Level-2A observations and maps metadata into the existing provenance layer. It does not download raster imagery, mask pixels, compute indices, detect HABs, score risk, or implement AS-102.

Use the existing Python 3.11 development environment. Install from the repository root:

```sh
python -m pip install -e ".[dev]"
```

The only new direct dependency is `pystac-client==0.9.0`. Its STAC client and pagination support avoid maintaining a custom protocol implementation; no geospatial processing dependencies were added. Standard-library types handle normalization and provenance IDs.

## Configuration

`config/default.toml` supplies:

```toml
[catalog]
endpoint = "https://stac.dataspace.copernicus.eu/v1/"
collection = "sentinel-2-l2a"
timeout_seconds = 30
```

Endpoint and collection are never hard-coded inside search logic. Timeout is configurable because the client otherwise permits indefinite waits; it applies to every metadata request. Automatic retries are disabled so failures remain promptly visible. There is no total result limit or silent truncation.

Configurations predating `[catalog]` still load with these defaults. Endpoint, collection, and timeout are validated alongside all existing configuration checks.

## Architecture and semantics

- `catalog/stac.py`: catalog/collection metadata access and fully paginated search through `pystac-client`, with explicit search-page validation.
- `ingestion/sentinel2.py`: `search_sentinel2(context)`, `normalize_item`, typed `Sentinel2Candidate`/`AssetReference`, and `to_source_record()`.
- The configured primary validation AOI must be a Polygon and is passed as STAC `intersects`, preserving longitude/latitude coordinates. The reference point is not searched as an intake.
- Start and end dates are inclusive UTC days: the default query interval is `2023-03-01T00:00:00Z/2023-05-31T23:59:59.999999Z`.
- The query uses `{"eo:cloud_cover": {"lte": 30.0}}`. Returned dates and cloud values are checked locally as well, so a provider ignoring filters cannot widen the result set.
- Results are sorted by UTC acquisition timestamp, then item ID. Identical normalized duplicates collapse; conflicting duplicates fail explicitly, independently of response order.
- Pagination follows the client's GET/POST next-link behavior. Missing page features, ambiguous/cyclic pagination, or empty pages advertising further results raise errors rather than returning partial success.
- Each candidate preserves item ID, acquisition timestamp, supplied platform, collection, cloud percentage, catalog endpoint, optional self URL/licence, and sorted asset references with media types and roles. Relative asset references require a self URL for resolution. No asset content is fetched.

## Provenance and failure policy

Every returned candidate is checked for conversion to a valid, unchanged `SourceRecord`.

Source IDs have the form `stac:<endpoint-sha256>:<escaped-collection>:<escaped-item-id>`. The endpoint's trailing slash is ignored when hashing; collection and item separators are escaped. `product_id` retains the provider's item ID, and all supplied provenance metadata is preserved.

Item-level licence metadata takes precedence over the collection's supplied licence. No particular reuse permission is inferred from a licence marker such as `other`.

Failure categories are explicit:

| Outcome | Behavior |
|---|---|
| Valid zero-result search | Empty tuple |
| Invalid configured AOI/date/cloud/settings | `InvalidSearchInputError` |
| Missing item ID, collection, datetime, platform, cloud, or assets | `MissingItemMetadataError` |
| Malformed or conflicting item metadata | `MalformedItemMetadataError` |
| Malformed catalog/page or incomplete pagination | `CatalogMetadataError` |
| Network/service failure | Underlying `pystac_client.exceptions.APIError` propagates |

Missing cloud cover is never zero. Required fields fail the entire search rather than silently discarding malformed observations. Platform is required for valid candidates because the existing provenance model requires it; a missing platform is not replaced with an invented value. Optional self URLs and licence values may be `None`.

## Reproduce the smoke test

Run from the repository root with the Python 3.11 environment active:

```sh
python - <<'PY'
from aquasentinel.ingestion.sentinel2 import search_sentinel2
from aquasentinel.provenance import source_record_to_dict
from aquasentinel.runtime import build_runtime_context

context = build_runtime_context()
scenes = search_sentinel2(context)
print("Scene count:", len(scenes))
if scenes:
    print("Earliest:", scenes[0].acquired_at.isoformat())
    print("Latest:", scenes[-1].acquired_at.isoformat())
    for scene in scenes[:5]:
        print(scene.item_id, scene.cloud_cover_percent)
for scene in scenes:
    source_record_to_dict(scene.to_source_record())
print("All returned scenes converted to valid provenance.")
PY
```

The metadata query needs HTTPS access to `stac.dataspace.copernicus.eu`. The validated query required no credentials. Future asset retrieval may have different authentication requirements and is outside AS-101.

## Recorded real-data result

On 2 October 2026, the real CDSE query for the Al Raha Bay validation Polygon, 1 March–31 May 2023, and scene cloud cover <= 30% succeeded:

- **44 unique candidate scenes**.
- Earliest acquisition: `2023-03-04T06:47:51.024Z`.
- Latest acquisition: `2023-05-28T06:46:29.024Z`.
- Observed scene cloud-cover range: **0.12–24.96%**.
- Provenance conversion and serialization succeeded for **all 44**.
- First scene's supplied platform: `sentinel-2a`; collection licence marker: `other`; 47 asset references retained.

Example items:

| Item ID | Scene cloud cover (%) |
|---|---:|
| `S2A_MSIL2A_20230304T064751_N0510_R020_T39RZH_20240819T072511` | 1.92 |
| `S2A_MSIL2A_20230304T064751_N0510_R020_T40RBN_20240819T072511` | 2.46 |
| `S2A_MSIL2A_20230307T065731_N0510_R063_T39RZH_20240821T003413` | 1.01 |
| `S2A_MSIL2A_20230307T065731_N0510_R063_T40RBN_20240821T003413` | 0.88 |
| `S2B_MSIL2A_20230309T064719_N0510_R020_T39RZH_20240823T054455` | 23.01 |

The catalog can change or reprocess products; this count is observed evidence, not a permanent expected test assertion.

## Offline validation and limitations

```sh
git diff --check
python -m pytest -v
python -m ruff check .
```

Recorded result: **92 tests passed**, Ruff passed, and the diff check passed. All 17 original tests remain intact. New tests exercise configurable settings and legacy loading, request geometry/date/cloud/timeout, GET/POST pagination, later-page errors and cycles, normalization, optional/missing/malformed fields, UTC boundaries, local filter checks, deterministic duplicates, and provenance. Only HTTP responses are replaced for catalog tests; the real client's search and pagination logic executes offline.

Catalog search proves metadata availability only. Scene cloud cover is not AOI-specific water/cloud masking. Overlapping tiles remain separate products; scene count is not a count of independent acquisition dates. Asset accessibility and raster suitability have not been tested. The analyst-defined Al Raha validation AOI remains distinct from any operational intake. AS-102 has not started.
