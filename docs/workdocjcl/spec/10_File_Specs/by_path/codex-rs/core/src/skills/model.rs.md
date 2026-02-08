# `codex-rs/core/src/skills/model.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `1924`
- sha256: `320a9fb1d4014045998a4ba286d1d8511b20430b10abe47d35d3476537cd841b`
- generated_utc: `2026-02-08T10:45:33Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/skills/model.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub struct SkillMetadata {`
- `pub struct SkillInterface {`
- `pub struct SkillDependencies {`
- `pub struct SkillToolDependency {`
- `pub struct SkillError {`
- `pub struct SkillLoadOutcome {`
- `pub fn is_skill_enabled(&self, skill: &SkillMetadata) -> bool {`
- `pub fn enabled_skills(&self) -> Vec<SkillMetadata> {`
- `pub fn skills_with_enabled(&self) -> impl Iterator<Item = (&SkillMetadata, bool)> {`

## Definitions (auto, per-file)
- `use` `codex-rs/core/src/skills/model.rs:1` `use std::collections::HashSet;`
- `use` `codex-rs/core/src/skills/model.rs:2` `use std::path::PathBuf;`
- `use` `codex-rs/core/src/skills/model.rs:4` `use codex_protocol::protocol::SkillScope;`
- `struct` `codex-rs/core/src/skills/model.rs:7` `pub struct SkillMetadata {`
- `struct` `codex-rs/core/src/skills/model.rs:18` `pub struct SkillInterface {`
- `struct` `codex-rs/core/src/skills/model.rs:28` `pub struct SkillDependencies {`
- `struct` `codex-rs/core/src/skills/model.rs:33` `pub struct SkillToolDependency {`
- `struct` `codex-rs/core/src/skills/model.rs:43` `pub struct SkillError {`
- `struct` `codex-rs/core/src/skills/model.rs:49` `pub struct SkillLoadOutcome {`
- `impl` `codex-rs/core/src/skills/model.rs:55` `impl SkillLoadOutcome {`
- `fn` `codex-rs/core/src/skills/model.rs:56` `pub fn is_skill_enabled(&self, skill: &SkillMetadata) -> bool {`
- `fn` `codex-rs/core/src/skills/model.rs:60` `pub fn enabled_skills(&self) -> Vec<SkillMetadata> {`
- `fn` `codex-rs/core/src/skills/model.rs:68` `pub fn skills_with_enabled(&self) -> impl Iterator<Item = (&SkillMetadata, bool)> {`

## Dependencies (auto sample)
### Imports / Includes
- `use std::collections::HashSet;`
- `use std::path::PathBuf;`
- `use codex_protocol::protocol::SkillScope;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- `docs/workdocjcl/spec/00_Overview/ARCHITECTURE.md`
