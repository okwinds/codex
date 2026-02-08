# `codex-rs/core/src/project_doc.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `24219`
- sha256: `43093558b9a0df82b78f0f8aa760fd146ef47b2fe44557faf5ece254f7b78485`
- generated_utc: `2026-02-03T16:08:29Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/project_doc.rs` (read)

### Outputs / Side Effects
- writes to filesystem

## Public Surface (auto)
- `pub fn discover_project_doc_paths(config: &Config) -> std::io::Result<Vec<PathBuf>> {`

## Definitions (auto, per-file)
- `use` `codex-rs/core/src/project_doc.rs:16` `use crate::config::Config;`
- `use` `codex-rs/core/src/project_doc.rs:17` `use crate::features::Feature;`
- `use` `codex-rs/core/src/project_doc.rs:18` `use crate::skills::SkillMetadata;`
- `use` `codex-rs/core/src/project_doc.rs:19` `use crate::skills::render_skills_section;`
- `use` `codex-rs/core/src/project_doc.rs:20` `use dunce::canonicalize as normalize_path;`
- `use` `codex-rs/core/src/project_doc.rs:21` `use std::path::PathBuf;`
- `use` `codex-rs/core/src/project_doc.rs:22` `use tokio::io::AsyncReadExt;`
- `use` `codex-rs/core/src/project_doc.rs:23` `use tracing::error;`
- `const` `codex-rs/core/src/project_doc.rs:29` `pub const DEFAULT_PROJECT_DOC_FILENAME: &str = "AGENTS.md";`
- `const` `codex-rs/core/src/project_doc.rs:31` `pub const LOCAL_PROJECT_DOC_FILENAME: &str = "AGENTS.override.md";`
- `const` `codex-rs/core/src/project_doc.rs:35` `const PROJECT_DOC_SEPARATOR: &str = "\n\n--- project-doc ---\n\n";`
- `fn` `codex-rs/core/src/project_doc.rs:92` `pub async fn read_project_docs(config: &Config) -> std::io::Result<Option<String>> {`
- `fn` `codex-rs/core/src/project_doc.rs:150` `pub fn discover_project_doc_paths(config: &Config) -> std::io::Result<Vec<PathBuf>> {`
- `use` `codex-rs/core/src/project_doc.rs:237` `use super::*;`
- `use` `codex-rs/core/src/project_doc.rs:238` `use crate::config::ConfigBuilder;`
- `use` `codex-rs/core/src/project_doc.rs:239` `use crate::skills::load_skills;`
- `use` `codex-rs/core/src/project_doc.rs:240` `use std::fs;`
- `use` `codex-rs/core/src/project_doc.rs:241` `use std::path::PathBuf;`
- `use` `codex-rs/core/src/project_doc.rs:242` `use tempfile::TempDir;`
- `fn` `codex-rs/core/src/project_doc.rs:249` `async fn make_config(root: &TempDir, limit: usize, instructions: Option<&str>) -> Config {`
- `fn` `codex-rs/core/src/project_doc.rs:264` `async fn make_config_with_fallback(`
- `fn` `codex-rs/core/src/project_doc.rs:280` `async fn no_doc_file_returns_none() {`
- `fn` `codex-rs/core/src/project_doc.rs:293` `async fn doc_smaller_than_limit_is_returned() {`
- `fn` `codex-rs/core/src/project_doc.rs:309` `async fn doc_larger_than_limit_is_truncated() {`
- `const` `codex-rs/core/src/project_doc.rs:310` `const LIMIT: usize = 1024;`
- `fn` `codex-rs/core/src/project_doc.rs:327` `async fn finds_doc_in_repo_root() {`
- `fn` `codex-rs/core/src/project_doc.rs:356` `async fn zero_byte_limit_disables_docs() {`
- `fn` `codex-rs/core/src/project_doc.rs:370` `async fn merges_existing_instructions_with_project_doc() {`
- `const` `codex-rs/core/src/project_doc.rs:374` `const INSTRUCTIONS: &str = "base instructions";`
- `fn` `codex-rs/core/src/project_doc.rs:388` `async fn keeps_existing_instructions_when_doc_missing() {`
- `const` `codex-rs/core/src/project_doc.rs:391` `const INSTRUCTIONS: &str = "some instructions";`
- `fn` `codex-rs/core/src/project_doc.rs:402` `async fn concatenates_root_and_cwd_docs() {`
- `fn` `codex-rs/core/src/project_doc.rs:431` `async fn agents_local_md_preferred() {`
- `fn` `codex-rs/core/src/project_doc.rs:454` `async fn uses_configured_fallback_when_agents_missing() {`
- `fn` `codex-rs/core/src/project_doc.rs:469` `async fn agents_md_preferred_over_fallbacks() {`
- `fn` `codex-rs/core/src/project_doc.rs:494` `async fn skills_are_appended_to_project_doc() {`
- `fn` `codex-rs/core/src/project_doc.rs:527` `async fn skills_render_without_project_doc() {`
- `fn` `codex-rs/core/src/project_doc.rs:550` `fn create_skill(codex_home: PathBuf, name: &str, description: &str) {`

## Dependencies (auto sample)
### Imports / Includes
- `use crate::config::Config;`
- `use crate::features::Feature;`
- `use crate::skills::SkillMetadata;`
- `use crate::skills::render_skills_section;`
- `use dunce::canonicalize as normalize_path;`
- `use std::path::PathBuf;`
- `use tokio::io::AsyncReadExt;`
- `use tracing::error;`
- `use super::*;`
- `use crate::config::ConfigBuilder;`
- `use crate::skills::load_skills;`
- `use std::fs;`
- `use std::path::PathBuf;`
- `use tempfile::TempDir;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- `workdocjcl/spec/00_Overview/ARCHITECTURE.md`
