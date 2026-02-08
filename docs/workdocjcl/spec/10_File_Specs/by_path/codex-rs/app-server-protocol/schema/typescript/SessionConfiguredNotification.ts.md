# `codex-rs/app-server-protocol/schema/typescript/SessionConfiguredNotification.ts`

## Identity
- kind: `source`
- ext: `.ts`
- size_bytes: `536`
- sha256: `203548f232bd35c2d6970862a8eba30d910d62e84ad908b6bcadb016323b4e3e`
- generated_utc: `2026-02-08T10:45:14Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server-protocol/schema/typescript/SessionConfiguredNotification.ts` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `export type SessionConfiguredNotification = { sessionId: ThreadId, model: string, reasoningEffort: ReasoningEffort | null, historyLogId: bigint, historyEntryCount: number, initialMessages: Array<EventMsg> | null, rolloutPath: string, };`

## Definitions (auto, per-file)
- `import` `codex-rs/app-server-protocol/schema/typescript/SessionConfiguredNotification.ts:4` `import type { EventMsg } from "./EventMsg";`
- `import` `codex-rs/app-server-protocol/schema/typescript/SessionConfiguredNotification.ts:5` `import type { ReasoningEffort } from "./ReasoningEffort";`
- `import` `codex-rs/app-server-protocol/schema/typescript/SessionConfiguredNotification.ts:6` `import type { ThreadId } from "./ThreadId";`
- `export` `codex-rs/app-server-protocol/schema/typescript/SessionConfiguredNotification.ts:8` `export type SessionConfiguredNotification = { sessionId: ThreadId, model: string, reasoningEffort: ReasoningEffort | null, historyLogId: bigint, historyEntryCount: number, initialMessages: Array<EventMsg> | null, rolloutPath: string, };`

## Dependencies (auto sample)
### Imports / Includes
- `import type { EventMsg } from "./EventMsg";`
- `import type { ReasoningEffort } from "./ReasoningEffort";`
- `import type { ThreadId } from "./ThreadId";`
- `export type SessionConfiguredNotification = { sessionId: ThreadId, model: string, reasoningEffort: ReasoningEffort | null, historyLogId: bigint, historyEntryCount: number, initialMessages: Array<EventMsg> | null, rolloutPath: string, };`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
