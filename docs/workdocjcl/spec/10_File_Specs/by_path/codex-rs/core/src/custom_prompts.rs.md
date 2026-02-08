# `codex-rs/core/src/custom_prompts.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `8630`
- sha256: `6e9f9c9cd27dba076c5b8a9630c501fdfb4ef2fb37ff115afb4038b16754eacd`
- generated_utc: `2026-02-08T10:45:32Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/custom_prompts.rs` (read)

### Outputs / Side Effects
- writes to filesystem

## Public Surface (auto)
- `pub fn default_prompts_dir() -> Option<PathBuf> {`

## Definitions (auto, per-file)
- `use` `codex-rs/core/src/custom_prompts.rs:1` `use codex_protocol::custom_prompts::CustomPrompt;`
- `use` `codex-rs/core/src/custom_prompts.rs:2` `use std::collections::HashSet;`
- `use` `codex-rs/core/src/custom_prompts.rs:3` `use std::path::Path;`
- `use` `codex-rs/core/src/custom_prompts.rs:4` `use std::path::PathBuf;`
- `use` `codex-rs/core/src/custom_prompts.rs:5` `use tokio::fs;`
- `fn` `codex-rs/core/src/custom_prompts.rs:9` `pub fn default_prompts_dir() -> Option<PathBuf> {`
- `fn` `codex-rs/core/src/custom_prompts.rs:17` `pub async fn discover_prompts_in(dir: &Path) -> Vec<CustomPrompt> {`
- `fn` `codex-rs/core/src/custom_prompts.rs:23` `pub async fn discover_prompts_in_excluding(`
- `fn` `codex-rs/core/src/custom_prompts.rs:83` `fn parse_frontmatter(content: &str) -> (Option<String>, Option<String>, String) {`
- `use` `codex-rs/core/src/custom_prompts.rs:149` `use super::*;`
- `use` `codex-rs/core/src/custom_prompts.rs:150` `use std::fs;`
- `use` `codex-rs/core/src/custom_prompts.rs:151` `use tempfile::tempdir;`
- `fn` `codex-rs/core/src/custom_prompts.rs:154` `async fn empty_when_dir_missing() {`
- `fn` `codex-rs/core/src/custom_prompts.rs:162` `async fn discovers_and_sorts_files() {`
- `fn` `codex-rs/core/src/custom_prompts.rs:174` `async fn excludes_builtins() {`
- `fn` `codex-rs/core/src/custom_prompts.rs:187` `async fn skips_non_utf8_files() {`
- `fn` `codex-rs/core/src/custom_prompts.rs:201` `async fn discovers_symlinked_md_files() {`
- `fn` `codex-rs/core/src/custom_prompts.rs:219` `async fn parses_frontmatter_and_strips_from_body() {`
- `fn` `codex-rs/core/src/custom_prompts.rs:237` `fn parse_frontmatter_preserves_body_newlines() {`

## Dependencies (auto sample)
### Imports / Includes
- `use codex_protocol::custom_prompts::CustomPrompt;`
- `use std::collections::HashSet;`
- `use std::path::Path;`
- `use std::path::PathBuf;`
- `use tokio::fs;`
- `use super::*;`
- `use std::fs;`
- `use tempfile::tempdir;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- `docs/workdocjcl/spec/00_Overview/ARCHITECTURE.md`
