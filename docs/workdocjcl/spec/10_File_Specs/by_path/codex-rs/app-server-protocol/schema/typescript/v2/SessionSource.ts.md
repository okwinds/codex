# `codex-rs/app-server-protocol/schema/typescript/v2/SessionSource.ts`

## Identity
- kind: `source`
- ext: `.ts`
- size_bytes: `324`
- sha256: `99f92ffde56b5cb33bc21c6b56f407ab8c908d29a98b5510c64d7f907df0ffb7`
- generated_utc: `2026-02-08T10:45:14Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server-protocol/schema/typescript/v2/SessionSource.ts` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `export type SessionSource = "cli" | "vscode" | "exec" | "appServer" | { "subAgent": SubAgentSource } | "unknown";`

## Definitions (auto, per-file)
- `import` `codex-rs/app-server-protocol/schema/typescript/v2/SessionSource.ts:4` `import type { SubAgentSource } from "../SubAgentSource";`
- `export` `codex-rs/app-server-protocol/schema/typescript/v2/SessionSource.ts:6` `export type SessionSource = "cli" | "vscode" | "exec" | "appServer" | { "subAgent": SubAgentSource } | "unknown";`

## Dependencies (auto sample)
### Imports / Includes
- `import type { SubAgentSource } from "../SubAgentSource";`
- `export type SessionSource = "cli" | "vscode" | "exec" | "appServer" | { "subAgent": SubAgentSource } | "unknown";`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
