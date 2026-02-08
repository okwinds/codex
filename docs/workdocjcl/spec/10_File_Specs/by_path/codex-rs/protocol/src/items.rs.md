# `codex-rs/protocol/src/items.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `7219`
- sha256: `5ad3a470e17847fba97fd7714aa7a62e9ad6733b5322d1132697e2f30857dbbc`
- generated_utc: `2026-02-03T16:08:30Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/protocol/src/items.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub enum TurnItem {`
- `pub struct UserMessageItem {`
- `pub enum AgentMessageContent {`
- `pub struct AgentMessageItem {`
- `pub struct PlanItem {`
- `pub struct ReasoningItem {`
- `pub struct WebSearchItem {`
- `pub struct ContextCompactionItem {`
- `pub fn new() -> Self {`
- `pub fn as_legacy_event(&self) -> EventMsg {`
- `pub fn new(content: &[UserInput]) -> Self {`
- `pub fn as_legacy_event(&self) -> EventMsg {`
- `pub fn message(&self) -> String {`
- `pub fn text_elements(&self) -> Vec<TextElement> {`
- `pub fn image_urls(&self) -> Vec<String> {`
- `pub fn local_image_paths(&self) -> Vec<std::path::PathBuf> {`
- `pub fn new(content: &[AgentMessageContent]) -> Self {`
- `pub fn as_legacy_events(&self) -> Vec<EventMsg> {`
- `pub fn as_legacy_events(&self, show_raw_agent_reasoning: bool) -> Vec<EventMsg> {`
- `pub fn as_legacy_event(&self) -> EventMsg {`
- `pub fn id(&self) -> String {`
- `pub fn as_legacy_events(&self, show_raw_agent_reasoning: bool) -> Vec<EventMsg> {`

## Definitions (auto, per-file)
- `use` `codex-rs/protocol/src/items.rs:1` `use crate::models::WebSearchAction;`
- `use` `codex-rs/protocol/src/items.rs:2` `use crate::protocol::AgentMessageEvent;`
- `use` `codex-rs/protocol/src/items.rs:3` `use crate::protocol::AgentReasoningEvent;`
- `use` `codex-rs/protocol/src/items.rs:4` `use crate::protocol::AgentReasoningRawContentEvent;`
- `use` `codex-rs/protocol/src/items.rs:5` `use crate::protocol::ContextCompactedEvent;`
- `use` `codex-rs/protocol/src/items.rs:6` `use crate::protocol::EventMsg;`
- `use` `codex-rs/protocol/src/items.rs:7` `use crate::protocol::UserMessageEvent;`
- `use` `codex-rs/protocol/src/items.rs:8` `use crate::protocol::WebSearchEndEvent;`
- `use` `codex-rs/protocol/src/items.rs:9` `use crate::user_input::ByteRange;`
- `use` `codex-rs/protocol/src/items.rs:10` `use crate::user_input::TextElement;`
- `use` `codex-rs/protocol/src/items.rs:11` `use crate::user_input::UserInput;`
- `use` `codex-rs/protocol/src/items.rs:12` `use schemars::JsonSchema;`
- `use` `codex-rs/protocol/src/items.rs:13` `use serde::Deserialize;`
- `use` `codex-rs/protocol/src/items.rs:14` `use serde::Serialize;`
- `use` `codex-rs/protocol/src/items.rs:15` `use ts_rs::TS;`
- `enum` `codex-rs/protocol/src/items.rs:20` `pub enum TurnItem {`
- `struct` `codex-rs/protocol/src/items.rs:30` `pub struct UserMessageItem {`
- `enum` `codex-rs/protocol/src/items.rs:38` `pub enum AgentMessageContent {`
- `struct` `codex-rs/protocol/src/items.rs:43` `pub struct AgentMessageItem {`
- `struct` `codex-rs/protocol/src/items.rs:49` `pub struct PlanItem {`
- `struct` `codex-rs/protocol/src/items.rs:55` `pub struct ReasoningItem {`
- `struct` `codex-rs/protocol/src/items.rs:63` `pub struct WebSearchItem {`
- `struct` `codex-rs/protocol/src/items.rs:70` `pub struct ContextCompactionItem {`
- `impl` `codex-rs/protocol/src/items.rs:74` `impl ContextCompactionItem {`
- `fn` `codex-rs/protocol/src/items.rs:75` `pub fn new() -> Self {`
- `fn` `codex-rs/protocol/src/items.rs:81` `pub fn as_legacy_event(&self) -> EventMsg {`
- `impl` `codex-rs/protocol/src/items.rs:86` `impl Default for ContextCompactionItem {`
- `fn` `codex-rs/protocol/src/items.rs:87` `fn default() -> Self {`
- `impl` `codex-rs/protocol/src/items.rs:92` `impl UserMessageItem {`
- `fn` `codex-rs/protocol/src/items.rs:93` `pub fn new(content: &[UserInput]) -> Self {`
- `fn` `codex-rs/protocol/src/items.rs:100` `pub fn as_legacy_event(&self) -> EventMsg {`
- `fn` `codex-rs/protocol/src/items.rs:111` `pub fn message(&self) -> String {`
- `fn` `codex-rs/protocol/src/items.rs:122` `pub fn text_elements(&self) -> Vec<TextElement> {`
- `fn` `codex-rs/protocol/src/items.rs:149` `pub fn image_urls(&self) -> Vec<String> {`
- `fn` `codex-rs/protocol/src/items.rs:159` `pub fn local_image_paths(&self) -> Vec<std::path::PathBuf> {`
- `impl` `codex-rs/protocol/src/items.rs:170` `impl AgentMessageItem {`
- `fn` `codex-rs/protocol/src/items.rs:171` `pub fn new(content: &[AgentMessageContent]) -> Self {`
- `fn` `codex-rs/protocol/src/items.rs:178` `pub fn as_legacy_events(&self) -> Vec<EventMsg> {`
- `impl` `codex-rs/protocol/src/items.rs:190` `impl ReasoningItem {`
- `fn` `codex-rs/protocol/src/items.rs:191` `pub fn as_legacy_events(&self, show_raw_agent_reasoning: bool) -> Vec<EventMsg> {`
- `impl` `codex-rs/protocol/src/items.rs:213` `impl WebSearchItem {`
- `fn` `codex-rs/protocol/src/items.rs:214` `pub fn as_legacy_event(&self) -> EventMsg {`
- `impl` `codex-rs/protocol/src/items.rs:223` `impl TurnItem {`
- `fn` `codex-rs/protocol/src/items.rs:224` `pub fn id(&self) -> String {`
- `fn` `codex-rs/protocol/src/items.rs:235` `pub fn as_legacy_events(&self, show_raw_agent_reasoning: bool) -> Vec<EventMsg> {`

## Dependencies (auto sample)
### Imports / Includes
- `use crate::models::WebSearchAction;`
- `use crate::protocol::AgentMessageEvent;`
- `use crate::protocol::AgentReasoningEvent;`
- `use crate::protocol::AgentReasoningRawContentEvent;`
- `use crate::protocol::ContextCompactedEvent;`
- `use crate::protocol::EventMsg;`
- `use crate::protocol::UserMessageEvent;`
- `use crate::protocol::WebSearchEndEvent;`
- `use crate::user_input::ByteRange;`
- `use crate::user_input::TextElement;`
- `use crate::user_input::UserInput;`
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
