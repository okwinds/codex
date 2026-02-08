# `codex-rs/file-search/src/main.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `2748`
- sha256: `6a7ef6cf4b6c937beb396b9a4d7c2d9d44cd008d5d8b45958b335886c707da83`
- generated_utc: `2026-02-08T10:45:37Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/file-search/src/main.rs` (read)

### Outputs / Side Effects
- writes to stdout/stderr

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `use` `codex-rs/file-search/src/main.rs:1` `use std::io::IsTerminal;`
- `use` `codex-rs/file-search/src/main.rs:2` `use std::path::Path;`
- `use` `codex-rs/file-search/src/main.rs:4` `use clap::Parser;`
- `use` `codex-rs/file-search/src/main.rs:5` `use codex_file_search::Cli;`
- `use` `codex-rs/file-search/src/main.rs:6` `use codex_file_search::FileMatch;`
- `use` `codex-rs/file-search/src/main.rs:7` `use codex_file_search::Reporter;`
- `use` `codex-rs/file-search/src/main.rs:8` `use codex_file_search::run_main;`
- `use` `codex-rs/file-search/src/main.rs:9` `use serde_json::json;`
- `fn` `codex-rs/file-search/src/main.rs:12` `async fn main() -> anyhow::Result<()> {`
- `struct` `codex-rs/file-search/src/main.rs:22` `struct StdioReporter {`
- `impl` `codex-rs/file-search/src/main.rs:27` `impl Reporter for StdioReporter {`
- `fn` `codex-rs/file-search/src/main.rs:28` `fn report_match(&self, file_match: &FileMatch) {`
- `fn` `codex-rs/file-search/src/main.rs:61` `fn warn_matches_truncated(&self, total_match_count: usize, shown_match_count: usize) {`
- `fn` `codex-rs/file-search/src/main.rs:72` `fn warn_no_search_pattern(&self, search_directory: &Path) {`

## Dependencies (auto sample)
### Imports / Includes
- `use std::io::IsTerminal;`
- `use std::path::Path;`
- `use clap::Parser;`
- `use codex_file_search::Cli;`
- `use codex_file_search::FileMatch;`
- `use codex_file_search::Reporter;`
- `use codex_file_search::run_main;`
- `use serde_json::json;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
