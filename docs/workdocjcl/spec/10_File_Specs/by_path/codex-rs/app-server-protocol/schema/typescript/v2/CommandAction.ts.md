# `codex-rs/app-server-protocol/schema/typescript/v2/CommandAction.ts`

## Identity
- kind: `source`
- ext: `.ts`
- size_bytes: `438`
- sha256: `3bde37a4ee26998cb2c83eb3e16b2a81bd4ff726ae28a0bf49e0499960674cd7`
- generated_utc: `2026-02-08T10:45:14Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server-protocol/schema/typescript/v2/CommandAction.ts` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `export type CommandAction = { "type": "read", command: string, name: string, path: string, } | { "type": "listFiles", command: string, path: string | null, } | { "type": "search", command: string, query: string | null, path: string | null, } | { "type": "unknown", command: string, };`

## Definitions (auto, per-file)
- `export` `codex-rs/app-server-protocol/schema/typescript/v2/CommandAction.ts:5` `export type CommandAction = { "type": "read", command: string, name: string, path: string, } | { "type": "listFiles", command: string, path: string | null, } | { "type": "search", command: string, query: string | null, path: string | null, } | { "type": "unknown", command: string, };`

## Dependencies (auto sample)
### Imports / Includes
- `export type CommandAction = { "type": "read", command: string, name: string, path: string, } | { "type": "listFiles", command: string, path: string | null, } | { "type": "search", command: string, query: string | null, path: string | null, } | { "type": "unknown", command: string, };`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
