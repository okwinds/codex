# `codex-rs/tui/src/get_git_diff.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `4064`
- sha256: `c321c6800024882f4943ee9c7d693142fd26a455492899c59c47131fea980dfe`
- generated_utc: `2026-02-08T10:45:40Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/tui/src/get_git_diff.rs` (read)

### Outputs / Side Effects
- spawns subprocesses

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `use` `codex-rs/tui/src/get_git_diff.rs:8` `use std::io;`
- `use` `codex-rs/tui/src/get_git_diff.rs:9` `use std::path::Path;`
- `use` `codex-rs/tui/src/get_git_diff.rs:10` `use std::process::Stdio;`
- `use` `codex-rs/tui/src/get_git_diff.rs:11` `use tokio::process::Command;`
- `fn` `codex-rs/tui/src/get_git_diff.rs:66` `async fn run_git_capture_stdout(args: &[&str]) -> io::Result<String> {`
- `fn` `codex-rs/tui/src/get_git_diff.rs:86` `async fn run_git_capture_diff(args: &[&str]) -> io::Result<String> {`
- `fn` `codex-rs/tui/src/get_git_diff.rs:105` `async fn inside_git_repo() -> io::Result<bool> {`

## Dependencies (auto sample)
### Imports / Includes
- `use std::io;`
- `use std::path::Path;`
- `use std::process::Stdio;`
- `use tokio::process::Command;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)

## Spec Links
- `docs/workdocjcl/spec/06_UI/TUI.md`
