# `codex-rs/protocol/src/items.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `7997`
- sha256: `6808f83f17aee98e32169f8f7f9665da1a9f653119530345a23864d00de2f57a`
- generated_utc: `2026-02-08T10:45:38Z`

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
- `use` `codex-rs/protocol/src/items.rs:1` `use crate::models::MessagePhase;`
- `use` `codex-rs/protocol/src/items.rs:2` `use crate::models::WebSearchAction;`
- `use` `codex-rs/protocol/src/items.rs:3` `use crate::protocol::AgentMessageEvent;`
- `use` `codex-rs/protocol/src/items.rs:4` `use crate::protocol::AgentReasoningEvent;`
- `use` `codex-rs/protocol/src/items.rs:5` `use crate::protocol::AgentReasoningRawContentEvent;`
- `use` `codex-rs/protocol/src/items.rs:6` `use crate::protocol::ContextCompactedEvent;`
- `use` `codex-rs/protocol/src/items.rs:7` `use crate::protocol::EventMsg;`
- `use` `codex-rs/protocol/src/items.rs:8` `use crate::protocol::UserMessageEvent;`
- `use` `codex-rs/protocol/src/items.rs:9` `use crate::protocol::WebSearchEndEvent;`
- `use` `codex-rs/protocol/src/items.rs:10` `use crate::user_input::ByteRange;`
- `use` `codex-rs/protocol/src/items.rs:11` `use crate::user_input::TextElement;`
- `use` `codex-rs/protocol/src/items.rs:12` `use crate::user_input::UserInput;`
- `use` `codex-rs/protocol/src/items.rs:13` `use schemars::JsonSchema;`
- `use` `codex-rs/protocol/src/items.rs:14` `use serde::Deserialize;`
- `use` `codex-rs/protocol/src/items.rs:15` `use serde::Serialize;`
- `use` `codex-rs/protocol/src/items.rs:16` `use ts_rs::TS;`
- `enum` `codex-rs/protocol/src/items.rs:21` `pub enum TurnItem {`
- `struct` `codex-rs/protocol/src/items.rs:31` `pub struct UserMessageItem {`
- `enum` `codex-rs/protocol/src/items.rs:39` `pub enum AgentMessageContent {`
- `struct` `codex-rs/protocol/src/items.rs:49` `pub struct AgentMessageItem {`
- `struct` `codex-rs/protocol/src/items.rs:62` `pub struct PlanItem {`
- `struct` `codex-rs/protocol/src/items.rs:68` `pub struct ReasoningItem {`
- `struct` `codex-rs/protocol/src/items.rs:76` `pub struct WebSearchItem {`
- `struct` `codex-rs/protocol/src/items.rs:83` `pub struct ContextCompactionItem {`
- `impl` `codex-rs/protocol/src/items.rs:87` `impl ContextCompactionItem {`
- `fn` `codex-rs/protocol/src/items.rs:88` `pub fn new() -> Self {`
- `fn` `codex-rs/protocol/src/items.rs:94` `pub fn as_legacy_event(&self) -> EventMsg {`
- `impl` `codex-rs/protocol/src/items.rs:99` `impl Default for ContextCompactionItem {`
- `fn` `codex-rs/protocol/src/items.rs:100` `fn default() -> Self {`
- `impl` `codex-rs/protocol/src/items.rs:105` `impl UserMessageItem {`
- `fn` `codex-rs/protocol/src/items.rs:106` `pub fn new(content: &[UserInput]) -> Self {`
- `fn` `codex-rs/protocol/src/items.rs:113` `pub fn as_legacy_event(&self) -> EventMsg {`
- `fn` `codex-rs/protocol/src/items.rs:124` `pub fn message(&self) -> String {`
- `fn` `codex-rs/protocol/src/items.rs:135` `pub fn text_elements(&self) -> Vec<TextElement> {`
- `fn` `codex-rs/protocol/src/items.rs:162` `pub fn image_urls(&self) -> Vec<String> {`
- `fn` `codex-rs/protocol/src/items.rs:172` `pub fn local_image_paths(&self) -> Vec<std::path::PathBuf> {`
- `impl` `codex-rs/protocol/src/items.rs:183` `impl AgentMessageItem {`
- `fn` `codex-rs/protocol/src/items.rs:184` `pub fn new(content: &[AgentMessageContent]) -> Self {`
- `fn` `codex-rs/protocol/src/items.rs:192` `pub fn as_legacy_events(&self) -> Vec<EventMsg> {`
- `impl` `codex-rs/protocol/src/items.rs:206` `impl ReasoningItem {`
- `fn` `codex-rs/protocol/src/items.rs:207` `pub fn as_legacy_events(&self, show_raw_agent_reasoning: bool) -> Vec<EventMsg> {`
- `impl` `codex-rs/protocol/src/items.rs:229` `impl WebSearchItem {`
- `fn` `codex-rs/protocol/src/items.rs:230` `pub fn as_legacy_event(&self) -> EventMsg {`
- `impl` `codex-rs/protocol/src/items.rs:239` `impl TurnItem {`
- `fn` `codex-rs/protocol/src/items.rs:240` `pub fn id(&self) -> String {`
- `fn` `codex-rs/protocol/src/items.rs:251` `pub fn as_legacy_events(&self, show_raw_agent_reasoning: bool) -> Vec<EventMsg> {`

## Dependencies (auto sample)
### Imports / Includes
- `use crate::models::MessagePhase;`
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
- `docs/workdocjcl/spec/02_Data/ROLLOUT_FORMAT.md`
