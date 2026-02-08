# `codex-rs/app-server-protocol/schema/typescript/AgentMessageItem.ts`

## Identity
- kind: `source`
- ext: `.ts`
- size_bytes: `304`
- sha256: `1221e468cbc3dc73e79873f59b0c5729975bd4e7869e1e389f982587740ad2f3`
- generated_utc: `2026-02-03T16:08:28Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server-protocol/schema/typescript/AgentMessageItem.ts` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `export type AgentMessageItem = { id: string, content: Array<AgentMessageContent>, };`

## Definitions (auto, per-file)
- `import` `codex-rs/app-server-protocol/schema/typescript/AgentMessageItem.ts:4` `import type { AgentMessageContent } from "./AgentMessageContent";`
- `export` `codex-rs/app-server-protocol/schema/typescript/AgentMessageItem.ts:6` `export type AgentMessageItem = { id: string, content: Array<AgentMessageContent>, };`

## Dependencies (auto sample)
### Imports / Includes
- `import type { AgentMessageContent } from "./AgentMessageContent";`
- `export type AgentMessageItem = { id: string, content: Array<AgentMessageContent>, };`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
