# AS-201 M48 — Sentinel-1 source implementation / offline engineering validation

## Scope and publication lineage

M48 / E48 / EV-052 implements merged Decision 054; not a new scientific decision.
Official base: `1d2d994c7a04cca712485ce53dc9132db50615a8` (PR #29). Existing owner-identified WIP
`d6f89ce07eaf6216308f39087ce094877d2bfd02`, `feat: implement AS-201 Sentinel-1 retrieval`,
is a direct child of that base and remains preserved. Follow-up correction is on
`feature/as-201-sentinel1-retrieval`; no amendment, rewrite, force-push, PR or merge.
M45/M46/M47 and accepted HAB evidence remain historical and unchanged.

Pre-publication fetch also found related remote correction
`2abbe5a64e4017b8fc30ba243e3fe4c30f509a3c` (`fix: harden Sentinel-1 asset identity`).
Its two source/test changes were reviewed and preserved as ancestors via a
fast-forward, with no merge commit or history rewrite. A 22-file external recovery
backup and temporary stash protected local completion work. Twenty non-overlapping
files restored byte-identically; the resolver matching conflict combined upstream
polarization/root checks with defensive malformed-URL handling. Both added upstream
tests remain. Temporary recovery stash d128ae2 remains retained separately from the
two original safety stashes; no stash was dropped or applied over another worktree.

## Twelve-path WIP review

| Original path | Review / completion |
|---|---|
| `config/default.toml` | Minimal SAR service settings retained; no AS-202 numerics. |
| `src/aquasentinel/catalog/stac.py` | Optional no-cloud query and all-page semantics retained; offline pagination test added. |
| `src/aquasentinel/config/__init__.py` | SAR export retained; no unrelated exports changed. |
| `src/aquasentinel/config/loader.py` | SAR section/host tuple loading retained; default/legacy load tests added. |
| `src/aquasentinel/config/models.py` | Frozen provider/collection/host and HTTPS configuration validated. |
| `src/aquasentinel/ingestion/sentinel1.py` | Focused public exports retained, complete models/access API exposed. |
| `src/aquasentinel/ingestion/sentinel1_policy.py` | Deep immutable metadata, source/group/set fingerprints, coverage and derived registry lineage added. |
| `src/aquasentinel/ingestion/sentinel1_resolver.py` | Native product checks, duplicate/ambiguous records, same-source paths and footprint normalization hardened. |
| `src/aquasentinel/ingestion/sentinel1_metadata.py` | Chained overview IFDs, exact ranges/budgets, schema/identity/nonempty XML structures hardened. |
| `tests/catalog/test_stac_non_optical.py` | No-cloud query retained; real client consumes synthetic paginated pages. |
| `tests/config/test_sar.py` | Frozen endpoints/hosts/collection, timeout and TOML defaults tested. |
| `tests/ingestion/test_sentinel1.py` | Weak empty XML/SubIFD fixtures replaced with valid nonempty structures/chained directories; original behaviors retained. |

Additional focused files: metadata coverage module, adversarial contract tests,
structural PC transport typing, Shapely pin and implementation/continuity evidence.
First full gate exposed two integration fixtures: optical catalog text replacement
also changed the new SAR endpoint, and a transport test expected OpticalConfig
typing. Scoped endpoint replacement and the shared Protocol annotation fix those
fixtures; functional/security checks and optical algorithms remain unchanged.
That diagnostic run was 2 failed / 1427 passed / six existing warnings (36.99s);
the actual final gate below supersedes it, without hiding the initial failure.

## Completed handoff and acceptance scope

Exact fixed CDSE/native → PC mapping; acquisition start AND end at microsecond
precision, S1A/IW/GRD(H)/ascending/orbit101/VV+VH, strict cardinality and no fallback.
All six slots remain in three chronological two-slice groups. `UNAVAILABLE` is
explicit, `RESOLVED_NOT_ACCESSED` is not access acceptance, and readiness requires
six `AVAILABLE` header/XML-validated VV sources. Auxiliary VH identity/reference is
retained; no VH scientific dependency or inferred calibration/noise validation.

Metadata footprint topology is canonical WGS84 MultiPolygon. Date unions,
envelope intersections, three-date common support and gap polygons are retained.
Missing footprint inventory is a lower bound, not a pixel-validity assertion.
Shapely 2.1.2 is justified by arbitrary polygon topology; it performs no pixel
operation or geodetic petroleum-area calculation.

Immutable source/group/set metadata, deterministic SHA-256 and stable unsigned
serialization feed an explicit derived retrieval record with CDSE discovery and
PC access parents. Canonical sorted-key compact UTF-8 strict finite JSON excludes
creation/request time and credentials. All-missing sets have no invented source
lineage. Registry registration is explicit and conflict checked; generic
SourceRecord/DerivedProductRecord/schema are unchanged. Re-registration compares
canonical stable parameters/lineage/type/version, ignoring creation time and
list/tuple representation; it retains the original record and rejects genuine
semantic conflicts. No new disk-cache schema.

TIFF checks traverse classic little-endian metadata directories (including next-IFD
overviews), not image offsets; exact 206/Content-Range and budgets bound access.
Actual native dimensions govern, not reversed `proj:shape`. One-band uint16,
ZSTD/1024²/nodata0, six overview levels, finite geographic tiepoints/GeoKeys and
absence of a native affine are checked. Metadata/image-block overlap is rejected.
XML roots, native product/platform/mode/acquisition/orbit/polarization, dimensions,
nonempty finite LUT/geolocation structures and per-slice thermal state are checked.
No LUT is applied. Known `schema-product-vv` RFI mislabel is not trusted; only known
same-native-product normalized manifest/product/calibration/noise paths are used.

Shared token/signing subsystem is reused through configuration Protocol typing;
its runtime behavior and optical algorithms were not rewritten. Stable assets
require unsigned allowlisted HTTPS, effective443/no userinfo/no fragments.
Unsafe redirects/ranges and signed failure diagnostics are rejected/sanitized;
transient signed values are cleared in finally and never enter identity/provenance.

## Offline test matrix

Source identity/interval/mode/orbit/product/polarization; zero/duplicate/invalid
provider matches with no replacement; no cloud query and all-page pagination;
wrong native asset root/polarization; raw/calibrated/RTC/unknown representation;
actual header dimensions, chained overviews/cycles/budgets/image-span overlap;
XML root/RFI/header/identity/empty/count/LUT/geolocation/finite checks; missing XML;
per-source true/false/unknown thermal state; VH retained without pixel use;
source/group/common support and gaps; immutable copied metadata; canonical geometry;
order/time-independent fingerprints; tampered derived lineage rejection and explicit
registry integration and reload/repeat across creation-time or tuple/list differences;
SAS/credentials/nonfinite stable-boundary rejection; unsafe
host/port/userinfo/fragment/redirect; exact range/full-response rejection; sanitized
failures. Synthetic six-source header/XML acceptance explicitly prohibits rasterio.open.

## Actual M48 engineering gates

- Focused AS-201 offline suite: **147 passed in 0.88s**.
- Final integrated full repository `python -m pytest -v`: **1432 passed,
  six existing Rasterio PendingDeprecationWarnings in 35.58s**.
- Ruff: **All checks passed!**; tracked and new-file whitespace: **PASS**.
- Strict JSON, finite-number rejection, independent canonical identity
  reconstruction/deterministic repeat and credential/SAS scan: **PASS**.
- Pre-remote-integration gate: 1429 passed / six warnings (37.21s); the final
  integrated run retains the remote commit's two additional tests.
- No actual GitHub CI check success is claimed.
- Evidence semantic SHA-256: `b644156c028badf29778828b88e1cf5b7d417d3c2c7d14b8f787b7882f9bfda9`;
  sorted-key compact UTF-8 strict JSON over `semantic`, excluding gate runtime and
  preservation inventory. This is implementation evidence, not a SAR science product.

## Preservation

Snapshot: 151 tracked hashes before edits. Only scoped AS-201/interface/fixture/
continuity paths change. All other tracked files and 32 prior accepted evidence
files (including M47 design) are byte-identical. Frozen Decision 050/051/052/053/054
section hashes match the pre-edit snapshot; no Decision 055 exists. Generic
provenance and optical/temporal/HAB algorithms remain unchanged.

Protected external files: **44/44 SHA-256 unchanged**; **57/57 modes unchanged**.
No scientific cache/raster artifact created. Both original safety stashes remain:
`f93950aab6fdfb40bb100158915ef12692aa1665` and
`d979a433a5ab8ae600282048f184eb5fd06a8f17`.
Original inventory entries remain untouched; additional temporary recovery stash
`d128ae2a00e61e28db274f682666e21361a69efb` is deliberately retained.
External recovery backup `/tmp/as201-m48/remote-advance-recovery` remains available.
All follow-up files are non-executable (Git 100644; workspace local 0600/0644).

## Network / scientific accounting and limitations

Live CDSE/PC metadata, signing, TIFF range and XML requests: **0 each**.
EO asset requests/bytes: **0 / 0**. SAR pixel read calls/bytes: **0 / 0**.
Real scientific SAR compute calls: **0**. Synthetic engineering metadata arithmetic
is not radiometric calibration or scientific SAR processing. Existing full-suite
optical/HAB fixtures are engineering tests, not real EO reruns. No live M48 probe.
Package installation of the pinned Shapely dependency is separate from EO/provider
traffic; no unrelated dependency upgraded.

This completes offline AS-201 source engineering, not live six-slice readiness,
calibrated backscatter, slick detection, petroleum/source confirmation, water
safety or shutdown advice. M46 historical access is not relabelled M48 real
acceptance. Metadata support may overstate actual usable pixels; source gaps and
access failures remain explicit. Reference is not an oil negative; follow-up is
not recovery. No scientific output or candidate geometry was generated.

Next: owner implementation review → separately authorized PR/merge. Any further
provider metadata acceptance and AS-202 design require separate owner direction.
AS-202 NOT STARTED. Decision 055 ABSENT. No PR/merge in this task.
