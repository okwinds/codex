# `codex-rs/core/src/analytics_client.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `9695`
- sha256: `ed341f3ab587fda298a60be9fdd1121855a8044b29c44ef7871c09bda93c4b8f`
- generated_utc: `2026-02-03T16:08:29Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/analytics_client.rs` (read)

### Outputs / Side Effects
- spawns subprocesses

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `use` `codex-rs/core/src/analytics_client.rs:1` `use crate::AuthManager;`
- `use` `codex-rs/core/src/analytics_client.rs:2` `use crate::config::Config;`
- `use` `codex-rs/core/src/analytics_client.rs:3` `use crate::default_client::create_client;`
- `use` `codex-rs/core/src/analytics_client.rs:4` `use crate::git_info::collect_git_info;`
- `use` `codex-rs/core/src/analytics_client.rs:5` `use crate::git_info::get_git_repo_root;`
- `use` `codex-rs/core/src/analytics_client.rs:6` `use codex_protocol::protocol::SkillScope;`
- `use` `codex-rs/core/src/analytics_client.rs:7` `use serde::Serialize;`
- `use` `codex-rs/core/src/analytics_client.rs:8` `use sha1::Digest;`
- `use` `codex-rs/core/src/analytics_client.rs:9` `use sha1::Sha1;`
- `use` `codex-rs/core/src/analytics_client.rs:10` `use std::path::Path;`
- `use` `codex-rs/core/src/analytics_client.rs:11` `use std::path::PathBuf;`
- `use` `codex-rs/core/src/analytics_client.rs:12` `use std::sync::Arc;`
- `use` `codex-rs/core/src/analytics_client.rs:13` `use std::time::Duration;`
- `use` `codex-rs/core/src/analytics_client.rs:14` `use tokio::sync::mpsc;`
- `impl` `codex-rs/core/src/analytics_client.rs:48` `impl AnalyticsEventsQueue {`
- `fn` `codex-rs/core/src/analytics_client.rs:59` `fn try_send(&self, job: TrackEventsJob) {`
- `impl` `codex-rs/core/src/analytics_client.rs:67` `impl AnalyticsEventsClient {`
- `struct` `codex-rs/core/src/analytics_client.rs:89` `struct TrackEventsJob {`
- `const` `codex-rs/core/src/analytics_client.rs:95` `const ANALYTICS_EVENTS_QUEUE_SIZE: usize = 256;`
- `const` `codex-rs/core/src/analytics_client.rs:96` `const ANALYTICS_EVENTS_TIMEOUT: Duration = Duration::from_secs(10);`
- `struct` `codex-rs/core/src/analytics_client.rs:99` `struct TrackEventsRequest {`
- `struct` `codex-rs/core/src/analytics_client.rs:104` `struct TrackEvent {`
- `struct` `codex-rs/core/src/analytics_client.rs:112` `struct TrackEventParams {`
- `fn` `codex-rs/core/src/analytics_client.rs:144` `async fn send_track_skill_invocations(auth_manager: &AuthManager, job: TrackEventsJob) {`
- `fn` `codex-rs/core/src/analytics_client.rs:228` `fn skill_id_for_local_skill(`
- `fn` `codex-rs/core/src/analytics_client.rs:250` `fn normalize_path_for_skill_id(`
- `use` `codex-rs/core/src/analytics_client.rs:272` `use super::normalize_path_for_skill_id;`
- `use` `codex-rs/core/src/analytics_client.rs:273` `use pretty_assertions::assert_eq;`
- `use` `codex-rs/core/src/analytics_client.rs:274` `use std::path::PathBuf;`
- `fn` `codex-rs/core/src/analytics_client.rs:276` `fn expected_absolute_path(path: &PathBuf) -> String {`
- `fn` `codex-rs/core/src/analytics_client.rs:284` `fn normalize_path_for_skill_id_repo_scoped_uses_relative_path() {`
- `fn` `codex-rs/core/src/analytics_client.rs:298` `fn normalize_path_for_skill_id_user_scoped_uses_absolute_path() {`
- `fn` `codex-rs/core/src/analytics_client.rs:308` `fn normalize_path_for_skill_id_admin_scoped_uses_absolute_path() {`
- `fn` `codex-rs/core/src/analytics_client.rs:318` `fn normalize_path_for_skill_id_repo_root_not_in_skill_path_uses_absolute_path() {`

## Dependencies (auto sample)
### Imports / Includes
- `use crate::AuthManager;`
- `use crate::config::Config;`
- `use crate::default_client::create_client;`
- `use crate::git_info::collect_git_info;`
- `use crate::git_info::get_git_repo_root;`
- `use codex_protocol::protocol::SkillScope;`
- `use serde::Serialize;`
- `use sha1::Digest;`
- `use sha1::Sha1;`
- `use std::path::Path;`
- `use std::path::PathBuf;`
- `use std::sync::Arc;`
- `use std::time::Duration;`
- `use tokio::sync::mpsc;`
- `use super::normalize_path_for_skill_id;`
- `use pretty_assertions::assert_eq;`
- `use std::path::PathBuf;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- has retry/timeout/backoff logic

## Spec Links
- `workdocjcl/spec/00_Overview/ARCHITECTURE.md`
