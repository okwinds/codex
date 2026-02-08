# `codex-rs/tui/src/status/rate_limits.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `9870`
- sha256: `955f8d4ab91038b85196dfdc64ec8ca778e9e4fbe1d2b613fd0414c145c2ba0d`
- generated_utc: `2026-02-08T10:45:40Z`

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
- `use` `codex-rs/tui/src/status/rate_limits.rs:8` `use crate::chatwidget::get_limits_duration;`
- `use` `codex-rs/tui/src/status/rate_limits.rs:9` `use crate::text_formatting::capitalize_first;`
- `use` `codex-rs/tui/src/status/rate_limits.rs:11` `use super::helpers::format_reset_timestamp;`
- `use` `codex-rs/tui/src/status/rate_limits.rs:12` `use chrono::DateTime;`
- `use` `codex-rs/tui/src/status/rate_limits.rs:13` `use chrono::Duration as ChronoDuration;`
- `use` `codex-rs/tui/src/status/rate_limits.rs:14` `use chrono::Local;`
- `use` `codex-rs/tui/src/status/rate_limits.rs:15` `use chrono::Utc;`
- `use` `codex-rs/tui/src/status/rate_limits.rs:16` `use codex_core::protocol::CreditsSnapshot as CoreCreditsSnapshot;`
- `use` `codex-rs/tui/src/status/rate_limits.rs:17` `use codex_core::protocol::RateLimitSnapshot;`
- `use` `codex-rs/tui/src/status/rate_limits.rs:18` `use codex_core::protocol::RateLimitWindow;`
- `const` `codex-rs/tui/src/status/rate_limits.rs:20` `const STATUS_LIMIT_BAR_SEGMENTS: usize = 20;`
- `const` `codex-rs/tui/src/status/rate_limits.rs:21` `const STATUS_LIMIT_BAR_FILLED: &str = "█";`
- `const` `codex-rs/tui/src/status/rate_limits.rs:22` `const STATUS_LIMIT_BAR_EMPTY: &str = "░";`
- `impl` `codex-rs/tui/src/status/rate_limits.rs:71` `impl RateLimitWindowDisplay {`
- `fn` `codex-rs/tui/src/status/rate_limits.rs:72` `fn from_window(window: &RateLimitWindow, captured_at: DateTime<Local>) -> Self {`
- `impl` `codex-rs/tui/src/status/rate_limits.rs:132` `impl From<&CoreCreditsSnapshot> for CreditsSnapshotDisplay {`
- `fn` `codex-rs/tui/src/status/rate_limits.rs:133` `fn from(value: &CoreCreditsSnapshot) -> Self {`
- `fn` `codex-rs/tui/src/status/rate_limits.rs:230` `fn credit_status_row(credits: &CreditsSnapshotDisplay) -> Option<StatusRateLimitRow> {`
- `fn` `codex-rs/tui/src/status/rate_limits.rs:248` `fn format_credit_balance(raw: &str) -> Option<String> {`

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
- `docs/workdocjcl/spec/06_UI/TUI.md`
