# `codex-rs/app-server-protocol/schema/typescript/SendUserMessageParams.ts`

## Identity
- kind: `source`
- ext: `.ts`
- size_bytes: `335`
- sha256: `077f050afd1dd22271595dfb2175691e93a690015c6743ffde2ea837d989ec99`
- generated_utc: `2026-02-08T10:45:14Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server-protocol/schema/typescript/SendUserMessageParams.ts` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `export type SendUserMessageParams = { conversationId: ThreadId, items: Array<InputItem>, };`

## Definitions (auto, per-file)
- `import` `codex-rs/app-server-protocol/schema/typescript/SendUserMessageParams.ts:4` `import type { InputItem } from "./InputItem";`
- `import` `codex-rs/app-server-protocol/schema/typescript/SendUserMessageParams.ts:5` `import type { ThreadId } from "./ThreadId";`
- `export` `codex-rs/app-server-protocol/schema/typescript/SendUserMessageParams.ts:7` `export type SendUserMessageParams = { conversationId: ThreadId, items: Array<InputItem>, };`

## Dependencies (auto sample)
### Imports / Includes
- `import type { InputItem } from "./InputItem";`
- `import type { ThreadId } from "./ThreadId";`
- `export type SendUserMessageParams = { conversationId: ThreadId, items: Array<InputItem>, };`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
