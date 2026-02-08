# `codex-rs/app-server-protocol/schema/typescript/SubAgentSource.ts`

## Identity
- kind: `source`
- ext: `.ts`
- size_bytes: `339`
- sha256: `cb052762fe3264859f61a114a5d869bc32bb71a97306ae372a09c77e9ef990e4`
- generated_utc: `2026-02-08T10:45:14Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server-protocol/schema/typescript/SubAgentSource.ts` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `export type SubAgentSource = "review" | "compact" | { "thread_spawn": { parent_thread_id: ThreadId, depth: number, } } | { "other": string };`

## Definitions (auto, per-file)
- `import` `codex-rs/app-server-protocol/schema/typescript/SubAgentSource.ts:4` `import type { ThreadId } from "./ThreadId";`
- `export` `codex-rs/app-server-protocol/schema/typescript/SubAgentSource.ts:6` `export type SubAgentSource = "review" | "compact" | { "thread_spawn": { parent_thread_id: ThreadId, depth: number, } } | { "other": string };`

## Dependencies (auto sample)
### Imports / Includes
- `import type { ThreadId } from "./ThreadId";`
- `export type SubAgentSource = "review" | "compact" | { "thread_spawn": { parent_thread_id: ThreadId, depth: number, } } | { "other": string };`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
