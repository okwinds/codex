# `codex-rs/app-server-protocol/schema/typescript/v2/CodexErrorInfo.ts`

## Identity
- kind: `source`
- ext: `.ts`
- size_bytes: `969`
- sha256: `b4d08e636a02662c2bfd7c20dc7ad7f605bc4a4e5a2444ddf4f653f707b5b9f6`
- generated_utc: `2026-02-03T16:08:28Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server-protocol/schema/typescript/v2/CodexErrorInfo.ts` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `export type CodexErrorInfo = "contextWindowExceeded" | "usageLimitExceeded" | { "modelCap": { model: string, reset_after_seconds: bigint | null, } } | { "httpConnectionFailed": { httpStatusCode: number | null, } } | { "responseStreamConnectionFailed": { httpStatusCode: number | null, } } | "internalServerError" | "unauthorized" | "badRequest" | "threadRollbackFailed" | "sandboxError" | { "responseStreamDisconnected": { httpStatusCode: number | null, } } | { "responseTooManyFailedAttempts": { httpStatusCode: number | null, } } | "other";`

## Definitions (auto, per-file)
- `export` `codex-rs/app-server-protocol/schema/typescript/v2/CodexErrorInfo.ts:11` `export type CodexErrorInfo = "contextWindowExceeded" | "usageLimitExceeded" | { "modelCap": { model: string, reset_after_seconds: bigint | null, } } | { "httpConnectionFailed": { httpStatusCode: number | null, } } | { "responseStreamConnectionFailed": { httpStatusCode: number | null, } } | "internalServerError" | "unauthorized" | "badRequest" | "threadRollbackFailed" | "sandboxError" | { "responseStreamDisconnected": { httpStatusCode: number | null, } } | { "responseTooManyFailedAttempts": { httpStatusCode: number | null, } } | "other";`

## Dependencies (auto sample)
### Imports / Includes
- `export type CodexErrorInfo = "contextWindowExceeded" | "usageLimitExceeded" | { "modelCap": { model: string, reset_after_seconds: bigint | null, } } | { "httpConnectionFailed": { httpStatusCode: number | null, } } | { "responseStreamConnectionFailed": { httpStatusCode: number | null, } } | "internalServerError" | "unauthorized" | "badRequest" | "threadRollbackFailed" | "sandboxError" | { "responseStreamDisconnected": { httpStatusCode: number | null, } } | { "responseTooManyFailedAttempts": { httpStatusCode: number | null, } } | "other";`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
