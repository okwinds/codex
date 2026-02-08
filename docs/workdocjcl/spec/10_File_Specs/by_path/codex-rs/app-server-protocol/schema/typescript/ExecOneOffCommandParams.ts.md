# `codex-rs/app-server-protocol/schema/typescript/ExecOneOffCommandParams.ts`

## Identity
- kind: `source`
- ext: `.ts`
- size_bytes: `357`
- sha256: `3008a65c6a47e937a104c9a0870ce1e672d436e2c0b257f09310555335a0b837`
- generated_utc: `2026-02-08T10:45:14Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server-protocol/schema/typescript/ExecOneOffCommandParams.ts` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `export type ExecOneOffCommandParams = { command: Array<string>, timeoutMs: bigint | null, cwd: string | null, sandboxPolicy: SandboxPolicy | null, };`

## Definitions (auto, per-file)
- `import` `codex-rs/app-server-protocol/schema/typescript/ExecOneOffCommandParams.ts:4` `import type { SandboxPolicy } from "./SandboxPolicy";`
- `export` `codex-rs/app-server-protocol/schema/typescript/ExecOneOffCommandParams.ts:6` `export type ExecOneOffCommandParams = { command: Array<string>, timeoutMs: bigint | null, cwd: string | null, sandboxPolicy: SandboxPolicy | null, };`

## Dependencies (auto sample)
### Imports / Includes
- `import type { SandboxPolicy } from "./SandboxPolicy";`
- `export type ExecOneOffCommandParams = { command: Array<string>, timeoutMs: bigint | null, cwd: string | null, sandboxPolicy: SandboxPolicy | null, };`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- has retry/timeout/backoff logic

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
