# `codex-rs/state/src/bin/logs_client.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `9107`
- sha256: `f729260760327b6e40a7e959431753014be9724b7acc6315b6619d0b42d5ccee`
- generated_utc: `2026-02-03T16:08:30Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/state/src/bin/logs_client.rs` (read)

### Outputs / Side Effects
- writes to stdout/stderr

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `use` `codex-rs/state/src/bin/logs_client.rs:1` `use std::path::PathBuf;`
- `use` `codex-rs/state/src/bin/logs_client.rs:2` `use std::time::Duration;`
- `use` `codex-rs/state/src/bin/logs_client.rs:4` `use anyhow::Context;`
- `use` `codex-rs/state/src/bin/logs_client.rs:5` `use chrono::DateTime;`
- `use` `codex-rs/state/src/bin/logs_client.rs:6` `use clap::Parser;`
- `use` `codex-rs/state/src/bin/logs_client.rs:7` `use codex_state::LogQuery;`
- `use` `codex-rs/state/src/bin/logs_client.rs:8` `use codex_state::LogRow;`
- `use` `codex-rs/state/src/bin/logs_client.rs:9` `use codex_state::STATE_DB_FILENAME;`
- `use` `codex-rs/state/src/bin/logs_client.rs:10` `use codex_state::StateRuntime;`
- `use` `codex-rs/state/src/bin/logs_client.rs:11` `use dirs::home_dir;`
- `use` `codex-rs/state/src/bin/logs_client.rs:12` `use owo_colors::OwoColorize;`
- `struct` `codex-rs/state/src/bin/logs_client.rs:17` `struct Args {`
- `struct` `codex-rs/state/src/bin/logs_client.rs:64` `struct LogFilter {`
- `fn` `codex-rs/state/src/bin/logs_client.rs:75` `async fn main() -> anyhow::Result<()> {`
- `fn` `codex-rs/state/src/bin/logs_client.rs:101` `fn resolve_db_path(args: &Args) -> anyhow::Result<PathBuf> {`
- `fn` `codex-rs/state/src/bin/logs_client.rs:110` `fn default_codex_home() -> PathBuf {`
- `fn` `codex-rs/state/src/bin/logs_client.rs:117` `fn build_filter(args: &Args) -> anyhow::Result<LogFilter> {`
- `fn` `codex-rs/state/src/bin/logs_client.rs:162` `fn parse_timestamp(value: &str) -> anyhow::Result<i64> {`
- `fn` `codex-rs/state/src/bin/logs_client.rs:172` `async fn print_backfill(`
- `fn` `codex-rs/state/src/bin/logs_client.rs:192` `async fn fetch_backfill(`
- `fn` `codex-rs/state/src/bin/logs_client.rs:204` `async fn fetch_new_rows(`
- `fn` `codex-rs/state/src/bin/logs_client.rs:216` `async fn fetch_max_id(runtime: &StateRuntime, filter: &LogFilter) -> anyhow::Result<i64> {`
- `fn` `codex-rs/state/src/bin/logs_client.rs:224` `fn to_log_query(`
- `fn` `codex-rs/state/src/bin/logs_client.rs:244` `fn format_row(row: &LogRow) -> String {`
- `fn` `codex-rs/state/src/bin/logs_client.rs:260` `fn heuristic_formatting(message: &str) -> String {`
- `use` `codex-rs/state/src/bin/logs_client.rs:275` `use chrono::DateTime;`
- `use` `codex-rs/state/src/bin/logs_client.rs:276` `use chrono::SecondsFormat;`
- `use` `codex-rs/state/src/bin/logs_client.rs:277` `use chrono::Utc;`
- `use` `codex-rs/state/src/bin/logs_client.rs:278` `use owo_colors::OwoColorize;`

## Dependencies (auto sample)
### Imports / Includes
- `use std::path::PathBuf;`
- `use std::time::Duration;`
- `use anyhow::Context;`
- `use chrono::DateTime;`
- `use clap::Parser;`
- `use codex_state::LogQuery;`
- `use codex_state::LogRow;`
- `use codex_state::STATE_DB_FILENAME;`
- `use codex_state::StateRuntime;`
- `use dirs::home_dir;`
- `use owo_colors::OwoColorize;`
- `use chrono::DateTime;`
- `use chrono::SecondsFormat;`
- `use chrono::Utc;`
- `use owo_colors::OwoColorize;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)

## Spec Links
- `workdocjcl/spec/02_Data/ENTITIES.md`
