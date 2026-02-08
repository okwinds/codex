# `codex-rs/app-server-protocol/schema/typescript/v2/ConfigRequirements.ts`

## Identity
- kind: `source`
- ext: `.ts`
- size_bytes: `619`
- sha256: `80c9035c222a5b237b4e416df913392696190d473495f29f751d484741b942e9`
- generated_utc: `2026-02-08T10:45:14Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server-protocol/schema/typescript/v2/ConfigRequirements.ts` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `export type ConfigRequirements = {allowedApprovalPolicies: Array<AskForApproval> | null, allowedSandboxModes: Array<SandboxMode> | null, allowedWebSearchModes: Array<WebSearchMode> | null, enforceResidency: ResidencyRequirement | null};`

## Definitions (auto, per-file)
- `import` `codex-rs/app-server-protocol/schema/typescript/v2/ConfigRequirements.ts:4` `import type { WebSearchMode } from "../WebSearchMode";`
- `import` `codex-rs/app-server-protocol/schema/typescript/v2/ConfigRequirements.ts:5` `import type { AskForApproval } from "./AskForApproval";`
- `import` `codex-rs/app-server-protocol/schema/typescript/v2/ConfigRequirements.ts:6` `import type { ResidencyRequirement } from "./ResidencyRequirement";`
- `import` `codex-rs/app-server-protocol/schema/typescript/v2/ConfigRequirements.ts:7` `import type { SandboxMode } from "./SandboxMode";`
- `export` `codex-rs/app-server-protocol/schema/typescript/v2/ConfigRequirements.ts:9` `export type ConfigRequirements = {allowedApprovalPolicies: Array<AskForApproval> | null, allowedSandboxModes: Array<SandboxMode> | null, allowedWebSearchModes: Array<WebSearchMode> | null, enforceResidency: ResidencyRequirement | null};`

## Dependencies (auto sample)
### Imports / Includes
- `import type { WebSearchMode } from "../WebSearchMode";`
- `import type { AskForApproval } from "./AskForApproval";`
- `import type { ResidencyRequirement } from "./ResidencyRequirement";`
- `import type { SandboxMode } from "./SandboxMode";`
- `export type ConfigRequirements = {allowedApprovalPolicies: Array<AskForApproval> | null, allowedSandboxModes: Array<SandboxMode> | null, allowedWebSearchModes: Array<WebSearchMode> | null, enforceResidency: ResidencyRequirement | null};`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
