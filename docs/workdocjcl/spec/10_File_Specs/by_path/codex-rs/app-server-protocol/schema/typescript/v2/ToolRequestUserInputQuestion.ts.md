# `codex-rs/app-server-protocol/schema/typescript/v2/ToolRequestUserInputQuestion.ts`

## Identity
- kind: `source`
- ext: `.ts`
- size_bytes: `509`
- sha256: `d0eaa32baa3b41a8ee3a3b764e84ffd75f7474f385eebeb779fe61f18deb2b24`
- generated_utc: `2026-02-08T10:45:14Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server-protocol/schema/typescript/v2/ToolRequestUserInputQuestion.ts` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `export type ToolRequestUserInputQuestion = { id: string, header: string, question: string, isOther: boolean, isSecret: boolean, options: Array<ToolRequestUserInputOption> | null, };`

## Definitions (auto, per-file)
- `import` `codex-rs/app-server-protocol/schema/typescript/v2/ToolRequestUserInputQuestion.ts:4` `import type { ToolRequestUserInputOption } from "./ToolRequestUserInputOption";`
- `export` `codex-rs/app-server-protocol/schema/typescript/v2/ToolRequestUserInputQuestion.ts:9` `export type ToolRequestUserInputQuestion = { id: string, header: string, question: string, isOther: boolean, isSecret: boolean, options: Array<ToolRequestUserInputOption> | null, };`

## Dependencies (auto sample)
### Imports / Includes
- `import type { ToolRequestUserInputOption } from "./ToolRequestUserInputOption";`
- `export type ToolRequestUserInputQuestion = { id: string, header: string, question: string, isOther: boolean, isSecret: boolean, options: Array<ToolRequestUserInputOption> | null, };`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
