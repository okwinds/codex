# `codex-rs/core/src/skills/render.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `3007`
- sha256: `64fd21e131d05cb897431109ad530f965a489611768b53458d2dbaed8ebc1a55`
- generated_utc: `2026-02-08T10:45:33Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/skills/render.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub fn render_skills_section(skills: &[SkillMetadata]) -> Option<String> {`

## Definitions (auto, per-file)
- `use` `codex-rs/core/src/skills/render.rs:1` `use crate::skills::model::SkillMetadata;`
- `fn` `codex-rs/core/src/skills/render.rs:3` `pub fn render_skills_section(skills: &[SkillMetadata]) -> Option<String> {`

## Dependencies (auto sample)
### Imports / Includes
- `use crate::skills::model::SkillMetadata;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- `docs/workdocjcl/spec/00_Overview/ARCHITECTURE.md`
