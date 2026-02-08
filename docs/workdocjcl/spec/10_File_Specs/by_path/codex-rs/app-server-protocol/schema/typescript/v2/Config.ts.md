# `codex-rs/app-server-protocol/schema/typescript/v2/Config.ts`

## Identity
- kind: `source`
- ext: `.ts`
- size_bytes: `1730`
- sha256: `bf132343237f570274b3253066e709e914ff3a34ed11c19e8c656b98f0d89116`
- generated_utc: `2026-02-08T10:45:14Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server-protocol/schema/typescript/v2/Config.ts` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `export type Config = {model: string | null, review_model: string | null, model_context_window: bigint | null, model_auto_compact_token_limit: bigint | null, model_provider: string | null, approval_policy: AskForApproval | null, sandbox_mode: SandboxMode | null, sandbox_workspace_write: SandboxWorkspaceWrite | null, forced_chatgpt_workspace_id: string | null, forced_login_method: ForcedLoginMethod | null, web_search: WebSearchMode | null, tools: ToolsV2 | null, profile: string | null, profiles: { [key in string]?: ProfileV2 }, instructions: string | null, developer_instructions: string | null, compact_prompt: string | null, model_reasoning_effort: ReasoningEffort | null, model_reasoning_summary: ReasoningSummary | null, model_verbosity: Verbosity | null, analytics: AnalyticsConfig | null} & ({ [key in string]?: number | string | boolean | Array<JsonValue> | { [key in string]?: JsonValue } | null });`

## Definitions (auto, per-file)
- `import` `codex-rs/app-server-protocol/schema/typescript/v2/Config.ts:4` `import type { ForcedLoginMethod } from "../ForcedLoginMethod";`
- `import` `codex-rs/app-server-protocol/schema/typescript/v2/Config.ts:5` `import type { ReasoningEffort } from "../ReasoningEffort";`
- `import` `codex-rs/app-server-protocol/schema/typescript/v2/Config.ts:6` `import type { ReasoningSummary } from "../ReasoningSummary";`
- `import` `codex-rs/app-server-protocol/schema/typescript/v2/Config.ts:7` `import type { Verbosity } from "../Verbosity";`
- `import` `codex-rs/app-server-protocol/schema/typescript/v2/Config.ts:8` `import type { WebSearchMode } from "../WebSearchMode";`
- `import` `codex-rs/app-server-protocol/schema/typescript/v2/Config.ts:9` `import type { JsonValue } from "../serde_json/JsonValue";`
- `import` `codex-rs/app-server-protocol/schema/typescript/v2/Config.ts:10` `import type { AnalyticsConfig } from "./AnalyticsConfig";`
- `import` `codex-rs/app-server-protocol/schema/typescript/v2/Config.ts:11` `import type { AskForApproval } from "./AskForApproval";`
- `import` `codex-rs/app-server-protocol/schema/typescript/v2/Config.ts:12` `import type { ProfileV2 } from "./ProfileV2";`
- `import` `codex-rs/app-server-protocol/schema/typescript/v2/Config.ts:13` `import type { SandboxMode } from "./SandboxMode";`
- `import` `codex-rs/app-server-protocol/schema/typescript/v2/Config.ts:14` `import type { SandboxWorkspaceWrite } from "./SandboxWorkspaceWrite";`
- `import` `codex-rs/app-server-protocol/schema/typescript/v2/Config.ts:15` `import type { ToolsV2 } from "./ToolsV2";`
- `export` `codex-rs/app-server-protocol/schema/typescript/v2/Config.ts:17` `export type Config = {model: string | null, review_model: string | null, model_context_window: bigint | null, model_auto_compact_token_limit: bigint | null, model_provider: string | null, approval_policy: AskForApproval | null, sandbox_mode: SandboxMode | null, sandbox_workspace_write: SandboxWorkspaceWrite | null, forced_chatgpt_workspace_id: string | null, forced_login_method: ForcedLoginMethod | null, web_search: WebSearchMode | null, tools: ToolsV2 | null, profile: string | null, profiles: { [key in string]?: ProfileV2 }, instructions: string | null, developer_instructions: string | null, compact_prompt: string | null, model_reasoning_effort: ReasoningEffort | null, model_reasoning_summary: ReasoningSummary | null, model_verbosity: Verbosity | null, analytics: AnalyticsConfig | null} & ({ [key in string]?: number | string | boolean | Array<JsonValue> | { [key in string]?: JsonValue } | null });`

## Dependencies (auto sample)
### Imports / Includes
- `import type { ForcedLoginMethod } from "../ForcedLoginMethod";`
- `import type { ReasoningEffort } from "../ReasoningEffort";`
- `import type { ReasoningSummary } from "../ReasoningSummary";`
- `import type { Verbosity } from "../Verbosity";`
- `import type { WebSearchMode } from "../WebSearchMode";`
- `import type { JsonValue } from "../serde_json/JsonValue";`
- `import type { AnalyticsConfig } from "./AnalyticsConfig";`
- `import type { AskForApproval } from "./AskForApproval";`
- `import type { ProfileV2 } from "./ProfileV2";`
- `import type { SandboxMode } from "./SandboxMode";`
- `import type { SandboxWorkspaceWrite } from "./SandboxWorkspaceWrite";`
- `import type { ToolsV2 } from "./ToolsV2";`
- `export type Config = {model: string | null, review_model: string | null, model_context_window: bigint | null, model_auto_compact_token_limit: bigint | null, model_provider: string | null, approval_policy: AskForApproval | null, sandbox_mode: SandboxMode | null, sandbox_workspace_write: SandboxWorkspaceWrite | null, forced_chatgpt_workspace_id: string | null, forced_login_method: ForcedLoginMethod | null, web_search: WebSearchMode | null, tools: ToolsV2 | null, profile: string | null, profiles: { [key in string]?: ProfileV2 }, instructions: string | null, developer_instructions: string | null, compact_prompt: string | null, model_reasoning_effort: ReasoningEffort | null, model_reasoning_summary: ReasoningSummary | null, model_verbosity: Verbosity | null, analytics: AnalyticsConfig | null} & ({ [key in string]?: number | string | boolean | Array<JsonValue> | { [key in string]?: JsonValue } | null });`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
