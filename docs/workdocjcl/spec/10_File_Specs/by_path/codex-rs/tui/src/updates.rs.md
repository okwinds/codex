# `codex-rs/tui/src/updates.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `7469`
- sha256: `5e29075bcd5e7a0684da9e127655f7d7e9172b6743b2fac0285e6897a09cf603`
- generated_utc: `2026-02-08T10:45:41Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/tui/src/updates.rs` (read)

### Outputs / Side Effects
- spawns subprocesses
- writes to filesystem

## Public Surface (auto)
- `pub fn get_upgrade_version(config: &Config) -> Option<String> {`
- `pub fn get_upgrade_version_for_popup(config: &Config) -> Option<String> {`

## Definitions (auto, per-file)
- `use` `codex-rs/tui/src/updates.rs:3` `use crate::update_action;`
- `use` `codex-rs/tui/src/updates.rs:4` `use crate::update_action::UpdateAction;`
- `use` `codex-rs/tui/src/updates.rs:5` `use chrono::DateTime;`
- `use` `codex-rs/tui/src/updates.rs:6` `use chrono::Duration;`
- `use` `codex-rs/tui/src/updates.rs:7` `use chrono::Utc;`
- `use` `codex-rs/tui/src/updates.rs:8` `use codex_core::config::Config;`
- `use` `codex-rs/tui/src/updates.rs:9` `use codex_core::default_client::create_client;`
- `use` `codex-rs/tui/src/updates.rs:10` `use serde::Deserialize;`
- `use` `codex-rs/tui/src/updates.rs:11` `use serde::Serialize;`
- `use` `codex-rs/tui/src/updates.rs:12` `use std::path::Path;`
- `use` `codex-rs/tui/src/updates.rs:13` `use std::path::PathBuf;`
- `use` `codex-rs/tui/src/updates.rs:15` `use crate::version::CODEX_CLI_VERSION;`
- `fn` `codex-rs/tui/src/updates.rs:17` `pub fn get_upgrade_version(config: &Config) -> Option<String> {`
- `struct` `codex-rs/tui/src/updates.rs:49` `struct VersionInfo {`
- `const` `codex-rs/tui/src/updates.rs:57` `const VERSION_FILENAME: &str = "version.json";`
- `const` `codex-rs/tui/src/updates.rs:59` `const HOMEBREW_CASK_API_URL: &str = "https://formulae.brew.sh/api/cask/codex.json";`
- `const` `codex-rs/tui/src/updates.rs:60` `const LATEST_RELEASE_URL: &str = "https://api.github.com/repos/openai/codex/releases/latest";`
- `struct` `codex-rs/tui/src/updates.rs:63` `struct ReleaseInfo {`
- `struct` `codex-rs/tui/src/updates.rs:68` `struct HomebrewCaskInfo {`
- `fn` `codex-rs/tui/src/updates.rs:72` `fn version_filepath(config: &Config) -> PathBuf {`
- `fn` `codex-rs/tui/src/updates.rs:76` `fn read_version_info(version_file: &Path) -> anyhow::Result<VersionInfo> {`
- `fn` `codex-rs/tui/src/updates.rs:81` `async fn check_for_update(version_file: &Path) -> anyhow::Result<()> {`
- `fn` `codex-rs/tui/src/updates.rs:123` `fn is_newer(latest: &str, current: &str) -> Option<bool> {`
- `fn` `codex-rs/tui/src/updates.rs:130` `fn extract_version_from_latest_tag(latest_tag_name: &str) -> anyhow::Result<String> {`
- `fn` `codex-rs/tui/src/updates.rs:139` `pub fn get_upgrade_version_for_popup(config: &Config) -> Option<String> {`
- `fn` `codex-rs/tui/src/updates.rs:157` `pub async fn dismiss_version(config: &Config, version: &str) -> anyhow::Result<()> {`
- `fn` `codex-rs/tui/src/updates.rs:172` `fn parse_version(v: &str) -> Option<(u64, u64, u64)> {`
- `use` `codex-rs/tui/src/updates.rs:182` `use super::*;`
- `fn` `codex-rs/tui/src/updates.rs:185` `fn extract_version_from_brew_api_json() {`
- `fn` `codex-rs/tui/src/updates.rs:200` `fn extracts_version_from_latest_tag() {`
- `fn` `codex-rs/tui/src/updates.rs:208` `fn latest_tag_without_prefix_is_invalid() {`
- `fn` `codex-rs/tui/src/updates.rs:213` `fn prerelease_version_is_not_considered_newer() {`
- `fn` `codex-rs/tui/src/updates.rs:219` `fn plain_semver_comparisons_work() {`
- `fn` `codex-rs/tui/src/updates.rs:227` `fn whitespace_is_ignored() {`

## Dependencies (auto sample)
### Imports / Includes
- `use crate::update_action;`
- `use crate::update_action::UpdateAction;`
- `use chrono::DateTime;`
- `use chrono::Duration;`
- `use chrono::Utc;`
- `use codex_core::config::Config;`
- `use codex_core::default_client::create_client;`
- `use serde::Deserialize;`
- `use serde::Serialize;`
- `use std::path::Path;`
- `use std::path::PathBuf;`
- `use crate::version::CODEX_CLI_VERSION;`
- `use super::*;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- `docs/workdocjcl/spec/06_UI/TUI.md`
