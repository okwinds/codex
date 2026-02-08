# `sdk/typescript/src/items.ts`

## Identity
- kind: `source`
- ext: `.ts`
- size_bytes: `3577`
- sha256: `d041eae2941c65136c5558022b3e633458ae4bc051cdfa83e361a60fcdcf1765`
- generated_utc: `2026-02-08T10:45:42Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `sdk/typescript/src/items.ts` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `export type CommandExecutionStatus = "in_progress" | "completed" | "failed";`
- `export type CommandExecutionItem = {`
- `export type PatchChangeKind = "add" | "delete" | "update";`
- `export type FileUpdateChange = {`
- `export type PatchApplyStatus = "completed" | "failed";`
- `export type FileChangeItem = {`
- `export type McpToolCallStatus = "in_progress" | "completed" | "failed";`
- `export type McpToolCallItem = {`
- `export type AgentMessageItem = {`
- `export type ReasoningItem = {`
- `export type WebSearchItem = {`
- `export type ErrorItem = {`
- `export type TodoItem = {`
- `export type TodoListItem = {`
- `export type ThreadItem =`

## Definitions (auto, per-file)
- `import` `sdk/typescript/src/items.ts:3` `import type { ContentBlock as McpContentBlock } from "@modelcontextprotocol/sdk/types.js";`
- `export` `sdk/typescript/src/items.ts:6` `export type CommandExecutionStatus = "in_progress" | "completed" | "failed";`
- `export` `sdk/typescript/src/items.ts:9` `export type CommandExecutionItem = {`
- `export` `sdk/typescript/src/items.ts:23` `export type PatchChangeKind = "add" | "delete" | "update";`
- `export` `sdk/typescript/src/items.ts:26` `export type FileUpdateChange = {`
- `export` `sdk/typescript/src/items.ts:32` `export type PatchApplyStatus = "completed" | "failed";`
- `export` `sdk/typescript/src/items.ts:35` `export type FileChangeItem = {`
- `export` `sdk/typescript/src/items.ts:45` `export type McpToolCallStatus = "in_progress" | "completed" | "failed";`
- `export` `sdk/typescript/src/items.ts:51` `export type McpToolCallItem = {`
- `export` `sdk/typescript/src/items.ts:74` `export type AgentMessageItem = {`
- `export` `sdk/typescript/src/items.ts:82` `export type ReasoningItem = {`
- `export` `sdk/typescript/src/items.ts:89` `export type WebSearchItem = {`
- `export` `sdk/typescript/src/items.ts:96` `export type ErrorItem = {`
- `export` `sdk/typescript/src/items.ts:103` `export type TodoItem = {`
- `export` `sdk/typescript/src/items.ts:112` `export type TodoListItem = {`
- `export` `sdk/typescript/src/items.ts:119` `export type ThreadItem =`

## Dependencies (auto sample)
### Imports / Includes
- `import type { ContentBlock as McpContentBlock } from "@modelcontextprotocol/sdk/types.js";`
- `export type CommandExecutionStatus = "in_progress" | "completed" | "failed";`
- `export type CommandExecutionItem = {`
- `export type PatchChangeKind = "add" | "delete" | "update";`
- `export type FileUpdateChange = {`
- `export type PatchApplyStatus = "completed" | "failed";`
- `export type FileChangeItem = {`
- `export type McpToolCallStatus = "in_progress" | "completed" | "failed";`
- `export type McpToolCallItem = {`
- `export type AgentMessageItem = {`
- `export type ReasoningItem = {`
- `export type WebSearchItem = {`
- `export type ErrorItem = {`
- `export type TodoItem = {`
- `export type TodoListItem = {`
- `export type ThreadItem =`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- `docs/workdocjcl/spec/00_Overview/PROJECT.md`
