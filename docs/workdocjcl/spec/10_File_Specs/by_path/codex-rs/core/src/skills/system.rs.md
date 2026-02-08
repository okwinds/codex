# `codex-rs/core/src/skills/system.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `7199`
- sha256: `b3fdedc3bb72478fab0896fd6dc063e1db59521ebdbac018b9adc4d9cd4c4d5a`
- generated_utc: `2026-02-03T16:08:29Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/skills/system.rs` (read)

### Outputs / Side Effects
- writes to filesystem
- writes to stdout/stderr

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `use` `codex-rs/core/src/skills/system.rs:1` `use codex_utils_absolute_path::AbsolutePathBuf;`
- `use` `codex-rs/core/src/skills/system.rs:2` `use include_dir::Dir;`
- `use` `codex-rs/core/src/skills/system.rs:3` `use std::collections::hash_map::DefaultHasher;`
- `use` `codex-rs/core/src/skills/system.rs:4` `use std::fs;`
- `use` `codex-rs/core/src/skills/system.rs:5` `use std::hash::Hash;`
- `use` `codex-rs/core/src/skills/system.rs:6` `use std::hash::Hasher;`
- `use` `codex-rs/core/src/skills/system.rs:7` `use std::path::Path;`
- `use` `codex-rs/core/src/skills/system.rs:8` `use std::path::PathBuf;`
- `use` `codex-rs/core/src/skills/system.rs:10` `use thiserror::Error;`
- `const` `codex-rs/core/src/skills/system.rs:12` `const SYSTEM_SKILLS_DIR: Dir =`
- `const` `codex-rs/core/src/skills/system.rs:15` `const SYSTEM_SKILLS_DIR_NAME: &str = ".system";`
- `const` `codex-rs/core/src/skills/system.rs:16` `const SKILLS_DIR_NAME: &str = "skills";`
- `const` `codex-rs/core/src/skills/system.rs:17` `const SYSTEM_SKILLS_MARKER_FILENAME: &str = ".codex-system-skills.marker";`
- `const` `codex-rs/core/src/skills/system.rs:18` `const SYSTEM_SKILLS_MARKER_SALT: &str = "v1";`
- `fn` `codex-rs/core/src/skills/system.rs:34` `fn system_cache_root_dir_abs(codex_home: &AbsolutePathBuf) -> std::io::Result<AbsolutePathBuf> {`
- `fn` `codex-rs/core/src/skills/system.rs:81` `fn read_marker(path: &AbsolutePathBuf) -> Result<String, SystemSkillsError> {`
- `fn` `codex-rs/core/src/skills/system.rs:88` `fn embedded_system_skills_fingerprint() -> String {`
- `fn` `codex-rs/core/src/skills/system.rs:102` `fn collect_fingerprint_items(dir: &Dir<'_>, items: &mut Vec<(String, Option<u64>)>) {`
- `fn` `codex-rs/core/src/skills/system.rs:124` `fn write_embedded_dir(dir: &Dir<'_>, dest: &AbsolutePathBuf) -> Result<(), SystemSkillsError> {`
- `impl` `codex-rs/core/src/skills/system.rs:167` `impl SystemSkillsError {`
- `fn` `codex-rs/core/src/skills/system.rs:168` `fn io(action: &'static str, source: std::io::Error) -> Self {`
- `use` `codex-rs/core/src/skills/system.rs:175` `use super::SYSTEM_SKILLS_DIR;`
- `use` `codex-rs/core/src/skills/system.rs:176` `use super::collect_fingerprint_items;`
- `fn` `codex-rs/core/src/skills/system.rs:179` `fn fingerprint_traverses_nested_entries() {`

## Dependencies (auto sample)
### Imports / Includes
- `use codex_utils_absolute_path::AbsolutePathBuf;`
- `use include_dir::Dir;`
- `use std::collections::hash_map::DefaultHasher;`
- `use std::fs;`
- `use std::hash::Hash;`
- `use std::hash::Hasher;`
- `use std::path::Path;`
- `use std::path::PathBuf;`
- `use thiserror::Error;`
- `use super::SYSTEM_SKILLS_DIR;`
- `use super::collect_fingerprint_items;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)

## Spec Links
- `workdocjcl/spec/00_Overview/ARCHITECTURE.md`
