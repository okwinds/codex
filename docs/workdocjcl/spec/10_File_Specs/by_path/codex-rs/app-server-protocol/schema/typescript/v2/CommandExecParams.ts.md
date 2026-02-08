# `codex-rs/app-server-protocol/schema/typescript/v2/CommandExecParams.ts`

## Identity
- kind: `source`
- ext: `.ts`
- size_bytes: `351`
- sha256: `6577fed820ef782b45936304492a14c1219ba9c3bb2acdd21c0240bcb8f1ec54`
- generated_utc: `2026-02-03T16:08:28Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server-protocol/schema/typescript/v2/CommandExecParams.ts` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `export type CommandExecParams = { command: Array<string>, timeoutMs: number | null, cwd: string | null, sandboxPolicy: SandboxPolicy | null, };`

## Definitions (auto, per-file)
- `import` `codex-rs/app-server-protocol/schema/typescript/v2/CommandExecParams.ts:4` `import type { SandboxPolicy } from "./SandboxPolicy";`
- `export` `codex-rs/app-server-protocol/schema/typescript/v2/CommandExecParams.ts:6` `export type CommandExecParams = { command: Array<string>, timeoutMs: number | null, cwd: string | null, sandboxPolicy: SandboxPolicy | null, };`

## Dependencies (auto sample)
### Imports / Includes
- `import type { SandboxPolicy } from "./SandboxPolicy";`
- `export type CommandExecParams = { command: Array<string>, timeoutMs: number | null, cwd: string | null, sandboxPolicy: SandboxPolicy | null, };`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- has retry/timeout/backoff logic

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
