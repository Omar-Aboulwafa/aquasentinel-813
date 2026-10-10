# AS-201 M47 — Retrieval Design Freeze Evidence

**11 October 2026 (Asia/Dubai); M47 / E47 / EV-051; Decision 054 FINAL / FROZEN
DESIGN / NOT IMPLEMENTED.** Documentation/policy only. No candidate pixels/SAR science.
Base `9a8a15c489a6aa3e678b642d2ccf5160affc56bd`, PR #28, exact parents
`865cd14398c6bcdbeaed6a19210f5615beb638e6` /
`83d18db82d818cfe43710ffcc43839c241be7142`, verified from Git; clean isolated
`docs/as-201-design-freeze`, `/workspace/aquasentinel-813-as201-m47`.
Git merge subject/tree/parents establish PR #28 merge; no invented GitHub API timestamp.
AS-107 closed; AS-108 merged PARTIALLY_CONSISTENT with unavailable POST preserved.

## Historical predecessor audits, not retroactive repository edits

M45 / E45 / EV-049: read-only Sentinel-1 feasibility/metadata audit COMPLETE.
M46 / E46 / EV-050: read-only provider/access/representation gate COMPLETE / PASS.
Both identifiers were unused as recorded checkpoints; M47 records them historically,
not as claims they wrote repository files. M47/E47/EV-051 and Decision 054 unused
before work. Earlier mentions of absent Decision 054 remain historical.
Accepted facts are supplied in owner M47 authorization, supplemented by already
existing read-only local M46 continuation metadata. Prior temporary reports are
**not** repository artifacts; compact accepted facts are now in this JSON.
No new inventories, TIFF/XML access, RTC/Sentinel Hub requests or geometry calculation.

M46 historical GRD access blocker became PASS after allowlist update. Six fixed
VV plus one representative VH headers: **224 ranges, 115,563 header bytes**, zero
image-block overlap/pixel reads. TIFF uint16/nodata0, ZSTD/1024², six overviews,
geographic tiepoints. Seven validated header dimensions are retained in JSON.
Historical XML access: **3,298,504 bytes**, bounded representative metadata only.
The wrongly labelled RFI asset, two 404 annotation attempts, and later successful
main product annotation are retained, not rewritten into first-attempt success.
Manifest/product/calibration/noise identities matched representative May6 A43B.
27 calibration / 27 range-noise / 3 azimuth-noise vectors and noise-correction=false
are representative facts, not universal slice counts. VH LUT contents not inspected.
Historical audit network counts are explicitly separate from M47's zero EO requests.

## Frozen design and evidence authority

The [canonical contract](../AS_201_SENTINEL1_RETRIEVAL.md) states exact six mappings,
all typed fields, security/cache/lineage rules and unfrozen AS-202 numerical choices.
Decision 054 repeats that policy text; `design` in [JSON](AS_201_DESIGN_FREEZE.json)
is its machine-readable contract. No silent provider/date/polarization fallback.
Both slices mandatory. Envelope [49.60,28.60,50.70,29.60] retains southern documentary
context; rejected narrower envelope is not the P0 AOI. Source gaps explicit,
direct comparisons common three-date support. Coverage summaries are metadata area,
not petroleum area. Data Desk facts supplied externally, not independently fetched.

## Digest and integrity

Schema `as201-m47-design-freeze-v1`; SHA-256 **`11ce3efc96f62a539be899162b418718cd5ece9a8438cb44a1a4dce356a6f7f2`** over `design` only.
UTF-8 sorted compact JSON, ensure_ascii=false, allow_nan=false; semantic lists fixed.
Independent parser/serialization reconstruction and repeat must match. Duplicate
keys, NaN/Infinity rejected. Publication/engineering timestamps/statuses excluded.
Pre-edit snapshot: all 141 tracked hashes; Decisions 050–053 section hashes;
30 external file hashes and 44 file/directory modes; complete stash inventory.
Protected acceptance bundles, handoffs, recovery files and scientific caches are
read-only. Accepted AS-107/M42/M43/M44 evidence must remain byte-identical.
Quality/preservation results are recorded below after actual execution.

## Execution boundary and presentation handoff

M47 EO metadata/asset requests, EO bytes, SAR pixel reads and scientific compute
calls: **0 / 0 / 0 / 0 / 0**. Git fetch/push and synthetic repository engineering
tests only. No GitHub CI success claimed. No SAS, signed query or credential persisted.
“Before looking for dark pixels, AquaSentinel froze the same-track Sentinel-1
sequence and raw-data contract.” Apr24 → May6 → May18, S1A ascending orbit101,
two slices/date. Timeline/coverage/metadata-defect cards are **proposed**, not
existing screenshots. No oil candidate exists from these access/design audits.
Owner review/PR/merge and later AS-201 implementation require separate authorization.
AS-201 implementation/AS-202 NOT STARTED; Decision055 absent; no PR/merge in M47.

## Actual M47 engineering and preservation results

- Python 3.11 existing environment: **1,285 tests passed in 36.40s**;
  six existing Rasterio PendingDeprecationWarnings, no failures/skips.
- Ruff PASS; tracked diff and all three new-file whitespace checks PASS.
- Strict finite JSON/no duplicate keys, independent design digest and deterministic
  repeat PASS; credential/SAS/signed-URL scan PASS; exactly eight authorized paths.
- Decisions 050/051/052/053 complete frozen sections byte-identical; source/tests/
  configuration/dependencies and **136 non-authorized tracked files** byte-identical.
  All accepted AS-107, M42, M43, M44 evidence unchanged. Decision055 absent.
- Pre-edit external snapshot: **30 file hashes / 44 modes** unchanged. Additional
  comparison with the committed M44 protected inventory: **44 hashes / 57 modes**
  match, including **14 accepted AS-102 cache files**; no cache product was created.
  Sealed acceptance/handoff/recovery material retained without permission changes.
- Complete stash inventory unchanged, including
  `f93950aab6fdfb40bb100158915ef12692aa1665` and
  `d979a433a5ab8ae600282048f184eb5fd06a8f17`; neither applied/dropped/rewritten.
- M47 EO metadata/asset requests, bytes, SAR pixel reads and scientific compute
  calls remain **zero**. Package-local engineering tests do not represent real
  SAR processing. No GitHub CI success claimed.

These are design/documentation engineering results, not SAR detection acceptance.
