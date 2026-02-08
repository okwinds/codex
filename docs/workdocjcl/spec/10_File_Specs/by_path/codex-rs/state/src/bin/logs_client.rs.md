# `codex-rs/state/src/bin/logs_client.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `9092`
- sha256: `b355b0392ea2113c4f8a62f5b418333e0efad470a1f8548340649abd8735f16c`
- generated_utc: `2026-02-08T10:45:38Z`

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
- `use` `codex-rs/state/src/bin/logs_client.rs:9` `use codex_state::StateRuntime;`
- `use` `codex-rs/state/src/bin/logs_client.rs:10` `use dirs::home_dir;`
- `use` `codex-rs/state/src/bin/logs_client.rs:11` `use owo_colors::OwoColorize;`
- `struct` `codex-rs/state/src/bin/logs_client.rs:16` `struct Args {`
- `struct` `codex-rs/state/src/bin/logs_client.rs:63` `struct LogFilter {`
- `fn` `codex-rs/state/src/bin/logs_client.rs:74` `async fn main() -> anyhow::Result<()> {`
- `fn` `codex-rs/state/src/bin/logs_client.rs:100` `fn resolve_db_path(args: &Args) -> anyhow::Result<PathBuf> {`
- `fn` `codex-rs/state/src/bin/logs_client.rs:109` `fn default_codex_home() -> PathBuf {`
- `fn` `codex-rs/state/src/bin/logs_client.rs:116` `fn build_filter(args: &Args) -> anyhow::Result<LogFilter> {`
- `fn` `codex-rs/state/src/bin/logs_client.rs:161` `fn parse_timestamp(value: &str) -> anyhow::Result<i64> {`
- `fn` `codex-rs/state/src/bin/logs_client.rs:171` `async fn print_backfill(`
- `fn` `codex-rs/state/src/bin/logs_client.rs:191` `async fn fetch_backfill(`
- `fn` `codex-rs/state/src/bin/logs_client.rs:203` `async fn fetch_new_rows(`
- `fn` `codex-rs/state/src/bin/logs_client.rs:215` `async fn fetch_max_id(runtime: &StateRuntime, filter: &LogFilter) -> anyhow::Result<i64> {`
- `fn` `codex-rs/state/src/bin/logs_client.rs:223` `fn to_log_query(`
- `fn` `codex-rs/state/src/bin/logs_client.rs:243` `fn format_row(row: &LogRow) -> String {`
- `fn` `codex-rs/state/src/bin/logs_client.rs:259` `fn heuristic_formatting(message: &str) -> String {`
- `use` `codex-rs/state/src/bin/logs_client.rs:274` `use chrono::DateTime;`
- `use` `codex-rs/state/src/bin/logs_client.rs:275` `use chrono::SecondsFormat;`
- `use` `codex-rs/state/src/bin/logs_client.rs:276` `use chrono::Utc;`
- `use` `codex-rs/state/src/bin/logs_client.rs:277` `use owo_colors::OwoColorize;`

## Dependencies (auto sample)
### Imports / Includes
- `use std::path::PathBuf;`
- `use std::time::Duration;`
- `use anyhow::Context;`
- `use chrono::DateTime;`
- `use clap::Parser;`
- `use codex_state::LogQuery;`
- `use codex_state::LogRow;`
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
- `docs/workdocjcl/spec/02_Data/ENTITIES.md`
