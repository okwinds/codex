# `codex-rs/core/tests/suite/personality_migration.rs`

## Identity
- kind: `test`
- ext: `.rs`
- size_bytes: `11289`
- sha256: `640a3cadfd7bba6be7339c993a90efb4c564b96c832fcd9c00f03031ac0d013f`
- generated_utc: `2026-02-08T10:45:36Z`

## Purpose (Why)
Test or snapshot file used for automated verification.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/tests/suite/personality_migration.rs` (read)

### Outputs / Side Effects
- none (file is declarative: doc/config/test/asset)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- (not extracted)

## Dependencies (auto sample)
### Imports / Includes
- `use codex_core::ARCHIVED_SESSIONS_SUBDIR;`
- `use codex_core::SESSIONS_SUBDIR;`
- `use codex_core::config::ConfigToml;`
- `use codex_core::personality_migration::PERSONALITY_MIGRATION_FILENAME;`
- `use codex_core::personality_migration::PersonalityMigrationStatus;`
- `use codex_core::personality_migration::maybe_migrate_personality;`
- `use codex_protocol::ThreadId;`
- `use codex_protocol::config_types::Personality;`
- `use codex_protocol::protocol::EventMsg;`
- `use codex_protocol::protocol::RolloutItem;`
- `use codex_protocol::protocol::RolloutLine;`
- `use codex_protocol::protocol::SessionMeta;`
- `use codex_protocol::protocol::SessionMetaLine;`
- `use codex_protocol::protocol::SessionSource;`
- `use codex_protocol::protocol::UserMessageEvent;`
- `use pretty_assertions::assert_eq;`
- `use std::io;`
- `use std::path::Path;`
- `use tempfile::TempDir;`
- `use tokio::io::AsyncWriteExt;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (none detected)

## Spec Links
- `docs/workdocjcl/spec/00_Overview/ARCHITECTURE.md`
