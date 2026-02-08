# `codex-rs/tui/src/tui/event_stream.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `19662`
- sha256: `58176ee776dd4d2a249af433b1d13637ae77062751be229c424377e42123e3ce`
- generated_utc: `2026-02-08T10:45:40Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/tui/src/tui/event_stream.rs` (read)

### Outputs / Side Effects
- spawns subprocesses

## Public Surface (auto)
- `pub trait EventSource: Send + 'static {`
- `pub struct EventBroker<S: EventSource = CrosstermEventSource> {`
- `pub fn new() -> Self {`
- `pub fn pause_events(&self) {`
- `pub fn resume_events(&self) {`
- `pub fn resume_events_rx(&self) -> watch::Receiver<()> {`
- `pub struct CrosstermEventSource(pub crossterm::event::EventStream);`
- `pub struct TuiEventStream<S: EventSource + Default + Unpin = CrosstermEventSource> {`
- `pub fn new(`
- `pub fn poll_crossterm_event(&mut self, cx: &mut Context<'_>) -> Poll<Option<TuiEvent>> {`
- `pub fn poll_draw_event(&mut self, cx: &mut Context<'_>) -> Poll<Option<TuiEvent>> {`

## Definitions (auto, per-file)
- `use` `codex-rs/tui/src/tui/event_stream.rs:20` `use std::pin::Pin;`
- `use` `codex-rs/tui/src/tui/event_stream.rs:21` `use std::sync::Arc;`
- `use` `codex-rs/tui/src/tui/event_stream.rs:22` `use std::sync::Mutex;`
- `use` `codex-rs/tui/src/tui/event_stream.rs:23` `use std::sync::atomic::AtomicBool;`
- `use` `codex-rs/tui/src/tui/event_stream.rs:24` `use std::sync::atomic::Ordering;`
- `use` `codex-rs/tui/src/tui/event_stream.rs:25` `use std::task::Context;`
- `use` `codex-rs/tui/src/tui/event_stream.rs:26` `use std::task::Poll;`
- `use` `codex-rs/tui/src/tui/event_stream.rs:28` `use crossterm::event::Event;`
- `use` `codex-rs/tui/src/tui/event_stream.rs:29` `use tokio::sync::broadcast;`
- `use` `codex-rs/tui/src/tui/event_stream.rs:30` `use tokio::sync::watch;`
- `use` `codex-rs/tui/src/tui/event_stream.rs:31` `use tokio_stream::Stream;`
- `use` `codex-rs/tui/src/tui/event_stream.rs:32` `use tokio_stream::wrappers::BroadcastStream;`
- `use` `codex-rs/tui/src/tui/event_stream.rs:33` `use tokio_stream::wrappers::WatchStream;`
- `use` `codex-rs/tui/src/tui/event_stream.rs:34` `use tokio_stream::wrappers::errors::BroadcastStreamRecvError;`
- `use` `codex-rs/tui/src/tui/event_stream.rs:36` `use super::TuiEvent;`
- `type` `codex-rs/tui/src/tui/event_stream.rs:39` `pub type EventResult = std::io::Result<Event>;`
- `trait` `codex-rs/tui/src/tui/event_stream.rs:43` `pub trait EventSource: Send + 'static {`
- `fn` `codex-rs/tui/src/tui/event_stream.rs:44` `fn poll_next(self: Pin<&mut Self>, cx: &mut Context<'_>) -> Poll<Option<EventResult>>;`
- `struct` `codex-rs/tui/src/tui/event_stream.rs:51` `pub struct EventBroker<S: EventSource = CrosstermEventSource> {`
- `enum` `codex-rs/tui/src/tui/event_stream.rs:57` `enum EventBrokerState<S: EventSource> {`
- `impl` `codex-rs/tui/src/tui/event_stream.rs:63` `impl<S: EventSource + Default> EventBrokerState<S> {`
- `fn` `codex-rs/tui/src/tui/event_stream.rs:65` `fn active_event_source_mut(&mut self) -> Option<&mut S> {`
- `impl` `codex-rs/tui/src/tui/event_stream.rs:80` `impl<S: EventSource + Default> EventBroker<S> {`
- `fn` `codex-rs/tui/src/tui/event_stream.rs:81` `pub fn new() -> Self {`
- `fn` `codex-rs/tui/src/tui/event_stream.rs:90` `pub fn pause_events(&self) {`
- `fn` `codex-rs/tui/src/tui/event_stream.rs:99` `pub fn resume_events(&self) {`
- `fn` `codex-rs/tui/src/tui/event_stream.rs:112` `pub fn resume_events_rx(&self) -> watch::Receiver<()> {`
- `struct` `codex-rs/tui/src/tui/event_stream.rs:118` `pub struct CrosstermEventSource(pub crossterm::event::EventStream);`
- `impl` `codex-rs/tui/src/tui/event_stream.rs:120` `impl Default for CrosstermEventSource {`
- `fn` `codex-rs/tui/src/tui/event_stream.rs:121` `fn default() -> Self {`
- `impl` `codex-rs/tui/src/tui/event_stream.rs:126` `impl EventSource for CrosstermEventSource {`
- `fn` `codex-rs/tui/src/tui/event_stream.rs:127` `fn poll_next(self: Pin<&mut Self>, cx: &mut Context<'_>) -> Poll<Option<EventResult>> {`
- `struct` `codex-rs/tui/src/tui/event_stream.rs:139` `pub struct TuiEventStream<S: EventSource + Default + Unpin = CrosstermEventSource> {`
- `impl` `codex-rs/tui/src/tui/event_stream.rs:151` `impl<S: EventSource + Default + Unpin> TuiEventStream<S> {`
- `fn` `codex-rs/tui/src/tui/event_stream.rs:152` `pub fn new(`
- `fn` `codex-rs/tui/src/tui/event_stream.rs:178` `pub fn poll_crossterm_event(&mut self, cx: &mut Context<'_>) -> Poll<Option<TuiEvent>> {`
- `fn` `codex-rs/tui/src/tui/event_stream.rs:225` `pub fn poll_draw_event(&mut self, cx: &mut Context<'_>) -> Poll<Option<TuiEvent>> {`
- `fn` `codex-rs/tui/src/tui/event_stream.rs:237` `fn map_crossterm_event(&mut self, event: Event) -> Option<TuiEvent> {`
- `impl` `codex-rs/tui/src/tui/event_stream.rs:265` `impl<S: EventSource + Default + Unpin> Stream for TuiEventStream<S> {`
- `type` `codex-rs/tui/src/tui/event_stream.rs:266` `type Item = TuiEvent;`
- `fn` `codex-rs/tui/src/tui/event_stream.rs:268` `fn poll_next(mut self: Pin<&mut Self>, cx: &mut Context<'_>) -> Poll<Option<Self::Item>> {`
- `use` `codex-rs/tui/src/tui/event_stream.rs:295` `use super::*;`
- `use` `codex-rs/tui/src/tui/event_stream.rs:296` `use crossterm::event::Event;`
- `use` `codex-rs/tui/src/tui/event_stream.rs:297` `use crossterm::event::KeyCode;`
- `use` `codex-rs/tui/src/tui/event_stream.rs:298` `use crossterm::event::KeyEvent;`
- `use` `codex-rs/tui/src/tui/event_stream.rs:299` `use crossterm::event::KeyModifiers;`
- `use` `codex-rs/tui/src/tui/event_stream.rs:300` `use pretty_assertions::assert_eq;`
- `use` `codex-rs/tui/src/tui/event_stream.rs:301` `use std::task::Context;`
- `use` `codex-rs/tui/src/tui/event_stream.rs:302` `use std::task::Poll;`
- `use` `codex-rs/tui/src/tui/event_stream.rs:303` `use std::time::Duration;`
- `use` `codex-rs/tui/src/tui/event_stream.rs:304` `use tokio::sync::broadcast;`
- `use` `codex-rs/tui/src/tui/event_stream.rs:305` `use tokio::sync::mpsc;`
- `use` `codex-rs/tui/src/tui/event_stream.rs:306` `use tokio::time::timeout;`
- `use` `codex-rs/tui/src/tui/event_stream.rs:307` `use tokio_stream::StreamExt;`
- `struct` `codex-rs/tui/src/tui/event_stream.rs:310` `struct FakeEventSource {`
- `struct` `codex-rs/tui/src/tui/event_stream.rs:315` `struct FakeEventSourceHandle {`
- `impl` `codex-rs/tui/src/tui/event_stream.rs:319` `impl FakeEventSource {`
- `fn` `codex-rs/tui/src/tui/event_stream.rs:320` `fn new() -> Self {`
- `impl` `codex-rs/tui/src/tui/event_stream.rs:326` `impl Default for FakeEventSource {`
- `fn` `codex-rs/tui/src/tui/event_stream.rs:327` `fn default() -> Self {`
- `impl` `codex-rs/tui/src/tui/event_stream.rs:332` `impl FakeEventSourceHandle {`
- `fn` `codex-rs/tui/src/tui/event_stream.rs:333` `fn new(broker: Arc<EventBroker<FakeEventSource>>) -> Self {`
- `fn` `codex-rs/tui/src/tui/event_stream.rs:337` `fn send(&self, event: EventResult) {`
- `impl` `codex-rs/tui/src/tui/event_stream.rs:350` `impl EventSource for FakeEventSource {`
- `fn` `codex-rs/tui/src/tui/event_stream.rs:351` `fn poll_next(self: Pin<&mut Self>, cx: &mut Context<'_>) -> Poll<Option<EventResult>> {`
- `fn` `codex-rs/tui/src/tui/event_stream.rs:356` `fn make_stream(`
- `type` `codex-rs/tui/src/tui/event_stream.rs:372` `type SetupState = (`
- `fn` `codex-rs/tui/src/tui/event_stream.rs:380` `fn setup() -> SetupState {`
- `fn` `codex-rs/tui/src/tui/event_stream.rs:392` `async fn key_event_skips_unmapped() {`
- `fn` `codex-rs/tui/src/tui/event_stream.rs:412` `async fn draw_and_key_events_yield_both() {`
- `fn` `codex-rs/tui/src/tui/event_stream.rs:442` `async fn lagged_draw_maps_to_draw() {`
- `fn` `codex-rs/tui/src/tui/event_stream.rs:455` `async fn error_or_eof_ends_stream() {`
- `fn` `codex-rs/tui/src/tui/event_stream.rs:466` `async fn resume_wakes_paused_stream() {`
- `fn` `codex-rs/tui/src/tui/event_stream.rs:490` `async fn resume_wakes_pending_stream() {`

## Dependencies (auto sample)
### Imports / Includes
- `use std::pin::Pin;`
- `use std::sync::Arc;`
- `use std::sync::Mutex;`
- `use std::sync::atomic::AtomicBool;`
- `use std::sync::atomic::Ordering;`
- `use std::task::Context;`
- `use std::task::Poll;`
- `use crossterm::event::Event;`
- `use tokio::sync::broadcast;`
- `use tokio::sync::watch;`
- `use tokio_stream::Stream;`
- `use tokio_stream::wrappers::BroadcastStream;`
- `use tokio_stream::wrappers::WatchStream;`
- `use tokio_stream::wrappers::errors::BroadcastStreamRecvError;`
- `use super::TuiEvent;`
- `use super::*;`
- `use crossterm::event::Event;`
- `use crossterm::event::KeyCode;`
- `use crossterm::event::KeyEvent;`
- `use crossterm::event::KeyModifiers;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- has retry/timeout/backoff logic
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- `docs/workdocjcl/spec/06_UI/TUI.md`
