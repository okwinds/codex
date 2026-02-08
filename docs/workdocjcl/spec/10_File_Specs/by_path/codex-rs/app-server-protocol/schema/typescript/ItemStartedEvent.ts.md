# `codex-rs/app-server-protocol/schema/typescript/ItemStartedEvent.ts`

## Identity
- kind: `source`
- ext: `.ts`
- size_bytes: `331`
- sha256: `4b7e48e10751a64042e99c92c5a26f82f2ca50157131f472784393e440782d2a`
- generated_utc: `2026-02-03T16:08:28Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server-protocol/schema/typescript/ItemStartedEvent.ts` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `export type ItemStartedEvent = { thread_id: ThreadId, turn_id: string, item: TurnItem, };`

## Definitions (auto, per-file)
- `import` `codex-rs/app-server-protocol/schema/typescript/ItemStartedEvent.ts:4` `import type { ThreadId } from "./ThreadId";`
- `import` `codex-rs/app-server-protocol/schema/typescript/ItemStartedEvent.ts:5` `import type { TurnItem } from "./TurnItem";`
- `export` `codex-rs/app-server-protocol/schema/typescript/ItemStartedEvent.ts:7` `export type ItemStartedEvent = { thread_id: ThreadId, turn_id: string, item: TurnItem, };`

## Dependencies (auto sample)
### Imports / Includes
- `import type { ThreadId } from "./ThreadId";`
- `import type { TurnItem } from "./TurnItem";`
- `export type ItemStartedEvent = { thread_id: ThreadId, turn_id: string, item: TurnItem, };`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
