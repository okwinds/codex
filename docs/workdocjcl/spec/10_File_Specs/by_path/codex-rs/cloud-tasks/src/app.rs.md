# `codex-rs/cloud-tasks/src/app.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `15977`
- sha256: `875c8e02a6e613d2624f88d98e15321b0b72d3c8dd32fed10b6a49085597150a`
- generated_utc: `2026-02-03T16:08:28Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/cloud-tasks/src/app.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub struct EnvironmentRow {`
- `pub struct EnvModalState {`
- `pub struct BestOfModalState {`
- `pub enum ApplyResultLevel {`
- `pub struct ApplyModalState {`
- `pub struct App {`
- `pub fn new() -> Self {`
- `pub fn next(&mut self) {`
- `pub fn prev(&mut self) {`
- `pub struct DiffOverlay {`
- `pub struct AttemptView {`
- `pub fn has_diff(&self) -> bool {`
- `pub fn has_text(&self) -> bool {`
- `pub fn new(task_id: TaskId, title: String, attempt_total_hint: Option<usize>) -> Self {`
- `pub fn current_attempt(&self) -> Option<&AttemptView> {`
- `pub fn base_attempt_mut(&mut self) -> &mut AttemptView {`
- `pub fn set_view(&mut self, view: DetailView) {`
- `pub fn expected_attempts(&self) -> Option<usize> {`
- `pub fn attempt_count(&self) -> usize {`
- `pub fn attempt_display_total(&self) -> usize {`
- `pub fn step_attempt(&mut self, delta: isize) -> bool {`
- `pub fn current_can_apply(&self) -> bool {`
- `pub fn apply_selection_to_fields(&mut self) {`
- `pub enum DetailView {`
- `pub enum AppEvent {`

## Definitions (auto, per-file)
- `use` `codex-rs/cloud-tasks/src/app.rs:1` `use std::time::Duration;`
- `use` `codex-rs/cloud-tasks/src/app.rs:2` `use std::time::Instant;`
- `struct` `codex-rs/cloud-tasks/src/app.rs:6` `pub struct EnvironmentRow {`
- `struct` `codex-rs/cloud-tasks/src/app.rs:14` `pub struct EnvModalState {`
- `struct` `codex-rs/cloud-tasks/src/app.rs:20` `pub struct BestOfModalState {`
- `enum` `codex-rs/cloud-tasks/src/app.rs:25` `pub enum ApplyResultLevel {`
- `struct` `codex-rs/cloud-tasks/src/app.rs:32` `pub struct ApplyModalState {`
- `use` `codex-rs/cloud-tasks/src/app.rs:42` `use crate::scrollable_diff::ScrollableDiff;`
- `use` `codex-rs/cloud-tasks/src/app.rs:43` `use codex_cloud_tasks_client::CloudBackend;`
- `use` `codex-rs/cloud-tasks/src/app.rs:44` `use codex_cloud_tasks_client::TaskId;`
- `use` `codex-rs/cloud-tasks/src/app.rs:45` `use codex_cloud_tasks_client::TaskSummary;`
- `struct` `codex-rs/cloud-tasks/src/app.rs:47` `pub struct App {`
- `impl` `codex-rs/cloud-tasks/src/app.rs:77` `impl App {`
- `fn` `codex-rs/cloud-tasks/src/app.rs:78` `pub fn new() -> Self {`
- `fn` `codex-rs/cloud-tasks/src/app.rs:104` `pub fn next(&mut self) {`
- `fn` `codex-rs/cloud-tasks/src/app.rs:111` `pub fn prev(&mut self) {`
- `fn` `codex-rs/cloud-tasks/src/app.rs:121` `pub async fn load_tasks(`
- `struct` `codex-rs/cloud-tasks/src/app.rs:136` `pub struct DiffOverlay {`
- `struct` `codex-rs/cloud-tasks/src/app.rs:153` `pub struct AttemptView {`
- `impl` `codex-rs/cloud-tasks/src/app.rs:163` `impl AttemptView {`
- `fn` `codex-rs/cloud-tasks/src/app.rs:164` `pub fn has_diff(&self) -> bool {`
- `fn` `codex-rs/cloud-tasks/src/app.rs:168` `pub fn has_text(&self) -> bool {`
- `impl` `codex-rs/cloud-tasks/src/app.rs:173` `impl DiffOverlay {`
- `fn` `codex-rs/cloud-tasks/src/app.rs:174` `pub fn new(task_id: TaskId, title: String, attempt_total_hint: Option<usize>) -> Self {`
- `fn` `codex-rs/cloud-tasks/src/app.rs:194` `pub fn current_attempt(&self) -> Option<&AttemptView> {`
- `fn` `codex-rs/cloud-tasks/src/app.rs:198` `pub fn base_attempt_mut(&mut self) -> &mut AttemptView {`
- `fn` `codex-rs/cloud-tasks/src/app.rs:205` `pub fn set_view(&mut self, view: DetailView) {`
- `fn` `codex-rs/cloud-tasks/src/app.rs:210` `pub fn expected_attempts(&self) -> Option<usize> {`
- `fn` `codex-rs/cloud-tasks/src/app.rs:220` `pub fn attempt_count(&self) -> usize {`
- `fn` `codex-rs/cloud-tasks/src/app.rs:224` `pub fn attempt_display_total(&self) -> usize {`
- `fn` `codex-rs/cloud-tasks/src/app.rs:229` `pub fn step_attempt(&mut self, delta: isize) -> bool {`
- `fn` `codex-rs/cloud-tasks/src/app.rs:244` `pub fn current_can_apply(&self) -> bool {`
- `fn` `codex-rs/cloud-tasks/src/app.rs:253` `pub fn apply_selection_to_fields(&mut self) {`
- `enum` `codex-rs/cloud-tasks/src/app.rs:292` `pub enum DetailView {`
- `enum` `codex-rs/cloud-tasks/src/app.rs:300` `pub enum AppEvent {`
- `use` `codex-rs/cloud-tasks/src/app.rs:355` `use super::*;`
- `use` `codex-rs/cloud-tasks/src/app.rs:356` `use chrono::Utc;`
- `use` `codex-rs/cloud-tasks/src/app.rs:357` `use codex_cloud_tasks_client::CloudTaskError;`
- `struct` `codex-rs/cloud-tasks/src/app.rs:359` `struct FakeBackend {`
- `impl` `codex-rs/cloud-tasks/src/app.rs:365` `impl codex_cloud_tasks_client::CloudBackend for FakeBackend {`
- `fn` `codex-rs/cloud-tasks/src/app.rs:366` `async fn list_tasks(`
- `fn` `codex-rs/cloud-tasks/src/app.rs:407` `async fn get_task_summary(`
- `fn` `codex-rs/cloud-tasks/src/app.rs:419` `async fn get_task_diff(`
- `fn` `codex-rs/cloud-tasks/src/app.rs:428` `async fn get_task_messages(`
- `fn` `codex-rs/cloud-tasks/src/app.rs:434` `async fn get_task_text(`
- `fn` `codex-rs/cloud-tasks/src/app.rs:448` `async fn list_sibling_attempts(`
- `fn` `codex-rs/cloud-tasks/src/app.rs:456` `async fn apply_task(`
- `fn` `codex-rs/cloud-tasks/src/app.rs:466` `async fn apply_task_preflight(`
- `fn` `codex-rs/cloud-tasks/src/app.rs:476` `async fn create_task(`
- `fn` `codex-rs/cloud-tasks/src/app.rs:491` `async fn load_tasks_uses_env_parameter() {`

## Dependencies (auto sample)
### Imports / Includes
- `use std::time::Duration;`
- `use std::time::Instant;`
- `use crate::scrollable_diff::ScrollableDiff;`
- `use codex_cloud_tasks_client::CloudBackend;`
- `use codex_cloud_tasks_client::TaskId;`
- `use codex_cloud_tasks_client::TaskSummary;`
- `use super::*;`
- `use chrono::Utc;`
- `use codex_cloud_tasks_client::CloudTaskError;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- has retry/timeout/backoff logic
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
