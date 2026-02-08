# `codex-rs/app-server-protocol/schema/typescript/ErrorEvent.ts`

## Identity
- kind: `source`
- ext: `.ts`
- size_bytes: `297`
- sha256: `03ad0e37d759f1a44d4523b16f85477d616fc6798c08fff3e3579d6b54d59fa0`
- generated_utc: `2026-02-08T10:45:14Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server-protocol/schema/typescript/ErrorEvent.ts` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `export type ErrorEvent = { message: string, codex_error_info: CodexErrorInfo | null, };`

## Definitions (auto, per-file)
- `import` `codex-rs/app-server-protocol/schema/typescript/ErrorEvent.ts:4` `import type { CodexErrorInfo } from "./CodexErrorInfo";`
- `export` `codex-rs/app-server-protocol/schema/typescript/ErrorEvent.ts:6` `export type ErrorEvent = { message: string, codex_error_info: CodexErrorInfo | null, };`

## Dependencies (auto sample)
### Imports / Includes
- `import type { CodexErrorInfo } from "./CodexErrorInfo";`
- `export type ErrorEvent = { message: string, codex_error_info: CodexErrorInfo | null, };`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
