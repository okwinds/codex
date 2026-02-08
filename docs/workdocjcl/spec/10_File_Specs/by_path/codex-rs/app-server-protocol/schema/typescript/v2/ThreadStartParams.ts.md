# `codex-rs/app-server-protocol/schema/typescript/v2/ThreadStartParams.ts`

## Identity
- kind: `source`
- ext: `.ts`
- size_bytes: `899`
- sha256: `bb44a4fef10aab02e8c9c379482474ee034ab58545400c51a7e5ee46b6727cf0`
- generated_utc: `2026-02-08T10:45:14Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server-protocol/schema/typescript/v2/ThreadStartParams.ts` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `export type ThreadStartParams = {model?: string | null, modelProvider?: string | null, cwd?: string | null, approvalPolicy?: AskForApproval | null, sandbox?: SandboxMode | null, config?: { [key in string]?: JsonValue } | null, baseInstructions?: string | null, developerInstructions?: string | null, personality?: Personality | null, ephemeral?: boolean | null, /**`

## Definitions (auto, per-file)
- `import` `codex-rs/app-server-protocol/schema/typescript/v2/ThreadStartParams.ts:4` `import type { Personality } from "../Personality";`
- `import` `codex-rs/app-server-protocol/schema/typescript/v2/ThreadStartParams.ts:5` `import type { JsonValue } from "../serde_json/JsonValue";`
- `import` `codex-rs/app-server-protocol/schema/typescript/v2/ThreadStartParams.ts:6` `import type { AskForApproval } from "./AskForApproval";`
- `import` `codex-rs/app-server-protocol/schema/typescript/v2/ThreadStartParams.ts:7` `import type { SandboxMode } from "./SandboxMode";`
- `export` `codex-rs/app-server-protocol/schema/typescript/v2/ThreadStartParams.ts:9` `export type ThreadStartParams = {model?: string | null, modelProvider?: string | null, cwd?: string | null, approvalPolicy?: AskForApproval | null, sandbox?: SandboxMode | null, config?: { [key in string]?: JsonValue } | null, baseInstructions?: string | null, developerInstructions?: string | null, personality?: Personality | null, ephemeral?: boolean | null, /**`

## Dependencies (auto sample)
### Imports / Includes
- `import type { Personality } from "../Personality";`
- `import type { JsonValue } from "../serde_json/JsonValue";`
- `import type { AskForApproval } from "./AskForApproval";`
- `import type { SandboxMode } from "./SandboxMode";`
- `export type ThreadStartParams = {model?: string | null, modelProvider?: string | null, cwd?: string | null, approvalPolicy?: AskForApproval | null, sandbox?: SandboxMode | null, config?: { [key in string]?: JsonValue } | null, baseInstructions?: string | null, developerInstructions?: string | null, personality?: Personality | null, ephemeral?: boolean | null, /**`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
