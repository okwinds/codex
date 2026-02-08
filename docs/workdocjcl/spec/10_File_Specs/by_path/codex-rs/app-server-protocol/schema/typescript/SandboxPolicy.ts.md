# `codex-rs/app-server-protocol/schema/typescript/SandboxPolicy.ts`

## Identity
- kind: `source`
- ext: `.ts`
- size_bytes: `1210`
- sha256: `5c8a0c2dceb166f38fc466f8af8396ab337def7ab5e370f02ae1aabaf9952711`
- generated_utc: `2026-02-08T10:45:14Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server-protocol/schema/typescript/SandboxPolicy.ts` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `export type SandboxPolicy = { "type": "danger-full-access" } | { "type": "read-only" } | { "type": "external-sandbox",`

## Definitions (auto, per-file)
- `import` `codex-rs/app-server-protocol/schema/typescript/SandboxPolicy.ts:4` `import type { AbsolutePathBuf } from "./AbsolutePathBuf";`
- `import` `codex-rs/app-server-protocol/schema/typescript/SandboxPolicy.ts:5` `import type { NetworkAccess } from "./NetworkAccess";`
- `export` `codex-rs/app-server-protocol/schema/typescript/SandboxPolicy.ts:10` `export type SandboxPolicy = { "type": "danger-full-access" } | { "type": "read-only" } | { "type": "external-sandbox",`

## Dependencies (auto sample)
### Imports / Includes
- `import type { AbsolutePathBuf } from "./AbsolutePathBuf";`
- `import type { NetworkAccess } from "./NetworkAccess";`
- `export type SandboxPolicy = { "type": "danger-full-access" } | { "type": "read-only" } | { "type": "external-sandbox",`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
