# `codex-rs/app-server-protocol/schema/typescript/AgentMessageItem.ts`

## Identity
- kind: `source`
- ext: `.ts`
- size_bytes: `842`
- sha256: `6174368ac90c8f00fcb2233da74ac50cc7b1a3a5e1987c3e7ee4bc43155335d9`
- generated_utc: `2026-02-08T10:45:14Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server-protocol/schema/typescript/AgentMessageItem.ts` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `export type AgentMessageItem = { id: string, content: Array<AgentMessageContent>,`

## Definitions (auto, per-file)
- `import` `codex-rs/app-server-protocol/schema/typescript/AgentMessageItem.ts:4` `import type { AgentMessageContent } from "./AgentMessageContent";`
- `import` `codex-rs/app-server-protocol/schema/typescript/AgentMessageItem.ts:5` `import type { MessagePhase } from "./MessagePhase";`
- `export` `codex-rs/app-server-protocol/schema/typescript/AgentMessageItem.ts:14` `export type AgentMessageItem = { id: string, content: Array<AgentMessageContent>,`

## Dependencies (auto sample)
### Imports / Includes
- `import type { AgentMessageContent } from "./AgentMessageContent";`
- `import type { MessagePhase } from "./MessagePhase";`
- `export type AgentMessageItem = { id: string, content: Array<AgentMessageContent>,`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
