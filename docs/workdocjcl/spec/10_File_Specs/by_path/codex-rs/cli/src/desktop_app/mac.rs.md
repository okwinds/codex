# `codex-rs/cli/src/desktop_app/mac.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `8448`
- sha256: `5d25d18f7fd97ed78e88a2b447e32ca52068602035e1299b11f8db818f385a77`
- generated_utc: `2026-02-08T10:45:16Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/cli/src/desktop_app/mac.rs` (read)
- env: `HOME`

### Outputs / Side Effects
- spawns subprocesses
- writes to filesystem
- writes to stdout/stderr

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `use` `codex-rs/cli/src/desktop_app/mac.rs:1` `use anyhow::Context as _;`
- `use` `codex-rs/cli/src/desktop_app/mac.rs:2` `use std::path::Path;`
- `use` `codex-rs/cli/src/desktop_app/mac.rs:3` `use std::path::PathBuf;`
- `use` `codex-rs/cli/src/desktop_app/mac.rs:4` `use tempfile::Builder;`
- `use` `codex-rs/cli/src/desktop_app/mac.rs:5` `use tokio::process::Command;`
- `fn` `codex-rs/cli/src/desktop_app/mac.rs:7` `pub async fn run_mac_app_open_or_install(`
- `fn` `codex-rs/cli/src/desktop_app/mac.rs:31` `fn find_existing_codex_app_path() -> Option<PathBuf> {`
- `fn` `codex-rs/cli/src/desktop_app/mac.rs:37` `fn candidate_codex_app_paths() -> Vec<PathBuf> {`
- `fn` `codex-rs/cli/src/desktop_app/mac.rs:45` `async fn open_codex_app(app_path: &Path, workspace: &Path) -> anyhow::Result<()> {`
- `fn` `codex-rs/cli/src/desktop_app/mac.rs:69` `async fn download_and_install_codex_to_user_applications(dmg_url: &str) -> anyhow::Result<PathBuf> {`
- `fn` `codex-rs/cli/src/desktop_app/mac.rs:104` `async fn install_codex_app_bundle(app_in_volume: &Path) -> anyhow::Result<PathBuf> {`
- `fn` `codex-rs/cli/src/desktop_app/mac.rs:136` `fn candidate_applications_dirs() -> anyhow::Result<Vec<PathBuf>> {`
- `fn` `codex-rs/cli/src/desktop_app/mac.rs:142` `async fn download_dmg(url: &str, dest: &Path) -> anyhow::Result<()> {`
- `fn` `codex-rs/cli/src/desktop_app/mac.rs:163` `async fn mount_dmg(dmg_path: &Path) -> anyhow::Result<PathBuf> {`
- `fn` `codex-rs/cli/src/desktop_app/mac.rs:187` `async fn detach_dmg(mount_point: &Path) -> anyhow::Result<()> {`
- `fn` `codex-rs/cli/src/desktop_app/mac.rs:201` `fn find_codex_app_in_mount(mount_point: &Path) -> anyhow::Result<PathBuf> {`
- `fn` `codex-rs/cli/src/desktop_app/mac.rs:226` `async fn copy_app_bundle(src_app: &Path, dest_app: &Path) -> anyhow::Result<()> {`
- `fn` `codex-rs/cli/src/desktop_app/mac.rs:240` `fn user_applications_dir() -> anyhow::Result<PathBuf> {`
- `fn` `codex-rs/cli/src/desktop_app/mac.rs:245` `fn parse_hdiutil_attach_mount_point(output: &str) -> Option<String> {`
- `use` `codex-rs/cli/src/desktop_app/mac.rs:261` `use super::parse_hdiutil_attach_mount_point;`
- `use` `codex-rs/cli/src/desktop_app/mac.rs:262` `use pretty_assertions::assert_eq;`
- `fn` `codex-rs/cli/src/desktop_app/mac.rs:265` `fn parses_mount_point_from_tab_separated_hdiutil_output() {`
- `fn` `codex-rs/cli/src/desktop_app/mac.rs:274` `fn parses_mount_point_with_spaces() {`

## Dependencies (auto sample)
### Imports / Includes
- `use anyhow::Context as _;`
- `use std::path::Path;`
- `use std::path::PathBuf;`
- `use tempfile::Builder;`
- `use tokio::process::Command;`
- `use super::parse_hdiutil_attach_mount_point;`
- `use pretty_assertions::assert_eq;`
### Referenced env vars
- `HOME`

## Error Handling / Edge Cases
- has retry/timeout/backoff logic
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- `docs/workdocjcl/spec/03_API/CLI.md`
