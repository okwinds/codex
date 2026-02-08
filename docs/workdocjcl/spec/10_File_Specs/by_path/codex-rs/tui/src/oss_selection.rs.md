# `codex-rs/tui/src/oss_selection.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `12333`
- sha256: `9d113f1b8ce793cb6ef9899a7b361828869820659bca7596e00b99065669f906`
- generated_utc: `2026-02-08T10:45:40Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/tui/src/oss_selection.rs` (read)

### Outputs / Side Effects
- performs network I/O

## Public Surface (auto)
- `pub struct OssSelectionWidget<'a> {`
- `pub fn handle_key_event(&mut self, key: KeyEvent) -> Option<String> {`
- `pub fn is_complete(&self) -> bool {`
- `pub fn desired_height(&self, width: u16) -> u16 {`

## Definitions (auto, per-file)
- `use` `codex-rs/tui/src/oss_selection.rs:1` `use std::io;`
- `use` `codex-rs/tui/src/oss_selection.rs:2` `use std::sync::LazyLock;`
- `use` `codex-rs/tui/src/oss_selection.rs:4` `use codex_core::DEFAULT_LMSTUDIO_PORT;`
- `use` `codex-rs/tui/src/oss_selection.rs:5` `use codex_core::DEFAULT_OLLAMA_PORT;`
- `use` `codex-rs/tui/src/oss_selection.rs:6` `use codex_core::LMSTUDIO_OSS_PROVIDER_ID;`
- `use` `codex-rs/tui/src/oss_selection.rs:7` `use codex_core::OLLAMA_OSS_PROVIDER_ID;`
- `use` `codex-rs/tui/src/oss_selection.rs:8` `use codex_core::config::set_default_oss_provider;`
- `use` `codex-rs/tui/src/oss_selection.rs:9` `use crossterm::event::Event;`
- `use` `codex-rs/tui/src/oss_selection.rs:10` `use crossterm::event::KeyCode;`
- `use` `codex-rs/tui/src/oss_selection.rs:11` `use crossterm::event::KeyEvent;`
- `use` `codex-rs/tui/src/oss_selection.rs:12` `use crossterm::event::KeyEventKind;`
- `use` `codex-rs/tui/src/oss_selection.rs:13` `use crossterm::event::{self};`
- `use` `codex-rs/tui/src/oss_selection.rs:14` `use crossterm::execute;`
- `use` `codex-rs/tui/src/oss_selection.rs:15` `use crossterm::terminal::EnterAlternateScreen;`
- `use` `codex-rs/tui/src/oss_selection.rs:16` `use crossterm::terminal::LeaveAlternateScreen;`
- `use` `codex-rs/tui/src/oss_selection.rs:17` `use crossterm::terminal::disable_raw_mode;`
- `use` `codex-rs/tui/src/oss_selection.rs:18` `use crossterm::terminal::enable_raw_mode;`
- `use` `codex-rs/tui/src/oss_selection.rs:19` `use ratatui::Terminal;`
- `use` `codex-rs/tui/src/oss_selection.rs:20` `use ratatui::backend::CrosstermBackend;`
- `use` `codex-rs/tui/src/oss_selection.rs:21` `use ratatui::buffer::Buffer;`
- `use` `codex-rs/tui/src/oss_selection.rs:22` `use ratatui::layout::Alignment;`
- `use` `codex-rs/tui/src/oss_selection.rs:23` `use ratatui::layout::Constraint;`
- `use` `codex-rs/tui/src/oss_selection.rs:24` `use ratatui::layout::Direction;`
- `use` `codex-rs/tui/src/oss_selection.rs:25` `use ratatui::layout::Layout;`
- `use` `codex-rs/tui/src/oss_selection.rs:26` `use ratatui::layout::Margin;`
- `use` `codex-rs/tui/src/oss_selection.rs:27` `use ratatui::layout::Rect;`
- `use` `codex-rs/tui/src/oss_selection.rs:28` `use ratatui::prelude::*;`
- `use` `codex-rs/tui/src/oss_selection.rs:29` `use ratatui::style::Color;`
- `use` `codex-rs/tui/src/oss_selection.rs:30` `use ratatui::style::Modifier;`
- `use` `codex-rs/tui/src/oss_selection.rs:31` `use ratatui::style::Style;`
- `use` `codex-rs/tui/src/oss_selection.rs:32` `use ratatui::text::Line;`
- `use` `codex-rs/tui/src/oss_selection.rs:33` `use ratatui::text::Span;`
- `use` `codex-rs/tui/src/oss_selection.rs:34` `use ratatui::widgets::Paragraph;`
- `use` `codex-rs/tui/src/oss_selection.rs:35` `use ratatui::widgets::Widget;`
- `use` `codex-rs/tui/src/oss_selection.rs:36` `use ratatui::widgets::WidgetRef;`
- `use` `codex-rs/tui/src/oss_selection.rs:37` `use ratatui::widgets::Wrap;`
- `use` `codex-rs/tui/src/oss_selection.rs:38` `use std::time::Duration;`
- `struct` `codex-rs/tui/src/oss_selection.rs:41` `struct ProviderOption {`
- `enum` `codex-rs/tui/src/oss_selection.rs:47` `enum ProviderStatus {`
- `struct` `codex-rs/tui/src/oss_selection.rs:56` `struct SelectOption {`
- `static` `codex-rs/tui/src/oss_selection.rs:63` `static OSS_SELECT_OPTIONS: LazyLock<Vec<SelectOption>> = LazyLock::new(|| {`
- `struct` `codex-rs/tui/src/oss_selection.rs:80` `pub struct OssSelectionWidget<'a> {`
- `impl` `codex-rs/tui/src/oss_selection.rs:94` `impl OssSelectionWidget<'_> {`
- `fn` `codex-rs/tui/src/oss_selection.rs:95` `fn new(lmstudio_status: ProviderStatus, ollama_status: ProviderStatus) -> io::Result<Self> {`
- `fn` `codex-rs/tui/src/oss_selection.rs:149` `fn get_confirmation_prompt_height(&self, width: u16) -> u16 {`
- `fn` `codex-rs/tui/src/oss_selection.rs:159` `pub fn handle_key_event(&mut self, key: KeyEvent) -> Option<String> {`
- `fn` `codex-rs/tui/src/oss_selection.rs:173` `fn normalize_keycode(code: KeyCode) -> KeyCode {`
- `fn` `codex-rs/tui/src/oss_selection.rs:180` `fn handle_select_key(&mut self, key_event: KeyEvent) {`
- `fn` `codex-rs/tui/src/oss_selection.rs:216` `fn send_decision(&mut self, selection: String) {`
- `fn` `codex-rs/tui/src/oss_selection.rs:223` `pub fn is_complete(&self) -> bool {`
- `fn` `codex-rs/tui/src/oss_selection.rs:227` `pub fn desired_height(&self, width: u16) -> u16 {`
- `impl` `codex-rs/tui/src/oss_selection.rs:232` `impl WidgetRef for &OssSelectionWidget<'_> {`
- `fn` `codex-rs/tui/src/oss_selection.rs:233` `fn render_ref(&self, area: Rect, buf: &mut Buffer) {`
- `fn` `codex-rs/tui/src/oss_selection.rs:282` `fn get_status_symbol_and_color(status: &ProviderStatus) -> (&'static str, Color) {`
- `fn` `codex-rs/tui/src/oss_selection.rs:290` `pub async fn select_oss_provider(codex_home: &std::path::Path) -> io::Result<String> {`
- `fn` `codex-rs/tui/src/oss_selection.rs:345` `async fn check_lmstudio_status() -> ProviderStatus {`
- `fn` `codex-rs/tui/src/oss_selection.rs:353` `async fn check_ollama_status() -> ProviderStatus {`
- `fn` `codex-rs/tui/src/oss_selection.rs:361` `async fn check_port_status(port: u16) -> io::Result<bool> {`

## Dependencies (auto sample)
### Imports / Includes
- `use std::io;`
- `use std::sync::LazyLock;`
- `use codex_core::DEFAULT_LMSTUDIO_PORT;`
- `use codex_core::DEFAULT_OLLAMA_PORT;`
- `use codex_core::LMSTUDIO_OSS_PROVIDER_ID;`
- `use codex_core::OLLAMA_OSS_PROVIDER_ID;`
- `use codex_core::config::set_default_oss_provider;`
- `use crossterm::event::Event;`
- `use crossterm::event::KeyCode;`
- `use crossterm::event::KeyEvent;`
- `use crossterm::event::KeyEventKind;`
- `use crossterm::event::{self};`
- `use crossterm::execute;`
- `use crossterm::terminal::EnterAlternateScreen;`
- `use crossterm::terminal::LeaveAlternateScreen;`
- `use crossterm::terminal::disable_raw_mode;`
- `use crossterm::terminal::enable_raw_mode;`
- `use ratatui::Terminal;`
- `use ratatui::backend::CrosstermBackend;`
- `use ratatui::buffer::Buffer;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- has retry/timeout/backoff logic
- returns structured errors (Result/ErrorKind)

## Spec Links
- `docs/workdocjcl/spec/06_UI/TUI.md`
