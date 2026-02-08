# `codex-rs/app-server-protocol/schema/typescript/v2/GetAccountRateLimitsResponse.ts`

## Identity
- kind: `source`
- ext: `.ts`
- size_bytes: `294`
- sha256: `23a13aa7d9c3c428fb5c4d3add6a52c4738a3b98f94267444a0b1df4a61e44ec`
- generated_utc: `2026-02-08T10:45:14Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server-protocol/schema/typescript/v2/GetAccountRateLimitsResponse.ts` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `export type GetAccountRateLimitsResponse = { rateLimits: RateLimitSnapshot, };`

## Definitions (auto, per-file)
- `import` `codex-rs/app-server-protocol/schema/typescript/v2/GetAccountRateLimitsResponse.ts:4` `import type { RateLimitSnapshot } from "./RateLimitSnapshot";`
- `export` `codex-rs/app-server-protocol/schema/typescript/v2/GetAccountRateLimitsResponse.ts:6` `export type GetAccountRateLimitsResponse = { rateLimits: RateLimitSnapshot, };`

## Dependencies (auto sample)
### Imports / Includes
- `import type { RateLimitSnapshot } from "./RateLimitSnapshot";`
- `export type GetAccountRateLimitsResponse = { rateLimits: RateLimitSnapshot, };`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
