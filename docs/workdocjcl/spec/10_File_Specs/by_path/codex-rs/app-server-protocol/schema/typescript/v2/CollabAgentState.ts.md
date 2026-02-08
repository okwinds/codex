# `codex-rs/app-server-protocol/schema/typescript/v2/CollabAgentState.ts`

## Identity
- kind: `source`
- ext: `.ts`
- size_bytes: `302`
- sha256: `ea8bb25942c0ac161368f5fabd1252e4a1dabb496819513333f339e6647f3bd4`
- generated_utc: `2026-02-08T10:45:14Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server-protocol/schema/typescript/v2/CollabAgentState.ts` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `export type CollabAgentState = { status: CollabAgentStatus, message: string | null, };`

## Definitions (auto, per-file)
- `import` `codex-rs/app-server-protocol/schema/typescript/v2/CollabAgentState.ts:4` `import type { CollabAgentStatus } from "./CollabAgentStatus";`
- `export` `codex-rs/app-server-protocol/schema/typescript/v2/CollabAgentState.ts:6` `export type CollabAgentState = { status: CollabAgentStatus, message: string | null, };`

## Dependencies (auto sample)
### Imports / Includes
- `import type { CollabAgentStatus } from "./CollabAgentStatus";`
- `export type CollabAgentState = { status: CollabAgentStatus, message: string | null, };`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
