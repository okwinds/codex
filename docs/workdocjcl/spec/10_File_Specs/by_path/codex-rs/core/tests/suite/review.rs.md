# `codex-rs/core/tests/suite/review.rs`

## Identity
- kind: `test`
- ext: `.rs`
- size_bytes: `34875`
- sha256: `43ea1875e8d4ed8da25479d0f32e95511244ec6972c3c1cb8d152b03bb0a4f93`
- generated_utc: `2026-02-08T10:45:36Z`

## Purpose (Why)
Test or snapshot file used for automated verification.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/tests/suite/review.rs` (read)

### Outputs / Side Effects
- none (file is declarative: doc/config/test/asset)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- (not extracted)

## Dependencies (auto sample)
### Imports / Includes
- `use codex_core::CodexThread;`
- `use codex_core::ContentItem;`
- `use codex_core::REVIEW_PROMPT;`
- `use codex_core::ResponseItem;`
- `use codex_core::config::Config;`
- `use codex_core::protocol::ENVIRONMENT_CONTEXT_OPEN_TAG;`
- `use codex_core::protocol::EventMsg;`
- `use codex_core::protocol::ExitedReviewModeEvent;`
- `use codex_core::protocol::Op;`
- `use codex_core::protocol::ReviewCodeLocation;`
- `use codex_core::protocol::ReviewFinding;`
- `use codex_core::protocol::ReviewLineRange;`
- `use codex_core::protocol::ReviewOutputEvent;`
- `use codex_core::protocol::ReviewRequest;`
- `use codex_core::protocol::ReviewTarget;`
- `use codex_core::protocol::RolloutItem;`
- `use codex_core::protocol::RolloutLine;`
- `use codex_core::review_format::render_review_output_text;`
- `use codex_protocol::user_input::UserInput;`
- `use core_test_support::load_sse_fixture_with_id_from_str;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (none detected)

## Spec Links
- `docs/workdocjcl/spec/00_Overview/ARCHITECTURE.md`
