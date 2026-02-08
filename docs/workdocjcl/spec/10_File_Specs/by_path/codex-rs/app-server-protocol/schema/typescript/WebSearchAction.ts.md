# `codex-rs/app-server-protocol/schema/typescript/WebSearchAction.ts`

## Identity
- kind: `source`
- ext: `.ts`
- size_bytes: `372`
- sha256: `dd495f13fb38ec0fb4d5746a2b706e7890c60795e3e768cb1f640109fd0e0b07`
- generated_utc: `2026-02-03T16:08:28Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server-protocol/schema/typescript/WebSearchAction.ts` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `export type WebSearchAction = { "type": "search", query?: string, queries?: Array<string>, } | { "type": "open_page", url?: string, } | { "type": "find_in_page", url?: string, pattern?: string, } | { "type": "other" };`

## Definitions (auto, per-file)
- `export` `codex-rs/app-server-protocol/schema/typescript/WebSearchAction.ts:5` `export type WebSearchAction = { "type": "search", query?: string, queries?: Array<string>, } | { "type": "open_page", url?: string, } | { "type": "find_in_page", url?: string, pattern?: string, } | { "type": "other" };`

## Dependencies (auto sample)
### Imports / Includes
- `export type WebSearchAction = { "type": "search", query?: string, queries?: Array<string>, } | { "type": "open_page", url?: string, } | { "type": "find_in_page", url?: string, pattern?: string, } | { "type": "other" };`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
