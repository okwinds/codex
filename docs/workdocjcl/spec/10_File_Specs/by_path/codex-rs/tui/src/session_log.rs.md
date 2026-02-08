# `codex-rs/tui/src/session_log.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `5790`
- sha256: `9ca46cad1a1aaff0d31aeb1a39f564298add10595c10f40fb8fe41217e1f03c9`
- generated_utc: `2026-02-03T16:08:30Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/tui/src/session_log.rs` (read)
- env: `CODEX_TUI_RECORD_SESSION`, `CODEX_TUI_SESSION_LOG_PATH`

### Outputs / Side Effects
- writes to filesystem

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `use` `codex-rs/tui/src/session_log.rs:1` `use std::fs::File;`
- `use` `codex-rs/tui/src/session_log.rs:2` `use std::fs::OpenOptions;`
- `use` `codex-rs/tui/src/session_log.rs:3` `use std::io::Write;`
- `use` `codex-rs/tui/src/session_log.rs:4` `use std::path::PathBuf;`
- `use` `codex-rs/tui/src/session_log.rs:5` `use std::sync::LazyLock;`
- `use` `codex-rs/tui/src/session_log.rs:6` `use std::sync::Mutex;`
- `use` `codex-rs/tui/src/session_log.rs:7` `use std::sync::OnceLock;`
- `use` `codex-rs/tui/src/session_log.rs:9` `use codex_core::config::Config;`
- `use` `codex-rs/tui/src/session_log.rs:10` `use codex_core::protocol::Op;`
- `use` `codex-rs/tui/src/session_log.rs:11` `use serde::Serialize;`
- `use` `codex-rs/tui/src/session_log.rs:12` `use serde_json::json;`
- `use` `codex-rs/tui/src/session_log.rs:14` `use crate::app_event::AppEvent;`
- `static` `codex-rs/tui/src/session_log.rs:16` `static LOGGER: LazyLock<SessionLogger> = LazyLock::new(SessionLogger::new);`
- `struct` `codex-rs/tui/src/session_log.rs:18` `struct SessionLogger {`
- `impl` `codex-rs/tui/src/session_log.rs:22` `impl SessionLogger {`
- `fn` `codex-rs/tui/src/session_log.rs:23` `fn new() -> Self {`
- `fn` `codex-rs/tui/src/session_log.rs:29` `fn open(&self, path: PathBuf) -> std::io::Result<()> {`
- `use` `codex-rs/tui/src/session_log.rs:35` `use std::os::unix::fs::OpenOptionsExt;`
- `fn` `codex-rs/tui/src/session_log.rs:44` `fn write_json_line(&self, value: serde_json::Value) {`
- `fn` `codex-rs/tui/src/session_log.rs:70` `fn is_enabled(&self) -> bool {`
- `fn` `codex-rs/tui/src/session_log.rs:75` `fn now_ts() -> String {`

## Dependencies (auto sample)
### Imports / Includes
- `use std::fs::File;`
- `use std::fs::OpenOptions;`
- `use std::io::Write;`
- `use std::path::PathBuf;`
- `use std::sync::LazyLock;`
- `use std::sync::Mutex;`
- `use std::sync::OnceLock;`
- `use codex_core::config::Config;`
- `use codex_core::protocol::Op;`
- `use serde::Serialize;`
- `use serde_json::json;`
- `use crate::app_event::AppEvent;`
- `use std::os::unix::fs::OpenOptionsExt;`
### Referenced env vars
- `CODEX_TUI_RECORD_SESSION`
- `CODEX_TUI_SESSION_LOG_PATH`

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)

## Spec Links
- `workdocjcl/spec/06_UI/TUI.md`
