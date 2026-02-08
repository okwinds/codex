# `codex-rs/app-server-protocol/schema/typescript/v2/ToolRequestUserInputParams.ts`

## Identity
- kind: `source`
- ext: `.ts`
- size_bytes: `451`
- sha256: `8f460bcc0408f291ec9fe2f81ea87cc2072dba95db5d2869fb3b31aa77c01481`
- generated_utc: `2026-02-08T10:45:14Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server-protocol/schema/typescript/v2/ToolRequestUserInputParams.ts` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `export type ToolRequestUserInputParams = { threadId: string, turnId: string, itemId: string, questions: Array<ToolRequestUserInputQuestion>, };`

## Definitions (auto, per-file)
- `import` `codex-rs/app-server-protocol/schema/typescript/v2/ToolRequestUserInputParams.ts:4` `import type { ToolRequestUserInputQuestion } from "./ToolRequestUserInputQuestion";`
- `export` `codex-rs/app-server-protocol/schema/typescript/v2/ToolRequestUserInputParams.ts:9` `export type ToolRequestUserInputParams = { threadId: string, turnId: string, itemId: string, questions: Array<ToolRequestUserInputQuestion>, };`

## Dependencies (auto sample)
### Imports / Includes
- `import type { ToolRequestUserInputQuestion } from "./ToolRequestUserInputQuestion";`
- `export type ToolRequestUserInputParams = { threadId: string, turnId: string, itemId: string, questions: Array<ToolRequestUserInputQuestion>, };`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
