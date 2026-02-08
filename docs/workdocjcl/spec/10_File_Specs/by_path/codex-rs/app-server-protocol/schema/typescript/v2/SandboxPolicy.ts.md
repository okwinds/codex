# `codex-rs/app-server-protocol/schema/typescript/v2/SandboxPolicy.ts`

## Identity
- kind: `source`
- ext: `.ts`
- size_bytes: `565`
- sha256: `5019793e16b6d8f990d24e495ee4136079691edafb1a6aefbbf6071bcdac9428`
- generated_utc: `2026-02-03T16:08:28Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server-protocol/schema/typescript/v2/SandboxPolicy.ts` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `export type SandboxPolicy = { "type": "dangerFullAccess" } | { "type": "readOnly" } | { "type": "externalSandbox", networkAccess: NetworkAccess, } | { "type": "workspaceWrite", writableRoots: Array<AbsolutePathBuf>, networkAccess: boolean, excludeTmpdirEnvVar: boolean, excludeSlashTmp: boolean, };`

## Definitions (auto, per-file)
- `import` `codex-rs/app-server-protocol/schema/typescript/v2/SandboxPolicy.ts:4` `import type { AbsolutePathBuf } from "../AbsolutePathBuf";`
- `import` `codex-rs/app-server-protocol/schema/typescript/v2/SandboxPolicy.ts:5` `import type { NetworkAccess } from "./NetworkAccess";`
- `export` `codex-rs/app-server-protocol/schema/typescript/v2/SandboxPolicy.ts:7` `export type SandboxPolicy = { "type": "dangerFullAccess" } | { "type": "readOnly" } | { "type": "externalSandbox", networkAccess: NetworkAccess, } | { "type": "workspaceWrite", writableRoots: Array<AbsolutePathBuf>, networkAccess: boolean, excludeTmpdirEnvVar: boolean, excludeSlashTmp: boolean, };`

## Dependencies (auto sample)
### Imports / Includes
- `import type { AbsolutePathBuf } from "../AbsolutePathBuf";`
- `import type { NetworkAccess } from "./NetworkAccess";`
- `export type SandboxPolicy = { "type": "dangerFullAccess" } | { "type": "readOnly" } | { "type": "externalSandbox", networkAccess: NetworkAccess, } | { "type": "workspaceWrite", writableRoots: Array<AbsolutePathBuf>, networkAccess: boolean, excludeTmpdirEnvVar: boolean, excludeSlashTmp: boolean, };`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
