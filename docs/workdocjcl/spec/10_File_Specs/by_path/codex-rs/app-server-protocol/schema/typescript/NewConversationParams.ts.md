# `codex-rs/app-server-protocol/schema/typescript/NewConversationParams.ts`

## Identity
- kind: `source`
- ext: `.ts`
- size_bytes: `709`
- sha256: `234747a778bec6c4091b9f3135190ae7e4decba949a8ba191067b9169a2f2b02`
- generated_utc: `2026-02-08T10:45:14Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server-protocol/schema/typescript/NewConversationParams.ts` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `export type NewConversationParams = { model: string | null, modelProvider: string | null, profile: string | null, cwd: string | null, approvalPolicy: AskForApproval | null, sandbox: SandboxMode | null, config: { [key in string]?: JsonValue } | null, baseInstructions: string | null, developerInstructions: string | null, compactPrompt: string | null, includeApplyPatchTool: boolean | null, };`

## Definitions (auto, per-file)
- `import` `codex-rs/app-server-protocol/schema/typescript/NewConversationParams.ts:4` `import type { AskForApproval } from "./AskForApproval";`
- `import` `codex-rs/app-server-protocol/schema/typescript/NewConversationParams.ts:5` `import type { SandboxMode } from "./SandboxMode";`
- `import` `codex-rs/app-server-protocol/schema/typescript/NewConversationParams.ts:6` `import type { JsonValue } from "./serde_json/JsonValue";`
- `export` `codex-rs/app-server-protocol/schema/typescript/NewConversationParams.ts:8` `export type NewConversationParams = { model: string | null, modelProvider: string | null, profile: string | null, cwd: string | null, approvalPolicy: AskForApproval | null, sandbox: SandboxMode | null, config: { [key in string]?: JsonValue } | null, baseInstructions: string | null, developerInstructions: string | null, compactPrompt: string | null, includeApplyPatchTool: boolean | null, };`

## Dependencies (auto sample)
### Imports / Includes
- `import type { AskForApproval } from "./AskForApproval";`
- `import type { SandboxMode } from "./SandboxMode";`
- `import type { JsonValue } from "./serde_json/JsonValue";`
- `export type NewConversationParams = { model: string | null, modelProvider: string | null, profile: string | null, cwd: string | null, approvalPolicy: AskForApproval | null, sandbox: SandboxMode | null, config: { [key in string]?: JsonValue } | null, baseInstructions: string | null, developerInstructions: string | null, compactPrompt: string | null, includeApplyPatchTool: boolean | null, };`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
