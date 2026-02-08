# `codex-rs/tui/src/render/renderable.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `12671`
- sha256: `79e13e0e52845124cf0e0a94dc92e7b53e0e477787d62335959e13fc208b2fb6`
- generated_utc: `2026-02-03T16:08:30Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/tui/src/render/renderable.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub trait Renderable {`
- `pub enum RenderableItem<'a> {`
- `pub struct ColumnRenderable<'a> {`
- `pub fn new() -> Self {`
- `pub fn push(&mut self, child: impl Into<Box<dyn Renderable + 'a>>) {`
- `pub struct FlexChild<'a> {`
- `pub struct FlexRenderable<'a> {`
- `pub fn new() -> Self {`
- `pub fn push(&mut self, flex: i32, child: impl Into<RenderableItem<'a>>) {`
- `pub struct RowRenderable<'a> {`
- `pub fn new() -> Self {`
- `pub fn push(&mut self, width: u16, child: impl Into<Box<dyn Renderable>>) {`
- `pub struct InsetRenderable<'a> {`
- `pub fn new(child: impl Into<RenderableItem<'a>>, insets: Insets) -> Self {`
- `pub trait RenderableExt<'a> {`

## Definitions (auto, per-file)
- `use` `codex-rs/tui/src/render/renderable.rs:1` `use std::sync::Arc;`
- `use` `codex-rs/tui/src/render/renderable.rs:3` `use ratatui::buffer::Buffer;`
- `use` `codex-rs/tui/src/render/renderable.rs:4` `use ratatui::layout::Rect;`
- `use` `codex-rs/tui/src/render/renderable.rs:5` `use ratatui::text::Line;`
- `use` `codex-rs/tui/src/render/renderable.rs:6` `use ratatui::text::Span;`
- `use` `codex-rs/tui/src/render/renderable.rs:7` `use ratatui::widgets::Paragraph;`
- `use` `codex-rs/tui/src/render/renderable.rs:8` `use ratatui::widgets::WidgetRef;`
- `use` `codex-rs/tui/src/render/renderable.rs:10` `use crate::render::Insets;`
- `use` `codex-rs/tui/src/render/renderable.rs:11` `use crate::render::RectExt as _;`
- `trait` `codex-rs/tui/src/render/renderable.rs:13` `pub trait Renderable {`
- `fn` `codex-rs/tui/src/render/renderable.rs:14` `fn render(&self, area: Rect, buf: &mut Buffer);`
- `fn` `codex-rs/tui/src/render/renderable.rs:15` `fn desired_height(&self, width: u16) -> u16;`
- `fn` `codex-rs/tui/src/render/renderable.rs:16` `fn cursor_pos(&self, _area: Rect) -> Option<(u16, u16)> {`
- `enum` `codex-rs/tui/src/render/renderable.rs:21` `pub enum RenderableItem<'a> {`
- `impl` `codex-rs/tui/src/render/renderable.rs:26` `impl<'a> Renderable for RenderableItem<'a> {`
- `fn` `codex-rs/tui/src/render/renderable.rs:27` `fn render(&self, area: Rect, buf: &mut Buffer) {`
- `fn` `codex-rs/tui/src/render/renderable.rs:34` `fn desired_height(&self, width: u16) -> u16 {`
- `fn` `codex-rs/tui/src/render/renderable.rs:41` `fn cursor_pos(&self, area: Rect) -> Option<(u16, u16)> {`
- `impl` `codex-rs/tui/src/render/renderable.rs:49` `impl<'a> From<Box<dyn Renderable + 'a>> for RenderableItem<'a> {`
- `fn` `codex-rs/tui/src/render/renderable.rs:50` `fn from(value: Box<dyn Renderable + 'a>) -> Self {`
- `fn` `codex-rs/tui/src/render/renderable.rs:59` `fn from(value: R) -> Self {`
- `impl` `codex-rs/tui/src/render/renderable.rs:64` `impl Renderable for () {`
- `fn` `codex-rs/tui/src/render/renderable.rs:65` `fn render(&self, _area: Rect, _buf: &mut Buffer) {}`
- `fn` `codex-rs/tui/src/render/renderable.rs:66` `fn desired_height(&self, _width: u16) -> u16 {`
- `impl` `codex-rs/tui/src/render/renderable.rs:71` `impl Renderable for &str {`
- `fn` `codex-rs/tui/src/render/renderable.rs:72` `fn render(&self, area: Rect, buf: &mut Buffer) {`
- `fn` `codex-rs/tui/src/render/renderable.rs:75` `fn desired_height(&self, _width: u16) -> u16 {`
- `impl` `codex-rs/tui/src/render/renderable.rs:80` `impl Renderable for String {`
- `fn` `codex-rs/tui/src/render/renderable.rs:81` `fn render(&self, area: Rect, buf: &mut Buffer) {`
- `fn` `codex-rs/tui/src/render/renderable.rs:84` `fn desired_height(&self, _width: u16) -> u16 {`
- `impl` `codex-rs/tui/src/render/renderable.rs:89` `impl<'a> Renderable for Span<'a> {`
- `fn` `codex-rs/tui/src/render/renderable.rs:90` `fn render(&self, area: Rect, buf: &mut Buffer) {`
- `fn` `codex-rs/tui/src/render/renderable.rs:93` `fn desired_height(&self, _width: u16) -> u16 {`
- `impl` `codex-rs/tui/src/render/renderable.rs:98` `impl<'a> Renderable for Line<'a> {`
- `fn` `codex-rs/tui/src/render/renderable.rs:99` `fn render(&self, area: Rect, buf: &mut Buffer) {`
- `fn` `codex-rs/tui/src/render/renderable.rs:102` `fn desired_height(&self, _width: u16) -> u16 {`
- `impl` `codex-rs/tui/src/render/renderable.rs:107` `impl<'a> Renderable for Paragraph<'a> {`
- `fn` `codex-rs/tui/src/render/renderable.rs:108` `fn render(&self, area: Rect, buf: &mut Buffer) {`
- `fn` `codex-rs/tui/src/render/renderable.rs:111` `fn desired_height(&self, width: u16) -> u16 {`
- `impl` `codex-rs/tui/src/render/renderable.rs:116` `impl<R: Renderable> Renderable for Option<R> {`
- `fn` `codex-rs/tui/src/render/renderable.rs:117` `fn render(&self, area: Rect, buf: &mut Buffer) {`
- `fn` `codex-rs/tui/src/render/renderable.rs:123` `fn desired_height(&self, width: u16) -> u16 {`
- `impl` `codex-rs/tui/src/render/renderable.rs:132` `impl<R: Renderable> Renderable for Arc<R> {`
- `fn` `codex-rs/tui/src/render/renderable.rs:133` `fn render(&self, area: Rect, buf: &mut Buffer) {`
- `fn` `codex-rs/tui/src/render/renderable.rs:136` `fn desired_height(&self, width: u16) -> u16 {`
- `struct` `codex-rs/tui/src/render/renderable.rs:141` `pub struct ColumnRenderable<'a> {`
- `impl` `codex-rs/tui/src/render/renderable.rs:145` `impl Renderable for ColumnRenderable<'_> {`
- `fn` `codex-rs/tui/src/render/renderable.rs:146` `fn render(&self, area: Rect, buf: &mut Buffer) {`
- `fn` `codex-rs/tui/src/render/renderable.rs:158` `fn desired_height(&self, width: u16) -> u16 {`
- `fn` `codex-rs/tui/src/render/renderable.rs:169` `fn cursor_pos(&self, area: Rect) -> Option<(u16, u16)> {`
- `impl` `codex-rs/tui/src/render/renderable.rs:185` `impl<'a> ColumnRenderable<'a> {`
- `fn` `codex-rs/tui/src/render/renderable.rs:186` `pub fn new() -> Self {`
- `fn` `codex-rs/tui/src/render/renderable.rs:200` `pub fn push(&mut self, child: impl Into<Box<dyn Renderable + 'a>>) {`
- `struct` `codex-rs/tui/src/render/renderable.rs:214` `pub struct FlexChild<'a> {`
- `struct` `codex-rs/tui/src/render/renderable.rs:219` `pub struct FlexRenderable<'a> {`
- `impl` `codex-rs/tui/src/render/renderable.rs:227` `impl<'a> FlexRenderable<'a> {`
- `fn` `codex-rs/tui/src/render/renderable.rs:228` `pub fn new() -> Self {`
- `fn` `codex-rs/tui/src/render/renderable.rs:232` `pub fn push(&mut self, flex: i32, child: impl Into<RenderableItem<'a>>) {`
- `fn` `codex-rs/tui/src/render/renderable.rs:242` `fn allocate(&self, area: Rect) -> Vec<Rect> {`
- `impl` `codex-rs/tui/src/render/renderable.rs:293` `impl<'a> Renderable for FlexRenderable<'a> {`
- `fn` `codex-rs/tui/src/render/renderable.rs:294` `fn render(&self, area: Rect, buf: &mut Buffer) {`
- `fn` `codex-rs/tui/src/render/renderable.rs:303` `fn desired_height(&self, width: u16) -> u16 {`
- `fn` `codex-rs/tui/src/render/renderable.rs:310` `fn cursor_pos(&self, area: Rect) -> Option<(u16, u16)> {`
- `struct` `codex-rs/tui/src/render/renderable.rs:318` `pub struct RowRenderable<'a> {`
- `impl` `codex-rs/tui/src/render/renderable.rs:322` `impl Renderable for RowRenderable<'_> {`
- `fn` `codex-rs/tui/src/render/renderable.rs:323` `fn render(&self, area: Rect, buf: &mut Buffer) {`
- `fn` `codex-rs/tui/src/render/renderable.rs:335` `fn desired_height(&self, width: u16) -> u16 {`
- `fn` `codex-rs/tui/src/render/renderable.rs:352` `fn cursor_pos(&self, area: Rect) -> Option<(u16, u16)> {`
- `impl` `codex-rs/tui/src/render/renderable.rs:368` `impl<'a> RowRenderable<'a> {`
- `fn` `codex-rs/tui/src/render/renderable.rs:369` `pub fn new() -> Self {`
- `fn` `codex-rs/tui/src/render/renderable.rs:373` `pub fn push(&mut self, width: u16, child: impl Into<Box<dyn Renderable>>) {`
- `struct` `codex-rs/tui/src/render/renderable.rs:388` `pub struct InsetRenderable<'a> {`
- `impl` `codex-rs/tui/src/render/renderable.rs:393` `impl<'a> Renderable for InsetRenderable<'a> {`
- `fn` `codex-rs/tui/src/render/renderable.rs:394` `fn render(&self, area: Rect, buf: &mut Buffer) {`
- `fn` `codex-rs/tui/src/render/renderable.rs:397` `fn desired_height(&self, width: u16) -> u16 {`
- `fn` `codex-rs/tui/src/render/renderable.rs:403` `fn cursor_pos(&self, area: Rect) -> Option<(u16, u16)> {`
- `impl` `codex-rs/tui/src/render/renderable.rs:408` `impl<'a> InsetRenderable<'a> {`
- `fn` `codex-rs/tui/src/render/renderable.rs:409` `pub fn new(child: impl Into<RenderableItem<'a>>, insets: Insets) -> Self {`
- `trait` `codex-rs/tui/src/render/renderable.rs:417` `pub trait RenderableExt<'a> {`
- `fn` `codex-rs/tui/src/render/renderable.rs:418` `fn inset(self, insets: Insets) -> RenderableItem<'a>;`
- `fn` `codex-rs/tui/src/render/renderable.rs:425` `fn inset(self, insets: Insets) -> RenderableItem<'a> {`

## Dependencies (auto sample)
### Imports / Includes
- `use std::sync::Arc;`
- `use ratatui::buffer::Buffer;`
- `use ratatui::layout::Rect;`
- `use ratatui::text::Line;`
- `use ratatui::text::Span;`
- `use ratatui::widgets::Paragraph;`
- `use ratatui::widgets::WidgetRef;`
- `use crate::render::Insets;`
- `use crate::render::RectExt as _;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- `workdocjcl/spec/06_UI/TUI.md`
