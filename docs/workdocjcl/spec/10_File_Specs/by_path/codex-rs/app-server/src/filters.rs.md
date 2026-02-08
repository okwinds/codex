# `codex-rs/app-server/src/filters.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `5661`
- sha256: `22f19d7b3a7b4fe60c5fccd32dbbac4d57f2710d3a27b063a4a29df0acfec65d`
- generated_utc: `2026-02-08T10:45:15Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server/src/filters.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `use` `codex-rs/app-server/src/filters.rs:1` `use codex_app_server_protocol::ThreadSourceKind;`
- `use` `codex-rs/app-server/src/filters.rs:2` `use codex_core::INTERACTIVE_SESSION_SOURCES;`
- `use` `codex-rs/app-server/src/filters.rs:3` `use codex_protocol::protocol::SessionSource as CoreSessionSource;`
- `use` `codex-rs/app-server/src/filters.rs:4` `use codex_protocol::protocol::SubAgentSource as CoreSubAgentSource;`
- `use` `codex-rs/app-server/src/filters.rs:86` `use super::*;`
- `use` `codex-rs/app-server/src/filters.rs:87` `use codex_protocol::ThreadId;`
- `use` `codex-rs/app-server/src/filters.rs:88` `use pretty_assertions::assert_eq;`
- `use` `codex-rs/app-server/src/filters.rs:89` `use uuid::Uuid;`
- `fn` `codex-rs/app-server/src/filters.rs:92` `fn compute_source_filters_defaults_to_interactive_sources() {`
- `fn` `codex-rs/app-server/src/filters.rs:100` `fn compute_source_filters_empty_means_interactive_sources() {`
- `fn` `codex-rs/app-server/src/filters.rs:108` `fn compute_source_filters_interactive_only_skips_post_filtering() {`
- `fn` `codex-rs/app-server/src/filters.rs:120` `fn compute_source_filters_subagent_variant_requires_post_filtering() {`
- `fn` `codex-rs/app-server/src/filters.rs:129` `fn source_kind_matches_distinguishes_subagent_variants() {`

## Dependencies (auto sample)
### Imports / Includes
- `use codex_app_server_protocol::ThreadSourceKind;`
- `use codex_core::INTERACTIVE_SESSION_SOURCES;`
- `use codex_protocol::protocol::SessionSource as CoreSessionSource;`
- `use codex_protocol::protocol::SubAgentSource as CoreSubAgentSource;`
- `use super::*;`
- `use codex_protocol::ThreadId;`
- `use pretty_assertions::assert_eq;`
- `use uuid::Uuid;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
