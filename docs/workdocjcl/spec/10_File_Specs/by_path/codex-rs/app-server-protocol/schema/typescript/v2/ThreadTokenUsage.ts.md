# `codex-rs/app-server-protocol/schema/typescript/v2/ThreadTokenUsage.ts`

## Identity
- kind: `source`
- ext: `.ts`
- size_bytes: `345`
- sha256: `27cae6c3e6c44696225e9a0903e0531c6eff126c6de3da2176bc5cdd904def4e`
- generated_utc: `2026-02-03T16:08:28Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server-protocol/schema/typescript/v2/ThreadTokenUsage.ts` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `export type ThreadTokenUsage = { total: TokenUsageBreakdown, last: TokenUsageBreakdown, modelContextWindow: number | null, };`

## Definitions (auto, per-file)
- `import` `codex-rs/app-server-protocol/schema/typescript/v2/ThreadTokenUsage.ts:4` `import type { TokenUsageBreakdown } from "./TokenUsageBreakdown";`
- `export` `codex-rs/app-server-protocol/schema/typescript/v2/ThreadTokenUsage.ts:6` `export type ThreadTokenUsage = { total: TokenUsageBreakdown, last: TokenUsageBreakdown, modelContextWindow: number | null, };`

## Dependencies (auto sample)
### Imports / Includes
- `import type { TokenUsageBreakdown } from "./TokenUsageBreakdown";`
- `export type ThreadTokenUsage = { total: TokenUsageBreakdown, last: TokenUsageBreakdown, modelContextWindow: number | null, };`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
