# `codex-rs/state/src/lib.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `1462`
- sha256: `a7fb492db83f1841270e63970e0e848689dedc1274b02f9ebc02f971b3260bc9`
- generated_utc: `2026-02-03T16:08:30Z`

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
- `const` `codex-rs/state/src/lib.rs:34` `pub const DB_ERROR_METRIC: &str = "codex.db.error";`
- `const` `codex-rs/state/src/lib.rs:36` `pub const DB_METRIC_BACKFILL: &str = "codex.db.backfill";`
- `const` `codex-rs/state/src/lib.rs:38` `pub const DB_METRIC_BACKFILL_DURATION_MS: &str = "codex.db.backfill.duration_ms";`
- `const` `codex-rs/state/src/lib.rs:40` `pub const DB_METRIC_COMPARE_ERROR: &str = "codex.db.compare_error";`

## Dependencies (auto sample)
### Imports / Includes
- (none detected)
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- `workdocjcl/spec/02_Data/ENTITIES.md`
