# `codex-rs/app-server-protocol/schema/typescript/v2/McpServerOauthLoginParams.ts`

## Identity
- kind: `source`
- ext: `.ts`
- size_bytes: `272`
- sha256: `e3893bc134483c4435eecfb33ad9d25e771ea77efa13052a2e2da5a9fd17dbd3`
- generated_utc: `2026-02-08T10:45:14Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server-protocol/schema/typescript/v2/McpServerOauthLoginParams.ts` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `export type McpServerOauthLoginParams = { name: string, scopes?: Array<string> | null, timeoutSecs?: bigint | null, };`

## Definitions (auto, per-file)
- `export` `codex-rs/app-server-protocol/schema/typescript/v2/McpServerOauthLoginParams.ts:5` `export type McpServerOauthLoginParams = { name: string, scopes?: Array<string> | null, timeoutSecs?: bigint | null, };`

## Dependencies (auto sample)
### Imports / Includes
- `export type McpServerOauthLoginParams = { name: string, scopes?: Array<string> | null, timeoutSecs?: bigint | null, };`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- has retry/timeout/backoff logic

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
