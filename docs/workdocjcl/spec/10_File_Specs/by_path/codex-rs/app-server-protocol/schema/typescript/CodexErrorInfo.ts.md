# `codex-rs/app-server-protocol/schema/typescript/CodexErrorInfo.ts`

## Identity
- kind: `source`
- ext: `.ts`
- size_bytes: `777`
- sha256: `7ccecc1983dfbc6333276e0b5c4542d479e80a1e5e75605645a994e73a5ace59`
- generated_utc: `2026-02-03T16:08:28Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server-protocol/schema/typescript/CodexErrorInfo.ts` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `export type CodexErrorInfo = "context_window_exceeded" | "usage_limit_exceeded" | { "model_cap": { model: string, reset_after_seconds: bigint | null, } } | { "http_connection_failed": { http_status_code: number | null, } } | { "response_stream_connection_failed": { http_status_code: number | null, } } | "internal_server_error" | "unauthorized" | "bad_request" | "sandbox_error" | { "response_stream_disconnected": { http_status_code: number | null, } } | { "response_too_many_failed_attempts": { http_status_code: number | null, } } | "thread_rollback_failed" | "other";`

## Definitions (auto, per-file)
- `export` `codex-rs/app-server-protocol/schema/typescript/CodexErrorInfo.ts:8` `export type CodexErrorInfo = "context_window_exceeded" | "usage_limit_exceeded" | { "model_cap": { model: string, reset_after_seconds: bigint | null, } } | { "http_connection_failed": { http_status_code: number | null, } } | { "response_stream_connection_failed": { http_status_code: number | null, } } | "internal_server_error" | "unauthorized" | "bad_request" | "sandbox_error" | { "response_stream_disconnected": { http_status_code: number | null, } } | { "response_too_many_failed_attempts": { http_status_code: number | null, } } | "thread_rollback_failed" | "other";`

## Dependencies (auto sample)
### Imports / Includes
- `export type CodexErrorInfo = "context_window_exceeded" | "usage_limit_exceeded" | { "model_cap": { model: string, reset_after_seconds: bigint | null, } } | { "http_connection_failed": { http_status_code: number | null, } } | { "response_stream_connection_failed": { http_status_code: number | null, } } | "internal_server_error" | "unauthorized" | "bad_request" | "sandbox_error" | { "response_stream_disconnected": { http_status_code: number | null, } } | { "response_too_many_failed_attempts": { http_status_code: number | null, } } | "thread_rollback_failed" | "other";`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
