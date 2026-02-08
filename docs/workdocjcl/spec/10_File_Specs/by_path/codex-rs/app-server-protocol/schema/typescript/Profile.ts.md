# `codex-rs/app-server-protocol/schema/typescript/Profile.ts`

## Identity
- kind: `source`
- ext: `.ts`
- size_bytes: `650`
- sha256: `b140dc0de6149e3fd10632fe37fc266eee44bffbe9a10b81c8a9f41430c59a4a`
- generated_utc: `2026-02-03T16:08:28Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server-protocol/schema/typescript/Profile.ts` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `export type Profile = { model: string | null, modelProvider: string | null, approvalPolicy: AskForApproval | null, modelReasoningEffort: ReasoningEffort | null, modelReasoningSummary: ReasoningSummary | null, modelVerbosity: Verbosity | null, chatgptBaseUrl: string | null, };`

## Definitions (auto, per-file)
- `import` `codex-rs/app-server-protocol/schema/typescript/Profile.ts:4` `import type { AskForApproval } from "./AskForApproval";`
- `import` `codex-rs/app-server-protocol/schema/typescript/Profile.ts:5` `import type { ReasoningEffort } from "./ReasoningEffort";`
- `import` `codex-rs/app-server-protocol/schema/typescript/Profile.ts:6` `import type { ReasoningSummary } from "./ReasoningSummary";`
- `import` `codex-rs/app-server-protocol/schema/typescript/Profile.ts:7` `import type { Verbosity } from "./Verbosity";`
- `export` `codex-rs/app-server-protocol/schema/typescript/Profile.ts:9` `export type Profile = { model: string | null, modelProvider: string | null, approvalPolicy: AskForApproval | null, modelReasoningEffort: ReasoningEffort | null, modelReasoningSummary: ReasoningSummary | null, modelVerbosity: Verbosity | null, chatgptBaseUrl: string | null, };`

## Dependencies (auto sample)
### Imports / Includes
- `import type { AskForApproval } from "./AskForApproval";`
- `import type { ReasoningEffort } from "./ReasoningEffort";`
- `import type { ReasoningSummary } from "./ReasoningSummary";`
- `import type { Verbosity } from "./Verbosity";`
- `export type Profile = { model: string | null, modelProvider: string | null, approvalPolicy: AskForApproval | null, modelReasoningEffort: ReasoningEffort | null, modelReasoningSummary: ReasoningSummary | null, modelVerbosity: Verbosity | null, chatgptBaseUrl: string | null, };`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
