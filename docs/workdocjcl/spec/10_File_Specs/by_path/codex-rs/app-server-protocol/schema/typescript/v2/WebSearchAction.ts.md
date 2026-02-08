# `codex-rs/app-server-protocol/schema/typescript/v2/WebSearchAction.ts`

## Identity
- kind: `source`
- ext: `.ts`
- size_bytes: `399`
- sha256: `f1dc1197e35b48fd16134a80353ebb606256126a634b4580406a5bffed1b0395`
- generated_utc: `2026-02-08T10:45:14Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server-protocol/schema/typescript/v2/WebSearchAction.ts` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `export type WebSearchAction = { "type": "search", query: string | null, queries: Array<string> | null, } | { "type": "openPage", url: string | null, } | { "type": "findInPage", url: string | null, pattern: string | null, } | { "type": "other" };`

## Definitions (auto, per-file)
- `export` `codex-rs/app-server-protocol/schema/typescript/v2/WebSearchAction.ts:5` `export type WebSearchAction = { "type": "search", query: string | null, queries: Array<string> | null, } | { "type": "openPage", url: string | null, } | { "type": "findInPage", url: string | null, pattern: string | null, } | { "type": "other" };`

## Dependencies (auto sample)
### Imports / Includes
- `export type WebSearchAction = { "type": "search", query: string | null, queries: Array<string> | null, } | { "type": "openPage", url: string | null, } | { "type": "findInPage", url: string | null, pattern: string | null, } | { "type": "other" };`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
