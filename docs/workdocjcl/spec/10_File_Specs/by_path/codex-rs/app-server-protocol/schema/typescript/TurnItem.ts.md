# `codex-rs/app-server-protocol/schema/typescript/TurnItem.ts`

## Identity
- kind: `source`
- ext: `.ts`
- size_bytes: `783`
- sha256: `1e14d39dd3772b5484c5e8725dda0fa86b0bde7c12b2a034346ce877a0035d41`
- generated_utc: `2026-02-08T10:45:14Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server-protocol/schema/typescript/TurnItem.ts` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `export type TurnItem = { "type": "UserMessage" } & UserMessageItem | { "type": "AgentMessage" } & AgentMessageItem | { "type": "Plan" } & PlanItem | { "type": "Reasoning" } & ReasoningItem | { "type": "WebSearch" } & WebSearchItem | { "type": "ContextCompaction" } & ContextCompactionItem;`

## Definitions (auto, per-file)
- `import` `codex-rs/app-server-protocol/schema/typescript/TurnItem.ts:4` `import type { AgentMessageItem } from "./AgentMessageItem";`
- `import` `codex-rs/app-server-protocol/schema/typescript/TurnItem.ts:5` `import type { ContextCompactionItem } from "./ContextCompactionItem";`
- `import` `codex-rs/app-server-protocol/schema/typescript/TurnItem.ts:6` `import type { PlanItem } from "./PlanItem";`
- `import` `codex-rs/app-server-protocol/schema/typescript/TurnItem.ts:7` `import type { ReasoningItem } from "./ReasoningItem";`
- `import` `codex-rs/app-server-protocol/schema/typescript/TurnItem.ts:8` `import type { UserMessageItem } from "./UserMessageItem";`
- `import` `codex-rs/app-server-protocol/schema/typescript/TurnItem.ts:9` `import type { WebSearchItem } from "./WebSearchItem";`
- `export` `codex-rs/app-server-protocol/schema/typescript/TurnItem.ts:11` `export type TurnItem = { "type": "UserMessage" } & UserMessageItem | { "type": "AgentMessage" } & AgentMessageItem | { "type": "Plan" } & PlanItem | { "type": "Reasoning" } & ReasoningItem | { "type": "WebSearch" } & WebSearchItem | { "type": "ContextCompaction" } & ContextCompactionItem;`

## Dependencies (auto sample)
### Imports / Includes
- `import type { AgentMessageItem } from "./AgentMessageItem";`
- `import type { ContextCompactionItem } from "./ContextCompactionItem";`
- `import type { PlanItem } from "./PlanItem";`
- `import type { ReasoningItem } from "./ReasoningItem";`
- `import type { UserMessageItem } from "./UserMessageItem";`
- `import type { WebSearchItem } from "./WebSearchItem";`
- `export type TurnItem = { "type": "UserMessage" } & UserMessageItem | { "type": "AgentMessage" } & AgentMessageItem | { "type": "Plan" } & PlanItem | { "type": "Reasoning" } & ReasoningItem | { "type": "WebSearch" } & WebSearchItem | { "type": "ContextCompaction" } & ContextCompactionItem;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
