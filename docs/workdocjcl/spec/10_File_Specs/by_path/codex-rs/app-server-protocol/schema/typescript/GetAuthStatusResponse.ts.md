# `codex-rs/app-server-protocol/schema/typescript/GetAuthStatusResponse.ts`

## Identity
- kind: `source`
- ext: `.ts`
- size_bytes: `329`
- sha256: `9aaaa5326b399883165edd426d2b340fe4d58e19d0481c860ca28813a365d853`
- generated_utc: `2026-02-03T16:08:28Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server-protocol/schema/typescript/GetAuthStatusResponse.ts` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `export type GetAuthStatusResponse = { authMethod: AuthMode | null, authToken: string | null, requiresOpenaiAuth: boolean | null, };`

## Definitions (auto, per-file)
- `import` `codex-rs/app-server-protocol/schema/typescript/GetAuthStatusResponse.ts:4` `import type { AuthMode } from "./AuthMode";`
- `export` `codex-rs/app-server-protocol/schema/typescript/GetAuthStatusResponse.ts:6` `export type GetAuthStatusResponse = { authMethod: AuthMode | null, authToken: string | null, requiresOpenaiAuth: boolean | null, };`

## Dependencies (auto sample)
### Imports / Includes
- `import type { AuthMode } from "./AuthMode";`
- `export type GetAuthStatusResponse = { authMethod: AuthMode | null, authToken: string | null, requiresOpenaiAuth: boolean | null, };`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
