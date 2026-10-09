# AS-102 — Reusable Planetary Computer SAS Token Transport Fix

## Task and goal

Decision 049, explicitly authorized on 9 October 2026 (Asia/Dubai): replace
per-asset authentication with transient account/container tokens. Implement in
`/workspace/aquasentinel-813-pc-sas-token-fix` on
`fix/as-102-reusable-pc-sas-token`, based on PR #10 merge
`39f2aee90c727fc151886efbdea44daec0e3f9b4`. Leave the fix uncommitted for review.

## Existing failure and provider evidence

AS-104 resumed after merged Decision 048 and encountered intermittent PC `/sign`
HTTP 504 responses. The read-only investigation observed three B02 504s at about
15 seconds each and metadata responses 200/504/200. It observed no HTTP 429;
rate limiting is not established. Previously each cold preprocessing scene
required eleven authentication calls: nine reflectance bands, SCL and XML.

The official SDK, pinned to commit
`90ef249ef0ab92045e39a8400fa30eddf14d3c37`, and SAS OpenAPI describe
`/api/sas/v1/token/{account}/{container}`, response fields `token` and
`msft:expiry`, process-memory reuse, a 60-second refresh margin, and transient
statuses 429/500/502/503/504. Authoritative references:

- [SDK sas.py](https://github.com/microsoft/planetary-computer-sdk-for-python/blob/90ef249ef0ab92045e39a8400fa30eddf14d3c37/planetary_computer/sas.py)
- [SDK settings.py](https://github.com/microsoft/planetary-computer-sdk-for-python/blob/90ef249ef0ab92045e39a8400fa30eddf14d3c37/planetary_computer/settings.py)
- [SAS OpenAPI](https://planetarycomputer.microsoft.com/api/sas/v1/openapi.json)

A corrected authorized diagnostic acquired an anonymous token (HTTP 200), then
read only 1,024 XML bytes and a 4,096-byte B02 TIFF header (both HTTP 206). Tokens
were discarded. Availability is an observation, not a service guarantee.

## Inputs, outputs and API compatibility

Inputs remain stable unsigned asset HREFs and `OpticalConfig`. Output remains a
transient signed HREF. Preserve `sign_asset(href: str, settings: OpticalConfig)
-> str`; callers in optical/alignment/assets need no change. No new dependency,
SDK, TOML field, subscription key, environment variable or credential requirement.

## Design, scope and endpoint

First run existing strict unsigned-HREF validation. Derive an Azure account
from the validated `.blob.core.windows.net` hostname and container from the
first path segment, enforcing Azure account/container naming rules. Reject
ambiguous or unsupported scopes; never broaden the host allowlist.

Map only the configured HTTPS `/api/sas/v1/sign` service to
`/api/sas/v1/token/{account}/{container}`. Normalize hostname and effective HTTPS
port, retaining validated issuer scheme/host/port. Reject userinfo, query,
fragment, whitespace or unmappable routes. No arbitrary-host fallback.

## Cache lifecycle and expiry

Use a private process-memory dictionary keyed by the canonical, credential-free
token-request URL (issuer/account/container). No disk cache. Token material is
excluded from object representation and equality. Cache only bounded, valid
JSON containing usable nonempty SAS query material and an aware `msft:expiry`.
Reuse only with remaining lifetime >60 seconds; refresh at exactly 60 seconds,
below 60 seconds or expiry. Reject newly acquired near-expiry tokens too.
Construct a signed HREF locally, then revalidate HTTPS, allowlist, same canonical
host/effective port/exact path and nonempty query. Preserve encoded blob paths.

## Retry and failure behavior

Token acquisition alone gets at most five total attempts. Retry HTTP
429/500/502/503/504 and typed transient connection/timeout failures. Use mocked
sleep in tests and exponential delays 0.8, 1.6, 3.2, 6.4 seconds; no sleep after
success or final failure. Each HTTP request retains `settings.timeout_seconds`.
Terminal 4xx, malformed payloads, invalid scopes, unsafe URLs and programming/type
errors fail without retry. Strip all raw provider exception text and chains.
Do not add read_bytes/XML GET retries or change GDAL/Rasterio settings.

## Security and identity/provenance

Tokens/signed HREFs stay in process memory only, never in logs, exceptions,
documents, processing parameters, provenance, product IDs or cache manifests.
Stable unsigned assets remain authoritative. No AS-102 identity, schema,
decoding, grid, mask, resampling or source model change. Do not rewrite accepted
cache files; compare their hashes and all original-worktree file/status hashes
before and after. Existing synthetic SAS fixtures remain clearly marked fake.

## Files likely to change

Exactly nine authorized paths:

- `docs/AS_102_REUSABLE_PC_SAS_TOKEN_FIX.md`
- `docs/evidence/AS_102_REUSABLE_PC_SAS_TOKEN_FIX_VALIDATION.md`
- `src/aquasentinel/ingestion/planetary_computer.py`
- `tests/preprocessing/test_transport.py`
- `docs/DECISIONS.md`
- `docs/PROJECT_STATE.md`
- `docs/HANDOFF.md`
- `docs/PRESENTATION_JOURNAL.md`
- `docs/evidence/PRESENTATION_EVIDENCE_INDEX.md`

## Validation and acceptance criteria

Test same-scope reuse across eleven assets/scenes; account/container/issuer
isolation; canonical issuer identity; expiry boundaries; malformed/unsafe
payload rejection; all retry statuses; typed transient failures; terminal
failures; exact attempt/backoff limits; signed-HREF security; sanitized exception
chains; unchanged stable source serialization and public API. Retain existing
read_bytes and synthetic-SAS persistence tests.

Run from this fix worktree using the existing Python 3.11 environment, pointing
imports here: `python -m pytest -v`, `python -m ruff check .`,
`git diff --check`, name/stat/status review. Main baseline: 421 tests and six
existing Rasterio PendingDeprecationWarnings; report actual final results.

Only after offline gates pass, in a fresh process, sign the actual eleven assets
of `S2A_MSIL2A_20230304T064751_R020_T40RBN_20230304T113736` (05.09).
Count token HTTP attempts, successful acquisitions and signed assets; goal one
successful acquisition for eleven same-scope assets. Make a bounded 1,024-byte
XML GET and 4,096-byte B02 header-range read using that token. Sign B03/SCL/XML
again without clearing cache and prove no extra acquisition while >60 seconds
remain. Record only safe timestamps, counters, status, latency, bytes and format
confirmation. Never persist/print credentials. No raster processing/cache output.

## AS-104 coordination and historical numbering

The preserved original worktree owns Decision 047, M19/E18–E19/EV-022–EV-023
and later transport blocker M21/E21/EV-025. Do not copy their bodies or renumber
them. Main contains Decision 048/M20/E20/EV-024. This isolated fix owns
Decision 049/M22/E22/EV-026. The chronology is AS-104 implementation → baseline
ambiguity → Decision 048 → resumed AS-104 → transport 504 blocker → Decision 049.
Retain safety stash `f93950aab6fdfb40bb100158915ef12692aa1665` untouched.

## Risks, scientific guardrails and non-goals

Anonymous service can fail; bounded retries do not guarantee availability.
Unsupported scope/issuer fails explicitly. Process cache does not promise
cross-process sharing or concurrent single-flight acquisition. Fix review/merge
must precede AS-104 real acceptance. Transport success proves no HAB, chlorophyll,
toxin/species, water safety, operational risk, alert, lead time, usable March
histories or full raster completion. No AS-104 algorithm changes, AS-105+,
P1 homogeneous-05.10 study, commits, push, PR or merge.

## Execution status

Plan and Decision 049 were written before source edits. Implementation and
offline gates passed: 531 tests, Ruff/diff PASS, six unchanged historical warnings.
Fresh bounded smoke passed with one token HTTP attempt, eleven signs, two tiny
206 reads and zero additional acquisition for reuse. Original worktree, stash
and cache hashes remain unchanged. See the companion validation record for exact
timestamps and limits. Final review state remains uncommitted; no publication or
AS-104 real acceptance.
