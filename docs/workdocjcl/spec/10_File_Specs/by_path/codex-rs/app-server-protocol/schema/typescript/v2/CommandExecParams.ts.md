# `codex-rs/app-server-protocol/schema/typescript/v2/CommandExecParams.ts`

## Identity
- kind: `source`
- ext: `.ts`
- size_bytes: `354`
- sha256: `ea0918150de91f93466cb0b6e47eb496d7c6db54f2e092d2b87f82776e7a1363`
- generated_utc: `2026-02-08T10:45:14Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server-protocol/schema/typescript/v2/CommandExecParams.ts` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `export type CommandExecParams = { command: Array<string>, timeoutMs?: number | null, cwd?: string | null, sandboxPolicy?: SandboxPolicy | null, };`

## Definitions (auto, per-file)
- `import` `codex-rs/app-server-protocol/schema/typescript/v2/CommandExecParams.ts:4` `import type { SandboxPolicy } from "./SandboxPolicy";`
- `export` `codex-rs/app-server-protocol/schema/typescript/v2/CommandExecParams.ts:6` `export type CommandExecParams = { command: Array<string>, timeoutMs?: number | null, cwd?: string | null, sandboxPolicy?: SandboxPolicy | null, };`

## Dependencies (auto sample)
### Imports / Includes
- `import type { SandboxPolicy } from "./SandboxPolicy";`
- `export type CommandExecParams = { command: Array<string>, timeoutMs?: number | null, cwd?: string | null, sandboxPolicy?: SandboxPolicy | null, };`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- has retry/timeout/backoff logic

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
