# `codex-rs/app-server-protocol/schema/typescript/AuthStatusChangeNotification.ts`

## Identity
- kind: `source`
- ext: `.ts`
- size_bytes: `350`
- sha256: `b4c13c2672d6f16ec0f372a703fac219dbe753afee76a4875b7f0d267a5eaa1b`
- generated_utc: `2026-02-08T10:45:14Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server-protocol/schema/typescript/AuthStatusChangeNotification.ts` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `export type AuthStatusChangeNotification = { authMethod: AuthMode | null, };`

## Definitions (auto, per-file)
- `import` `codex-rs/app-server-protocol/schema/typescript/AuthStatusChangeNotification.ts:4` `import type { AuthMode } from "./AuthMode";`
- `export` `codex-rs/app-server-protocol/schema/typescript/AuthStatusChangeNotification.ts:9` `export type AuthStatusChangeNotification = { authMethod: AuthMode | null, };`

## Dependencies (auto sample)
### Imports / Includes
- `import type { AuthMode } from "./AuthMode";`
- `export type AuthStatusChangeNotification = { authMethod: AuthMode | null, };`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
