# `codex-rs/otel/tests/suite/send.rs`

## Identity
- kind: `test`
- ext: `.rs`
- size_bytes: `7926`
- sha256: `f674193e47578ca80f5a9886a9ea2190f1d04a6cc831855a51f47b5c13eec008`
- generated_utc: `2026-02-08T10:45:38Z`

## Purpose (Why)
Test or snapshot file used for automated verification.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/otel/tests/suite/send.rs` (read)

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
- `use crate::harness::find_metric;`
- `use crate::harness::histogram_data;`
- `use crate::harness::latest_metrics;`
- `use codex_otel::metrics::Result;`
- `use pretty_assertions::assert_eq;`
- `use std::collections::BTreeMap;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (none detected)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
