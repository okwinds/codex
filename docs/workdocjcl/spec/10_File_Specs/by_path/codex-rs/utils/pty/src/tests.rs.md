# `codex-rs/utils/pty/src/tests.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `10423`
- sha256: `d7529ef63e13c11675386fd15e7ff88dc57eca511681db501cee12a6412e6da6`
- generated_utc: `2026-02-03T16:08:31Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/utils/pty/src/tests.rs` (read)
- env: `COMSPEC`

### Outputs / Side Effects
- spawns subprocesses
- writes to stdout/stderr

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `use` `codex-rs/utils/pty/src/tests.rs:1` `use std::collections::HashMap;`
- `use` `codex-rs/utils/pty/src/tests.rs:2` `use std::path::Path;`
- `use` `codex-rs/utils/pty/src/tests.rs:4` `use pretty_assertions::assert_eq;`
- `use` `codex-rs/utils/pty/src/tests.rs:6` `use crate::spawn_pipe_process;`
- `use` `codex-rs/utils/pty/src/tests.rs:7` `use crate::spawn_pty_process;`
- `fn` `codex-rs/utils/pty/src/tests.rs:9` `fn find_python() -> Option<String> {`
- `fn` `codex-rs/utils/pty/src/tests.rs:23` `fn setsid_available() -> bool {`
- `fn` `codex-rs/utils/pty/src/tests.rs:34` `fn shell_command(program: &str) -> (String, Vec<String>) {`
- `fn` `codex-rs/utils/pty/src/tests.rs:46` `fn echo_sleep_command(marker: &str) -> String {`
- `fn` `codex-rs/utils/pty/src/tests.rs:54` `async fn collect_output_until_exit(`
- `fn` `codex-rs/utils/pty/src/tests.rs:97` `async fn pty_python_repl_emits_output_and_exits() -> anyhow::Result<()> {`
- `fn` `codex-rs/utils/pty/src/tests.rs:127` `async fn pipe_process_round_trips_stdin() -> anyhow::Result<()> {`
- `fn` `codex-rs/utils/pty/src/tests.rs:157` `async fn pipe_process_detaches_from_parent_session() -> anyhow::Result<()> {`
- `fn` `codex-rs/utils/pty/src/tests.rs:199` `async fn pipe_and_pty_share_interface() -> anyhow::Result<()> {`
- `fn` `codex-rs/utils/pty/src/tests.rs:230` `async fn pipe_drains_stderr_without_stdout_activity() -> anyhow::Result<()> {`
- `fn` `codex-rs/utils/pty/src/tests.rs:251` `async fn pipe_terminate_aborts_detached_readers() -> anyhow::Result<()> {`

## Dependencies (auto sample)
### Imports / Includes
- `use std::collections::HashMap;`
- `use std::path::Path;`
- `use pretty_assertions::assert_eq;`
- `use crate::spawn_pipe_process;`
- `use crate::spawn_pty_process;`
### Referenced env vars
- `COMSPEC`

## Error Handling / Edge Cases
- has retry/timeout/backoff logic
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
