# `codex-rs/app-server-protocol/schema/typescript/ResponseItem.ts`

## Identity
- kind: `source`
- ext: `.ts`
- size_bytes: `1708`
- sha256: `5c4f2f829bda2231365c72a35b1449fb5bc75490fbe8f55f2918cafcf068ffcc`
- generated_utc: `2026-02-03T16:08:28Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server-protocol/schema/typescript/ResponseItem.ts` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `export type ResponseItem = { "type": "message", role: string, content: Array<ContentItem>, end_turn?: boolean, phase?: MessagePhase, } | { "type": "reasoning", summary: Array<ReasoningItemReasoningSummary>, content?: Array<ReasoningItemContent>, encrypted_content: string | null, } | { "type": "local_shell_call",`

## Definitions (auto, per-file)
- `import` `codex-rs/app-server-protocol/schema/typescript/ResponseItem.ts:4` `import type { ContentItem } from "./ContentItem";`
- `import` `codex-rs/app-server-protocol/schema/typescript/ResponseItem.ts:5` `import type { FunctionCallOutputPayload } from "./FunctionCallOutputPayload";`
- `import` `codex-rs/app-server-protocol/schema/typescript/ResponseItem.ts:6` `import type { GhostCommit } from "./GhostCommit";`
- `import` `codex-rs/app-server-protocol/schema/typescript/ResponseItem.ts:7` `import type { LocalShellAction } from "./LocalShellAction";`
- `import` `codex-rs/app-server-protocol/schema/typescript/ResponseItem.ts:8` `import type { LocalShellStatus } from "./LocalShellStatus";`
- `import` `codex-rs/app-server-protocol/schema/typescript/ResponseItem.ts:9` `import type { MessagePhase } from "./MessagePhase";`
- `import` `codex-rs/app-server-protocol/schema/typescript/ResponseItem.ts:10` `import type { ReasoningItemContent } from "./ReasoningItemContent";`
- `import` `codex-rs/app-server-protocol/schema/typescript/ResponseItem.ts:11` `import type { ReasoningItemReasoningSummary } from "./ReasoningItemReasoningSummary";`
- `import` `codex-rs/app-server-protocol/schema/typescript/ResponseItem.ts:12` `import type { WebSearchAction } from "./WebSearchAction";`
- `export` `codex-rs/app-server-protocol/schema/typescript/ResponseItem.ts:14` `export type ResponseItem = { "type": "message", role: string, content: Array<ContentItem>, end_turn?: boolean, phase?: MessagePhase, } | { "type": "reasoning", summary: Array<ReasoningItemReasoningSummary>, content?: Array<ReasoningItemContent>, encrypted_content: string | null, } | { "type": "local_shell_call",`

## Dependencies (auto sample)
### Imports / Includes
- `import type { ContentItem } from "./ContentItem";`
- `import type { FunctionCallOutputPayload } from "./FunctionCallOutputPayload";`
- `import type { GhostCommit } from "./GhostCommit";`
- `import type { LocalShellAction } from "./LocalShellAction";`
- `import type { LocalShellStatus } from "./LocalShellStatus";`
- `import type { MessagePhase } from "./MessagePhase";`
- `import type { ReasoningItemContent } from "./ReasoningItemContent";`
- `import type { ReasoningItemReasoningSummary } from "./ReasoningItemReasoningSummary";`
- `import type { WebSearchAction } from "./WebSearchAction";`
- `export type ResponseItem = { "type": "message", role: string, content: Array<ContentItem>, end_turn?: boolean, phase?: MessagePhase, } | { "type": "reasoning", summary: Array<ReasoningItemReasoningSummary>, content?: Array<ReasoningItemContent>, encrypted_content: string | null, } | { "type": "local_shell_call",`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
