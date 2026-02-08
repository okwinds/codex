# `codex-rs/app-server-protocol/schema/typescript/v2/CommandExecutionRequestApprovalParams.ts`

## Identity
- kind: `source`
- ext: `.ts`
- size_bytes: `879`
- sha256: `522df78a0012f468df65a971a55fa6db256e12fe646ebe5300465ea4914cf18f`
- generated_utc: `2026-02-08T10:45:14Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server-protocol/schema/typescript/v2/CommandExecutionRequestApprovalParams.ts` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `export type CommandExecutionRequestApprovalParams = { threadId: string, turnId: string, itemId: string,`

## Definitions (auto, per-file)
- `import` `codex-rs/app-server-protocol/schema/typescript/v2/CommandExecutionRequestApprovalParams.ts:4` `import type { CommandAction } from "./CommandAction";`
- `import` `codex-rs/app-server-protocol/schema/typescript/v2/CommandExecutionRequestApprovalParams.ts:5` `import type { ExecPolicyAmendment } from "./ExecPolicyAmendment";`
- `export` `codex-rs/app-server-protocol/schema/typescript/v2/CommandExecutionRequestApprovalParams.ts:7` `export type CommandExecutionRequestApprovalParams = { threadId: string, turnId: string, itemId: string,`

## Dependencies (auto sample)
### Imports / Includes
- `import type { CommandAction } from "./CommandAction";`
- `import type { ExecPolicyAmendment } from "./ExecPolicyAmendment";`
- `export type CommandExecutionRequestApprovalParams = { threadId: string, turnId: string, itemId: string,`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
