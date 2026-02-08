# `codex-rs/debug-client/src/output.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `3383`
- sha256: `4ebbe3bd81081e7ae09073f82bc8aa2ecfc620e3c49854871d30fa2bd3468381`
- generated_utc: `2026-02-08T10:45:36Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/debug-client/src/output.rs` (read)
- env: `NO_COLOR`

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub enum LabelColor {`
- `pub struct Output {`
- `pub fn new() -> Self {`
- `pub fn server_line(&self, line: &str) -> io::Result<()> {`
- `pub fn client_line(&self, line: &str) -> io::Result<()> {`
- `pub fn prompt(&self, thread_id: &str) -> io::Result<()> {`
- `pub fn set_prompt(&self, thread_id: &str) {`
- `pub fn format_label(&self, label: &str, color: LabelColor) -> String {`

## Definitions (auto, per-file)
- `use` `codex-rs/debug-client/src/output.rs:1` `use std::io;`
- `use` `codex-rs/debug-client/src/output.rs:2` `use std::io::IsTerminal;`
- `use` `codex-rs/debug-client/src/output.rs:3` `use std::io::Write;`
- `use` `codex-rs/debug-client/src/output.rs:4` `use std::sync::Arc;`
- `use` `codex-rs/debug-client/src/output.rs:5` `use std::sync::Mutex;`
- `enum` `codex-rs/debug-client/src/output.rs:8` `pub enum LabelColor {`
- `struct` `codex-rs/debug-client/src/output.rs:16` `struct PromptState {`
- `struct` `codex-rs/debug-client/src/output.rs:22` `pub struct Output {`
- `impl` `codex-rs/debug-client/src/output.rs:28` `impl Output {`
- `fn` `codex-rs/debug-client/src/output.rs:29` `pub fn new() -> Self {`
- `fn` `codex-rs/debug-client/src/output.rs:39` `pub fn server_line(&self, line: &str) -> io::Result<()> {`
- `fn` `codex-rs/debug-client/src/output.rs:48` `pub fn client_line(&self, line: &str) -> io::Result<()> {`
- `fn` `codex-rs/debug-client/src/output.rs:56` `pub fn prompt(&self, thread_id: &str) -> io::Result<()> {`
- `fn` `codex-rs/debug-client/src/output.rs:62` `pub fn set_prompt(&self, thread_id: &str) {`
- `fn` `codex-rs/debug-client/src/output.rs:67` `pub fn format_label(&self, label: &str, color: LabelColor) -> String {`
- `fn` `codex-rs/debug-client/src/output.rs:81` `fn clear_prompt_line_locked(&self) -> io::Result<()> {`
- `fn` `codex-rs/debug-client/src/output.rs:92` `fn redraw_prompt_locked(&self) -> io::Result<()> {`
- `fn` `codex-rs/debug-client/src/output.rs:105` `fn set_prompt_locked(&self, thread_id: &str) {`
- `fn` `codex-rs/debug-client/src/output.rs:110` `fn write_prompt_locked(&self) -> io::Result<()> {`

## Dependencies (auto sample)
### Imports / Includes
- `use std::io;`
- `use std::io::IsTerminal;`
- `use std::io::Write;`
- `use std::sync::Arc;`
- `use std::sync::Mutex;`
### Referenced env vars
- `NO_COLOR`

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
