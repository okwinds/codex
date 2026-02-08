# `codex-rs/app-server-protocol/schema/typescript/McpStartupCompleteEvent.ts`

## Identity
- kind: `source`
- ext: `.ts`
- size_bytes: `340`
- sha256: `630336a5effce842b51348cb6b59b04aacc50064c82cedaaa703cf7b39b01545`
- generated_utc: `2026-02-03T16:08:28Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server-protocol/schema/typescript/McpStartupCompleteEvent.ts` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `export type McpStartupCompleteEvent = { ready: Array<string>, failed: Array<McpStartupFailure>, cancelled: Array<string>, };`

## Definitions (auto, per-file)
- `import` `codex-rs/app-server-protocol/schema/typescript/McpStartupCompleteEvent.ts:4` `import type { McpStartupFailure } from "./McpStartupFailure";`
- `export` `codex-rs/app-server-protocol/schema/typescript/McpStartupCompleteEvent.ts:6` `export type McpStartupCompleteEvent = { ready: Array<string>, failed: Array<McpStartupFailure>, cancelled: Array<string>, };`

## Dependencies (auto sample)
### Imports / Includes
- `import type { McpStartupFailure } from "./McpStartupFailure";`
- `export type McpStartupCompleteEvent = { ready: Array<string>, failed: Array<McpStartupFailure>, cancelled: Array<string>, };`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
