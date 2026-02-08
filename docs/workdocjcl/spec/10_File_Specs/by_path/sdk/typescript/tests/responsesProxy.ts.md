# `sdk/typescript/tests/responsesProxy.ts`

## Identity
- kind: `test`
- ext: `.ts`
- size_bytes: `5701`
- sha256: `793e3bf969156f9a2cc09a14c23aa39cf5bd4130cb8443e1423177fd41e2e4d1`
- generated_utc: `2026-02-08T10:45:42Z`

## Purpose (Why)
Test or snapshot file used for automated verification.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `sdk/typescript/tests/responsesProxy.ts` (read)

### Outputs / Side Effects
- none (file is declarative: doc/config/test/asset)

## Public Surface (auto)
- `export type SseEvent = {`
- `export type SseResponseBody = {`
- `export type ResponsesProxyOptions = {`
- `export type ResponsesProxy = {`
- `export type ResponsesApiRequest = {`
- `export type RecordedRequest = {`
- `export async function startResponsesTestProxy(`
- `export function sse(...events: SseEvent[]): SseResponseBody {`
- `export function responseStarted(responseId: string = DEFAULT_RESPONSE_ID): SseEvent {`
- `export function assistantMessage(text: string, itemId: string = DEFAULT_MESSAGE_ID): SseEvent {`
- `export function shell_call(): SseEvent {`
- `export function responseFailed(errorMessage: string): SseEvent {`
- `export function responseCompleted(`

## Definitions (auto, per-file)
- (not extracted)

## Dependencies (auto sample)
### Imports / Includes
- `import http from "node:http";`
- `export type SseEvent = {`
- `export type SseResponseBody = {`
- `export type ResponsesProxyOptions = {`
- `export type ResponsesProxy = {`
- `export type ResponsesApiRequest = {`
- `export type RecordedRequest = {`
- `export async function startResponsesTestProxy(`
- `export function sse(...events: SseEvent[]): SseResponseBody {`
- `export function responseStarted(responseId: string = DEFAULT_RESPONSE_ID): SseEvent {`
- `export function assistantMessage(text: string, itemId: string = DEFAULT_MESSAGE_ID): SseEvent {`
- `export function shell_call(): SseEvent {`
- `export function responseFailed(errorMessage: string): SseEvent {`
- `export function responseCompleted(`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (none detected)

## Spec Links
- `docs/workdocjcl/spec/00_Overview/PROJECT.md`
