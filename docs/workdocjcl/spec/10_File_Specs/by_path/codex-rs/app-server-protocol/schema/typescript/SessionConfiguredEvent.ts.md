# `codex-rs/app-server-protocol/schema/typescript/SessionConfiguredEvent.ts`

## Identity
- kind: `source`
- ext: `.ts`
- size_bytes: `1565`
- sha256: `6b61e6ee48e93b63215daf83b23832b7517b3ba8b65cf611a76debb33c2c70eb`
- generated_utc: `2026-02-08T10:45:14Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server-protocol/schema/typescript/SessionConfiguredEvent.ts` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `export type SessionConfiguredEvent = { session_id: ThreadId, forked_from_id: ThreadId | null,`

## Definitions (auto, per-file)
- `import` `codex-rs/app-server-protocol/schema/typescript/SessionConfiguredEvent.ts:4` `import type { AskForApproval } from "./AskForApproval";`
- `import` `codex-rs/app-server-protocol/schema/typescript/SessionConfiguredEvent.ts:5` `import type { EventMsg } from "./EventMsg";`
- `import` `codex-rs/app-server-protocol/schema/typescript/SessionConfiguredEvent.ts:6` `import type { ReasoningEffort } from "./ReasoningEffort";`
- `import` `codex-rs/app-server-protocol/schema/typescript/SessionConfiguredEvent.ts:7` `import type { SandboxPolicy } from "./SandboxPolicy";`
- `import` `codex-rs/app-server-protocol/schema/typescript/SessionConfiguredEvent.ts:8` `import type { ThreadId } from "./ThreadId";`
- `export` `codex-rs/app-server-protocol/schema/typescript/SessionConfiguredEvent.ts:10` `export type SessionConfiguredEvent = { session_id: ThreadId, forked_from_id: ThreadId | null,`

## Dependencies (auto sample)
### Imports / Includes
- `import type { AskForApproval } from "./AskForApproval";`
- `import type { EventMsg } from "./EventMsg";`
- `import type { ReasoningEffort } from "./ReasoningEffort";`
- `import type { SandboxPolicy } from "./SandboxPolicy";`
- `import type { ThreadId } from "./ThreadId";`
- `export type SessionConfiguredEvent = { session_id: ThreadId, forked_from_id: ThreadId | null,`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
