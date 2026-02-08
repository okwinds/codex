# `codex-rs/app-server-protocol/schema/typescript/v2/Model.ts`

## Identity
- kind: `source`
- ext: `.ts`
- size_bytes: `642`
- sha256: `3526262d12003c5c91959e41219fd99d72b93e16e465c93b7690ec8cf94d6056`
- generated_utc: `2026-02-08T10:45:14Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server-protocol/schema/typescript/v2/Model.ts` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `export type Model = { id: string, model: string, upgrade: string | null, displayName: string, description: string, supportedReasoningEfforts: Array<ReasoningEffortOption>, defaultReasoningEffort: ReasoningEffort, inputModalities: Array<InputModality>, supportsPersonality: boolean, isDefault: boolean, };`

## Definitions (auto, per-file)
- `import` `codex-rs/app-server-protocol/schema/typescript/v2/Model.ts:4` `import type { InputModality } from "../InputModality";`
- `import` `codex-rs/app-server-protocol/schema/typescript/v2/Model.ts:5` `import type { ReasoningEffort } from "../ReasoningEffort";`
- `import` `codex-rs/app-server-protocol/schema/typescript/v2/Model.ts:6` `import type { ReasoningEffortOption } from "./ReasoningEffortOption";`
- `export` `codex-rs/app-server-protocol/schema/typescript/v2/Model.ts:8` `export type Model = { id: string, model: string, upgrade: string | null, displayName: string, description: string, supportedReasoningEfforts: Array<ReasoningEffortOption>, defaultReasoningEffort: ReasoningEffort, inputModalities: Array<InputModality>, supportsPersonality: boolean, isDefault: boolean, };`

## Dependencies (auto sample)
### Imports / Includes
- `import type { InputModality } from "../InputModality";`
- `import type { ReasoningEffort } from "../ReasoningEffort";`
- `import type { ReasoningEffortOption } from "./ReasoningEffortOption";`
- `export type Model = { id: string, model: string, upgrade: string | null, displayName: string, description: string, supportedReasoningEfforts: Array<ReasoningEffortOption>, defaultReasoningEffort: ReasoningEffort, inputModalities: Array<InputModality>, supportsPersonality: boolean, isDefault: boolean, };`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
