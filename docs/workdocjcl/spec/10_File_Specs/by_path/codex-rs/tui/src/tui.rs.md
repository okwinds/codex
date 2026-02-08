# `codex-rs/tui/src/tui.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `19004`
- sha256: `fbb5c0d7d5712883fa15c339fceaec9db93cc93dc2e4d82be29b01eccc02e029`
- generated_utc: `2026-02-03T16:08:30Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/tui/src/tui.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub fn set_modes() -> Result<()> {`
- `pub fn restore() -> Result<()> {`
- `pub fn restore_keep_raw() -> Result<()> {`
- `pub enum RestoreMode {`
- `pub fn init() -> Result<Terminal> {`
- `pub enum TuiEvent {`
- `pub struct Tui {`
- `pub fn new(terminal: Terminal) -> Self {`
- `pub fn set_alt_screen_enabled(&mut self, enabled: bool) {`
- `pub fn set_notification_method(&mut self, method: NotificationMethod) {`
- `pub fn frame_requester(&self) -> FrameRequester {`
- `pub fn enhanced_keys_supported(&self) -> bool {`
- `pub fn is_alt_screen_active(&self) -> bool {`
- `pub fn pause_events(&mut self) {`
- `pub fn resume_events(&mut self) {`
- `pub fn notify(&mut self, message: impl AsRef<str>) -> bool {`
- `pub fn event_stream(&self) -> Pin<Box<dyn Stream<Item = TuiEvent> + Send + 'static>> {`
- `pub fn enter_alt_screen(&mut self) -> Result<()> {`
- `pub fn leave_alt_screen(&mut self) -> Result<()> {`
- `pub fn insert_history_lines(&mut self, lines: Vec<Line<'static>>) {`
- `pub fn draw(`

## Definitions (auto, per-file)
- `use` `codex-rs/tui/src/tui.rs:1` `use std::fmt;`
- `use` `codex-rs/tui/src/tui.rs:2` `use std::future::Future;`
- `use` `codex-rs/tui/src/tui.rs:3` `use std::io::IsTerminal;`
- `use` `codex-rs/tui/src/tui.rs:4` `use std::io::Result;`
- `use` `codex-rs/tui/src/tui.rs:5` `use std::io::Stdout;`
- `use` `codex-rs/tui/src/tui.rs:6` `use std::io::stdin;`
- `use` `codex-rs/tui/src/tui.rs:7` `use std::io::stdout;`
- `use` `codex-rs/tui/src/tui.rs:8` `use std::panic;`
- `use` `codex-rs/tui/src/tui.rs:9` `use std::pin::Pin;`
- `use` `codex-rs/tui/src/tui.rs:10` `use std::sync::Arc;`
- `use` `codex-rs/tui/src/tui.rs:11` `use std::sync::atomic::AtomicBool;`
- `use` `codex-rs/tui/src/tui.rs:12` `use std::sync::atomic::Ordering;`
- `use` `codex-rs/tui/src/tui.rs:14` `use crossterm::Command;`
- `use` `codex-rs/tui/src/tui.rs:15` `use crossterm::SynchronizedUpdate;`
- `use` `codex-rs/tui/src/tui.rs:16` `use crossterm::event::DisableBracketedPaste;`
- `use` `codex-rs/tui/src/tui.rs:17` `use crossterm::event::DisableFocusChange;`
- `use` `codex-rs/tui/src/tui.rs:18` `use crossterm::event::EnableBracketedPaste;`
- `use` `codex-rs/tui/src/tui.rs:19` `use crossterm::event::EnableFocusChange;`
- `use` `codex-rs/tui/src/tui.rs:20` `use crossterm::event::KeyEvent;`
- `use` `codex-rs/tui/src/tui.rs:21` `use crossterm::event::KeyboardEnhancementFlags;`
- `use` `codex-rs/tui/src/tui.rs:22` `use crossterm::event::PopKeyboardEnhancementFlags;`
- `use` `codex-rs/tui/src/tui.rs:23` `use crossterm::event::PushKeyboardEnhancementFlags;`
- `use` `codex-rs/tui/src/tui.rs:24` `use crossterm::terminal::EnterAlternateScreen;`
- `use` `codex-rs/tui/src/tui.rs:25` `use crossterm::terminal::LeaveAlternateScreen;`
- `use` `codex-rs/tui/src/tui.rs:26` `use crossterm::terminal::supports_keyboard_enhancement;`
- `use` `codex-rs/tui/src/tui.rs:27` `use ratatui::backend::Backend;`
- `use` `codex-rs/tui/src/tui.rs:28` `use ratatui::backend::CrosstermBackend;`
- `use` `codex-rs/tui/src/tui.rs:29` `use ratatui::crossterm::execute;`
- `use` `codex-rs/tui/src/tui.rs:30` `use ratatui::crossterm::terminal::disable_raw_mode;`
- `use` `codex-rs/tui/src/tui.rs:31` `use ratatui::crossterm::terminal::enable_raw_mode;`
- `use` `codex-rs/tui/src/tui.rs:32` `use ratatui::layout::Offset;`
- `use` `codex-rs/tui/src/tui.rs:33` `use ratatui::layout::Rect;`
- `use` `codex-rs/tui/src/tui.rs:34` `use ratatui::text::Line;`
- `use` `codex-rs/tui/src/tui.rs:35` `use tokio::sync::broadcast;`
- `use` `codex-rs/tui/src/tui.rs:36` `use tokio_stream::Stream;`
- `use` `codex-rs/tui/src/tui.rs:39` `use crate::custom_terminal;`
- `use` `codex-rs/tui/src/tui.rs:40` `use crate::custom_terminal::Terminal as CustomTerminal;`
- `use` `codex-rs/tui/src/tui.rs:41` `use crate::notifications::DesktopNotificationBackend;`
- `use` `codex-rs/tui/src/tui.rs:42` `use crate::notifications::detect_backend;`
- `use` `codex-rs/tui/src/tui.rs:43` `use crate::tui::event_stream::EventBroker;`
- `use` `codex-rs/tui/src/tui.rs:44` `use crate::tui::event_stream::TuiEventStream;`
- `use` `codex-rs/tui/src/tui.rs:46` `use crate::tui::job_control::SuspendContext;`
- `use` `codex-rs/tui/src/tui.rs:47` `use codex_core::config::types::NotificationMethod;`
- `mod` `codex-rs/tui/src/tui.rs:49` `mod event_stream;`
- `mod` `codex-rs/tui/src/tui.rs:50` `mod frame_rate_limiter;`
- `mod` `codex-rs/tui/src/tui.rs:51` `mod frame_requester;`
- `mod` `codex-rs/tui/src/tui.rs:53` `mod job_control;`
- `type` `codex-rs/tui/src/tui.rs:56` `pub type Terminal = CustomTerminal<CrosstermBackend<Stdout>>;`
- `fn` `codex-rs/tui/src/tui.rs:58` `pub fn set_modes() -> Result<()> {`
- `struct` `codex-rs/tui/src/tui.rs:82` `struct EnableAlternateScroll;`
- `impl` `codex-rs/tui/src/tui.rs:84` `impl Command for EnableAlternateScroll {`
- `fn` `codex-rs/tui/src/tui.rs:85` `fn write_ansi(&self, f: &mut impl fmt::Write) -> fmt::Result {`
- `fn` `codex-rs/tui/src/tui.rs:90` `fn execute_winapi(&self) -> Result<()> {`
- `fn` `codex-rs/tui/src/tui.rs:97` `fn is_ansi_code_supported(&self) -> bool {`
- `struct` `codex-rs/tui/src/tui.rs:103` `struct DisableAlternateScroll;`
- `impl` `codex-rs/tui/src/tui.rs:105` `impl Command for DisableAlternateScroll {`
- `fn` `codex-rs/tui/src/tui.rs:106` `fn write_ansi(&self, f: &mut impl fmt::Write) -> fmt::Result {`
- `fn` `codex-rs/tui/src/tui.rs:111` `fn execute_winapi(&self) -> Result<()> {`
- `fn` `codex-rs/tui/src/tui.rs:118` `fn is_ansi_code_supported(&self) -> bool {`
- `fn` `codex-rs/tui/src/tui.rs:123` `fn restore_common(should_disable_raw_mode: bool) -> Result<()> {`
- `fn` `codex-rs/tui/src/tui.rs:137` `pub fn restore() -> Result<()> {`
- `fn` `codex-rs/tui/src/tui.rs:143` `pub fn restore_keep_raw() -> Result<()> {`
- `enum` `codex-rs/tui/src/tui.rs:149` `pub enum RestoreMode {`
- `impl` `codex-rs/tui/src/tui.rs:155` `impl RestoreMode {`
- `fn` `codex-rs/tui/src/tui.rs:156` `fn restore(self) -> Result<()> {`
- `fn` `codex-rs/tui/src/tui.rs:167` `fn flush_terminal_input_buffer() {`
- `fn` `codex-rs/tui/src/tui.rs:179` `fn flush_terminal_input_buffer() {`
- `use` `codex-rs/tui/src/tui.rs:180` `use windows_sys::Win32::Foundation::GetLastError;`
- `use` `codex-rs/tui/src/tui.rs:181` `use windows_sys::Win32::Foundation::INVALID_HANDLE_VALUE;`
- `use` `codex-rs/tui/src/tui.rs:182` `use windows_sys::Win32::System::Console::FlushConsoleInputBuffer;`
- `use` `codex-rs/tui/src/tui.rs:183` `use windows_sys::Win32::System::Console::GetStdHandle;`
- `use` `codex-rs/tui/src/tui.rs:184` `use windows_sys::Win32::System::Console::STD_INPUT_HANDLE;`
- `fn` `codex-rs/tui/src/tui.rs:204` `pub fn init() -> Result<Terminal> {`
- `fn` `codex-rs/tui/src/tui.rs:220` `fn set_panic_hook() {`
- `enum` `codex-rs/tui/src/tui.rs:229` `pub enum TuiEvent {`
- `struct` `codex-rs/tui/src/tui.rs:235` `pub struct Tui {`
- `impl` `codex-rs/tui/src/tui.rs:254` `impl Tui {`
- `fn` `codex-rs/tui/src/tui.rs:255` `pub fn new(terminal: Terminal) -> Self {`
- `fn` `codex-rs/tui/src/tui.rs:284` `pub fn set_alt_screen_enabled(&mut self, enabled: bool) {`
- `fn` `codex-rs/tui/src/tui.rs:288` `pub fn set_notification_method(&mut self, method: NotificationMethod) {`
- `fn` `codex-rs/tui/src/tui.rs:292` `pub fn frame_requester(&self) -> FrameRequester {`
- `fn` `codex-rs/tui/src/tui.rs:296` `pub fn enhanced_keys_supported(&self) -> bool {`
- `fn` `codex-rs/tui/src/tui.rs:300` `pub fn is_alt_screen_active(&self) -> bool {`
- `fn` `codex-rs/tui/src/tui.rs:305` `pub fn pause_events(&mut self) {`
- `fn` `codex-rs/tui/src/tui.rs:311` `pub fn resume_events(&mut self) {`
- `fn` `codex-rs/tui/src/tui.rs:356` `pub fn notify(&mut self, message: impl AsRef<str>) -> bool {`
- `fn` `codex-rs/tui/src/tui.rs:381` `pub fn event_stream(&self) -> Pin<Box<dyn Stream<Item = TuiEvent> + Send + 'static>> {`
- `fn` `codex-rs/tui/src/tui.rs:401` `pub fn enter_alt_screen(&mut self) -> Result<()> {`
- `fn` `codex-rs/tui/src/tui.rs:423` `pub fn leave_alt_screen(&mut self) -> Result<()> {`
- `fn` `codex-rs/tui/src/tui.rs:437` `pub fn insert_history_lines(&mut self, lines: Vec<Line<'static>>) {`
- `fn` `codex-rs/tui/src/tui.rs:442` `pub fn draw(`
- `fn` `codex-rs/tui/src/tui.rs:515` `fn pending_viewport_area(&mut self) -> Result<Option<Rect>> {`

## Dependencies (auto sample)
### Imports / Includes
- `use std::fmt;`
- `use std::future::Future;`
- `use std::io::IsTerminal;`
- `use std::io::Result;`
- `use std::io::Stdout;`
- `use std::io::stdin;`
- `use std::io::stdout;`
- `use std::panic;`
- `use std::pin::Pin;`
- `use std::sync::Arc;`
- `use std::sync::atomic::AtomicBool;`
- `use std::sync::atomic::Ordering;`
- `use crossterm::Command;`
- `use crossterm::SynchronizedUpdate;`
- `use crossterm::event::DisableBracketedPaste;`
- `use crossterm::event::DisableFocusChange;`
- `use crossterm::event::EnableBracketedPaste;`
- `use crossterm::event::EnableFocusChange;`
- `use crossterm::event::KeyEvent;`
- `use crossterm::event::KeyboardEnhancementFlags;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)

## Spec Links
- `workdocjcl/spec/06_UI/TUI.md`
