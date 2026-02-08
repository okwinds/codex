# `codex-rs/app-server-protocol/schema/typescript/v2/GetAccountResponse.ts`

## Identity
- kind: `source`
- ext: `.ts`
- size_bytes: `287`
- sha256: `f16f348c9c37a760bd7b4c75c0b7d86a57d6cbd16bd6a1c4b06dffa39157b6a9`
- generated_utc: `2026-02-08T10:45:14Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server-protocol/schema/typescript/v2/GetAccountResponse.ts` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `export type GetAccountResponse = { account: Account | null, requiresOpenaiAuth: boolean, };`

## Definitions (auto, per-file)
- `import` `codex-rs/app-server-protocol/schema/typescript/v2/GetAccountResponse.ts:4` `import type { Account } from "./Account";`
- `export` `codex-rs/app-server-protocol/schema/typescript/v2/GetAccountResponse.ts:6` `export type GetAccountResponse = { account: Account | null, requiresOpenaiAuth: boolean, };`

## Dependencies (auto sample)
### Imports / Includes
- `import type { Account } from "./Account";`
- `export type GetAccountResponse = { account: Account | null, requiresOpenaiAuth: boolean, };`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
