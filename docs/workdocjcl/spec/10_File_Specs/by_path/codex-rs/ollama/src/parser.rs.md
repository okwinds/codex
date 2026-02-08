# `codex-rs/ollama/src/parser.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `2527`
- sha256: `142cbcbd252617f47f4393826c6c419ef181c1506bb4c0757fa3c34762db5388`
- generated_utc: `2026-02-08T10:45:38Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/ollama/src/parser.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `use` `codex-rs/ollama/src/parser.rs:1` `use serde_json::Value as JsonValue;`
- `use` `codex-rs/ollama/src/parser.rs:3` `use crate::pull::PullEvent;`
- `use` `codex-rs/ollama/src/parser.rs:33` `use assert_matches::assert_matches;`
- `use` `codex-rs/ollama/src/parser.rs:35` `use super::*;`
- `fn` `codex-rs/ollama/src/parser.rs:38` `fn test_pull_events_decoder_status_and_success() {`
- `fn` `codex-rs/ollama/src/parser.rs:51` `fn test_pull_events_decoder_progress() {`

## Dependencies (auto sample)
### Imports / Includes
- `use serde_json::Value as JsonValue;`
- `use crate::pull::PullEvent;`
- `use assert_matches::assert_matches;`
- `use super::*;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
