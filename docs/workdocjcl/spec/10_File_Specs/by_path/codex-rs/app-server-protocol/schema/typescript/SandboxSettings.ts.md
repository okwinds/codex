# `codex-rs/app-server-protocol/schema/typescript/SandboxSettings.ts`

## Identity
- kind: `source`
- ext: `.ts`
- size_bytes: `386`
- sha256: `04e0ec18a6d544cd11aa8bb7c3bfb7cdb90a06d75fde4f53a95ed1a715984b52`
- generated_utc: `2026-02-08T10:45:14Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server-protocol/schema/typescript/SandboxSettings.ts` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `export type SandboxSettings = { writableRoots: Array<AbsolutePathBuf>, networkAccess: boolean | null, excludeTmpdirEnvVar: boolean | null, excludeSlashTmp: boolean | null, };`

## Definitions (auto, per-file)
- `import` `codex-rs/app-server-protocol/schema/typescript/SandboxSettings.ts:4` `import type { AbsolutePathBuf } from "./AbsolutePathBuf";`
- `export` `codex-rs/app-server-protocol/schema/typescript/SandboxSettings.ts:6` `export type SandboxSettings = { writableRoots: Array<AbsolutePathBuf>, networkAccess: boolean | null, excludeTmpdirEnvVar: boolean | null, excludeSlashTmp: boolean | null, };`

## Dependencies (auto sample)
### Imports / Includes
- `import type { AbsolutePathBuf } from "./AbsolutePathBuf";`
- `export type SandboxSettings = { writableRoots: Array<AbsolutePathBuf>, networkAccess: boolean | null, excludeTmpdirEnvVar: boolean | null, excludeSlashTmp: boolean | null, };`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
