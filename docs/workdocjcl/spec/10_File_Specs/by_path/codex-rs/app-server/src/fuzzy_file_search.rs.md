# `codex-rs/app-server/src/fuzzy_file_search.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `2345`
- sha256: `2d2d17b491000f5047c742e6f1d3b6fc973ea5089029b8a915ff9a0bf35753c5`
- generated_utc: `2026-02-03T16:08:28Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server/src/fuzzy_file_search.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `use` `codex-rs/app-server/src/fuzzy_file_search.rs:1` `use std::num::NonZero;`
- `use` `codex-rs/app-server/src/fuzzy_file_search.rs:2` `use std::path::PathBuf;`
- `use` `codex-rs/app-server/src/fuzzy_file_search.rs:3` `use std::sync::Arc;`
- `use` `codex-rs/app-server/src/fuzzy_file_search.rs:4` `use std::sync::atomic::AtomicBool;`
- `use` `codex-rs/app-server/src/fuzzy_file_search.rs:6` `use codex_app_server_protocol::FuzzyFileSearchResult;`
- `use` `codex-rs/app-server/src/fuzzy_file_search.rs:7` `use codex_file_search as file_search;`
- `use` `codex-rs/app-server/src/fuzzy_file_search.rs:8` `use tracing::warn;`
- `const` `codex-rs/app-server/src/fuzzy_file_search.rs:10` `const MATCH_LIMIT: usize = 50;`
- `const` `codex-rs/app-server/src/fuzzy_file_search.rs:11` `const MAX_THREADS: usize = 12;`

## Dependencies (auto sample)
### Imports / Includes
- `use std::num::NonZero;`
- `use std::path::PathBuf;`
- `use std::sync::Arc;`
- `use std::sync::atomic::AtomicBool;`
- `use codex_app_server_protocol::FuzzyFileSearchResult;`
- `use codex_file_search as file_search;`
- `use tracing::warn;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
