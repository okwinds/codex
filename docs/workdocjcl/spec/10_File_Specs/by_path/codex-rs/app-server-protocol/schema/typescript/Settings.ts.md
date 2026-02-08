# `codex-rs/app-server-protocol/schema/typescript/Settings.ts`

## Identity
- kind: `source`
- ext: `.ts`
- size_bytes: `381`
- sha256: `75a444fb4aa9ce8c906871e5eedeaa04f4da1943fe89906725be16f582044066`
- generated_utc: `2026-02-03T16:08:28Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server-protocol/schema/typescript/Settings.ts` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `export type Settings = { model: string, reasoning_effort: ReasoningEffort | null, developer_instructions: string | null, };`

## Definitions (auto, per-file)
- `import` `codex-rs/app-server-protocol/schema/typescript/Settings.ts:4` `import type { ReasoningEffort } from "./ReasoningEffort";`
- `export` `codex-rs/app-server-protocol/schema/typescript/Settings.ts:9` `export type Settings = { model: string, reasoning_effort: ReasoningEffort | null, developer_instructions: string | null, };`

## Dependencies (auto sample)
### Imports / Includes
- `import type { ReasoningEffort } from "./ReasoningEffort";`
- `export type Settings = { model: string, reasoning_effort: ReasoningEffort | null, developer_instructions: string | null, };`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
