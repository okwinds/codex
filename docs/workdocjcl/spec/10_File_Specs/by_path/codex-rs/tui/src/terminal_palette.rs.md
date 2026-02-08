# `codex-rs/tui/src/terminal_palette.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `14940`
- sha256: `425ed39fbb9351f37b41c0e7b63d48223c8735e4ff781e0b0b319579837ee927`
- generated_utc: `2026-02-03T16:08:30Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/tui/src/terminal_palette.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub fn best_color(target: (u8, u8, u8)) -> Color {`
- `pub fn requery_default_colors() {`
- `pub struct DefaultColors {`
- `pub fn default_colors() -> Option<DefaultColors> {`
- `pub fn default_fg() -> Option<(u8, u8, u8)> {`
- `pub fn default_bg() -> Option<(u8, u8, u8)> {`
- `pub fn palette_version() -> u64 {`

## Definitions (auto, per-file)
- `use` `codex-rs/tui/src/terminal_palette.rs:1` `use crate::color::perceptual_distance;`
- `use` `codex-rs/tui/src/terminal_palette.rs:2` `use ratatui::style::Color;`
- `use` `codex-rs/tui/src/terminal_palette.rs:3` `use std::sync::atomic::AtomicU64;`
- `use` `codex-rs/tui/src/terminal_palette.rs:4` `use std::sync::atomic::Ordering;`
- `static` `codex-rs/tui/src/terminal_palette.rs:6` `static DEFAULT_PALETTE_VERSION: AtomicU64 = AtomicU64::new(0);`
- `fn` `codex-rs/tui/src/terminal_palette.rs:8` `fn bump_palette_version() {`
- `fn` `codex-rs/tui/src/terminal_palette.rs:13` `pub fn best_color(target: (u8, u8, u8)) -> Color {`
- `fn` `codex-rs/tui/src/terminal_palette.rs:36` `pub fn requery_default_colors() {`
- `struct` `codex-rs/tui/src/terminal_palette.rs:42` `pub struct DefaultColors {`
- `fn` `codex-rs/tui/src/terminal_palette.rs:47` `pub fn default_colors() -> Option<DefaultColors> {`
- `fn` `codex-rs/tui/src/terminal_palette.rs:51` `pub fn default_fg() -> Option<(u8, u8, u8)> {`
- `fn` `codex-rs/tui/src/terminal_palette.rs:55` `pub fn default_bg() -> Option<(u8, u8, u8)> {`
- `fn` `codex-rs/tui/src/terminal_palette.rs:63` `pub fn palette_version() -> u64 {`
- `use` `codex-rs/tui/src/terminal_palette.rs:69` `use super::DefaultColors;`
- `use` `codex-rs/tui/src/terminal_palette.rs:70` `use crossterm::style::Color as CrosstermColor;`
- `use` `codex-rs/tui/src/terminal_palette.rs:71` `use crossterm::style::query_background_color;`
- `use` `codex-rs/tui/src/terminal_palette.rs:72` `use crossterm::style::query_foreground_color;`
- `use` `codex-rs/tui/src/terminal_palette.rs:73` `use std::sync::Mutex;`
- `use` `codex-rs/tui/src/terminal_palette.rs:74` `use std::sync::OnceLock;`
- `struct` `codex-rs/tui/src/terminal_palette.rs:76` `struct Cache<T> {`
- `impl` `codex-rs/tui/src/terminal_palette.rs:81` `impl<T> Default for Cache<T> {`
- `fn` `codex-rs/tui/src/terminal_palette.rs:82` `fn default() -> Self {`
- `impl` `codex-rs/tui/src/terminal_palette.rs:90` `impl<T: Copy> Cache<T> {`
- `fn` `codex-rs/tui/src/terminal_palette.rs:91` `fn get_or_init_with(&mut self, mut init: impl FnMut() -> Option<T>) -> Option<T> {`
- `fn` `codex-rs/tui/src/terminal_palette.rs:99` `fn refresh_with(&mut self, mut init: impl FnMut() -> Option<T>) -> Option<T> {`
- `fn` `codex-rs/tui/src/terminal_palette.rs:106` `fn default_colors_cache() -> &'static Mutex<Cache<DefaultColors>> {`
- `static` `codex-rs/tui/src/terminal_palette.rs:107` `static CACHE: OnceLock<Mutex<Cache<DefaultColors>>> = OnceLock::new();`
- `fn` `codex-rs/tui/src/terminal_palette.rs:127` `fn query_default_colors() -> std::io::Result<Option<DefaultColors>> {`
- `fn` `codex-rs/tui/src/terminal_palette.rs:133` `fn color_to_tuple(color: CrosstermColor) -> Option<(u8, u8, u8)> {`
- `use` `codex-rs/tui/src/terminal_palette.rs:143` `use super::DefaultColors;`
- `fn` `codex-rs/tui/src/terminal_palette.rs:153` `fn xterm_fixed_colors() -> impl Iterator<Item = (usize, (u8, u8, u8))> {`
- `const` `codex-rs/tui/src/terminal_palette.rs:158` `pub const XTERM_COLORS: [(u8, u8, u8); 256] = [`

## Dependencies (auto sample)
### Imports / Includes
- `use crate::color::perceptual_distance;`
- `use ratatui::style::Color;`
- `use std::sync::atomic::AtomicU64;`
- `use std::sync::atomic::Ordering;`
- `use super::DefaultColors;`
- `use crossterm::style::Color as CrosstermColor;`
- `use crossterm::style::query_background_color;`
- `use crossterm::style::query_foreground_color;`
- `use std::sync::Mutex;`
- `use std::sync::OnceLock;`
- `use super::DefaultColors;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)

## Spec Links
- `workdocjcl/spec/06_UI/TUI.md`
