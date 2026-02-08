# `codex-rs/app-server-protocol/schema/typescript/v2/ThreadStartResponse.ts`

## Identity
- kind: `source`
- ext: `.ts`
- size_bytes: `565`
- sha256: `beeaabfea5f98b2ed7905203647492586290b322e77d19101aa84fe6a0b2464b`
- generated_utc: `2026-02-08T10:45:14Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server-protocol/schema/typescript/v2/ThreadStartResponse.ts` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `export type ThreadStartResponse = { thread: Thread, model: string, modelProvider: string, cwd: string, approvalPolicy: AskForApproval, sandbox: SandboxPolicy, reasoningEffort: ReasoningEffort | null, };`

## Definitions (auto, per-file)
- `import` `codex-rs/app-server-protocol/schema/typescript/v2/ThreadStartResponse.ts:4` `import type { ReasoningEffort } from "../ReasoningEffort";`
- `import` `codex-rs/app-server-protocol/schema/typescript/v2/ThreadStartResponse.ts:5` `import type { AskForApproval } from "./AskForApproval";`
- `import` `codex-rs/app-server-protocol/schema/typescript/v2/ThreadStartResponse.ts:6` `import type { SandboxPolicy } from "./SandboxPolicy";`
- `import` `codex-rs/app-server-protocol/schema/typescript/v2/ThreadStartResponse.ts:7` `import type { Thread } from "./Thread";`
- `export` `codex-rs/app-server-protocol/schema/typescript/v2/ThreadStartResponse.ts:9` `export type ThreadStartResponse = { thread: Thread, model: string, modelProvider: string, cwd: string, approvalPolicy: AskForApproval, sandbox: SandboxPolicy, reasoningEffort: ReasoningEffort | null, };`

## Dependencies (auto sample)
### Imports / Includes
- `import type { ReasoningEffort } from "../ReasoningEffort";`
- `import type { AskForApproval } from "./AskForApproval";`
- `import type { SandboxPolicy } from "./SandboxPolicy";`
- `import type { Thread } from "./Thread";`
- `export type ThreadStartResponse = { thread: Thread, model: string, modelProvider: string, cwd: string, approvalPolicy: AskForApproval, sandbox: SandboxPolicy, reasoningEffort: ReasoningEffort | null, };`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
