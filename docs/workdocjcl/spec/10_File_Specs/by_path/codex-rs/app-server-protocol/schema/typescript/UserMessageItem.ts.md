# `codex-rs/app-server-protocol/schema/typescript/UserMessageItem.ts`

## Identity
- kind: `source`
- ext: `.ts`
- size_bytes: `273`
- sha256: `db0e6c29dfc83ef6cdb724ba867b4312416844ae80f91051cd67542ac83a8e73`
- generated_utc: `2026-02-03T16:08:28Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server-protocol/schema/typescript/UserMessageItem.ts` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `export type UserMessageItem = { id: string, content: Array<UserInput>, };`

## Definitions (auto, per-file)
- `import` `codex-rs/app-server-protocol/schema/typescript/UserMessageItem.ts:4` `import type { UserInput } from "./UserInput";`
- `export` `codex-rs/app-server-protocol/schema/typescript/UserMessageItem.ts:6` `export type UserMessageItem = { id: string, content: Array<UserInput>, };`

## Dependencies (auto sample)
### Imports / Includes
- `import type { UserInput } from "./UserInput";`
- `export type UserMessageItem = { id: string, content: Array<UserInput>, };`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
