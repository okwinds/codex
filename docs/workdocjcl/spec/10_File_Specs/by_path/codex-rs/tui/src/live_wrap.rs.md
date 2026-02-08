# `codex-rs/tui/src/live_wrap.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `9637`
- sha256: `dc17083e7eeefd1d8a885a3823fa3246638d065237da6ca258e49185ea5f536f`
- generated_utc: `2026-02-08T10:45:40Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/tui/src/live_wrap.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub struct Row {`
- `pub fn width(&self) -> usize {`
- `pub struct RowBuilder {`
- `pub fn new(target_width: usize) -> Self {`
- `pub fn width(&self) -> usize {`
- `pub fn set_width(&mut self, width: usize) {`
- `pub fn push_fragment(&mut self, fragment: &str) {`
- `pub fn end_line(&mut self) {`
- `pub fn drain_rows(&mut self) -> Vec<Row> {`
- `pub fn rows(&self) -> &[Row] {`
- `pub fn display_rows(&self) -> Vec<Row> {`
- `pub fn drain_commit_ready(&mut self, max_keep: usize) -> Vec<Row> {`
- `pub fn take_prefix_by_width(text: &str, max_cols: usize) -> (String, &str, usize) {`

## Definitions (auto, per-file)
- `use` `codex-rs/tui/src/live_wrap.rs:1` `use unicode_width::UnicodeWidthChar;`
- `use` `codex-rs/tui/src/live_wrap.rs:2` `use unicode_width::UnicodeWidthStr;`
- `struct` `codex-rs/tui/src/live_wrap.rs:6` `pub struct Row {`
- `impl` `codex-rs/tui/src/live_wrap.rs:12` `impl Row {`
- `fn` `codex-rs/tui/src/live_wrap.rs:13` `pub fn width(&self) -> usize {`
- `struct` `codex-rs/tui/src/live_wrap.rs:21` `pub struct RowBuilder {`
- `impl` `codex-rs/tui/src/live_wrap.rs:29` `impl RowBuilder {`
- `fn` `codex-rs/tui/src/live_wrap.rs:30` `pub fn new(target_width: usize) -> Self {`
- `fn` `codex-rs/tui/src/live_wrap.rs:38` `pub fn width(&self) -> usize {`
- `fn` `codex-rs/tui/src/live_wrap.rs:42` `pub fn set_width(&mut self, width: usize) {`
- `fn` `codex-rs/tui/src/live_wrap.rs:58` `pub fn push_fragment(&mut self, fragment: &str) {`
- `fn` `codex-rs/tui/src/live_wrap.rs:80` `pub fn end_line(&mut self) {`
- `fn` `codex-rs/tui/src/live_wrap.rs:85` `pub fn drain_rows(&mut self) -> Vec<Row> {`
- `fn` `codex-rs/tui/src/live_wrap.rs:90` `pub fn rows(&self) -> &[Row] {`
- `fn` `codex-rs/tui/src/live_wrap.rs:95` `pub fn display_rows(&self) -> Vec<Row> {`
- `fn` `codex-rs/tui/src/live_wrap.rs:108` `pub fn drain_commit_ready(&mut self, max_keep: usize) -> Vec<Row> {`
- `fn` `codex-rs/tui/src/live_wrap.rs:122` `fn flush_current_line(&mut self, explicit_break: bool) {`
- `fn` `codex-rs/tui/src/live_wrap.rs:148` `fn wrap_current_line(&mut self) {`
- `fn` `codex-rs/tui/src/live_wrap.rs:187` `pub fn take_prefix_by_width(text: &str, max_cols: usize) -> (String, &str, usize) {`
- `use` `codex-rs/tui/src/live_wrap.rs:211` `use super::*;`
- `use` `codex-rs/tui/src/live_wrap.rs:212` `use pretty_assertions::assert_eq;`
- `fn` `codex-rs/tui/src/live_wrap.rs:215` `fn rows_do_not_exceed_width_ascii() {`
- `fn` `codex-rs/tui/src/live_wrap.rs:235` `fn rows_do_not_exceed_width_emoji_cjk() {`
- `fn` `codex-rs/tui/src/live_wrap.rs:253` `fn fragmentation_invariance_long_token() {`
- `fn` `codex-rs/tui/src/live_wrap.rs:270` `fn newline_splits_rows() {`
- `fn` `codex-rs/tui/src/live_wrap.rs:281` `fn rewrap_on_width_change() {`

## Dependencies (auto sample)
### Imports / Includes
- `use unicode_width::UnicodeWidthChar;`
- `use unicode_width::UnicodeWidthStr;`
- `use super::*;`
- `use pretty_assertions::assert_eq;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- `docs/workdocjcl/spec/06_UI/TUI.md`
