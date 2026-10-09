# Decision 049 / AS-102 — Reusable PC SAS Transport Validation

**Record:** EV-026 / M22 / E22.
**Date:** 9 October 2026 (Asia/Dubai).
**Status:** Implemented, offline and bounded transport smoke PASS; UNCOMMITTED,
not pushed/merged, no PR. READY FOR REVIEW, not AS-104 acceptance.
**Worktree:** `/workspace/aquasentinel-813-pc-sas-token-fix`.
**Branch:** `fix/as-102-reusable-pc-sas-token`.
**Exact base:** `39f2aee90c727fc151886efbdea44daec0e3f9b4`, merged PR #10.

## 1. Problem and chronology

AS-104 implementation exposed PC processing-product ambiguity. Decision 048
added explicit baseline selection and was merged via PR #10. AS-104 then resumed
and hit intermittent per-asset PC `/sign` HTTP 504s. This separately authorized
Decision 049 fix follows that transport failure. Previously the cold AS-102 path
required eleven authentication calls: nine bands, SCL and product XML.

The prior read-only diagnostic observed three B02 504s (~15.2 seconds each) and
metadata responses 200/504/200. No 429 was observed: rate limiting is not proven.
A corrected authorized replacement token diagnostic observed anonymous token
HTTP 200 and two tiny HTTP 206 reads. Its first discarded response reflected an
overly strict local permission check, not a demonstrated provider failure.

The original worktree retains Decision 047/M19/E18–E19/EV-022–EV-023 and the later
transport blocker M21/E21/EV-025. Their record bodies are not copied here. M20 /
E20 / EV-024 retain the original Decision 048 checkpoint; this report records
the later transport experiment as M22/E22/EV-026.

## 2. Authoritative protocol evidence

Official [SDK sas.py](https://github.com/microsoft/planetary-computer-sdk-for-python/blob/90ef249ef0ab92045e39a8400fa30eddf14d3c37/planetary_computer/sas.py),
[settings.py](https://github.com/microsoft/planetary-computer-sdk-for-python/blob/90ef249ef0ab92045e39a8400fa30eddf14d3c37/planetary_computer/settings.py)
and [SAS OpenAPI](https://planetarycomputer.microsoft.com/api/sas/v1/openapi.json)
establish the account/container token route, `token` and `msft:expiry` fields,
memory reuse and transient status list. Only this small behavior is reproduced
using the standard library; the SDK is not installed or added as a dependency.
Decision 049 requires refresh at <=60 seconds, including exactly 60 seconds.

## 3. Implemented transport contract

- `sign_asset(href: str, settings: OpticalConfig) -> str` is unchanged.
- Strict existing unsigned HREF allowlist/HTTPS/effective-443/userinfo/query/
  fragment/whitespace checks run before acquisition.
- Derive account from the allowed `.blob.core.windows.net` hostname and container
  from the first path segment; Azure naming rules reject ambiguous scopes.
- Map the configured HTTPS `/api/sas/v1/sign` route (optional trailing slash) to
  `/api/sas/v1/token/{account}/{container}`. Canonical issuer hostname and port
  form the credential-free key; implicit/explicit 443 are equivalent. Retain
  other validated issuer ports, without changing asset-port requirements.
- Private in-process dictionary; no disk token cache, key/config/env requirement.
  Token material is excluded from representation/equality.
- One GET is bounded to 16,384 bytes and uses configured per-request timeout.
  Response must be JSON object with nonempty usable query material (including
  nonempty signature) and timezone-aware `msft:expiry` more than 60 seconds away.
  Reject unsafe characters, malformed encoding/query, duplicate/empty fields,
  missing/invalid expiry and near-expiry tokens before caching. Do not invent
  a restriction requiring permission `sp` to be exactly read-only `r`.
- Same issuer/account/container can reuse across assets and scenes; refresh at
  exactly/below 60 seconds or expiry. No credential enters stable metadata.
- At most five total acquisition attempts. Retry only 429/500/502/503/504 or
  typed transient connection/timeouts, including temporary DNS EAI_AGAIN and
  selected temporary connection errno values. Untyped URLError strings,
  permanent DNS, other HTTP statuses, malformed responses, unsafe scopes and
  type/programming errors are terminal. Backoff 0.8/1.6/3.2/6.4 seconds; no sleep
  after success or final failure. No read_bytes/XML/GDAL retry changes.
- Construct transient signed HREF locally, retain encoded path exactly, then
  enforce allowed HTTPS host/effective port/exact original path/nonempty query.
  Errors contain neither raw provider text nor credential-bearing cause/context.

## 4. Offline validation

Run in the fix worktree with existing Python **3.11.16**, explicitly pointing
`PYTHONPATH` to this worktree's `src` and `PYTHONDONTWRITEBYTECODE=1`. Reuse the
existing environment without installation; no tests run in the original AS-104
worktree. Canonical commands:

```text
python -m pytest tests/preprocessing/test_transport.py -q
python -m pytest -v
python -m ruff check .
git diff --check
```

Results: **145 transport cases passed**; **531 full-suite tests passed**
(421 merged-main baseline +110 net new cases); Ruff PASS; diff check PASS.
Six existing Rasterio PendingDeprecationWarnings only, from windows.py transform
multiplication in the same three read/suppression tests. No new warning category.
No GitHub CI success is claimed.

Tests cover eleven-asset/two-scene reuse, isolated account/container/issuer/port,
canonical issuer and asset host/port, cached/new expiry boundaries, actual schema,
malformed/missing/unsafe material (including excessive JSON nesting), provider read/list permissions, each transient
status, terminal statuses including 408/501, later/last-attempt success, exactly
five failures/backoffs, typed transient and permanent/programming errors,
pre-request unsigned/scope/issuer validation, final resource security, response
size/timeout/no subscription header, private token representation/equality,
stable-source bytes/cache identity, public signature and synthetic SAS persistence.
Existing bounded HTTP/redirect/sanitization tests remain passing.

The first full suite passed before minor Ruff corrections; the corrected-source
offline gate passed **528 tests in 10.62 seconds** before the live experiment.
Ruff initially identified UTC/import/type/expiry style issues in new code; those
were corrected within authorized source/tests before live access. Final review
also added empty-delimiter rejection and sanitized excessive-JSON-nesting failure.
The final gate passed **531 tests in 10.91 seconds**, with the same six warnings;
Ruff and tracked/new-file whitespace checks passed.

## 5. Fresh live bounded smoke — direct observations

Experiment: `2026-10-09T06:44:49.076690+00:00`–
`2026-10-09T06:44:51.406274+00:00` UTC / approximately
`2026-10-09T10:44:49.076896+04:00`–`2026-10-09T10:44:51.406274+04:00`
Asia/Dubai. Fresh process with private token cache empty. Imports used fix source.

Actual PC item: `S2A_MSIL2A_20230304T064751_R020_T40RBN_20230304T113736`.
Validated identity: Sentinel-2A; acquisition `2023-03-04T06:47:51.024000+00:00`;
tile 40RBN; relative orbit 20; baseline **05.09**; generation
`2023-03-04T11:37:36.492429Z`.

All eleven actual unsigned assets (B02/B03/B04/B05/B06/B07/B08/B8A/B11/SCL/
product-metadata) had the identical derived scope:

- HTTPS hostname: `sentinel2l2a01.blob.core.windows.net`.
- Storage account: `sentinel2l2a01`.
- Container: `sentinel2-l2`.
- Derived request: `https://planetarycomputer.microsoft.com/api/sas/v1/token/sentinel2l2a01/sentinel2-l2`.

| Gate | Direct result | Limit |
|---|---|---|
| Cold token acquisition | **1 HTTP attempt**, HTTP **200**, **0.561498 s**, 1 successful transient token/cache entry | Anonymous availability at this instant only |
| Initial asset signing | **11/11 PASS**, original scheme/hostname/effective-port/exact path preserved, query present | Signed HREFs discarded after validation |
| Product XML minimal read | UTC `06:44:50.275486`; HTTP **206**; **1,024 bytes**; **0.596899 s**; XML prefix confirmed | Prefix only, no full XML decoding |
| B02 header-range read | UTC `06:44:50.872415`; HTTP **206**; **4,096 bytes**; **0.519146 s**; TIFF magic and Content-Range confirmed | Header only, no raster pixels/open/processing |
| Cache reuse | B03, SCL and XML signed again: **3/3 PASS**, **0 additional token HTTP attempts**, lifetime >60 seconds | Same process/scope while valid |
| Credential scan | **0 live-token/signature matches** in tracked/nonignored fix-worktree files | Comparison in memory; only count persisted |

The two bounded reads each used another cached sign call; the 11/11 result counts
the initial asset loop only. No acquisition retry was needed in this successful
live run; retry limits/backoff are verified offline, not induced on the provider.
No full scene, raster window/pixels, AS-102 product, AS-103 or AS-104 run.

A first local smoke attempt at `06:44:40.430596` UTC read item metadata but stopped
before any token request because the diagnostic used `mgrs_tile` instead of the
existing identity field `tile`. The external helper was corrected, then the
fresh successful experiment above ran. This was a diagnostic error, not a
transport or provider failure, and no repository caller change was made.

## 6. Identity, credentials and preservation

No live token, signature, signed HREF or provider body was printed or persisted.
Only safe summaries were written outside the repository; evidence contains no
credential query. Private cache and diagnostic signed URLs were cleared at exit.
Known synthetic SAS values in tests are explicitly fake, not leak findings.

Only the transport implementation and its tests change executable behavior.
Existing `validate_asset_href`, `_SameHostRedirect` and `read_bytes` are AST
identical to main; all callers, GDAL settings, dependency/config files, generic
provenance, cache schema, decoding, grid, masks, resampling and AS-103 code remain
byte-identical to the base. Stable unsigned source bytes and identity remain
independent of transient token state. No accepted manifest is rewritten.

Read-only before/after inventory of the original worktree verifies its branch
`feature/as-104-temporal-baseline`, HEAD
`39f2aee90c727fc151886efbdea44daec0e3f9b4`, full status and **83 working files**
remain identical. Retained safety stash
`f93950aab6fdfb40bb100158915ef12692aa1665` remains intact and unapplied.
Accepted April cache ID remains
`0725a908d21cd655e83f70d2bb11247dc0f1516f0c00ea275efc3239113ee4a6`:

- arrays SHA-256: `01512aa7ec3e1deab0f87fddb9c3888986d449ebcdd440830a7d4805bbc4f4a1`.
- manifest SHA-256: `9a5ca8d78b663426fd53732a52db387c15fe8a70acb2da93978a9f466ce15589`.

Both unchanged. No fix-worktree AS-102 cache directory/product created.

## 7. Limits and next gate

No concurrent single-flight or cross-process credential sharing guarantee;
private cache is intentionally process-local. Anonymous issuer availability and
network access remain external limitations. Unsupported blob scope/issuer routes
fail explicitly. Transport-only success does not prove full raster processing,
five usable March histories, AS-104 acceptance, radiometric validity, HAB,
chlorophyll, toxin/species, water safety, operational risk, alert or lead time.

Owner review/merge of Decision 049 must precede separately resuming AS-104 real
acceptance. AS-104 implementation stays uncommitted/preserved. No commit, push,
PR or merge in this task. AS-105+ and P1 homogeneous-05.10 experiment NOT started.
