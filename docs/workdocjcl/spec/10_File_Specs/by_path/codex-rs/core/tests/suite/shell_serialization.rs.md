# `codex-rs/core/tests/suite/shell_serialization.rs`

## Identity
- kind: `test`
- ext: `.rs`
- size_bytes: `28928`
- sha256: `68fbaf726eea20d76701d40a3816ab67bc61c223ccb807fb54ccce70d969ddd7`
- generated_utc: `2026-02-08T10:45:36Z`

## Purpose (Why)
Test or snapshot file used for automated verification.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/tests/suite/shell_serialization.rs` (read)

### Outputs / Side Effects
- none (file is declarative: doc/config/test/asset)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- (not extracted)

## Dependencies (auto sample)
### Imports / Includes
- `use anyhow::Result;`
- `use codex_core::protocol::SandboxPolicy;`
- `use core_test_support::assert_regex_match;`
- `use core_test_support::responses::ev_assistant_message;`
- `use core_test_support::responses::ev_completed;`
- `use core_test_support::responses::ev_function_call;`
- `use core_test_support::responses::ev_local_shell_call;`
- `use core_test_support::responses::ev_response_created;`
- `use core_test_support::responses::mount_sse_sequence;`
- `use core_test_support::responses::sse;`
- `use core_test_support::responses::start_mock_server;`
- `use core_test_support::skip_if_no_network;`
- `use core_test_support::test_codex::ApplyPatchModelOutput;`
- `use core_test_support::test_codex::ShellModelOutput;`
- `use core_test_support::test_codex::TestCodexBuilder;`
- `use core_test_support::test_codex::test_codex;`
- `use pretty_assertions::assert_eq;`
- `use regex_lite::Regex;`
- `use serde_json::Value;`
- `use serde_json::json;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (none detected)

## Spec Links
- `docs/workdocjcl/spec/00_Overview/ARCHITECTURE.md`
