# `codex-rs/app-server-protocol/schema/typescript/WebSearchItem.ts`

## Identity
- kind: `source`
- ext: `.ts`
- size_bytes: `296`
- sha256: `ff5fd969bf2976874780007c002d139250e005a14c551e78331d6fe87406d74e`
- generated_utc: `2026-02-03T16:08:28Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server-protocol/schema/typescript/WebSearchItem.ts` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `export type WebSearchItem = { id: string, query: string, action: WebSearchAction, };`

## Definitions (auto, per-file)
- `import` `codex-rs/app-server-protocol/schema/typescript/WebSearchItem.ts:4` `import type { WebSearchAction } from "./WebSearchAction";`
- `export` `codex-rs/app-server-protocol/schema/typescript/WebSearchItem.ts:6` `export type WebSearchItem = { id: string, query: string, action: WebSearchAction, };`

## Dependencies (auto sample)
### Imports / Includes
- `import type { WebSearchAction } from "./WebSearchAction";`
- `export type WebSearchItem = { id: string, query: string, action: WebSearchAction, };`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
