# `codex-rs/app-server-protocol/schema/typescript/ConversationSummary.ts`

## Identity
- kind: `source`
- ext: `.ts`
- size_bytes: `581`
- sha256: `1b9fb86de74b126bad433437458b9122acd3df1649099bc643084db342143822`
- generated_utc: `2026-02-08T10:45:14Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server-protocol/schema/typescript/ConversationSummary.ts` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `export type ConversationSummary = { conversationId: ThreadId, path: string, preview: string, timestamp: string | null, updatedAt: string | null, modelProvider: string, cwd: string, cliVersion: string, source: SessionSource, gitInfo: ConversationGitInfo | null, };`

## Definitions (auto, per-file)
- `import` `codex-rs/app-server-protocol/schema/typescript/ConversationSummary.ts:4` `import type { ConversationGitInfo } from "./ConversationGitInfo";`
- `import` `codex-rs/app-server-protocol/schema/typescript/ConversationSummary.ts:5` `import type { SessionSource } from "./SessionSource";`
- `import` `codex-rs/app-server-protocol/schema/typescript/ConversationSummary.ts:6` `import type { ThreadId } from "./ThreadId";`
- `export` `codex-rs/app-server-protocol/schema/typescript/ConversationSummary.ts:8` `export type ConversationSummary = { conversationId: ThreadId, path: string, preview: string, timestamp: string | null, updatedAt: string | null, modelProvider: string, cwd: string, cliVersion: string, source: SessionSource, gitInfo: ConversationGitInfo | null, };`

## Dependencies (auto sample)
### Imports / Includes
- `import type { ConversationGitInfo } from "./ConversationGitInfo";`
- `import type { SessionSource } from "./SessionSource";`
- `import type { ThreadId } from "./ThreadId";`
- `export type ConversationSummary = { conversationId: ThreadId, path: string, preview: string, timestamp: string | null, updatedAt: string | null, modelProvider: string, cwd: string, cliVersion: string, source: SessionSource, gitInfo: ConversationGitInfo | null, };`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
