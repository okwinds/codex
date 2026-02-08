# `codex-rs/app-server-protocol/schema/typescript/v2/McpServerStatus.ts`

## Identity
- kind: `source`
- ext: `.ts`
- size_bytes: `533`
- sha256: `f9d7e76bf6d36aa8bf9e20c2bfbe4af5c772cffea485f4543dda2b34960bcb6a`
- generated_utc: `2026-02-03T16:08:28Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server-protocol/schema/typescript/v2/McpServerStatus.ts` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `export type McpServerStatus = { name: string, tools: { [key in string]?: Tool }, resources: Array<Resource>, resourceTemplates: Array<ResourceTemplate>, authStatus: McpAuthStatus, };`

## Definitions (auto, per-file)
- `import` `codex-rs/app-server-protocol/schema/typescript/v2/McpServerStatus.ts:4` `import type { Resource } from "../Resource";`
- `import` `codex-rs/app-server-protocol/schema/typescript/v2/McpServerStatus.ts:5` `import type { ResourceTemplate } from "../ResourceTemplate";`
- `import` `codex-rs/app-server-protocol/schema/typescript/v2/McpServerStatus.ts:6` `import type { Tool } from "../Tool";`
- `import` `codex-rs/app-server-protocol/schema/typescript/v2/McpServerStatus.ts:7` `import type { McpAuthStatus } from "./McpAuthStatus";`
- `export` `codex-rs/app-server-protocol/schema/typescript/v2/McpServerStatus.ts:9` `export type McpServerStatus = { name: string, tools: { [key in string]?: Tool }, resources: Array<Resource>, resourceTemplates: Array<ResourceTemplate>, authStatus: McpAuthStatus, };`

## Dependencies (auto sample)
### Imports / Includes
- `import type { Resource } from "../Resource";`
- `import type { ResourceTemplate } from "../ResourceTemplate";`
- `import type { Tool } from "../Tool";`
- `import type { McpAuthStatus } from "./McpAuthStatus";`
- `export type McpServerStatus = { name: string, tools: { [key in string]?: Tool }, resources: Array<Resource>, resourceTemplates: Array<ResourceTemplate>, authStatus: McpAuthStatus, };`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
