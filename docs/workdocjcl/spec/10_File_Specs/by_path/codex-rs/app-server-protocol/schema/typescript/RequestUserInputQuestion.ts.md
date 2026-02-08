# `codex-rs/app-server-protocol/schema/typescript/RequestUserInputQuestion.ts`

## Identity
- kind: `source`
- ext: `.ts`
- size_bytes: `423`
- sha256: `4356c6c32a8dfe8ecd465a14f9d357b96b15a29270999fc3dec70f1a4338c351`
- generated_utc: `2026-02-08T10:45:14Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server-protocol/schema/typescript/RequestUserInputQuestion.ts` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `export type RequestUserInputQuestion = { id: string, header: string, question: string, isOther: boolean, isSecret: boolean, options: Array<RequestUserInputQuestionOption> | null, };`

## Definitions (auto, per-file)
- `import` `codex-rs/app-server-protocol/schema/typescript/RequestUserInputQuestion.ts:4` `import type { RequestUserInputQuestionOption } from "./RequestUserInputQuestionOption";`
- `export` `codex-rs/app-server-protocol/schema/typescript/RequestUserInputQuestion.ts:6` `export type RequestUserInputQuestion = { id: string, header: string, question: string, isOther: boolean, isSecret: boolean, options: Array<RequestUserInputQuestionOption> | null, };`

## Dependencies (auto sample)
### Imports / Includes
- `import type { RequestUserInputQuestionOption } from "./RequestUserInputQuestionOption";`
- `export type RequestUserInputQuestion = { id: string, header: string, question: string, isOther: boolean, isSecret: boolean, options: Array<RequestUserInputQuestionOption> | null, };`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
