# `codex-rs/app-server-protocol/schema/typescript/InitializeParams.ts`

## Identity
- kind: `source`
- ext: `.ts`
- size_bytes: `378`
- sha256: `bfc13b4fc9e37f629ee67b42d6e7f342ba38668ff528e738a911de5ebcfd545f`
- generated_utc: `2026-02-08T10:45:14Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server-protocol/schema/typescript/InitializeParams.ts` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `export type InitializeParams = { clientInfo: ClientInfo, capabilities: InitializeCapabilities | null, };`

## Definitions (auto, per-file)
- `import` `codex-rs/app-server-protocol/schema/typescript/InitializeParams.ts:4` `import type { ClientInfo } from "./ClientInfo";`
- `import` `codex-rs/app-server-protocol/schema/typescript/InitializeParams.ts:5` `import type { InitializeCapabilities } from "./InitializeCapabilities";`
- `export` `codex-rs/app-server-protocol/schema/typescript/InitializeParams.ts:7` `export type InitializeParams = { clientInfo: ClientInfo, capabilities: InitializeCapabilities | null, };`

## Dependencies (auto sample)
### Imports / Includes
- `import type { ClientInfo } from "./ClientInfo";`
- `import type { InitializeCapabilities } from "./InitializeCapabilities";`
- `export type InitializeParams = { clientInfo: ClientInfo, capabilities: InitializeCapabilities | null, };`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
