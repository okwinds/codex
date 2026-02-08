# `codex-rs/common/src/format_env_display.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `1686`
- sha256: `c134cb05ef1ce3995ea7f8bc194844cd6a6a32aa658188a0452dfbda703fee8e`
- generated_utc: `2026-02-03T16:08:29Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/common/src/format_env_display.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub fn format_env_display(env: Option<&HashMap<String, String>>, env_vars: &[String]) -> String {`

## Definitions (auto, per-file)
- `use` `codex-rs/common/src/format_env_display.rs:1` `use std::collections::HashMap;`
- `fn` `codex-rs/common/src/format_env_display.rs:3` `pub fn format_env_display(env: Option<&HashMap<String, String>>, env_vars: &[String]) -> String {`
- `use` `codex-rs/common/src/format_env_display.rs:25` `use super::*;`
- `fn` `codex-rs/common/src/format_env_display.rs:28` `fn returns_dash_when_empty() {`
- `fn` `codex-rs/common/src/format_env_display.rs:36` `fn formats_sorted_env_pairs() {`
- `fn` `codex-rs/common/src/format_env_display.rs:45` `fn formats_env_vars_with_dollar_prefix() {`
- `fn` `codex-rs/common/src/format_env_display.rs:52` `fn combines_env_pairs_and_vars() {`

## Dependencies (auto sample)
### Imports / Includes
- `use std::collections::HashMap;`
- `use super::*;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
