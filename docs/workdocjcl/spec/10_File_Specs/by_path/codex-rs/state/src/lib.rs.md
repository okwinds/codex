# `codex-rs/state/src/lib.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `1599`
- sha256: `a08bee1f0697b40fdeacbf3c0c72a86c5d9d27ecddf870d053c4ebef0feb6dac`
- generated_utc: `2026-02-08T10:45:38Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/state/src/lib.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `mod` `codex-rs/state/src/lib.rs:7` `mod extract;`
- `mod` `codex-rs/state/src/lib.rs:8` `pub mod log_db;`
- `mod` `codex-rs/state/src/lib.rs:9` `mod migrations;`
- `mod` `codex-rs/state/src/lib.rs:10` `mod model;`
- `mod` `codex-rs/state/src/lib.rs:11` `mod paths;`
- `mod` `codex-rs/state/src/lib.rs:12` `mod runtime;`
- `const` `codex-rs/state/src/lib.rs:40` `pub const DB_ERROR_METRIC: &str = "codex.db.error";`
- `const` `codex-rs/state/src/lib.rs:42` `pub const DB_METRIC_BACKFILL: &str = "codex.db.backfill";`
- `const` `codex-rs/state/src/lib.rs:44` `pub const DB_METRIC_BACKFILL_DURATION_MS: &str = "codex.db.backfill.duration_ms";`
- `const` `codex-rs/state/src/lib.rs:46` `pub const DB_METRIC_COMPARE_ERROR: &str = "codex.db.compare_error";`

## Dependencies (auto sample)
### Imports / Includes
- (none detected)
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- `docs/workdocjcl/spec/02_Data/ENTITIES.md`
