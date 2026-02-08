# `codex-rs/cloud-tasks/src/env_detect.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `13060`
- sha256: `86d5940f9695aeeedf287fe99701b4afd144426f3d2ad5a8866bcc29efa145f7`
- generated_utc: `2026-02-03T16:08:29Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/cloud-tasks/src/env_detect.rs` (read)

### Outputs / Side Effects
- performs network I/O
- spawns subprocesses

## Public Surface (auto)
- `pub struct AutodetectSelection {`

## Definitions (auto, per-file)
- `use` `codex-rs/cloud-tasks/src/env_detect.rs:1` `use reqwest::header::CONTENT_TYPE;`
- `use` `codex-rs/cloud-tasks/src/env_detect.rs:2` `use reqwest::header::HeaderMap;`
- `use` `codex-rs/cloud-tasks/src/env_detect.rs:3` `use std::collections::HashMap;`
- `use` `codex-rs/cloud-tasks/src/env_detect.rs:4` `use tracing::info;`
- `use` `codex-rs/cloud-tasks/src/env_detect.rs:5` `use tracing::warn;`
- `struct` `codex-rs/cloud-tasks/src/env_detect.rs:8` `struct CodeEnvironment {`
- `struct` `codex-rs/cloud-tasks/src/env_detect.rs:19` `pub struct AutodetectSelection {`
- `fn` `codex-rs/cloud-tasks/src/env_detect.rs:24` `pub async fn autodetect_environment_id(`
- `fn` `codex-rs/cloud-tasks/src/env_detect.rs:109` `fn pick_environment_row(`
- `fn` `codex-rs/cloud-tasks/src/env_detect.rs:170` `fn get_git_origins() -> Vec<String> {`
- `fn` `codex-rs/cloud-tasks/src/env_detect.rs:211` `fn uniq(mut v: Vec<String>) -> Vec<String> {`
- `fn` `codex-rs/cloud-tasks/src/env_detect.rs:217` `fn parse_owner_repo(url: &str) -> Option<(String, String)> {`
- `fn` `codex-rs/cloud-tasks/src/env_detect.rs:255` `pub async fn list_environments(`

## Dependencies (auto sample)
### Imports / Includes
- `use reqwest::header::CONTENT_TYPE;`
- `use reqwest::header::HeaderMap;`
- `use std::collections::HashMap;`
- `use tracing::info;`
- `use tracing::warn;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
