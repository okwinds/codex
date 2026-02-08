# `codex-rs/app-server-protocol/schema/typescript/GitDiffToRemoteResponse.ts`

## Identity
- kind: `source`
- ext: `.ts`
- size_bytes: `263`
- sha256: `c8b4be6e7a9c522a2865e2df4d8b54e0f0f16172f97c3a6c412997056a6297ab`
- generated_utc: `2026-02-08T10:45:14Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server-protocol/schema/typescript/GitDiffToRemoteResponse.ts` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `export type GitDiffToRemoteResponse = { sha: GitSha, diff: string, };`

## Definitions (auto, per-file)
- `import` `codex-rs/app-server-protocol/schema/typescript/GitDiffToRemoteResponse.ts:4` `import type { GitSha } from "./GitSha";`
- `export` `codex-rs/app-server-protocol/schema/typescript/GitDiffToRemoteResponse.ts:6` `export type GitDiffToRemoteResponse = { sha: GitSha, diff: string, };`

## Dependencies (auto sample)
### Imports / Includes
- `import type { GitSha } from "./GitSha";`
- `export type GitDiffToRemoteResponse = { sha: GitSha, diff: string, };`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
