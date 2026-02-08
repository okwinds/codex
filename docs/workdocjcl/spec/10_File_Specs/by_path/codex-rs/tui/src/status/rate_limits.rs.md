# `codex-rs/tui/src/status/rate_limits.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `7157`
- sha256: `06b21951ea39161f02c487d8a1ba4f0b6fb248b7be02d3e02240eec6ad44014f`
- generated_utc: `2026-02-03T16:08:30Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/tui/src/status/rate_limits.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `use` `codex-rs/tui/src/status/rate_limits.rs:1` `use crate::chatwidget::get_limits_duration;`
- `use` `codex-rs/tui/src/status/rate_limits.rs:2` `use crate::text_formatting::capitalize_first;`
- `use` `codex-rs/tui/src/status/rate_limits.rs:4` `use super::helpers::format_reset_timestamp;`
- `use` `codex-rs/tui/src/status/rate_limits.rs:5` `use chrono::DateTime;`
- `use` `codex-rs/tui/src/status/rate_limits.rs:6` `use chrono::Duration as ChronoDuration;`
- `use` `codex-rs/tui/src/status/rate_limits.rs:7` `use chrono::Local;`
- `use` `codex-rs/tui/src/status/rate_limits.rs:8` `use chrono::Utc;`
- `use` `codex-rs/tui/src/status/rate_limits.rs:9` `use codex_core::protocol::CreditsSnapshot as CoreCreditsSnapshot;`
- `use` `codex-rs/tui/src/status/rate_limits.rs:10` `use codex_core::protocol::RateLimitSnapshot;`
- `use` `codex-rs/tui/src/status/rate_limits.rs:11` `use codex_core::protocol::RateLimitWindow;`
- `const` `codex-rs/tui/src/status/rate_limits.rs:13` `const STATUS_LIMIT_BAR_SEGMENTS: usize = 20;`
- `const` `codex-rs/tui/src/status/rate_limits.rs:14` `const STATUS_LIMIT_BAR_FILLED: &str = "█";`
- `const` `codex-rs/tui/src/status/rate_limits.rs:15` `const STATUS_LIMIT_BAR_EMPTY: &str = "░";`
- `impl` `codex-rs/tui/src/status/rate_limits.rs:48` `impl RateLimitWindowDisplay {`
- `fn` `codex-rs/tui/src/status/rate_limits.rs:49` `fn from_window(window: &RateLimitWindow, captured_at: DateTime<Local>) -> Self {`
- `impl` `codex-rs/tui/src/status/rate_limits.rs:97` `impl From<&CoreCreditsSnapshot> for CreditsSnapshotDisplay {`
- `fn` `codex-rs/tui/src/status/rate_limits.rs:98` `fn from(value: &CoreCreditsSnapshot) -> Self {`
- `fn` `codex-rs/tui/src/status/rate_limits.rs:186` `fn credit_status_row(credits: &CreditsSnapshotDisplay) -> Option<StatusRateLimitRow> {`
- `fn` `codex-rs/tui/src/status/rate_limits.rs:204` `fn format_credit_balance(raw: &str) -> Option<String> {`

## Dependencies (auto sample)
### Imports / Includes
- `use crate::chatwidget::get_limits_duration;`
- `use crate::text_formatting::capitalize_first;`
- `use super::helpers::format_reset_timestamp;`
- `use chrono::DateTime;`
- `use chrono::Duration as ChronoDuration;`
- `use chrono::Local;`
- `use chrono::Utc;`
- `use codex_core::protocol::CreditsSnapshot as CoreCreditsSnapshot;`
- `use codex_core::protocol::RateLimitSnapshot;`
- `use codex_core::protocol::RateLimitWindow;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- `workdocjcl/spec/06_UI/TUI.md`
