# `codex-rs/app-server-protocol/schema/typescript/UserSavedConfig.ts`

## Identity
- kind: `source`
- ext: `.ts`
- size_bytes: `1093`
- sha256: `54d78c24fdf1ab7e32c9cdaea13bb53a0f7e07794aac839f941fb358766d46f4`
- generated_utc: `2026-02-08T10:45:14Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server-protocol/schema/typescript/UserSavedConfig.ts` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `export type UserSavedConfig = { approvalPolicy: AskForApproval | null, sandboxMode: SandboxMode | null, sandboxSettings: SandboxSettings | null, forcedChatgptWorkspaceId: string | null, forcedLoginMethod: ForcedLoginMethod | null, model: string | null, modelReasoningEffort: ReasoningEffort | null, modelReasoningSummary: ReasoningSummary | null, modelVerbosity: Verbosity | null, tools: Tools | null, profile: string | null, profiles: { [key in string]?: Profile }, };`

## Definitions (auto, per-file)
- `import` `codex-rs/app-server-protocol/schema/typescript/UserSavedConfig.ts:4` `import type { AskForApproval } from "./AskForApproval";`
- `import` `codex-rs/app-server-protocol/schema/typescript/UserSavedConfig.ts:5` `import type { ForcedLoginMethod } from "./ForcedLoginMethod";`
- `import` `codex-rs/app-server-protocol/schema/typescript/UserSavedConfig.ts:6` `import type { Profile } from "./Profile";`
- `import` `codex-rs/app-server-protocol/schema/typescript/UserSavedConfig.ts:7` `import type { ReasoningEffort } from "./ReasoningEffort";`
- `import` `codex-rs/app-server-protocol/schema/typescript/UserSavedConfig.ts:8` `import type { ReasoningSummary } from "./ReasoningSummary";`
- `import` `codex-rs/app-server-protocol/schema/typescript/UserSavedConfig.ts:9` `import type { SandboxMode } from "./SandboxMode";`
- `import` `codex-rs/app-server-protocol/schema/typescript/UserSavedConfig.ts:10` `import type { SandboxSettings } from "./SandboxSettings";`
- `import` `codex-rs/app-server-protocol/schema/typescript/UserSavedConfig.ts:11` `import type { Tools } from "./Tools";`
- `import` `codex-rs/app-server-protocol/schema/typescript/UserSavedConfig.ts:12` `import type { Verbosity } from "./Verbosity";`
- `export` `codex-rs/app-server-protocol/schema/typescript/UserSavedConfig.ts:14` `export type UserSavedConfig = { approvalPolicy: AskForApproval | null, sandboxMode: SandboxMode | null, sandboxSettings: SandboxSettings | null, forcedChatgptWorkspaceId: string | null, forcedLoginMethod: ForcedLoginMethod | null, model: string | null, modelReasoningEffort: ReasoningEffort | null, modelReasoningSummary: ReasoningSummary | null, modelVerbosity: Verbosity | null, tools: Tools | null, profile: string | null, profiles: { [key in string]?: Profile }, };`

## Dependencies (auto sample)
### Imports / Includes
- `import type { AskForApproval } from "./AskForApproval";`
- `import type { ForcedLoginMethod } from "./ForcedLoginMethod";`
- `import type { Profile } from "./Profile";`
- `import type { ReasoningEffort } from "./ReasoningEffort";`
- `import type { ReasoningSummary } from "./ReasoningSummary";`
- `import type { SandboxMode } from "./SandboxMode";`
- `import type { SandboxSettings } from "./SandboxSettings";`
- `import type { Tools } from "./Tools";`
- `import type { Verbosity } from "./Verbosity";`
- `export type UserSavedConfig = { approvalPolicy: AskForApproval | null, sandboxMode: SandboxMode | null, sandboxSettings: SandboxSettings | null, forcedChatgptWorkspaceId: string | null, forcedLoginMethod: ForcedLoginMethod | null, model: string | null, modelReasoningEffort: ReasoningEffort | null, modelReasoningSummary: ReasoningSummary | null, modelVerbosity: Verbosity | null, tools: Tools | null, profile: string | null, profiles: { [key in string]?: Profile }, };`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
