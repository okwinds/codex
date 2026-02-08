# `codex-rs/app-server-protocol/schema/typescript/v2/McpServerOauthLoginParams.ts`

## Identity
- kind: `source`
- ext: `.ts`
- size_bytes: `258`
- sha256: `613b058d07988f770e5b7047a60a2dba03ee0bd1d908f4d63201df66b5bd9071`
- generated_utc: `2026-02-03T16:08:28Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server-protocol/schema/typescript/v2/McpServerOauthLoginParams.ts` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `export type McpServerOauthLoginParams = { name: string, scopes?: Array<string>, timeoutSecs?: bigint, };`

## Definitions (auto, per-file)
- `export` `codex-rs/app-server-protocol/schema/typescript/v2/McpServerOauthLoginParams.ts:5` `export type McpServerOauthLoginParams = { name: string, scopes?: Array<string>, timeoutSecs?: bigint, };`

## Dependencies (auto sample)
### Imports / Includes
- `export type McpServerOauthLoginParams = { name: string, scopes?: Array<string>, timeoutSecs?: bigint, };`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- has retry/timeout/backoff logic

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
