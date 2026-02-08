# `codex-rs/app-server-protocol/schema/typescript/v2/Account.ts`

## Identity
- kind: `source`
- ext: `.ts`
- size_bytes: `303`
- sha256: `ba8adeb09e1db4a2cce0cd02159869006f38b7755258d5037d84f38fae591b2a`
- generated_utc: `2026-02-03T16:08:28Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server-protocol/schema/typescript/v2/Account.ts` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `export type Account = { "type": "apiKey", } | { "type": "chatgpt", email: string, planType: PlanType, };`

## Definitions (auto, per-file)
- `import` `codex-rs/app-server-protocol/schema/typescript/v2/Account.ts:4` `import type { PlanType } from "../PlanType";`
- `export` `codex-rs/app-server-protocol/schema/typescript/v2/Account.ts:6` `export type Account = { "type": "apiKey", } | { "type": "chatgpt", email: string, planType: PlanType, };`

## Dependencies (auto sample)
### Imports / Includes
- `import type { PlanType } from "../PlanType";`
- `export type Account = { "type": "apiKey", } | { "type": "chatgpt", email: string, planType: PlanType, };`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
