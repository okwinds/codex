# `codex-rs/app-server-protocol/schema/typescript/v2/ToolRequestUserInputResponse.ts`

## Identity
- kind: `source`
- ext: `.ts`
- size_bytes: `415`
- sha256: `39e4959095a1b31de3f7bf28422a6536d51d651581ad1f50bc5e30c02140498b`
- generated_utc: `2026-02-03T16:08:28Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server-protocol/schema/typescript/v2/ToolRequestUserInputResponse.ts` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `export type ToolRequestUserInputResponse = { answers: { [key in string]?: ToolRequestUserInputAnswer }, };`

## Definitions (auto, per-file)
- `import` `codex-rs/app-server-protocol/schema/typescript/v2/ToolRequestUserInputResponse.ts:4` `import type { ToolRequestUserInputAnswer } from "./ToolRequestUserInputAnswer";`
- `export` `codex-rs/app-server-protocol/schema/typescript/v2/ToolRequestUserInputResponse.ts:9` `export type ToolRequestUserInputResponse = { answers: { [key in string]?: ToolRequestUserInputAnswer }, };`

## Dependencies (auto sample)
### Imports / Includes
- `import type { ToolRequestUserInputAnswer } from "./ToolRequestUserInputAnswer";`
- `export type ToolRequestUserInputResponse = { answers: { [key in string]?: ToolRequestUserInputAnswer }, };`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
