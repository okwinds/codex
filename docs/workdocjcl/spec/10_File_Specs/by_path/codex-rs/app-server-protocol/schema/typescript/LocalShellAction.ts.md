# `codex-rs/app-server-protocol/schema/typescript/LocalShellAction.ts`

## Identity
- kind: `source`
- ext: `.ts`
- size_bytes: `295`
- sha256: `4cbe0baf839752c8aa69a3f93ce236236c7ffb9b3bcdcb6d1133a5493c5445cf`
- generated_utc: `2026-02-08T10:45:14Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server-protocol/schema/typescript/LocalShellAction.ts` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `export type LocalShellAction = { "type": "exec" } & LocalShellExecAction;`

## Definitions (auto, per-file)
- `import` `codex-rs/app-server-protocol/schema/typescript/LocalShellAction.ts:4` `import type { LocalShellExecAction } from "./LocalShellExecAction";`
- `export` `codex-rs/app-server-protocol/schema/typescript/LocalShellAction.ts:6` `export type LocalShellAction = { "type": "exec" } & LocalShellExecAction;`

## Dependencies (auto sample)
### Imports / Includes
- `import type { LocalShellExecAction } from "./LocalShellExecAction";`
- `export type LocalShellAction = { "type": "exec" } & LocalShellExecAction;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
