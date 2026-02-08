# `codex-rs/protocol/src/user_input.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `3434`
- sha256: `62ded43be651e6498e1b74fe07c829f4f05631837cbdb3beddc888a5af976eb0`
- generated_utc: `2026-02-03T16:08:30Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/protocol/src/user_input.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub enum UserInput {`
- `pub struct TextElement {`
- `pub fn new(byte_range: ByteRange, placeholder: Option<String>) -> Self {`
- `pub fn set_placeholder(&mut self, placeholder: Option<String>) {`
- `pub fn _placeholder_for_conversion_only(&self) -> Option<&str> {`
- `pub struct ByteRange {`

## Definitions (auto, per-file)
- `use` `codex-rs/protocol/src/user_input.rs:1` `use schemars::JsonSchema;`
- `use` `codex-rs/protocol/src/user_input.rs:2` `use serde::Deserialize;`
- `use` `codex-rs/protocol/src/user_input.rs:3` `use serde::Serialize;`
- `use` `codex-rs/protocol/src/user_input.rs:4` `use ts_rs::TS;`
- `enum` `codex-rs/protocol/src/user_input.rs:10` `pub enum UserInput {`
- `struct` `codex-rs/protocol/src/user_input.rs:37` `pub struct TextElement {`
- `impl` `codex-rs/protocol/src/user_input.rs:44` `impl TextElement {`
- `fn` `codex-rs/protocol/src/user_input.rs:45` `pub fn new(byte_range: ByteRange, placeholder: Option<String>) -> Self {`
- `fn` `codex-rs/protocol/src/user_input.rs:67` `pub fn set_placeholder(&mut self, placeholder: Option<String>) {`
- `fn` `codex-rs/protocol/src/user_input.rs:77` `pub fn _placeholder_for_conversion_only(&self) -> Option<&str> {`
- `struct` `codex-rs/protocol/src/user_input.rs:89` `pub struct ByteRange {`
- `impl` `codex-rs/protocol/src/user_input.rs:96` `impl From<std::ops::Range<usize>> for ByteRange {`
- `fn` `codex-rs/protocol/src/user_input.rs:97` `fn from(range: std::ops::Range<usize>) -> Self {`

## Dependencies (auto sample)
### Imports / Includes
- `use schemars::JsonSchema;`
- `use serde::Deserialize;`
- `use serde::Serialize;`
- `use ts_rs::TS;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- `workdocjcl/spec/02_Data/ROLLOUT_FORMAT.md`
