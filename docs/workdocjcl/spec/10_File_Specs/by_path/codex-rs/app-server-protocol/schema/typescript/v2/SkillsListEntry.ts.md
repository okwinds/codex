# `codex-rs/app-server-protocol/schema/typescript/v2/SkillsListEntry.ts`

## Identity
- kind: `source`
- ext: `.ts`
- size_bytes: `372`
- sha256: `90a88e7e15fdfffa9a4e7e6b04c81e2b04faae4b1fe95717e0d01e80573cce20`
- generated_utc: `2026-02-08T10:45:14Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server-protocol/schema/typescript/v2/SkillsListEntry.ts` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `export type SkillsListEntry = { cwd: string, skills: Array<SkillMetadata>, errors: Array<SkillErrorInfo>, };`

## Definitions (auto, per-file)
- `import` `codex-rs/app-server-protocol/schema/typescript/v2/SkillsListEntry.ts:4` `import type { SkillErrorInfo } from "./SkillErrorInfo";`
- `import` `codex-rs/app-server-protocol/schema/typescript/v2/SkillsListEntry.ts:5` `import type { SkillMetadata } from "./SkillMetadata";`
- `export` `codex-rs/app-server-protocol/schema/typescript/v2/SkillsListEntry.ts:7` `export type SkillsListEntry = { cwd: string, skills: Array<SkillMetadata>, errors: Array<SkillErrorInfo>, };`

## Dependencies (auto sample)
### Imports / Includes
- `import type { SkillErrorInfo } from "./SkillErrorInfo";`
- `import type { SkillMetadata } from "./SkillMetadata";`
- `export type SkillsListEntry = { cwd: string, skills: Array<SkillMetadata>, errors: Array<SkillErrorInfo>, };`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
