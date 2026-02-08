# `codex-rs/core/tests/common/responses.rs`

## Identity
- kind: `test`
- ext: `.rs`
- size_bytes: `39283`
- sha256: `5239f8e531735a476096a2c8174cff2f080f6573354f2901efa04028a3ecc177`
- generated_utc: `2026-02-08T10:45:34Z`

## Purpose (Why)
Test or snapshot file used for automated verification.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/tests/common/responses.rs` (read)

### Outputs / Side Effects
- none (file is declarative: doc/config/test/asset)

## Public Surface (auto)
- `pub struct ResponseMock {`
- `pub fn single_request(&self) -> ResponsesRequest {`
- `pub fn requests(&self) -> Vec<ResponsesRequest> {`
- `pub fn last_request(&self) -> Option<ResponsesRequest> {`
- `pub fn saw_function_call(&self, call_id: &str) -> bool {`
- `pub fn function_call_output_text(&self, call_id: &str) -> Option<String> {`
- `pub struct ResponsesRequest(wiremock::Request);`
- `pub fn body_json(&self) -> Value {`
- `pub fn body_bytes(&self) -> Vec<u8> {`
- `pub fn instructions_text(&self) -> String {`
- `pub fn message_input_texts(&self, role: &str) -> Vec<String> {`
- `pub fn input(&self) -> Vec<Value> {`
- `pub fn inputs_of_type(&self, ty: &str) -> Vec<Value> {`
- `pub fn function_call_output(&self, call_id: &str) -> Value {`
- `pub fn custom_tool_call_output(&self, call_id: &str) -> Value {`
- `pub fn call_output(&self, call_id: &str, call_type: &str) -> Value {`
- `pub fn has_function_call(&self, call_id: &str) -> bool {`
- `pub fn function_call_output_text(&self, call_id: &str) -> Option<String> {`
- `pub fn function_call_output_content_and_success(`
- `pub fn custom_tool_call_output_content_and_success(`
- `pub fn header(&self, name: &str) -> Option<String> {`
- `pub fn path(&self) -> String {`
- `pub fn query_param(&self, name: &str) -> Option<String> {`
- `pub struct WebSocketRequest {`
- `pub fn body_json(&self) -> Value {`
- `pub struct WebSocketHandshake {`
- `pub fn header(&self, name: &str) -> Option<String> {`
- `pub struct WebSocketConnectionConfig {`
- `pub struct WebSocketTestServer {`
- `pub fn uri(&self) -> &str {`
- `pub fn connections(&self) -> Vec<Vec<WebSocketRequest>> {`
- `pub fn single_connection(&self) -> Vec<WebSocketRequest> {`
- `pub fn handshakes(&self) -> Vec<WebSocketHandshake> {`
- `pub fn single_handshake(&self) -> WebSocketHandshake {`
- `pub struct ModelsMock {`
- `pub fn requests(&self) -> Vec<wiremock::Request> {`
- `pub fn single_request_path(&self) -> String {`
- `pub fn sse(events: Vec<Value>) -> String {`
- `pub fn sse_completed(id: &str) -> String {`
- `pub fn ev_completed(id: &str) -> Value {`
- `pub fn ev_done() -> Value {`
- `pub fn ev_response_created(id: &str) -> Value {`
- `pub fn ev_completed_with_tokens(id: &str, total_tokens: i64) -> Value {`
- `pub fn ev_assistant_message(id: &str, text: &str) -> Value {`
- `pub fn ev_message_item_added(id: &str, text: &str) -> Value {`
- `pub fn ev_output_text_delta(delta: &str) -> Value {`
- `pub fn ev_reasoning_item(id: &str, summary: &[&str], raw_content: &[&str]) -> Value {`
- `pub fn ev_reasoning_item_added(id: &str, summary: &[&str]) -> Value {`
- `pub fn ev_reasoning_summary_text_delta(delta: &str) -> Value {`
- `pub fn ev_reasoning_text_delta(delta: &str) -> Value {`

## Definitions (auto, per-file)
- (not extracted)

## Dependencies (auto sample)
### Imports / Includes
- `use std::collections::VecDeque;`
- `use std::sync::Arc;`
- `use std::sync::Mutex;`
- `use std::time::Duration;`
- `use anyhow::Result;`
- `use base64::Engine;`
- `use codex_protocol::openai_models::ModelsResponse;`
- `use futures::SinkExt;`
- `use futures::StreamExt;`
- `use serde_json::Value;`
- `use tokio::net::TcpListener;`
- `use tokio::sync::oneshot;`
- `use tokio_tungstenite::accept_hdr_async_with_config;`
- `use tokio_tungstenite::tungstenite::Message;`
- `use tokio_tungstenite::tungstenite::extensions::ExtensionsConfig;`
- `use tokio_tungstenite::tungstenite::extensions::compression::deflate::DeflateConfig;`
- `use tokio_tungstenite::tungstenite::handshake::server::Request;`
- `use tokio_tungstenite::tungstenite::handshake::server::Response;`
- `use tokio_tungstenite::tungstenite::protocol::WebSocketConfig;`
- `use wiremock::BodyPrintLimit;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (none detected)

## Spec Links
- `docs/workdocjcl/spec/00_Overview/ARCHITECTURE.md`
