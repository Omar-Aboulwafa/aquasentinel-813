# AS-201 M57 — Manifest Platform familyName Scope / Casing Correction

## Result and authorization

**M57 / E57 / EV-061: OFFLINE MANIFEST PLATFORM FAMILYNAME INTEROPERABILITY CORRECTION PASS.**
Official main: `cea91ab8b7fa8dbf4618a32c0a51ea1b2356f721`.
Chronology remains main → M55 live FAIL `ff00aafed870b0f427532159c4eb4ac3d08691d9`
→ M56 diagnostic `839b593a6f79722235494ab40c6df345ea17c7de` → M57 offline fix.
M56's sole parent is M55; both published heads and evidence verified unchanged.
Fresh branch: `fix/as-201-manifest-platform-familyname`, exactly from M56.
M57/E57/EV-061 were unused before allocation. No new Decision; 055 remains absent.

Goal: correct only the manifest platform identity representation diagnosed in M56.
Inputs: M56's six minimal structural facts and existing synthetic metadata fixtures
for the exact six frozen source policies. Outputs: one narrow production change,
one contract test file and six docs/evidence paths; no dependencies.
Acceptance: observed representation crosses the complete offline metadata contract;
invalid direct identity/cardinality remains fail-closed; all prior guards preserved.
Non-goals: live retry, provider requests, pixel access, SAR science, AS-202, PR/merge.

## Proven empirical facts reused, not re-retrieved

M56 [MD](AS_201_MANIFEST_PLATFORM_DIAGNOSTIC.md) / [JSON](AS_201_MANIFEST_PLATFORM_DIAGNOSTIC.json)
proved all six manifests have one platform, direct `familyName = SENTINEL-1`, number
`A`, and nested `instrument/familyName = Synthetic Aperture Radar`, abbreviation
`SAR`. Direct-child order: nssdcIdentifier, familyName, number, instrument.
Recursive lookup mixed the two distinct family texts and raised a cardinality error.
The later exact literal `Sentinel-1` also differed by case. No provider defect or
formal XML-schema compliance claim is made. No M55 or M56 rerun occurred.

## Exact production diff

Only `src/aquasentinel/ingestion/sentinel1_metadata.py` changes:

```diff
diff --git a/src/aquasentinel/ingestion/sentinel1_metadata.py b/src/aquasentinel/ingestion/sentinel1_metadata.py
index 32fc6d5..f11bf19 100644
--- a/src/aquasentinel/ingestion/sentinel1_metadata.py
+++ b/src/aquasentinel/ingestion/sentinel1_metadata.py
@@ -330,8 +330,15 @@ def _validate_manifest(root, expected):
     platforms = [e for e in root.iter() if _local(e.tag) == "platform"]
     if len(platforms) != 1 or _unique_text(platforms[0], "number") != "A":
         raise Sentinel1MetadataError("Manifest platform mismatch.")
-    family = _unique_text(platforms[0], "familyName")
-    if family != "Sentinel-1":
+    families = [e for e in platforms[0] if _local(e.tag).lower() == "familyname"]
+    if (
+        len(families) != 1
+        or not isinstance(families[0].text, str)
+        or not families[0].text.strip()
+    ):
+        raise Sentinel1MetadataError("Manifest requires one nonempty direct platform familyName.")
+    family = families[0].text.strip()
+    if family.casefold() != "Sentinel-1".casefold():
         raise Sentinel1MetadataError("Manifest platform family mismatch.")
     hrefs = [v for e in root.iter() for k, v in e.attrib.items() if _local(k) == "href"]
     parts = expected.native_source_product_id.lower().split("_")
```

At the manifest boundary only, iterate immediate children of the already uniquely
validated platform. Retain existing case-insensitive local-name matching; require
**exactly one direct familyName element**, even if duplicate texts would be equal.
Require string text with nonempty `.strip()`. Surrounding benign whitespace retains
existing XML text semantics. Compare that stripped text using `.casefold()` to
`Sentinel-1.casefold()` only. Internal whitespace and punctuation are not rewritten;
no alias, substring, prefix/suffix or broad mission regex is introduced.
Nested instrument families cannot contaminate or rescue direct platform identity.
The exact platform-number `A` guard, including its existing recursive selection,
is unchanged. All preceding and later guards are byte-identical.

## Complete six-source offline matrix

| Role / slice | Direct family | Nested instrument family | Full metadata validator | Summary vs original fixture |
|---|---|---|---|---|
| REFERENCE / 1 | `SENTINEL-1` | `Synthetic Aperture Radar` | PASS | Equal |
| REFERENCE / 2 | `SENTINEL-1` | `Synthetic Aperture Radar` | PASS | Equal |
| DOCUMENTARY_EVENT / 1 | `SENTINEL-1` | `Synthetic Aperture Radar` | PASS | Equal |
| DOCUMENTARY_EVENT / 2 | `SENTINEL-1` | `Synthetic Aperture Radar` | PASS | Equal |
| LATE_FOLLOW_UP / 1 | `SENTINEL-1` | `Synthetic Aperture Radar` | PASS | Equal |
| LATE_FOLLOW_UP / 2 | `SENTINEL-1` | `Synthetic Aperture Radar` | PASS | Equal |

These are synthetic fixtures reproducing M56's platform structure, not retrieved
provider XML. Exact frozen acquisition intervals use M54's permitted naive manifest
UTC representation; original product/calibration/noise fixtures stay strict.
Each of the six sources also passes with direct `Sentinel-1`, `sentinel-1`, and
surrounding whitespace; every complete summary equals the existing fixture result.
No later live PASS is inferred.

## Regression matrix

| Group | Added cases | Required outcome |
|---|---:|---|
| Six frozen sources × four benign case/text forms | 24 | Complete metadata summary equals original |
| Instrument family absent, empty, SAR, OTHER, SENTINEL-2, Sentinel-1 | 6 | Valid direct platform identity unaffected |
| Missing/None/empty/whitespace-only direct text, identical/conflicting/empty duplicates, incompatible mission and prefix/suffix/internal-space variants | 20 | FAIL even with valid nested Sentinel-1 |
| Shared recursive helpers unchanged | 1 | Original two-value lookup still raises; scoped manifest validation passes |
| Existing 18 tamper controls, additionally with nested M56 structure | 18 | Every preceding/later guard rejects tampering |
| **Total newly collected cases** | **69** | **PASS** |

Fail-closed mission examples: SENTINEL-2, Synthetic Aperture Radar, SENTINEL,
Sentinel_1, Sentinel-1A, prefix-Sentinel-1, Sentinel-1-suffix, Sentinel-10,
Sentinel -1, Sentinel- 1, Sentinel 1 and an internal newline.
An otherwise valid direct element plus an empty/None second element also fails.
Existing original-fixture guard controls remain retained.

Existing M54 tests continue to cover six sources × four timestamp serializations,
exact microsecond/second mismatches, swapped/invalid times, strict generic naive-time
rejection, strict non-manifest ADS/LUT times, and XML/native-witness/dimensions/
geolocation/incidence/calibration/noise/thermal tampering. No test was weakened.
Source-level proof: the entire production file equals its parent plus the one shown
replacement. Shared `_texts`, `_unique_text`, `_parse_manifest_time`, ADS/LUT helpers
and policy `_parse_time` source slices have identical before/after hashes in JSON.

## Actual engineering gates and integrity

**330 focused tests PASS (1.19 s);
1617 full tests PASS (37.41 s), six existing Rasterio
PendingDeprecationWarnings.** Ruff PASS; diff and new-file whitespace PASS.
Both test runs used an external engineering runner that forbids real socket
connections; zero connection attempts occurred. Repository tests remain synthetic.
No GitHub CI-success claim.

Strict finite JSON, independent semantic digest reconstruction with different object
insertion order, deterministic repeat and credential/signed-URL scans PASS.
Semantic SHA-256: **`a9efe173ca065f0b9f096b75491e3be7281ef7b4d8edcff18aa2d5e9ff62be25`**.
Canonical UTF-8 JSON uses sorted keys, compact separators, stable arrays,
ensure_ascii=False and allow_nan=False; only `semantic` is hashed. Engineering
results/preservation summaries are excluded. No signed URLs or credential material.

All non-authorized tracked hashes unchanged. M49–M56 and all accepted scientific
evidence, Decisions 050–054 entire file, policy/resolver/shared STAC/optical/config/
dependencies byte-identical. **44 protected external hashes / 57 modes / three
stashes unchanged**, recovery artifacts retained; no new scientific product/cache.

## Zero provider / SAR-science accounting

CDSE, PC STAC, signing, token, manifest GET, TIFF, other XML, ZIP, image-block
requests **0**; SAR pixel reads/bytes **0/0**; scientific SAR compute **0**.
Git fetch/push and offline synthetic engineering tests are distinct from provider
activity. No live script or accepted scientific workflow was executed.

## Interpretation and next boundary

**M55 remains HISTORICAL LIVE FAIL. M56 remains DIAGNOSTIC COMPLETE.
LIVE_READINESS remains UNPROVED. AS-202 NOT STARTED. Decision 055 ABSENT.**
M57 proves only that the exact representation diagnosed in M56 crosses the complete
offline metadata-validation contract; later live XML guards remain unproved.
No calibration/noise correction, sigma0/gamma0/dB, reprojection, mosaicking,
filtering or oil detection. No PR or merge.
Next: owner review → separately authorized publication/merge → separately
authorized controlled live engineering acceptance. No live retry in M57.
