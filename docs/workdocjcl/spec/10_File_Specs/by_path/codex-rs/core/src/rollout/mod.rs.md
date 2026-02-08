# `codex-rs/core/src/rollout/mod.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `1009`
- sha256: `8d74d2326219c7eef7cc8e1964a531ae477a3570b6c99eafa821192dc563da62`
- generated_utc: `2026-02-03T16:08:29Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/rollout/mod.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `use` `codex-rs/core/src/rollout/mod.rs:3` `use codex_protocol::protocol::SessionSource;`
- `const` `codex-rs/core/src/rollout/mod.rs:5` `pub const SESSIONS_SUBDIR: &str = "sessions";`
- `const` `codex-rs/core/src/rollout/mod.rs:6` `pub const ARCHIVED_SESSIONS_SUBDIR: &str = "archived_sessions";`
- `const` `codex-rs/core/src/rollout/mod.rs:7` `pub const INTERACTIVE_SESSION_SOURCES: &[SessionSource] =`
- `mod` `codex-rs/core/src/rollout/mod.rs:11` `pub mod list;`
- `mod` `codex-rs/core/src/rollout/mod.rs:14` `pub mod recorder;`
- `mod` `codex-rs/core/src/rollout/mod.rs:30` `pub mod tests;`

## Dependencies (auto sample)
### Imports / Includes
- `use codex_protocol::protocol::SessionSource;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- `workdocjcl/spec/00_Overview/ARCHITECTURE.md`
