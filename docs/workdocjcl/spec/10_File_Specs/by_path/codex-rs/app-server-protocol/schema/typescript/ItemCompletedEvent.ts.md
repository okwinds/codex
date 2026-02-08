# `codex-rs/app-server-protocol/schema/typescript/ItemCompletedEvent.ts`

## Identity
- kind: `source`
- ext: `.ts`
- size_bytes: `333`
- sha256: `ffb6e072385fe458a51599b6b29df78f15bb52c49b508cf3663b289699231961`
- generated_utc: `2026-02-08T10:45:14Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server-protocol/schema/typescript/ItemCompletedEvent.ts` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `export type ItemCompletedEvent = { thread_id: ThreadId, turn_id: string, item: TurnItem, };`

## Definitions (auto, per-file)
- `import` `codex-rs/app-server-protocol/schema/typescript/ItemCompletedEvent.ts:4` `import type { ThreadId } from "./ThreadId";`
- `import` `codex-rs/app-server-protocol/schema/typescript/ItemCompletedEvent.ts:5` `import type { TurnItem } from "./TurnItem";`
- `export` `codex-rs/app-server-protocol/schema/typescript/ItemCompletedEvent.ts:7` `export type ItemCompletedEvent = { thread_id: ThreadId, turn_id: string, item: TurnItem, };`

## Dependencies (auto sample)
### Imports / Includes
- `import type { ThreadId } from "./ThreadId";`
- `import type { TurnItem } from "./TurnItem";`
- `export type ItemCompletedEvent = { thread_id: ThreadId, turn_id: string, item: TurnItem, };`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
