# `codex-rs/tui/src/tooltips.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `10632`
- sha256: `2ff615467ed4493e55c55f9f01eeda581b12d39472528eec6ba9937abd69d903`
- generated_utc: `2026-02-08T10:45:40Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/tui/src/tooltips.rs` (read)

### Outputs / Side Effects
- performs network I/O
- spawns subprocesses

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `use` `codex-rs/tui/src/tooltips.rs:1` `use codex_core::features::FEATURES;`
- `use` `codex-rs/tui/src/tooltips.rs:2` `use codex_protocol::account::PlanType;`
- `use` `codex-rs/tui/src/tooltips.rs:3` `use lazy_static::lazy_static;`
- `use` `codex-rs/tui/src/tooltips.rs:4` `use rand::Rng;`
- `const` `codex-rs/tui/src/tooltips.rs:6` `const ANNOUNCEMENT_TIP_URL: &str =`
- `const` `codex-rs/tui/src/tooltips.rs:9` `const IS_MACOS: bool = cfg!(target_os = "macos");`
- `const` `codex-rs/tui/src/tooltips.rs:11` `const PAID_TOOLTIP: &str = "*New* Try the **Codex App** with 2x rate limits until *April 2nd*. Run 'codex app' or visit https://chatgpt.com/codex";`
- `const` `codex-rs/tui/src/tooltips.rs:12` `const PAID_TOOLTIP_NON_MAC: &str = "*New* 2x rate limits until *April 2nd*.";`
- `const` `codex-rs/tui/src/tooltips.rs:13` `const OTHER_TOOLTIP: &str =`
- `const` `codex-rs/tui/src/tooltips.rs:15` `const OTHER_TOOLTIP_NON_MAC: &str = "*New* Build faster with Codex.";`
- `const` `codex-rs/tui/src/tooltips.rs:16` `const FREE_GO_TOOLTIP: &str =`
- `const` `codex-rs/tui/src/tooltips.rs:19` `const RAW_TOOLTIPS: &str = include_str!("../tooltips.txt");`
- `static` `codex-rs/tui/src/tooltips.rs:22` `static ref TOOLTIPS: Vec<&'static str> = RAW_TOOLTIPS`
- `static` `codex-rs/tui/src/tooltips.rs:35` `static ref ALL_TOOLTIPS: Vec<&'static str> = {`
- `fn` `codex-rs/tui/src/tooltips.rs:43` `fn experimental_tooltips() -> Vec<&'static str> {`
- `use` `codex-rs/tui/src/tooltips.rs:101` `use crate::tooltips::ANNOUNCEMENT_TIP_URL;`
- `use` `codex-rs/tui/src/tooltips.rs:102` `use crate::version::CODEX_CLI_VERSION;`
- `use` `codex-rs/tui/src/tooltips.rs:103` `use chrono::NaiveDate;`
- `use` `codex-rs/tui/src/tooltips.rs:104` `use chrono::Utc;`
- `use` `codex-rs/tui/src/tooltips.rs:105` `use regex_lite::Regex;`
- `use` `codex-rs/tui/src/tooltips.rs:106` `use serde::Deserialize;`
- `use` `codex-rs/tui/src/tooltips.rs:107` `use std::sync::OnceLock;`
- `use` `codex-rs/tui/src/tooltips.rs:108` `use std::thread;`
- `use` `codex-rs/tui/src/tooltips.rs:109` `use std::time::Duration;`
- `static` `codex-rs/tui/src/tooltips.rs:111` `static ANNOUNCEMENT_TIP: OnceLock<Option<String>> = OnceLock::new();`
- `struct` `codex-rs/tui/src/tooltips.rs:128` `struct AnnouncementTipRaw {`
- `struct` `codex-rs/tui/src/tooltips.rs:137` `struct AnnouncementTipDocument {`
- `struct` `codex-rs/tui/src/tooltips.rs:142` `struct AnnouncementTip {`
- `fn` `codex-rs/tui/src/tooltips.rs:150` `fn init_announcement_tip_in_thread() -> Option<String> {`
- `fn` `codex-rs/tui/src/tooltips.rs:157` `fn blocking_init_announcement_tip() -> Option<String> {`
- `impl` `codex-rs/tui/src/tooltips.rs:193` `impl AnnouncementTip {`
- `fn` `codex-rs/tui/src/tooltips.rs:194` `fn from_raw(raw: AnnouncementTipRaw) -> Option<Self> {`
- `fn` `codex-rs/tui/src/tooltips.rs:222` `fn version_matches(&self, version: &str) -> bool {`
- `fn` `codex-rs/tui/src/tooltips.rs:228` `fn date_matches(&self, today: NaiveDate) -> bool {`
- `use` `codex-rs/tui/src/tooltips.rs:246` `use super::*;`
- `use` `codex-rs/tui/src/tooltips.rs:247` `use crate::tooltips::announcement::parse_announcement_tip_toml;`
- `use` `codex-rs/tui/src/tooltips.rs:248` `use rand::SeedableRng;`
- `use` `codex-rs/tui/src/tooltips.rs:249` `use rand::rngs::StdRng;`
- `fn` `codex-rs/tui/src/tooltips.rs:252` `fn random_tooltip_returns_some_tip_when_available() {`
- `fn` `codex-rs/tui/src/tooltips.rs:258` `fn random_tooltip_is_reproducible_with_seed() {`
- `fn` `codex-rs/tui/src/tooltips.rs:269` `fn announcement_tip_toml_picks_last_matching() {`
- `fn` `codex-rs/tui/src/tooltips.rs:312` `fn announcement_tip_toml_picks_no_match() {`
- `fn` `codex-rs/tui/src/tooltips.rs:332` `fn announcement_tip_toml_bad_deserialization() {`
- `fn` `codex-rs/tui/src/tooltips.rs:343` `fn announcement_tip_toml_parse_comments() {`

## Dependencies (auto sample)
### Imports / Includes
- `use codex_core::features::FEATURES;`
- `use codex_protocol::account::PlanType;`
- `use lazy_static::lazy_static;`
- `use rand::Rng;`
- `use crate::tooltips::ANNOUNCEMENT_TIP_URL;`
- `use crate::version::CODEX_CLI_VERSION;`
- `use chrono::NaiveDate;`
- `use chrono::Utc;`
- `use regex_lite::Regex;`
- `use serde::Deserialize;`
- `use std::sync::OnceLock;`
- `use std::thread;`
- `use std::time::Duration;`
- `use super::*;`
- `use crate::tooltips::announcement::parse_announcement_tip_toml;`
- `use rand::SeedableRng;`
- `use rand::rngs::StdRng;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- has retry/timeout/backoff logic

## Spec Links
- `docs/workdocjcl/spec/06_UI/TUI.md`
