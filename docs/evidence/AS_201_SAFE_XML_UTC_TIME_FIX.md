# AS-201 M60 — SAFE XML UTC time interoperability correction

**M60 / E60 / EV-064: OFFLINE SAFE XML UTC-TIME INTEROPERABILITY CORRECTION PASS.**

## Scope and immutable chronology

Official main: `225efc896bf74d87f62741e05a4251ac86d07395`. M58: `376754bed59eedbe9cbce47978ae5a52ae481410`
(`test: complete AS-201 live acceptance after M57`); M59: `dd35cbbce43bfe482bc573408893365e089e950a`
(`test: diagnose Sentinel-1 SAFE XML timestamps`), whose sole parent is M58.
Prepared on `fix/as-201-safe-xml-utc-time-normalization` directly from exact M59.
M60 is one new corrective commit; M58/M59 are not rewritten.

M60/E60/EV-064 were absent before allocation; Decision 055 remains absent.
Changes are confined to the eight authorized paths. No dependency added.

## Authoritative semantics, observed serialization, implemented rule

**Authoritative semantics:** Copernicus / SentiWiki, *Sentinel-1 Product
Specification*, Ref S1-RS-MDA-52-7441, 2025 specification, internal Issue/Revision
3/16/2, document date supplied as 01/10/2025.
Official document library: https://sentiwiki.copernicus.eu/web/s1-documents

Official specification facts supplied in M60 authorization; Codex did not
independently retrieve or inspect the source during M60. This does not claim that
the owner personally performed external inspection. Concise specification
paraphrases: timeType uses UTC and supports microsecond resolution; ADS start/stop
are output-image Zero Doppler UTC times; calibrationVector/azimuthTime and
noiseRangeVector/azimuthTime use timeType.

**Observed serialization:** immutable [M59 MD](AS_201_SAFE_XML_TIME_DIAGNOSTIC.md)
and [JSON](AS_201_SAFE_XML_TIME_DIAGNOSTIC.json), digest `0550fd44fc8a6f6e4a8f1746240587dd108a2faca83b7d41229fd366f16d5fa6`,
recorded 360/360 naive timestamps: 12 product ADS + 12 calibration ADS + 12 noise
ADS + 162 calibration-vector + 162 noise-range times. All had six fractional digits,
no offset/padding/missing/empty/malformed values. All 18 body hashes and lengths
matched M58. M59's historical UTC-review-pending statement remains unchanged;
M60's supplied specification now establishes UTC semantics. No XML was fetched again.

**Implemented interoperability rule:** only the reviewed SAFE XML timeType fields
interpret naive ISO timestamps as UTC. This is application representation
interoperability, not a provider defect. The helper validates raw XML text before
existing text normalization, preserving fail-closed padding behavior. It rejects
non-string/empty/padded text and fractions longer than six digits, uses
`datetime.fromisoformat`, normalizes aware values to UTC, and attaches UTC only to
naive SAFE timeType values. Exceptions remain sanitized at the unchanged public
boundary. Generic catalog/frozen-policy time parsing still requires an offset.

## Production diff

Only blank context-line marker spaces are omitted for Markdown whitespace hygiene.

```diff
diff --git a/src/aquasentinel/ingestion/sentinel1_metadata.py b/src/aquasentinel/ingestion/sentinel1_metadata.py
index f11bf19..37bceb4 100644
--- a/src/aquasentinel/ingestion/sentinel1_metadata.py
+++ b/src/aquasentinel/ingestion/sentinel1_metadata.py
@@ -30,7 +30,6 @@ from aquasentinel.ingestion.sentinel1_policy import (
     Sentinel1RetrievalError,
     Sentinel1RetrievalSet,
     Sentinel1SliceSource,
-    _parse_time,
     _with_fingerprint,
     assemble_retrieval,
 )
@@ -273,6 +272,23 @@ def _parse_xml(xml: bytes, role: str) -> ET.Element:
     return root


+def _parse_safe_metadata_time(root: ET.Element, name: str, field: str) -> datetime:
+    """Parse reviewed SAFE timeType fields, whose specification defines UTC."""
+    raw_values = [e.text for e in root.iter() if _local(e.tag).casefold() == name.casefold()]
+    if any(not isinstance(v, str) or not v or v != v.strip() for v in raw_values):
+        raise Sentinel1MetadataError(f"SAFE {field} must be nonempty unpadded timestamp text.")
+    value = _unique_text(root, name)
+    if re.search(r"[.,]\d{7}", value):
+        raise Sentinel1MetadataError(f"SAFE {field} exceeds microsecond precision.")
+    try:
+        parsed = datetime.fromisoformat(value)
+    except ValueError:
+        raise Sentinel1MetadataError(f"SAFE {field} timestamp is invalid.") from None
+    if parsed.tzinfo is None:
+        parsed = parsed.replace(tzinfo=UTC)
+    return parsed.astimezone(UTC)
+
+
 def _validate_ads_header(root: ET.Element, expected: FrozenSentinel1Source, role: str) -> None:
     headers = [e for e in root.iter() if _local(e.tag) == "adsHeader"]
     if len(headers) != 1:
@@ -282,8 +298,8 @@ def _validate_ads_header(root: ET.Element, expected: FrozenSentinel1Source, role
     product = _unique_text(root, "productType")
     polarisation = _unique_text(root, "polarisation")
     mode = _unique_text(root, "mode")
-    start = _parse_time(_unique_text(root, "startTime"), f"{role}.startTime")
-    stop = _parse_time(_unique_text(root, "stopTime"), f"{role}.stopTime")
+    start = _parse_safe_metadata_time(root, "startTime", f"{role}.startTime")
+    stop = _parse_safe_metadata_time(root, "stopTime", f"{role}.stopTime")
     if mission != "S1A" or product not in {"GRD", "GRDH"}:
         raise Sentinel1MetadataError(f"{role} XML mission/product identity is invalid.")
     if str(polarisation).upper() != "VV" or mode != "IW":
@@ -384,7 +400,7 @@ def _validate_luts(calibration, noise, product):
         if any(a >= b for a, b in pairwise(pixels)):
             raise Sentinel1MetadataError("Calibration coordinates must be ordered.")
         _numeric_values(vector, "line", integers=True)
-        _parse_time(_unique_text(vector, "azimuthTime"), "calibration.azimuthTime")
+        _parse_safe_metadata_time(vector, "azimuthTime", "calibration.azimuthTime")
         for field in ("betaNought", "sigmaNought", "gamma", "dn"):
             values = _numeric_values(vector, field, minimum=0)
             if len(values) != len(pixels) or any(v == 0 for v in values):
@@ -395,7 +411,7 @@ def _validate_luts(calibration, noise, product):
         if len(pixels) != len(values) or any(a >= b for a, b in pairwise(pixels)):
             raise Sentinel1MetadataError("Range noise LUT coordinates/length mismatch.")
         _numeric_values(vector, "line", integers=True)
-        _parse_time(_unique_text(vector, "azimuthTime"), "noise.azimuthTime")
+        _parse_safe_metadata_time(vector, "azimuthTime", "noise.azimuthTime")
     for vector in _vectors(noise, "noiseAzimuthVector"):
         lines = _numeric_values(vector, "line", integers=True)
         values = _numeric_values(vector, "noiseAzimuthLut", minimum=0)
```

Four call sites cover product/calibration/noise ADS start/stop and the two LUT
vector azimuthTime paths. No other timestamp boundary changes. ADS equality stays
exact to frozen source start/stop, including microseconds. No vector timing range,
interval/equality, calibration/noise correspondence or cadence rule is introduced.

## Complete six-source offline matrix

Synthetic fixtures mirror M59's serialization/counts, not its complete provider
XML. Each source has six ADS fields, 27 calibration vectors and 27 noise-range
vectors. The complete existing validator runs, including later metadata checks;
returned metadata summary equals the original aware fixture. Vector times beyond
ADS stop deliberately remain accepted under the existing parse-only contract.

| Frozen source | Naive six digits | Z | +00:00 | Equivalent +04:00 | Complete metadata |
|---|---|---|---|---|---|
| REFERENCE/1 | PASS | PASS | PASS | PASS | PASS |
| REFERENCE/2 | PASS | PASS | PASS | PASS | PASS |
| DOCUMENTARY_EVENT/1 | PASS | PASS | PASS | PASS | PASS |
| DOCUMENTARY_EVENT/2 | PASS | PASS | PASS | PASS | PASS |
| LATE_FOLLOW_UP/1 | PASS | PASS | PASS | PASS | PASS |
| LATE_FOLLOW_UP/2 | PASS | PASS | PASS | PASS | PASS |

All 24 complete representation cases PASS. Eight prior naive-SAFE rejection
expectations were updated because M60 explicitly changes these eight field
requirements; generic strict-parser tests are retained unchanged.

## Rejection and later-guard matrices

- 80 malformed cases: each of eight reviewed field paths rejects empty,
  whitespace-only, leading/trailing padding, malformed ISO, impossible date/time,
  and >6-digit fractions with naive/Z/explicit-offset representations.
  Supplied text does not appear in public exceptions.
- 18 ADS identity cases: each of product/calibration/noise rejects start/stop
  +1 microsecond, start/stop +1 second, swapped intervals and a wrong offset.
  Direct ADS validator confirms the exact mismatch; public wrapper remains sanitized.
- 41 later-guard cases reject calibration coordinate order, LUT length,
  zero/negative/nonfinite values; noise range coordinate order/length; noise
  azimuth order/length/both block bounds; latitude/longitude bounds;
  incidence scalar/nonfinite geolocation; both native spacings; all three ADS
  roles' mission/product/polarization/mode/orbit; sample/line dimensions;
  required beta/sigma/gamma/DN and range/azimuth structures; thermal boolean.
  The complete naive-time bundle passes before each mutation.
- Existing M54 tests retain naive/Z/offset acceptance and exact interval,
  malformed/padded/excess-precision rejection. Existing M57 tests retain direct
  platform scope/cardinality/case-only identity, nested instrument isolation and
  native VV witness. Generic parser naive-input regressions still fail with
  “must be timezone-aware.”

## Preservation proof

Production reverse-diff reconstruction proves the file equals M59 after reversing
only the new helper, unused import removal and four authorized call-site changes.
All other functions are byte-identical, including `_parse_manifest_time`,
`_validate_manifest`, `_texts`, `_unique_text`, transport/TIFF and the complete
validator. ADS/LUT bodies are otherwise byte-identical. Function hashes and the
unchanged generic policy file hash are recorded in the JSON.

All unauthorized tracked files retain snapshot SHA-256: policy/resolver/shared
STAC/optical/config/dependencies, Decisions 050–054, M49–M59 MD/JSON and accepted
scientific evidence. Data inventory unchanged. Protected external file hashes,
modes, recovery artifacts and all three safety stashes are preserved.

Protected inventory: **54 hashes / 67 modes / three unchanged stashes**.

## Engineering quality gates and network boundary

493 focused tests PASS; 1780 full tests PASS; six existing Rasterio
PendingDeprecationWarnings. Ruff PASS; diff/new-file whitespace PASS; strict finite
JSON PASS; independent semantic digest reconstruction/repeat PASS;
credential/signed-URL scan PASS; preservation audit PASS. No GitHub CI claim.
163 new regression cases; eight reviewed expectation changes.

External socket connection attempts in tests: 0. Provider/catalog/sign/token/
TIFF/XML/ZIP/image-block requests: 0. SAR pixel reads/bytes: 0/0.
Calibration/noise application, sigma0/gamma0/dB, reprojection/mosaicking/filtering,
oil detection, real persistence/risk scoring and AS-202 execution: 0.
Only authorized Git fetch/push use network. No M58/M59 rerun.

## Deterministic evidence

Schema `as201-m60-v1`; semantic SHA-256: `307c0515312fbd48e3893c9fc568ac12edd7858258412f0cabf4fc8af19b6e84`. Canonical UTF-8 JSON uses
sorted keys, compact separators, stable arrays, Unicode preserved and nonfinite
values forbidden. Quality gates/environment/publication metadata are outside the
semantic digest. Independent reconstruction with reordered keys and repeat agree.

## Current boundary and next action

M58: HISTORICAL LIVE FAIL. M59: DIAGNOSTIC COMPLETE.
M60: OFFLINE SAFE XML UTC-TIME INTEROPERABILITY CORRECTION PASS.
LIVE_READINESS: UNPROVED. SAR_SCIENTIFIC_READINESS: UNPROVED.
AS-202: NOT STARTED. Decision 055: ABSENT.

Owner review is next. PR, merge and a future controlled live acceptance each
require separate authorization. This complete offline synthetic path does not
prove real downstream metadata readiness or oil-science readiness.
No PR created; no merge performed.
