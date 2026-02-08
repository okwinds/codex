# `codex-rs/app-server-protocol/schema/typescript/TurnStartedEvent.ts`

## Identity
- kind: `source`
- ext: `.ts`
- size_bytes: `305`
- sha256: `2659072ca62aba1b0d7aba5bb7438b1bd2907bc4ebe15f23d8f2d5431a6cec5f`
- generated_utc: `2026-02-08T10:45:14Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server-protocol/schema/typescript/TurnStartedEvent.ts` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `export type TurnStartedEvent = { model_context_window: bigint | null, collaboration_mode_kind: ModeKind, };`

## Definitions (auto, per-file)
- `import` `codex-rs/app-server-protocol/schema/typescript/TurnStartedEvent.ts:4` `import type { ModeKind } from "./ModeKind";`
- `export` `codex-rs/app-server-protocol/schema/typescript/TurnStartedEvent.ts:6` `export type TurnStartedEvent = { model_context_window: bigint | null, collaboration_mode_kind: ModeKind, };`

## Dependencies (auto sample)
### Imports / Includes
- `import type { ModeKind } from "./ModeKind";`
- `export type TurnStartedEvent = { model_context_window: bigint | null, collaboration_mode_kind: ModeKind, };`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
