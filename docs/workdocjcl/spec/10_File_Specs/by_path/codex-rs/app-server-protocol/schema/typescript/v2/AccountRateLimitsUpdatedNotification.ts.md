# `codex-rs/app-server-protocol/schema/typescript/v2/AccountRateLimitsUpdatedNotification.ts`

## Identity
- kind: `source`
- ext: `.ts`
- size_bytes: `302`
- sha256: `6a4e8c2297d95bf89eccead5419b4b12cd481832627774d47e31c77f81c6fc54`
- generated_utc: `2026-02-03T16:08:28Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server-protocol/schema/typescript/v2/AccountRateLimitsUpdatedNotification.ts` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `export type AccountRateLimitsUpdatedNotification = { rateLimits: RateLimitSnapshot, };`

## Definitions (auto, per-file)
- `import` `codex-rs/app-server-protocol/schema/typescript/v2/AccountRateLimitsUpdatedNotification.ts:4` `import type { RateLimitSnapshot } from "./RateLimitSnapshot";`
- `export` `codex-rs/app-server-protocol/schema/typescript/v2/AccountRateLimitsUpdatedNotification.ts:6` `export type AccountRateLimitsUpdatedNotification = { rateLimits: RateLimitSnapshot, };`

## Dependencies (auto sample)
### Imports / Includes
- `import type { RateLimitSnapshot } from "./RateLimitSnapshot";`
- `export type AccountRateLimitsUpdatedNotification = { rateLimits: RateLimitSnapshot, };`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
