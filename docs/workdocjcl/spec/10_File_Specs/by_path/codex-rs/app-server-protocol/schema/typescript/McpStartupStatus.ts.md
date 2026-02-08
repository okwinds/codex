# `codex-rs/app-server-protocol/schema/typescript/McpStartupStatus.ts`

## Identity
- kind: `source`
- ext: `.ts`
- size_bytes: `299`
- sha256: `46398a38d9a841204a1c5912ec2392864eed74d7a6ced089ef45b7052a0bffd9`
- generated_utc: `2026-02-08T10:45:14Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server-protocol/schema/typescript/McpStartupStatus.ts` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `export type McpStartupStatus = { "state": "starting" } | { "state": "ready" } | { "state": "failed", error: string, } | { "state": "cancelled" };`

## Definitions (auto, per-file)
- `export` `codex-rs/app-server-protocol/schema/typescript/McpStartupStatus.ts:5` `export type McpStartupStatus = { "state": "starting" } | { "state": "ready" } | { "state": "failed", error: string, } | { "state": "cancelled" };`

## Dependencies (auto sample)
### Imports / Includes
- `export type McpStartupStatus = { "state": "starting" } | { "state": "ready" } | { "state": "failed", error: string, } | { "state": "cancelled" };`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
