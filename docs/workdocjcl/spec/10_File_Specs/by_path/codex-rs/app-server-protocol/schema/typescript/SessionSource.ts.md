# `codex-rs/app-server-protocol/schema/typescript/SessionSource.ts`

## Identity
- kind: `source`
- ext: `.ts`
- size_bytes: `317`
- sha256: `475dd71962e48e5eb880ced7def925602e13763439ed1a89b02eca3cdbca5c52`
- generated_utc: `2026-02-08T10:45:14Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server-protocol/schema/typescript/SessionSource.ts` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `export type SessionSource = "cli" | "vscode" | "exec" | "mcp" | { "subagent": SubAgentSource } | "unknown";`

## Definitions (auto, per-file)
- `import` `codex-rs/app-server-protocol/schema/typescript/SessionSource.ts:4` `import type { SubAgentSource } from "./SubAgentSource";`
- `export` `codex-rs/app-server-protocol/schema/typescript/SessionSource.ts:6` `export type SessionSource = "cli" | "vscode" | "exec" | "mcp" | { "subagent": SubAgentSource } | "unknown";`

## Dependencies (auto sample)
### Imports / Includes
- `import type { SubAgentSource } from "./SubAgentSource";`
- `export type SessionSource = "cli" | "vscode" | "exec" | "mcp" | { "subagent": SubAgentSource } | "unknown";`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
