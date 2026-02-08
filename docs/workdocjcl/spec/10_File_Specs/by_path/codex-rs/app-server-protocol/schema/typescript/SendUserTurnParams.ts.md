# `codex-rs/app-server-protocol/schema/typescript/SendUserTurnParams.ts`

## Identity
- kind: `source`
- ext: `.ts`
- size_bytes: `892`
- sha256: `f019e6f42c87501b780c5a01103876efb142a5a7d79f8a1fc918dc22526be03b`
- generated_utc: `2026-02-03T16:08:28Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server-protocol/schema/typescript/SendUserTurnParams.ts` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `export type SendUserTurnParams = { conversationId: ThreadId, items: Array<InputItem>, cwd: string, approvalPolicy: AskForApproval, sandboxPolicy: SandboxPolicy, model: string, effort: ReasoningEffort | null, summary: ReasoningSummary,`

## Definitions (auto, per-file)
- `import` `codex-rs/app-server-protocol/schema/typescript/SendUserTurnParams.ts:4` `import type { AskForApproval } from "./AskForApproval";`
- `import` `codex-rs/app-server-protocol/schema/typescript/SendUserTurnParams.ts:5` `import type { InputItem } from "./InputItem";`
- `import` `codex-rs/app-server-protocol/schema/typescript/SendUserTurnParams.ts:6` `import type { ReasoningEffort } from "./ReasoningEffort";`
- `import` `codex-rs/app-server-protocol/schema/typescript/SendUserTurnParams.ts:7` `import type { ReasoningSummary } from "./ReasoningSummary";`
- `import` `codex-rs/app-server-protocol/schema/typescript/SendUserTurnParams.ts:8` `import type { SandboxPolicy } from "./SandboxPolicy";`
- `import` `codex-rs/app-server-protocol/schema/typescript/SendUserTurnParams.ts:9` `import type { ThreadId } from "./ThreadId";`
- `import` `codex-rs/app-server-protocol/schema/typescript/SendUserTurnParams.ts:10` `import type { JsonValue } from "./serde_json/JsonValue";`
- `export` `codex-rs/app-server-protocol/schema/typescript/SendUserTurnParams.ts:12` `export type SendUserTurnParams = { conversationId: ThreadId, items: Array<InputItem>, cwd: string, approvalPolicy: AskForApproval, sandboxPolicy: SandboxPolicy, model: string, effort: ReasoningEffort | null, summary: ReasoningSummary,`

## Dependencies (auto sample)
### Imports / Includes
- `import type { AskForApproval } from "./AskForApproval";`
- `import type { InputItem } from "./InputItem";`
- `import type { ReasoningEffort } from "./ReasoningEffort";`
- `import type { ReasoningSummary } from "./ReasoningSummary";`
- `import type { SandboxPolicy } from "./SandboxPolicy";`
- `import type { ThreadId } from "./ThreadId";`
- `import type { JsonValue } from "./serde_json/JsonValue";`
- `export type SendUserTurnParams = { conversationId: ThreadId, items: Array<InputItem>, cwd: string, approvalPolicy: AskForApproval, sandboxPolicy: SandboxPolicy, model: string, effort: ReasoningEffort | null, summary: ReasoningSummary,`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
