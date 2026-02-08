# `codex-rs/app-server-protocol/schema/typescript/TokenUsageInfo.ts`

## Identity
- kind: `source`
- ext: `.ts`
- size_bytes: `333`
- sha256: `36959e81e3b43790b980a97ed6ae5ca846505a97b1781863c39d95c2150e5080`
- generated_utc: `2026-02-03T16:08:28Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server-protocol/schema/typescript/TokenUsageInfo.ts` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `export type TokenUsageInfo = { total_token_usage: TokenUsage, last_token_usage: TokenUsage, model_context_window: number | null, };`

## Definitions (auto, per-file)
- `import` `codex-rs/app-server-protocol/schema/typescript/TokenUsageInfo.ts:4` `import type { TokenUsage } from "./TokenUsage";`
- `export` `codex-rs/app-server-protocol/schema/typescript/TokenUsageInfo.ts:6` `export type TokenUsageInfo = { total_token_usage: TokenUsage, last_token_usage: TokenUsage, model_context_window: number | null, };`

## Dependencies (auto sample)
### Imports / Includes
- `import type { TokenUsage } from "./TokenUsage";`
- `export type TokenUsageInfo = { total_token_usage: TokenUsage, last_token_usage: TokenUsage, model_context_window: number | null, };`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
