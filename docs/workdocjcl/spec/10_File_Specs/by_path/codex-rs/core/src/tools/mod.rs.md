# `codex-rs/core/src/tools/mod.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `3416`
- sha256: `1790953c3722b87e666fef00135d66448f7efe84935e068152817ecb256087ce`
- generated_utc: `2026-02-08T10:45:33Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/tools/mod.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub fn format_exec_output_for_model_structured(`
- `pub fn format_exec_output_for_model_freeform(`
- `pub fn format_exec_output_str(`

## Definitions (auto, per-file)
- `mod` `codex-rs/core/src/tools/mod.rs:1` `pub mod context;`
- `mod` `codex-rs/core/src/tools/mod.rs:2` `pub mod events;`
- `mod` `codex-rs/core/src/tools/mod.rs:4` `pub mod orchestrator;`
- `mod` `codex-rs/core/src/tools/mod.rs:5` `pub mod parallel;`
- `mod` `codex-rs/core/src/tools/mod.rs:6` `pub mod registry;`
- `mod` `codex-rs/core/src/tools/mod.rs:7` `pub mod router;`
- `mod` `codex-rs/core/src/tools/mod.rs:8` `pub mod runtimes;`
- `mod` `codex-rs/core/src/tools/mod.rs:9` `pub mod sandboxing;`
- `mod` `codex-rs/core/src/tools/mod.rs:10` `pub mod spec;`
- `use` `codex-rs/core/src/tools/mod.rs:12` `use crate::exec::ExecToolCallOutput;`
- `use` `codex-rs/core/src/tools/mod.rs:13` `use crate::truncate::TruncationPolicy;`
- `use` `codex-rs/core/src/tools/mod.rs:14` `use crate::truncate::formatted_truncate_text;`
- `use` `codex-rs/core/src/tools/mod.rs:15` `use crate::truncate::truncate_text;`
- `use` `codex-rs/core/src/tools/mod.rs:17` `use serde::Serialize;`
- `fn` `codex-rs/core/src/tools/mod.rs:27` `pub fn format_exec_output_for_model_structured(`
- `struct` `codex-rs/core/src/tools/mod.rs:38` `struct ExecMetadata {`
- `struct` `codex-rs/core/src/tools/mod.rs:44` `struct ExecOutput<'a> {`
- `fn` `codex-rs/core/src/tools/mod.rs:66` `pub fn format_exec_output_for_model_freeform(`
- `fn` `codex-rs/core/src/tools/mod.rs:93` `pub fn format_exec_output_str(`
- `fn` `codex-rs/core/src/tools/mod.rs:104` `fn build_content_with_timeout(exec_output: &ExecToolCallOutput) -> String {`

## Dependencies (auto sample)
### Imports / Includes
- `use crate::exec::ExecToolCallOutput;`
- `use crate::truncate::TruncationPolicy;`
- `use crate::truncate::formatted_truncate_text;`
- `use crate::truncate::truncate_text;`
- `use serde::Serialize;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- has retry/timeout/backoff logic
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- `docs/workdocjcl/spec/00_Overview/ARCHITECTURE.md`
