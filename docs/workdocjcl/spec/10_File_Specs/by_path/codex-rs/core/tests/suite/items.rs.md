# `codex-rs/core/tests/suite/items.rs`

## Identity
- kind: `test`
- ext: `.rs`
- size_bytes: `22444`
- sha256: `b0c8c7c3655dedda853a3ace4a71687760ef3f2cdc7126b795e429343432fb58`
- generated_utc: `2026-02-08T10:45:36Z`

## Purpose (Why)
Test or snapshot file used for automated verification.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/tests/suite/items.rs` (read)

### Outputs / Side Effects
- none (file is declarative: doc/config/test/asset)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- (not extracted)

## Dependencies (auto sample)
### Imports / Includes
- `use anyhow::Ok;`
- `use codex_core::protocol::EventMsg;`
- `use codex_core::protocol::ItemCompletedEvent;`
- `use codex_core::protocol::ItemStartedEvent;`
- `use codex_core::protocol::Op;`
- `use codex_protocol::config_types::CollaborationMode;`
- `use codex_protocol::config_types::ModeKind;`
- `use codex_protocol::config_types::Settings;`
- `use codex_protocol::items::AgentMessageContent;`
- `use codex_protocol::items::TurnItem;`
- `use codex_protocol::models::WebSearchAction;`
- `use codex_protocol::user_input::ByteRange;`
- `use codex_protocol::user_input::TextElement;`
- `use codex_protocol::user_input::UserInput;`
- `use core_test_support::responses::ev_assistant_message;`
- `use core_test_support::responses::ev_completed;`
- `use core_test_support::responses::ev_message_item_added;`
- `use core_test_support::responses::ev_output_text_delta;`
- `use core_test_support::responses::ev_reasoning_item;`
- `use core_test_support::responses::ev_reasoning_item_added;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (none detected)

## Spec Links
- `docs/workdocjcl/spec/00_Overview/ARCHITECTURE.md`
