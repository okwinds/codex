# `codex-rs/app-server-protocol/schema/typescript/CollaborationModeMask.ts`

## Identity
- kind: `source`
- ext: `.ts`
- size_bytes: `597`
- sha256: `9526b0d4de04fa8a005d7afa4a089f18c7b770933faf42b2cc5c1c0f11b1d833`
- generated_utc: `2026-02-08T10:45:14Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server-protocol/schema/typescript/CollaborationModeMask.ts` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `export type CollaborationModeMask = { name: string, mode: ModeKind | null, model: string | null, reasoning_effort: ReasoningEffort | null | null, developer_instructions: string | null | null, };`

## Definitions (auto, per-file)
- `import` `codex-rs/app-server-protocol/schema/typescript/CollaborationModeMask.ts:4` `import type { ModeKind } from "./ModeKind";`
- `import` `codex-rs/app-server-protocol/schema/typescript/CollaborationModeMask.ts:5` `import type { ReasoningEffort } from "./ReasoningEffort";`
- `export` `codex-rs/app-server-protocol/schema/typescript/CollaborationModeMask.ts:11` `export type CollaborationModeMask = { name: string, mode: ModeKind | null, model: string | null, reasoning_effort: ReasoningEffort | null | null, developer_instructions: string | null | null, };`

## Dependencies (auto sample)
### Imports / Includes
- `import type { ModeKind } from "./ModeKind";`
- `import type { ReasoningEffort } from "./ReasoningEffort";`
- `export type CollaborationModeMask = { name: string, mode: ModeKind | null, model: string | null, reasoning_effort: ReasoningEffort | null | null, developer_instructions: string | null | null, };`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
