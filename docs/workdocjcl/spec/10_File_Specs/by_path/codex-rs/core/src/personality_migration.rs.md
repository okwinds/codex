# `codex-rs/core/src/personality_migration.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `9066`
- sha256: `75763de55c16c3b6803b27ed8c332986d0a1aa83624fe73223fd6ec55a40cdc4`
- generated_utc: `2026-02-03T16:08:29Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/personality_migration.rs` (read)

### Outputs / Side Effects
- writes to filesystem

## Public Surface (auto)
- `pub enum PersonalityMigrationStatus {`

## Definitions (auto, per-file)
- `use` `codex-rs/core/src/personality_migration.rs:1` `use crate::config::ConfigToml;`
- `use` `codex-rs/core/src/personality_migration.rs:2` `use crate::config::edit::ConfigEditsBuilder;`
- `use` `codex-rs/core/src/personality_migration.rs:3` `use crate::rollout::ARCHIVED_SESSIONS_SUBDIR;`
- `use` `codex-rs/core/src/personality_migration.rs:4` `use crate::rollout::SESSIONS_SUBDIR;`
- `use` `codex-rs/core/src/personality_migration.rs:5` `use crate::rollout::list::ThreadListConfig;`
- `use` `codex-rs/core/src/personality_migration.rs:6` `use crate::rollout::list::ThreadListLayout;`
- `use` `codex-rs/core/src/personality_migration.rs:7` `use crate::rollout::list::ThreadSortKey;`
- `use` `codex-rs/core/src/personality_migration.rs:8` `use crate::rollout::list::get_threads_in_root;`
- `use` `codex-rs/core/src/personality_migration.rs:9` `use crate::state_db;`
- `use` `codex-rs/core/src/personality_migration.rs:10` `use codex_protocol::config_types::Personality;`
- `use` `codex-rs/core/src/personality_migration.rs:11` `use codex_protocol::protocol::SessionSource;`
- `use` `codex-rs/core/src/personality_migration.rs:12` `use std::io;`
- `use` `codex-rs/core/src/personality_migration.rs:13` `use std::path::Path;`
- `use` `codex-rs/core/src/personality_migration.rs:14` `use tokio::fs::OpenOptions;`
- `use` `codex-rs/core/src/personality_migration.rs:15` `use tokio::io::AsyncWriteExt;`
- `const` `codex-rs/core/src/personality_migration.rs:17` `pub const PERSONALITY_MIGRATION_FILENAME: &str = ".personality_migration";`
- `enum` `codex-rs/core/src/personality_migration.rs:20` `pub enum PersonalityMigrationStatus {`
- `fn` `codex-rs/core/src/personality_migration.rs:27` `pub async fn maybe_migrate_personality(`
- `fn` `codex-rs/core/src/personality_migration.rs:66` `async fn has_recorded_sessions(codex_home: &Path, default_provider: &str) -> io::Result<bool> {`
- `fn` `codex-rs/core/src/personality_migration.rs:120` `async fn create_marker(marker_path: &Path) -> io::Result<()> {`
- `use` `codex-rs/core/src/personality_migration.rs:135` `use super::*;`
- `use` `codex-rs/core/src/personality_migration.rs:136` `use codex_protocol::ThreadId;`
- `use` `codex-rs/core/src/personality_migration.rs:137` `use codex_protocol::protocol::EventMsg;`
- `use` `codex-rs/core/src/personality_migration.rs:138` `use codex_protocol::protocol::RolloutItem;`
- `use` `codex-rs/core/src/personality_migration.rs:139` `use codex_protocol::protocol::RolloutLine;`
- `use` `codex-rs/core/src/personality_migration.rs:140` `use codex_protocol::protocol::SessionMeta;`
- `use` `codex-rs/core/src/personality_migration.rs:141` `use codex_protocol::protocol::SessionMetaLine;`
- `use` `codex-rs/core/src/personality_migration.rs:142` `use codex_protocol::protocol::SessionSource;`
- `use` `codex-rs/core/src/personality_migration.rs:143` `use codex_protocol::protocol::UserMessageEvent;`
- `use` `codex-rs/core/src/personality_migration.rs:144` `use pretty_assertions::assert_eq;`
- `use` `codex-rs/core/src/personality_migration.rs:145` `use tempfile::TempDir;`
- `use` `codex-rs/core/src/personality_migration.rs:146` `use tokio::io::AsyncWriteExt;`
- `const` `codex-rs/core/src/personality_migration.rs:148` `const TEST_TIMESTAMP: &str = "2025-01-01T00-00-00";`
- `fn` `codex-rs/core/src/personality_migration.rs:150` `async fn read_config_toml(codex_home: &Path) -> io::Result<ConfigToml> {`
- `fn` `codex-rs/core/src/personality_migration.rs:155` `async fn write_session_with_user_event(codex_home: &Path) -> io::Result<()> {`
- `fn` `codex-rs/core/src/personality_migration.rs:203` `async fn applies_when_sessions_exist_and_no_personality() -> io::Result<()> {`
- `fn` `codex-rs/core/src/personality_migration.rs:219` `async fn skips_when_marker_exists() -> io::Result<()> {`
- `fn` `codex-rs/core/src/personality_migration.rs:232` `async fn skips_when_personality_explicit() -> io::Result<()> {`
- `fn` `codex-rs/core/src/personality_migration.rs:255` `async fn skips_when_no_sessions() -> io::Result<()> {`

## Dependencies (auto sample)
### Imports / Includes
- `use crate::config::ConfigToml;`
- `use crate::config::edit::ConfigEditsBuilder;`
- `use crate::rollout::ARCHIVED_SESSIONS_SUBDIR;`
- `use crate::rollout::SESSIONS_SUBDIR;`
- `use crate::rollout::list::ThreadListConfig;`
- `use crate::rollout::list::ThreadListLayout;`
- `use crate::rollout::list::ThreadSortKey;`
- `use crate::rollout::list::get_threads_in_root;`
- `use crate::state_db;`
- `use codex_protocol::config_types::Personality;`
- `use codex_protocol::protocol::SessionSource;`
- `use std::io;`
- `use std::path::Path;`
- `use tokio::fs::OpenOptions;`
- `use tokio::io::AsyncWriteExt;`
- `use super::*;`
- `use codex_protocol::ThreadId;`
- `use codex_protocol::protocol::EventMsg;`
- `use codex_protocol::protocol::RolloutItem;`
- `use codex_protocol::protocol::RolloutLine;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)

## Spec Links
- `workdocjcl/spec/00_Overview/ARCHITECTURE.md`
