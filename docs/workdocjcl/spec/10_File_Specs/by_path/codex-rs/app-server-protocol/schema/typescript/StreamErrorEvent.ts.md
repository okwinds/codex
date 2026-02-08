# `codex-rs/app-server-protocol/schema/typescript/StreamErrorEvent.ts`

## Identity
- kind: `source`
- ext: `.ts`
- size_bytes: `514`
- sha256: `adbcfa09cd1fb6fd4b75671c6613dbc7921631be8295a1e21736da714381d391`
- generated_utc: `2026-02-03T16:08:28Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server-protocol/schema/typescript/StreamErrorEvent.ts` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `export type StreamErrorEvent = { message: string, codex_error_info: CodexErrorInfo | null,`

## Definitions (auto, per-file)
- `import` `codex-rs/app-server-protocol/schema/typescript/StreamErrorEvent.ts:4` `import type { CodexErrorInfo } from "./CodexErrorInfo";`
- `export` `codex-rs/app-server-protocol/schema/typescript/StreamErrorEvent.ts:6` `export type StreamErrorEvent = { message: string, codex_error_info: CodexErrorInfo | null,`

## Dependencies (auto sample)
### Imports / Includes
- `import type { CodexErrorInfo } from "./CodexErrorInfo";`
- `export type StreamErrorEvent = { message: string, codex_error_info: CodexErrorInfo | null,`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
