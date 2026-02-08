# `codex-rs/app-server-protocol/schema/typescript/AgentStatus.ts`

## Identity
- kind: `source`
- ext: `.ts`
- size_bytes: `355`
- sha256: `72c15384d09ee485ad05809d14ecafd7ff498346b4ed6ed30b21962fefc31ccc`
- generated_utc: `2026-02-03T16:08:28Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server-protocol/schema/typescript/AgentStatus.ts` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `export type AgentStatus = "pending_init" | "running" | { "completed": string | null } | { "errored": string } | "shutdown" | "not_found";`

## Definitions (auto, per-file)
- `export` `codex-rs/app-server-protocol/schema/typescript/AgentStatus.ts:8` `export type AgentStatus = "pending_init" | "running" | { "completed": string | null } | { "errored": string } | "shutdown" | "not_found";`

## Dependencies (auto sample)
### Imports / Includes
- `export type AgentStatus = "pending_init" | "running" | { "completed": string | null } | { "errored": string } | "shutdown" | "not_found";`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
