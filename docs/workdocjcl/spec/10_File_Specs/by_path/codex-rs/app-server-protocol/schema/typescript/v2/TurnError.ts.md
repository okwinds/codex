# `codex-rs/app-server-protocol/schema/typescript/v2/TurnError.ts`

## Identity
- kind: `source`
- ext: `.ts`
- size_bytes: `328`
- sha256: `afe278dbea975cc5da56cbdfe02f55064c3085d294c1e61c2a5b6b61f5e77786`
- generated_utc: `2026-02-08T10:45:14Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server-protocol/schema/typescript/v2/TurnError.ts` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `export type TurnError = { message: string, codexErrorInfo: CodexErrorInfo | null, additionalDetails: string | null, };`

## Definitions (auto, per-file)
- `import` `codex-rs/app-server-protocol/schema/typescript/v2/TurnError.ts:4` `import type { CodexErrorInfo } from "./CodexErrorInfo";`
- `export` `codex-rs/app-server-protocol/schema/typescript/v2/TurnError.ts:6` `export type TurnError = { message: string, codexErrorInfo: CodexErrorInfo | null, additionalDetails: string | null, };`

## Dependencies (auto sample)
### Imports / Includes
- `import type { CodexErrorInfo } from "./CodexErrorInfo";`
- `export type TurnError = { message: string, codexErrorInfo: CodexErrorInfo | null, additionalDetails: string | null, };`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
