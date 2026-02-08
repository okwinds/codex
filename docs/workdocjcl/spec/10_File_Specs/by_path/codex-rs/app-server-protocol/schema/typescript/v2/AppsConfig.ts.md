# `codex-rs/app-server-protocol/schema/typescript/v2/AppsConfig.ts`

## Identity
- kind: `source`
- ext: `.ts`
- size_bytes: `328`
- sha256: `63c9b8f87f8f28a83ff8a20e2a6028c8f9e4e99dc47058297e6f0423ac08f122`
- generated_utc: `2026-02-08T10:45:14Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server-protocol/schema/typescript/v2/AppsConfig.ts` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `export type AppsConfig = { [key in string]?: { enabled: boolean, disabled_reason: AppDisabledReason | null, } };`

## Definitions (auto, per-file)
- `import` `codex-rs/app-server-protocol/schema/typescript/v2/AppsConfig.ts:4` `import type { AppDisabledReason } from "./AppDisabledReason";`
- `export` `codex-rs/app-server-protocol/schema/typescript/v2/AppsConfig.ts:6` `export type AppsConfig = { [key in string]?: { enabled: boolean, disabled_reason: AppDisabledReason | null, } };`

## Dependencies (auto sample)
### Imports / Includes
- `import type { AppDisabledReason } from "./AppDisabledReason";`
- `export type AppsConfig = { [key in string]?: { enabled: boolean, disabled_reason: AppDisabledReason | null, } };`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
