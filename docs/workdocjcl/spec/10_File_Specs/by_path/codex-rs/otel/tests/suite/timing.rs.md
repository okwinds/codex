# `codex-rs/otel/tests/suite/timing.rs`

## Identity
- kind: `test`
- ext: `.rs`
- size_bytes: `2857`
- sha256: `8d50405077282542ab1da583a16cdb9879d84f554787c1d040e481db66e2958b`
- generated_utc: `2026-02-03T16:08:30Z`

## Purpose (Why)
Test or snapshot file used for automated verification.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/otel/tests/suite/timing.rs` (read)

### Outputs / Side Effects
- none (file is declarative: doc/config/test/asset)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- (not extracted)

## Dependencies (auto sample)
### Imports / Includes
- `use crate::harness::attributes_to_map;`
- `use crate::harness::build_metrics_with_defaults;`
- `use crate::harness::histogram_data;`
- `use crate::harness::latest_metrics;`
- `use codex_otel::metrics::Result;`
- `use pretty_assertions::assert_eq;`
- `use std::time::Duration;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (none detected)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
