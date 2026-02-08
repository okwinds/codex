# `codex-rs/tui/src/mention_codec.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `6580`
- sha256: `5408e67109b03e73976c12d5683370217bfc227817d0edb96cd6612ec9814e11`
- generated_utc: `2026-02-08T10:45:40Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/tui/src/mention_codec.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `use` `codex-rs/tui/src/mention_codec.rs:1` `use std::collections::HashMap;`
- `use` `codex-rs/tui/src/mention_codec.rs:2` `use std::collections::VecDeque;`
- `fn` `codex-rs/tui/src/mention_codec.rs:161` `fn is_mention_name_char(byte: u8) -> bool {`
- `fn` `codex-rs/tui/src/mention_codec.rs:165` `fn is_common_env_var(name: &str) -> bool {`
- `fn` `codex-rs/tui/src/mention_codec.rs:183` `fn is_tool_path(path: &str) -> bool {`
- `use` `codex-rs/tui/src/mention_codec.rs:195` `use super::*;`
- `use` `codex-rs/tui/src/mention_codec.rs:196` `use pretty_assertions::assert_eq;`
- `fn` `codex-rs/tui/src/mention_codec.rs:199` `fn decode_history_mentions_restores_visible_tokens() {`
- `fn` `codex-rs/tui/src/mention_codec.rs:220` `fn encode_history_mentions_links_bound_mentions_in_order() {`

## Dependencies (auto sample)
### Imports / Includes
- `use std::collections::HashMap;`
- `use std::collections::VecDeque;`
- `use super::*;`
- `use pretty_assertions::assert_eq;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- `docs/workdocjcl/spec/06_UI/TUI.md`
