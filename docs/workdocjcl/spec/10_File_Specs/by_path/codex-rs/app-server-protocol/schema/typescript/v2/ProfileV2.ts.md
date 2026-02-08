# `codex-rs/app-server-protocol/schema/typescript/v2/ProfileV2.ts`

## Identity
- kind: `source`
- ext: `.ts`
- size_bytes: `923`
- sha256: `4fc86a04a6563439997ef726ca45b61014be4a1056f12b35850655858c659abd`
- generated_utc: `2026-02-03T16:08:28Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server-protocol/schema/typescript/v2/ProfileV2.ts` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `export type ProfileV2 = { model: string | null, model_provider: string | null, approval_policy: AskForApproval | null, model_reasoning_effort: ReasoningEffort | null, model_reasoning_summary: ReasoningSummary | null, model_verbosity: Verbosity | null, web_search: WebSearchMode | null, chatgpt_base_url: string | null, } & ({ [key in string]?: number | string | boolean | Array<JsonValue> | { [key in string]?: JsonValue } | null });`

## Definitions (auto, per-file)
- `import` `codex-rs/app-server-protocol/schema/typescript/v2/ProfileV2.ts:4` `import type { ReasoningEffort } from "../ReasoningEffort";`
- `import` `codex-rs/app-server-protocol/schema/typescript/v2/ProfileV2.ts:5` `import type { ReasoningSummary } from "../ReasoningSummary";`
- `import` `codex-rs/app-server-protocol/schema/typescript/v2/ProfileV2.ts:6` `import type { Verbosity } from "../Verbosity";`
- `import` `codex-rs/app-server-protocol/schema/typescript/v2/ProfileV2.ts:7` `import type { WebSearchMode } from "../WebSearchMode";`
- `import` `codex-rs/app-server-protocol/schema/typescript/v2/ProfileV2.ts:8` `import type { JsonValue } from "../serde_json/JsonValue";`
- `import` `codex-rs/app-server-protocol/schema/typescript/v2/ProfileV2.ts:9` `import type { AskForApproval } from "./AskForApproval";`
- `export` `codex-rs/app-server-protocol/schema/typescript/v2/ProfileV2.ts:11` `export type ProfileV2 = { model: string | null, model_provider: string | null, approval_policy: AskForApproval | null, model_reasoning_effort: ReasoningEffort | null, model_reasoning_summary: ReasoningSummary | null, model_verbosity: Verbosity | null, web_search: WebSearchMode | null, chatgpt_base_url: string | null, } & ({ [key in string]?: number | string | boolean | Array<JsonValue> | { [key in string]?: JsonValue } | null });`

## Dependencies (auto sample)
### Imports / Includes
- `import type { ReasoningEffort } from "../ReasoningEffort";`
- `import type { ReasoningSummary } from "../ReasoningSummary";`
- `import type { Verbosity } from "../Verbosity";`
- `import type { WebSearchMode } from "../WebSearchMode";`
- `import type { JsonValue } from "../serde_json/JsonValue";`
- `import type { AskForApproval } from "./AskForApproval";`
- `export type ProfileV2 = { model: string | null, model_provider: string | null, approval_policy: AskForApproval | null, model_reasoning_effort: ReasoningEffort | null, model_reasoning_summary: ReasoningSummary | null, model_verbosity: Verbosity | null, web_search: WebSearchMode | null, chatgpt_base_url: string | null, } & ({ [key in string]?: number | string | boolean | Array<JsonValue> | { [key in string]?: JsonValue } | null });`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
