# `codex-rs/cloud-tasks/src/scrollable_diff.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `5993`
- sha256: `7da1a28cc1805da8861c999408ca2c11d8b858ae5124a0503ab445b9d966ab63`
- generated_utc: `2026-02-03T16:08:29Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/cloud-tasks/src/scrollable_diff.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub struct ScrollViewState {`
- `pub fn clamp(&mut self) {`
- `pub struct ScrollableDiff {`
- `pub fn new() -> Self {`
- `pub fn set_content(&mut self, lines: Vec<String>) {`
- `pub fn set_width(&mut self, width: u16) {`
- `pub fn set_viewport(&mut self, height: u16) {`
- `pub fn wrapped_lines(&self) -> &[String] {`
- `pub fn wrapped_src_indices(&self) -> &[usize] {`
- `pub fn raw_line_at(&self, idx: usize) -> &str {`
- `pub fn scroll_by(&mut self, delta: i16) {`
- `pub fn page_by(&mut self, delta: i16) {`
- `pub fn to_top(&mut self) {`
- `pub fn to_bottom(&mut self) {`
- `pub fn percent_scrolled(&self) -> Option<u8> {`

## Definitions (auto, per-file)
- `use` `codex-rs/cloud-tasks/src/scrollable_diff.rs:1` `use unicode_width::UnicodeWidthChar;`
- `use` `codex-rs/cloud-tasks/src/scrollable_diff.rs:2` `use unicode_width::UnicodeWidthStr;`
- `struct` `codex-rs/cloud-tasks/src/scrollable_diff.rs:6` `pub struct ScrollViewState {`
- `impl` `codex-rs/cloud-tasks/src/scrollable_diff.rs:12` `impl ScrollViewState {`
- `fn` `codex-rs/cloud-tasks/src/scrollable_diff.rs:13` `pub fn clamp(&mut self) {`
- `struct` `codex-rs/cloud-tasks/src/scrollable_diff.rs:26` `pub struct ScrollableDiff {`
- `impl` `codex-rs/cloud-tasks/src/scrollable_diff.rs:34` `impl ScrollableDiff {`
- `fn` `codex-rs/cloud-tasks/src/scrollable_diff.rs:35` `pub fn new() -> Self {`
- `fn` `codex-rs/cloud-tasks/src/scrollable_diff.rs:40` `pub fn set_content(&mut self, lines: Vec<String>) {`
- `fn` `codex-rs/cloud-tasks/src/scrollable_diff.rs:50` `pub fn set_width(&mut self, width: u16) {`
- `fn` `codex-rs/cloud-tasks/src/scrollable_diff.rs:60` `pub fn set_viewport(&mut self, height: u16) {`
- `fn` `codex-rs/cloud-tasks/src/scrollable_diff.rs:66` `pub fn wrapped_lines(&self) -> &[String] {`
- `fn` `codex-rs/cloud-tasks/src/scrollable_diff.rs:70` `pub fn wrapped_src_indices(&self) -> &[usize] {`
- `fn` `codex-rs/cloud-tasks/src/scrollable_diff.rs:74` `pub fn raw_line_at(&self, idx: usize) -> &str {`
- `fn` `codex-rs/cloud-tasks/src/scrollable_diff.rs:79` `pub fn scroll_by(&mut self, delta: i16) {`
- `fn` `codex-rs/cloud-tasks/src/scrollable_diff.rs:85` `pub fn page_by(&mut self, delta: i16) {`
- `fn` `codex-rs/cloud-tasks/src/scrollable_diff.rs:89` `pub fn to_top(&mut self) {`
- `fn` `codex-rs/cloud-tasks/src/scrollable_diff.rs:93` `pub fn to_bottom(&mut self) {`
- `fn` `codex-rs/cloud-tasks/src/scrollable_diff.rs:98` `pub fn percent_scrolled(&self) -> Option<u8> {`
- `fn` `codex-rs/cloud-tasks/src/scrollable_diff.rs:110` `fn max_scroll(&self) -> u16 {`
- `fn` `codex-rs/cloud-tasks/src/scrollable_diff.rs:114` `fn rewrap(&mut self, width: u16) {`

## Dependencies (auto sample)
### Imports / Includes
- `use unicode_width::UnicodeWidthChar;`
- `use unicode_width::UnicodeWidthStr;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- has retry/timeout/backoff logic

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
