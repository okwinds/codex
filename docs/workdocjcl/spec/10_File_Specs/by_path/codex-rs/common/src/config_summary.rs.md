# `codex-rs/common/src/config_summary.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `1116`
- sha256: `c65d7bc039e45024053c9c085c8c2dfd2378aa624c28f5d14ba7fb952ffac603`
- generated_utc: `2026-02-03T16:08:29Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/common/src/config_summary.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub fn create_config_summary_entries(config: &Config, model: &str) -> Vec<(&'static str, String)> {`

## Definitions (auto, per-file)
- `use` `codex-rs/common/src/config_summary.rs:1` `use codex_core::WireApi;`
- `use` `codex-rs/common/src/config_summary.rs:2` `use codex_core::config::Config;`
- `use` `codex-rs/common/src/config_summary.rs:4` `use crate::sandbox_summary::summarize_sandbox_policy;`
- `fn` `codex-rs/common/src/config_summary.rs:7` `pub fn create_config_summary_entries(config: &Config, model: &str) -> Vec<(&'static str, String)> {`

## Dependencies (auto sample)
### Imports / Includes
- `use codex_core::WireApi;`
- `use codex_core::config::Config;`
- `use crate::sandbox_summary::summarize_sandbox_policy;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
