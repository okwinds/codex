# `codex-rs/ollama/src/pull.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `5339`
- sha256: `d9b3e3aa521a11a511782b81c85ccf9685687990239dfe3bb7866530d576f462`
- generated_utc: `2026-02-03T16:08:30Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/ollama/src/pull.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub enum PullEvent {`
- `pub trait PullProgressReporter {`
- `pub struct CliProgressReporter {`
- `pub fn new() -> Self {`
- `pub struct TuiProgressReporter(CliProgressReporter);`

## Definitions (auto, per-file)
- `use` `codex-rs/ollama/src/pull.rs:1` `use std::collections::HashMap;`
- `use` `codex-rs/ollama/src/pull.rs:2` `use std::io;`
- `use` `codex-rs/ollama/src/pull.rs:3` `use std::io::Write;`
- `enum` `codex-rs/ollama/src/pull.rs:7` `pub enum PullEvent {`
- `trait` `codex-rs/ollama/src/pull.rs:25` `pub trait PullProgressReporter {`
- `fn` `codex-rs/ollama/src/pull.rs:26` `fn on_event(&mut self, event: &PullEvent) -> io::Result<()>;`
- `struct` `codex-rs/ollama/src/pull.rs:30` `pub struct CliProgressReporter {`
- `impl` `codex-rs/ollama/src/pull.rs:38` `impl Default for CliProgressReporter {`
- `fn` `codex-rs/ollama/src/pull.rs:39` `fn default() -> Self {`
- `impl` `codex-rs/ollama/src/pull.rs:44` `impl CliProgressReporter {`
- `fn` `codex-rs/ollama/src/pull.rs:45` `pub fn new() -> Self {`
- `impl` `codex-rs/ollama/src/pull.rs:56` `impl PullProgressReporter for CliProgressReporter {`
- `fn` `codex-rs/ollama/src/pull.rs:57` `fn on_event(&mut self, event: &PullEvent) -> io::Result<()> {`
- `struct` `codex-rs/ollama/src/pull.rs:141` `pub struct TuiProgressReporter(CliProgressReporter);`
- `impl` `codex-rs/ollama/src/pull.rs:143` `impl PullProgressReporter for TuiProgressReporter {`
- `fn` `codex-rs/ollama/src/pull.rs:144` `fn on_event(&mut self, event: &PullEvent) -> io::Result<()> {`

## Dependencies (auto sample)
### Imports / Includes
- `use std::collections::HashMap;`
- `use std::io;`
- `use std::io::Write;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
