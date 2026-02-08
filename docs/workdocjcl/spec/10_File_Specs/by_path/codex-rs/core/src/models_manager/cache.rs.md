# `codex-rs/core/src/models_manager/cache.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `5060`
- sha256: `69d39cf1eab58de1e04e9aa8c5cf2c1093227e7297105d93722d40d93d9ef423`
- generated_utc: `2026-02-03T16:08:29Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/models_manager/cache.rs` (read)

### Outputs / Side Effects
- writes to filesystem

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `use` `codex-rs/core/src/models_manager/cache.rs:1` `use chrono::DateTime;`
- `use` `codex-rs/core/src/models_manager/cache.rs:2` `use chrono::Utc;`
- `use` `codex-rs/core/src/models_manager/cache.rs:3` `use codex_protocol::openai_models::ModelInfo;`
- `use` `codex-rs/core/src/models_manager/cache.rs:4` `use serde::Deserialize;`
- `use` `codex-rs/core/src/models_manager/cache.rs:5` `use serde::Serialize;`
- `use` `codex-rs/core/src/models_manager/cache.rs:6` `use std::io;`
- `use` `codex-rs/core/src/models_manager/cache.rs:7` `use std::io::ErrorKind;`
- `use` `codex-rs/core/src/models_manager/cache.rs:8` `use std::path::PathBuf;`
- `use` `codex-rs/core/src/models_manager/cache.rs:9` `use std::time::Duration;`
- `use` `codex-rs/core/src/models_manager/cache.rs:10` `use tokio::fs;`
- `use` `codex-rs/core/src/models_manager/cache.rs:11` `use tracing::error;`
- `impl` `codex-rs/core/src/models_manager/cache.rs:20` `impl ModelsCacheManager {`
- `fn` `codex-rs/core/src/models_manager/cache.rs:75` `async fn load(&self) -> io::Result<Option<ModelsCache>> {`
- `fn` `codex-rs/core/src/models_manager/cache.rs:87` `async fn save_internal(&self, cache: &ModelsCache) -> io::Result<()> {`
- `impl` `codex-rs/core/src/models_manager/cache.rs:142` `impl ModelsCache {`
- `fn` `codex-rs/core/src/models_manager/cache.rs:144` `fn is_fresh(&self, ttl: Duration) -> bool {`

## Dependencies (auto sample)
### Imports / Includes
- `use chrono::DateTime;`
- `use chrono::Utc;`
- `use codex_protocol::openai_models::ModelInfo;`
- `use serde::Deserialize;`
- `use serde::Serialize;`
- `use std::io;`
- `use std::io::ErrorKind;`
- `use std::path::PathBuf;`
- `use std::time::Duration;`
- `use tokio::fs;`
- `use tracing::error;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)

## Spec Links
- `workdocjcl/spec/00_Overview/ARCHITECTURE.md`
