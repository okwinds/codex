# `codex-rs/app-server-protocol/src/protocol/common.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `37769`
- sha256: `13750436bea13bd8d73d733a8b7d82b27ce4a1a81829c069d6589299b644aafb`
- generated_utc: `2026-02-03T16:08:28Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server-protocol/src/protocol/common.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub struct GitSha(pub String);`
- `pub fn new(sha: &str) -> Self {`
- `pub enum AuthMode {`
- `pub enum ClientRequest {`
- `pub fn export_client_responses(`
- `pub fn export_client_response_schemas(`
- `pub fn export_client_param_schemas(`
- `pub enum ServerRequest {`
- `pub enum ServerRequestPayload {`
- `pub fn request_with_id(self, request_id: RequestId) -> ServerRequest {`
- `pub fn export_server_responses(`
- `pub fn export_server_response_schemas(`
- `pub fn export_server_param_schemas(`
- `pub enum ServerNotification {`
- `pub fn to_params(self) -> Result<serde_json::Value, serde_json::Error> {`
- `pub fn export_server_notification_schemas(`
- `pub enum ClientNotification {`
- `pub fn export_client_notification_schemas(`
- `pub struct FuzzyFileSearchParams {`
- `pub struct FuzzyFileSearchResult {`
- `pub struct FuzzyFileSearchResponse {`

## Definitions (auto, per-file)
- `use` `codex-rs/app-server-protocol/src/protocol/common.rs:1` `use std::path::Path;`
- `use` `codex-rs/app-server-protocol/src/protocol/common.rs:3` `use crate::JSONRPCNotification;`
- `use` `codex-rs/app-server-protocol/src/protocol/common.rs:4` `use crate::JSONRPCRequest;`
- `use` `codex-rs/app-server-protocol/src/protocol/common.rs:5` `use crate::RequestId;`
- `use` `codex-rs/app-server-protocol/src/protocol/common.rs:6` `use crate::export::GeneratedSchema;`
- `use` `codex-rs/app-server-protocol/src/protocol/common.rs:7` `use crate::export::write_json_schema;`
- `use` `codex-rs/app-server-protocol/src/protocol/common.rs:8` `use crate::protocol::v1;`
- `use` `codex-rs/app-server-protocol/src/protocol/common.rs:9` `use crate::protocol::v2;`
- `use` `codex-rs/app-server-protocol/src/protocol/common.rs:10` `use schemars::JsonSchema;`
- `use` `codex-rs/app-server-protocol/src/protocol/common.rs:11` `use serde::Deserialize;`
- `use` `codex-rs/app-server-protocol/src/protocol/common.rs:12` `use serde::Serialize;`
- `use` `codex-rs/app-server-protocol/src/protocol/common.rs:13` `use strum_macros::Display;`
- `use` `codex-rs/app-server-protocol/src/protocol/common.rs:14` `use ts_rs::TS;`
- `struct` `codex-rs/app-server-protocol/src/protocol/common.rs:18` `pub struct GitSha(pub String);`
- `impl` `codex-rs/app-server-protocol/src/protocol/common.rs:20` `impl GitSha {`
- `fn` `codex-rs/app-server-protocol/src/protocol/common.rs:21` `pub fn new(sha: &str) -> Self {`
- `enum` `codex-rs/app-server-protocol/src/protocol/common.rs:29` `pub enum AuthMode {`
- `enum` `codex-rs/app-server-protocol/src/protocol/common.rs:99` `pub enum ClientRequest {`
- `impl` `codex-rs/app-server-protocol/src/protocol/common.rs:112` `impl crate::experimental_api::ExperimentalApi for ClientRequest {`
- `fn` `codex-rs/app-server-protocol/src/protocol/common.rs:113` `fn experimental_reason(&self) -> Option<&'static str> {`
- `fn` `codex-rs/app-server-protocol/src/protocol/common.rs:144` `pub fn export_client_responses(`
- `fn` `codex-rs/app-server-protocol/src/protocol/common.rs:154` `pub fn export_client_response_schemas(`
- `fn` `codex-rs/app-server-protocol/src/protocol/common.rs:165` `pub fn export_client_param_schemas(`
- `enum` `codex-rs/app-server-protocol/src/protocol/common.rs:456` `pub enum ServerRequest {`
- `enum` `codex-rs/app-server-protocol/src/protocol/common.rs:469` `pub enum ServerRequestPayload {`
- `impl` `codex-rs/app-server-protocol/src/protocol/common.rs:473` `impl ServerRequestPayload {`
- `fn` `codex-rs/app-server-protocol/src/protocol/common.rs:474` `pub fn request_with_id(self, request_id: RequestId) -> ServerRequest {`
- `fn` `codex-rs/app-server-protocol/src/protocol/common.rs:481` `pub fn export_server_responses(`
- `fn` `codex-rs/app-server-protocol/src/protocol/common.rs:491` `pub fn export_server_response_schemas(`
- `fn` `codex-rs/app-server-protocol/src/protocol/common.rs:505` `pub fn export_server_param_schemas(`
- `enum` `codex-rs/app-server-protocol/src/protocol/common.rs:533` `pub enum ServerNotification {`
- `impl` `codex-rs/app-server-protocol/src/protocol/common.rs:541` `impl ServerNotification {`
- `fn` `codex-rs/app-server-protocol/src/protocol/common.rs:542` `pub fn to_params(self) -> Result<serde_json::Value, serde_json::Error> {`
- `impl` `codex-rs/app-server-protocol/src/protocol/common.rs:549` `impl TryFrom<JSONRPCNotification> for ServerNotification {`
- `type` `codex-rs/app-server-protocol/src/protocol/common.rs:550` `type Error = serde_json::Error;`
- `fn` `codex-rs/app-server-protocol/src/protocol/common.rs:552` `fn try_from(value: JSONRPCNotification) -> Result<Self, serde_json::Error> {`
- `fn` `codex-rs/app-server-protocol/src/protocol/common.rs:558` `pub fn export_server_notification_schemas(`
- `enum` `codex-rs/app-server-protocol/src/protocol/common.rs:578` `pub enum ClientNotification {`
- `fn` `codex-rs/app-server-protocol/src/protocol/common.rs:585` `pub fn export_client_notification_schemas(`
- `impl` `codex-rs/app-server-protocol/src/protocol/common.rs:595` `impl TryFrom<JSONRPCRequest> for ServerRequest {`
- `type` `codex-rs/app-server-protocol/src/protocol/common.rs:596` `type Error = serde_json::Error;`
- `fn` `codex-rs/app-server-protocol/src/protocol/common.rs:598` `fn try_from(value: JSONRPCRequest) -> Result<Self, Self::Error> {`
- `struct` `codex-rs/app-server-protocol/src/protocol/common.rs:654` `pub struct FuzzyFileSearchParams {`
- `struct` `codex-rs/app-server-protocol/src/protocol/common.rs:663` `pub struct FuzzyFileSearchResult {`
- `struct` `codex-rs/app-server-protocol/src/protocol/common.rs:672` `pub struct FuzzyFileSearchResponse {`
- `use` `codex-rs/app-server-protocol/src/protocol/common.rs:730` `use super::*;`
- `use` `codex-rs/app-server-protocol/src/protocol/common.rs:731` `use anyhow::Result;`
- `use` `codex-rs/app-server-protocol/src/protocol/common.rs:732` `use codex_protocol::ThreadId;`
- `use` `codex-rs/app-server-protocol/src/protocol/common.rs:733` `use codex_protocol::account::PlanType;`
- `use` `codex-rs/app-server-protocol/src/protocol/common.rs:734` `use codex_protocol::parse_command::ParsedCommand;`
- `use` `codex-rs/app-server-protocol/src/protocol/common.rs:735` `use codex_protocol::protocol::AskForApproval;`
- `use` `codex-rs/app-server-protocol/src/protocol/common.rs:736` `use pretty_assertions::assert_eq;`
- `use` `codex-rs/app-server-protocol/src/protocol/common.rs:737` `use serde_json::json;`
- `use` `codex-rs/app-server-protocol/src/protocol/common.rs:738` `use std::path::PathBuf;`
- `fn` `codex-rs/app-server-protocol/src/protocol/common.rs:741` `fn serialize_new_conversation() -> Result<()> {`
- `fn` `codex-rs/app-server-protocol/src/protocol/common.rs:780` `fn conversation_id_serializes_as_plain_string() -> Result<()> {`
- `fn` `codex-rs/app-server-protocol/src/protocol/common.rs:791` `fn conversation_id_deserializes_from_plain_string() -> Result<()> {`
- `fn` `codex-rs/app-server-protocol/src/protocol/common.rs:802` `fn serialize_client_notification() -> Result<()> {`
- `fn` `codex-rs/app-server-protocol/src/protocol/common.rs:815` `fn serialize_server_request() -> Result<()> {`
- `fn` `codex-rs/app-server-protocol/src/protocol/common.rs:859` `fn serialize_chatgpt_auth_tokens_refresh_request() -> Result<()> {`
- `fn` `codex-rs/app-server-protocol/src/protocol/common.rs:882` `fn serialize_get_account_rate_limits() -> Result<()> {`
- `fn` `codex-rs/app-server-protocol/src/protocol/common.rs:898` `fn serialize_config_requirements_read() -> Result<()> {`
- `fn` `codex-rs/app-server-protocol/src/protocol/common.rs:914` `fn serialize_account_login_api_key() -> Result<()> {`
- `fn` `codex-rs/app-server-protocol/src/protocol/common.rs:936` `fn serialize_account_login_chatgpt() -> Result<()> {`
- `fn` `codex-rs/app-server-protocol/src/protocol/common.rs:955` `fn serialize_account_logout() -> Result<()> {`
- `fn` `codex-rs/app-server-protocol/src/protocol/common.rs:971` `fn serialize_account_login_chatgpt_auth_tokens() -> Result<()> {`
- `fn` `codex-rs/app-server-protocol/src/protocol/common.rs:995` `fn serialize_get_account() -> Result<()> {`
- `fn` `codex-rs/app-server-protocol/src/protocol/common.rs:1016` `fn account_serializes_fields_in_camel_case() -> Result<()> {`
- `fn` `codex-rs/app-server-protocol/src/protocol/common.rs:1042` `fn serialize_list_models() -> Result<()> {`
- `fn` `codex-rs/app-server-protocol/src/protocol/common.rs:1062` `fn serialize_list_collaboration_modes() -> Result<()> {`
- `fn` `codex-rs/app-server-protocol/src/protocol/common.rs:1079` `fn mock_experimental_method_is_marked_experimental() {`
- `fn` `codex-rs/app-server-protocol/src/protocol/common.rs:1089` `fn thread_start_mock_field_is_marked_experimental() {`

## Dependencies (auto sample)
### Imports / Includes
- `use std::path::Path;`
- `use crate::JSONRPCNotification;`
- `use crate::JSONRPCRequest;`
- `use crate::RequestId;`
- `use crate::export::GeneratedSchema;`
- `use crate::export::write_json_schema;`
- `use crate::protocol::v1;`
- `use crate::protocol::v2;`
- `use schemars::JsonSchema;`
- `use serde::Deserialize;`
- `use serde::Serialize;`
- `use strum_macros::Display;`
- `use ts_rs::TS;`
- `use super::*;`
- `use anyhow::Result;`
- `use codex_protocol::ThreadId;`
- `use codex_protocol::account::PlanType;`
- `use codex_protocol::parse_command::ParsedCommand;`
- `use codex_protocol::protocol::AskForApproval;`
- `use pretty_assertions::assert_eq;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
