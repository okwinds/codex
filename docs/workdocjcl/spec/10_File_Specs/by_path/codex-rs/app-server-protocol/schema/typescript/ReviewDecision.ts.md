# `codex-rs/app-server-protocol/schema/typescript/ReviewDecision.ts`

## Identity
- kind: `source`
- ext: `.ts`
- size_bytes: `467`
- sha256: `ea5ceb26979ae0397be946a3d07c5416ab223ebf7681c624fa8a4ddc73c0dae1`
- generated_utc: `2026-02-08T10:45:14Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server-protocol/schema/typescript/ReviewDecision.ts` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `export type ReviewDecision = "approved" | { "approved_execpolicy_amendment": { proposed_execpolicy_amendment: ExecPolicyAmendment, } } | "approved_for_session" | "denied" | "abort";`

## Definitions (auto, per-file)
- `import` `codex-rs/app-server-protocol/schema/typescript/ReviewDecision.ts:4` `import type { ExecPolicyAmendment } from "./ExecPolicyAmendment";`
- `export` `codex-rs/app-server-protocol/schema/typescript/ReviewDecision.ts:9` `export type ReviewDecision = "approved" | { "approved_execpolicy_amendment": { proposed_execpolicy_amendment: ExecPolicyAmendment, } } | "approved_for_session" | "denied" | "abort";`

## Dependencies (auto sample)
### Imports / Includes
- `import type { ExecPolicyAmendment } from "./ExecPolicyAmendment";`
- `export type ReviewDecision = "approved" | { "approved_execpolicy_amendment": { proposed_execpolicy_amendment: ExecPolicyAmendment, } } | "approved_for_session" | "denied" | "abort";`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
