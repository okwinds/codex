# `codex-rs/tui/src/bottom_pane/paste_burst.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `24227`
- sha256: `fc6a11c4d8eb9d3cfe45a6a6fec68318ab21ec8299cb56dedf6d18d14fe341a0`
- generated_utc: `2026-02-03T16:08:30Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/tui/src/bottom_pane/paste_burst.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub fn recommended_flush_delay() -> Duration {`
- `pub fn on_plain_char(&mut self, ch: char, now: Instant) -> CharDecision {`
- `pub fn on_plain_char_no_hold(&mut self, now: Instant) -> Option<CharDecision> {`
- `pub fn flush_if_due(&mut self, now: Instant) -> FlushResult {`
- `pub fn append_newline_if_active(&mut self, now: Instant) -> bool {`
- `pub fn newline_should_insert_instead_of_submit(&self, now: Instant) -> bool {`
- `pub fn extend_window(&mut self, now: Instant) {`
- `pub fn begin_with_retro_grabbed(&mut self, grabbed: String, now: Instant) {`
- `pub fn append_char_to_buffer(&mut self, ch: char, now: Instant) {`
- `pub fn try_append_char_if_active(&mut self, ch: char, now: Instant) -> bool {`
- `pub fn decide_begin_buffer(`
- `pub fn flush_before_modified_input(&mut self) -> Option<String> {`
- `pub fn clear_window_after_non_char(&mut self) {`
- `pub fn is_active(&self) -> bool {`
- `pub fn clear_after_explicit_paste(&mut self) {`

## Definitions (auto, per-file)
- `use` `codex-rs/tui/src/bottom_pane/paste_burst.rs:148` `use std::time::Duration;`
- `use` `codex-rs/tui/src/bottom_pane/paste_burst.rs:149` `use std::time::Instant;`
- `const` `codex-rs/tui/src/bottom_pane/paste_burst.rs:153` `const PASTE_BURST_MIN_CHARS: u16 = 3;`
- `const` `codex-rs/tui/src/bottom_pane/paste_burst.rs:154` `const PASTE_BURST_CHAR_INTERVAL: Duration = Duration::from_millis(8);`
- `const` `codex-rs/tui/src/bottom_pane/paste_burst.rs:155` `const PASTE_ENTER_SUPPRESS_WINDOW: Duration = Duration::from_millis(120);`
- `const` `codex-rs/tui/src/bottom_pane/paste_burst.rs:159` `const PASTE_BURST_ACTIVE_IDLE_TIMEOUT: Duration = Duration::from_millis(8);`
- `const` `codex-rs/tui/src/bottom_pane/paste_burst.rs:161` `const PASTE_BURST_ACTIVE_IDLE_TIMEOUT: Duration = Duration::from_millis(60);`
- `impl` `codex-rs/tui/src/bottom_pane/paste_burst.rs:197` `impl PasteBurst {`
- `fn` `codex-rs/tui/src/bottom_pane/paste_burst.rs:204` `pub fn recommended_flush_delay() -> Duration {`
- `fn` `codex-rs/tui/src/bottom_pane/paste_burst.rs:214` `pub fn on_plain_char(&mut self, ch: char, now: Instant) -> CharDecision {`
- `fn` `codex-rs/tui/src/bottom_pane/paste_burst.rs:252` `pub fn on_plain_char_no_hold(&mut self, now: Instant) -> Option<CharDecision> {`
- `fn` `codex-rs/tui/src/bottom_pane/paste_burst.rs:269` `fn note_plain_char(&mut self, now: Instant) {`
- `fn` `codex-rs/tui/src/bottom_pane/paste_burst.rs:289` `pub fn flush_if_due(&mut self, now: Instant) -> FlushResult {`
- `fn` `codex-rs/tui/src/bottom_pane/paste_burst.rs:320` `pub fn append_newline_if_active(&mut self, now: Instant) -> bool {`
- `fn` `codex-rs/tui/src/bottom_pane/paste_burst.rs:331` `pub fn newline_should_insert_instead_of_submit(&self, now: Instant) -> bool {`
- `fn` `codex-rs/tui/src/bottom_pane/paste_burst.rs:337` `pub fn extend_window(&mut self, now: Instant) {`
- `fn` `codex-rs/tui/src/bottom_pane/paste_burst.rs:342` `pub fn begin_with_retro_grabbed(&mut self, grabbed: String, now: Instant) {`
- `fn` `codex-rs/tui/src/bottom_pane/paste_burst.rs:351` `pub fn append_char_to_buffer(&mut self, ch: char, now: Instant) {`
- `fn` `codex-rs/tui/src/bottom_pane/paste_burst.rs:359` `pub fn try_append_char_if_active(&mut self, ch: char, now: Instant) -> bool {`
- `fn` `codex-rs/tui/src/bottom_pane/paste_burst.rs:379` `pub fn decide_begin_buffer(`
- `fn` `codex-rs/tui/src/bottom_pane/paste_burst.rs:402` `pub fn flush_before_modified_input(&mut self) -> Option<String> {`
- `fn` `codex-rs/tui/src/bottom_pane/paste_burst.rs:418` `pub fn clear_window_after_non_char(&mut self) {`
- `fn` `codex-rs/tui/src/bottom_pane/paste_burst.rs:429` `pub fn is_active(&self) -> bool {`
- `fn` `codex-rs/tui/src/bottom_pane/paste_burst.rs:433` `fn is_active_internal(&self) -> bool {`
- `fn` `codex-rs/tui/src/bottom_pane/paste_burst.rs:437` `pub fn clear_after_explicit_paste(&mut self) {`
- `use` `codex-rs/tui/src/bottom_pane/paste_burst.rs:461` `use super::*;`
- `use` `codex-rs/tui/src/bottom_pane/paste_burst.rs:462` `use pretty_assertions::assert_eq;`
- `fn` `codex-rs/tui/src/bottom_pane/paste_burst.rs:467` `fn ascii_first_char_is_held_then_flushes_as_typed() {`
- `fn` `codex-rs/tui/src/bottom_pane/paste_burst.rs:483` `fn ascii_two_fast_chars_start_buffer_from_pending_and_flush_as_paste() {`
- `fn` `codex-rs/tui/src/bottom_pane/paste_burst.rs:508` `fn flush_before_modified_input_includes_pending_first_char() {`
- `fn` `codex-rs/tui/src/bottom_pane/paste_burst.rs:523` `fn decide_begin_buffer_only_triggers_for_pastey_prefixes() {`
- `fn` `codex-rs/tui/src/bottom_pane/paste_burst.rs:541` `fn newline_suppression_window_outlives_buffer_flush() {`

## Dependencies (auto sample)
### Imports / Includes
- `use std::time::Duration;`
- `use std::time::Instant;`
- `use super::*;`
- `use pretty_assertions::assert_eq;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- has retry/timeout/backoff logic
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- `workdocjcl/spec/06_UI/TUI.md`
