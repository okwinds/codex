# `sdk/typescript/src/events.ts`

## Identity
- kind: `source`
- ext: `.ts`
- size_bytes: `2183`
- sha256: `cedb276aa04cac17cd0e6c9ae783fad7b0f62749e8d902c8cbd60664116a5761`
- generated_utc: `2026-02-08T10:45:42Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `sdk/typescript/src/events.ts` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `export type ThreadStartedEvent = {`
- `export type TurnStartedEvent = {`
- `export type Usage = {`
- `export type TurnCompletedEvent = {`
- `export type TurnFailedEvent = {`
- `export type ItemStartedEvent = {`
- `export type ItemUpdatedEvent = {`
- `export type ItemCompletedEvent = {`
- `export type ThreadError = {`
- `export type ThreadErrorEvent = {`
- `export type ThreadEvent =`

## Definitions (auto, per-file)
- `import` `sdk/typescript/src/events.ts:3` `import type { ThreadItem } from "./items";`
- `export` `sdk/typescript/src/events.ts:6` `export type ThreadStartedEvent = {`
- `export` `sdk/typescript/src/events.ts:16` `export type TurnStartedEvent = {`
- `export` `sdk/typescript/src/events.ts:21` `export type Usage = {`
- `export` `sdk/typescript/src/events.ts:31` `export type TurnCompletedEvent = {`
- `export` `sdk/typescript/src/events.ts:37` `export type TurnFailedEvent = {`
- `export` `sdk/typescript/src/events.ts:43` `export type ItemStartedEvent = {`
- `export` `sdk/typescript/src/events.ts:49` `export type ItemUpdatedEvent = {`
- `export` `sdk/typescript/src/events.ts:55` `export type ItemCompletedEvent = {`
- `export` `sdk/typescript/src/events.ts:61` `export type ThreadError = {`
- `export` `sdk/typescript/src/events.ts:66` `export type ThreadErrorEvent = {`
- `export` `sdk/typescript/src/events.ts:72` `export type ThreadEvent =`

## Dependencies (auto sample)
### Imports / Includes
- `import type { ThreadItem } from "./items";`
- `export type ThreadStartedEvent = {`
- `export type TurnStartedEvent = {`
- `export type Usage = {`
- `export type TurnCompletedEvent = {`
- `export type TurnFailedEvent = {`
- `export type ItemStartedEvent = {`
- `export type ItemUpdatedEvent = {`
- `export type ItemCompletedEvent = {`
- `export type ThreadError = {`
- `export type ThreadErrorEvent = {`
- `export type ThreadEvent =`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- `docs/workdocjcl/spec/00_Overview/PROJECT.md`
