# `codex-rs/core/tests/suite/shell_command.rs`

## Identity
- kind: `test`
- ext: `.rs`
- size_bytes: `9500`
- sha256: `2983ebf992a7d29179d59369b0dbfb8b107dda31aa38562c750e295e5db2399f`
- generated_utc: `2026-02-08T10:45:36Z`

## Purpose (Why)
Test or snapshot file used for automated verification.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/tests/suite/shell_command.rs` (read)

### Outputs / Side Effects
- none (file is declarative: doc/config/test/asset)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- (not extracted)

## Dependencies (auto sample)
### Imports / Includes
- `use std::time::Duration;`
- `use anyhow::Result;`
- `use codex_core::features::Feature;`
- `use core_test_support::assert_regex_match;`
- `use core_test_support::responses::ev_assistant_message;`
- `use core_test_support::responses::ev_completed;`
- `use core_test_support::responses::ev_function_call;`
- `use core_test_support::responses::ev_response_created;`
- `use core_test_support::responses::mount_sse_sequence;`
- `use core_test_support::responses::sse;`
- `use core_test_support::skip_if_no_network;`
- `use core_test_support::skip_if_windows;`
- `use core_test_support::test_codex::TestCodexBuilder;`
- `use core_test_support::test_codex::TestCodexHarness;`
- `use core_test_support::test_codex::test_codex;`
- `use serde_json::json;`
- `use test_case::test_case;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (none detected)

## Spec Links
- `docs/workdocjcl/spec/00_Overview/ARCHITECTURE.md`
