# `codex-rs/utils/pty/src/tests.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `12703`
- sha256: `db2bc3fab295c531952bd6ad8858cdc6d2833d0693849fa60df11c0a6b590ac1`
- generated_utc: `2026-02-08T10:45:41Z`

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
- `fn` `codex-rs/utils/pty/src/tests.rs:96` `async fn wait_for_python_repl_ready(`
- `fn` `codex-rs/utils/pty/src/tests.rs:148` `async fn pty_python_repl_emits_output_and_exits() -> anyhow::Result<()> {`
- `fn` `codex-rs/utils/pty/src/tests.rs:183` `async fn pipe_process_round_trips_stdin() -> anyhow::Result<()> {`
- `fn` `codex-rs/utils/pty/src/tests.rs:213` `async fn pipe_process_detaches_from_parent_session() -> anyhow::Result<()> {`
- `fn` `codex-rs/utils/pty/src/tests.rs:255` `async fn pipe_and_pty_share_interface() -> anyhow::Result<()> {`
- `fn` `codex-rs/utils/pty/src/tests.rs:286` `async fn pipe_drains_stderr_without_stdout_activity() -> anyhow::Result<()> {`
- `fn` `codex-rs/utils/pty/src/tests.rs:307` `async fn pipe_terminate_aborts_detached_readers() -> anyhow::Result<()> {`

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
