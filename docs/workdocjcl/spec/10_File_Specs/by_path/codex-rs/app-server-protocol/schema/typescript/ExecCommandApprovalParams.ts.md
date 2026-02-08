# `codex-rs/app-server-protocol/schema/typescript/ExecCommandApprovalParams.ts`

## Identity
- kind: `source`
- ext: `.ts`
- size_bytes: `568`
- sha256: `38870dfef919d838cc018d331354831301a55453fe3fb9e61f8ce7c6e8044f9a`
- generated_utc: `2026-02-08T10:45:14Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server-protocol/schema/typescript/ExecCommandApprovalParams.ts` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `export type ExecCommandApprovalParams = { conversationId: ThreadId,`

## Definitions (auto, per-file)
- `import` `codex-rs/app-server-protocol/schema/typescript/ExecCommandApprovalParams.ts:4` `import type { ParsedCommand } from "./ParsedCommand";`
- `import` `codex-rs/app-server-protocol/schema/typescript/ExecCommandApprovalParams.ts:5` `import type { ThreadId } from "./ThreadId";`
- `export` `codex-rs/app-server-protocol/schema/typescript/ExecCommandApprovalParams.ts:7` `export type ExecCommandApprovalParams = { conversationId: ThreadId,`

## Dependencies (auto sample)
### Imports / Includes
- `import type { ParsedCommand } from "./ParsedCommand";`
- `import type { ThreadId } from "./ThreadId";`
- `export type ExecCommandApprovalParams = { conversationId: ThreadId,`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
