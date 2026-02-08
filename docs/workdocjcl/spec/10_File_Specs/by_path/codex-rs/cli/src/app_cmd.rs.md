# `codex-rs/cli/src/app_cmd.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `710`
- sha256: `c8983a8f6af4f1919bb4ffaecafb76d1fca43c15c3cff5ce2f806508b2dd0a5f`
- generated_utc: `2026-02-08T10:45:16Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/cli/src/app_cmd.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub struct AppCommand {`

## Definitions (auto, per-file)
- `use` `codex-rs/cli/src/app_cmd.rs:1` `use clap::Parser;`
- `use` `codex-rs/cli/src/app_cmd.rs:2` `use std::path::PathBuf;`
- `const` `codex-rs/cli/src/app_cmd.rs:4` `const DEFAULT_CODEX_DMG_URL: &str = "https://persistent.oaistatic.com/codex-app-prod/Codex.dmg";`
- `struct` `codex-rs/cli/src/app_cmd.rs:7` `pub struct AppCommand {`
- `fn` `codex-rs/cli/src/app_cmd.rs:18` `pub async fn run_app(cmd: AppCommand) -> anyhow::Result<()> {`

## Dependencies (auto sample)
### Imports / Includes
- `use clap::Parser;`
- `use std::path::PathBuf;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)

## Spec Links
- `docs/workdocjcl/spec/03_API/CLI.md`
