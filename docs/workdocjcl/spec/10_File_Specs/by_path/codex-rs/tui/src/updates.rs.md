# `codex-rs/tui/src/updates.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `7633`
- sha256: `85e9d9fe243adfc305b9e799967c52254bb077f16ad9555935d0bdddc2d02771`
- generated_utc: `2026-02-03T16:08:31Z`

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
- `const` `codex-rs/tui/src/updates.rs:59` `const HOMEBREW_CASK_URL: &str =`
- `const` `codex-rs/tui/src/updates.rs:61` `const LATEST_RELEASE_URL: &str = "https://api.github.com/repos/openai/codex/releases/latest";`
- `struct` `codex-rs/tui/src/updates.rs:64` `struct ReleaseInfo {`
- `fn` `codex-rs/tui/src/updates.rs:68` `fn version_filepath(config: &Config) -> PathBuf {`
- `fn` `codex-rs/tui/src/updates.rs:72` `fn read_version_info(version_file: &Path) -> anyhow::Result<VersionInfo> {`
- `fn` `codex-rs/tui/src/updates.rs:77` `async fn check_for_update(version_file: &Path) -> anyhow::Result<()> {`
- `fn` `codex-rs/tui/src/updates.rs:119` `fn is_newer(latest: &str, current: &str) -> Option<bool> {`
- `fn` `codex-rs/tui/src/updates.rs:126` `fn extract_version_from_cask(cask_contents: &str) -> anyhow::Result<String> {`
- `fn` `codex-rs/tui/src/updates.rs:138` `fn extract_version_from_latest_tag(latest_tag_name: &str) -> anyhow::Result<String> {`
- `fn` `codex-rs/tui/src/updates.rs:147` `pub fn get_upgrade_version_for_popup(config: &Config) -> Option<String> {`
- `fn` `codex-rs/tui/src/updates.rs:165` `pub async fn dismiss_version(config: &Config, version: &str) -> anyhow::Result<()> {`
- `fn` `codex-rs/tui/src/updates.rs:180` `fn parse_version(v: &str) -> Option<(u64, u64, u64)> {`
- `use` `codex-rs/tui/src/updates.rs:190` `use super::*;`
- `fn` `codex-rs/tui/src/updates.rs:193` `fn parses_version_from_cask_contents() {`
- `fn` `codex-rs/tui/src/updates.rs:206` `fn extracts_version_from_latest_tag() {`
- `fn` `codex-rs/tui/src/updates.rs:214` `fn latest_tag_without_prefix_is_invalid() {`
- `fn` `codex-rs/tui/src/updates.rs:219` `fn prerelease_version_is_not_considered_newer() {`
- `fn` `codex-rs/tui/src/updates.rs:225` `fn plain_semver_comparisons_work() {`
- `fn` `codex-rs/tui/src/updates.rs:233` `fn whitespace_is_ignored() {`

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
- `workdocjcl/spec/06_UI/TUI.md`
