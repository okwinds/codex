# `codex-rs/app-server-protocol/schema/typescript/TokenCountEvent.ts`

## Identity
- kind: `source`
- ext: `.ts`
- size_bytes: `374`
- sha256: `913ead30bf5e2905c175759fc6368f6fdc4a83c0ee1971661d3f35d8f65d98a4`
- generated_utc: `2026-02-03T16:08:28Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server-protocol/schema/typescript/TokenCountEvent.ts` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `export type TokenCountEvent = { info: TokenUsageInfo | null, rate_limits: RateLimitSnapshot | null, };`

## Definitions (auto, per-file)
- `import` `codex-rs/app-server-protocol/schema/typescript/TokenCountEvent.ts:4` `import type { RateLimitSnapshot } from "./RateLimitSnapshot";`
- `import` `codex-rs/app-server-protocol/schema/typescript/TokenCountEvent.ts:5` `import type { TokenUsageInfo } from "./TokenUsageInfo";`
- `export` `codex-rs/app-server-protocol/schema/typescript/TokenCountEvent.ts:7` `export type TokenCountEvent = { info: TokenUsageInfo | null, rate_limits: RateLimitSnapshot | null, };`

## Dependencies (auto sample)
### Imports / Includes
- `import type { RateLimitSnapshot } from "./RateLimitSnapshot";`
- `import type { TokenUsageInfo } from "./TokenUsageInfo";`
- `export type TokenCountEvent = { info: TokenUsageInfo | null, rate_limits: RateLimitSnapshot | null, };`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
