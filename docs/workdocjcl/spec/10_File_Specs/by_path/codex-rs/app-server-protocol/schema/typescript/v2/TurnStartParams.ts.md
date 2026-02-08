# `codex-rs/app-server-protocol/schema/typescript/v2/TurnStartParams.ts`

## Identity
- kind: `source`
- ext: `.ts`
- size_bytes: `1742`
- sha256: `90e26e852b88cde7ea1a5c0824dee11b7d67835893bab0bbf37c0434e8c7130d`
- generated_utc: `2026-02-03T16:08:28Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server-protocol/schema/typescript/v2/TurnStartParams.ts` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `export type TurnStartParams = { threadId: string, input: Array<UserInput>,`

## Definitions (auto, per-file)
- `import` `codex-rs/app-server-protocol/schema/typescript/v2/TurnStartParams.ts:4` `import type { CollaborationMode } from "../CollaborationMode";`
- `import` `codex-rs/app-server-protocol/schema/typescript/v2/TurnStartParams.ts:5` `import type { Personality } from "../Personality";`
- `import` `codex-rs/app-server-protocol/schema/typescript/v2/TurnStartParams.ts:6` `import type { ReasoningEffort } from "../ReasoningEffort";`
- `import` `codex-rs/app-server-protocol/schema/typescript/v2/TurnStartParams.ts:7` `import type { ReasoningSummary } from "../ReasoningSummary";`
- `import` `codex-rs/app-server-protocol/schema/typescript/v2/TurnStartParams.ts:8` `import type { JsonValue } from "../serde_json/JsonValue";`
- `import` `codex-rs/app-server-protocol/schema/typescript/v2/TurnStartParams.ts:9` `import type { AskForApproval } from "./AskForApproval";`
- `import` `codex-rs/app-server-protocol/schema/typescript/v2/TurnStartParams.ts:10` `import type { SandboxPolicy } from "./SandboxPolicy";`
- `import` `codex-rs/app-server-protocol/schema/typescript/v2/TurnStartParams.ts:11` `import type { UserInput } from "./UserInput";`
- `export` `codex-rs/app-server-protocol/schema/typescript/v2/TurnStartParams.ts:13` `export type TurnStartParams = { threadId: string, input: Array<UserInput>,`

## Dependencies (auto sample)
### Imports / Includes
- `import type { CollaborationMode } from "../CollaborationMode";`
- `import type { Personality } from "../Personality";`
- `import type { ReasoningEffort } from "../ReasoningEffort";`
- `import type { ReasoningSummary } from "../ReasoningSummary";`
- `import type { JsonValue } from "../serde_json/JsonValue";`
- `import type { AskForApproval } from "./AskForApproval";`
- `import type { SandboxPolicy } from "./SandboxPolicy";`
- `import type { UserInput } from "./UserInput";`
- `export type TurnStartParams = { threadId: string, input: Array<UserInput>,`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
