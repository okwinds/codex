# `codex-rs/app-server-protocol/schema/typescript/LocalShellExecAction.ts`

## Identity
- kind: `source`
- ext: `.ts`
- size_bytes: `341`
- sha256: `7f579ad71d9ac2ecfc94bea32e05d229b4d653eb0fb5491afc7a53ccaaaf8672`
- generated_utc: `2026-02-03T16:08:28Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server-protocol/schema/typescript/LocalShellExecAction.ts` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `export type LocalShellExecAction = { command: Array<string>, timeout_ms: bigint | null, working_directory: string | null, env: { [key in string]?: string } | null, user: string | null, };`

## Definitions (auto, per-file)
- `export` `codex-rs/app-server-protocol/schema/typescript/LocalShellExecAction.ts:5` `export type LocalShellExecAction = { command: Array<string>, timeout_ms: bigint | null, working_directory: string | null, env: { [key in string]?: string } | null, user: string | null, };`

## Dependencies (auto sample)
### Imports / Includes
- `export type LocalShellExecAction = { command: Array<string>, timeout_ms: bigint | null, working_directory: string | null, env: { [key in string]?: string } | null, user: string | null, };`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- has retry/timeout/backoff logic

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
