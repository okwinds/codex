# `codex-rs/app-server/src/message_processor.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `17306`
- sha256: `02a0efd64abe6de96526182fec8863e924cba54babd0e0783aac4a0764482df3`
- generated_utc: `2026-02-08T10:45:15Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server/src/message_processor.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `use` `codex-rs/app-server/src/message_processor.rs:1` `use std::path::PathBuf;`
- `use` `codex-rs/app-server/src/message_processor.rs:2` `use std::sync::Arc;`
- `use` `codex-rs/app-server/src/message_processor.rs:3` `use std::sync::RwLock;`
- `use` `codex-rs/app-server/src/message_processor.rs:5` `use crate::codex_message_processor::CodexMessageProcessor;`
- `use` `codex-rs/app-server/src/message_processor.rs:6` `use crate::codex_message_processor::CodexMessageProcessorArgs;`
- `use` `codex-rs/app-server/src/message_processor.rs:7` `use crate::config_api::ConfigApi;`
- `use` `codex-rs/app-server/src/message_processor.rs:8` `use crate::error_code::INVALID_REQUEST_ERROR_CODE;`
- `use` `codex-rs/app-server/src/message_processor.rs:9` `use crate::outgoing_message::ConnectionId;`
- `use` `codex-rs/app-server/src/message_processor.rs:10` `use crate::outgoing_message::ConnectionRequestId;`
- `use` `codex-rs/app-server/src/message_processor.rs:11` `use crate::outgoing_message::OutgoingMessageSender;`
- `use` `codex-rs/app-server/src/message_processor.rs:12` `use async_trait::async_trait;`
- `use` `codex-rs/app-server/src/message_processor.rs:13` `use codex_app_server_protocol::ChatgptAuthTokensRefreshParams;`
- `use` `codex-rs/app-server/src/message_processor.rs:14` `use codex_app_server_protocol::ChatgptAuthTokensRefreshReason;`
- `use` `codex-rs/app-server/src/message_processor.rs:15` `use codex_app_server_protocol::ChatgptAuthTokensRefreshResponse;`
- `use` `codex-rs/app-server/src/message_processor.rs:16` `use codex_app_server_protocol::ClientInfo;`
- `use` `codex-rs/app-server/src/message_processor.rs:17` `use codex_app_server_protocol::ClientRequest;`
- `use` `codex-rs/app-server/src/message_processor.rs:18` `use codex_app_server_protocol::ConfigBatchWriteParams;`
- `use` `codex-rs/app-server/src/message_processor.rs:19` `use codex_app_server_protocol::ConfigReadParams;`
- `use` `codex-rs/app-server/src/message_processor.rs:20` `use codex_app_server_protocol::ConfigValueWriteParams;`
- `use` `codex-rs/app-server/src/message_processor.rs:21` `use codex_app_server_protocol::ConfigWarningNotification;`
- `use` `codex-rs/app-server/src/message_processor.rs:22` `use codex_app_server_protocol::ExperimentalApi;`
- `use` `codex-rs/app-server/src/message_processor.rs:23` `use codex_app_server_protocol::InitializeResponse;`
- `use` `codex-rs/app-server/src/message_processor.rs:24` `use codex_app_server_protocol::JSONRPCError;`
- `use` `codex-rs/app-server/src/message_processor.rs:25` `use codex_app_server_protocol::JSONRPCErrorError;`
- `use` `codex-rs/app-server/src/message_processor.rs:26` `use codex_app_server_protocol::JSONRPCNotification;`
- `use` `codex-rs/app-server/src/message_processor.rs:27` `use codex_app_server_protocol::JSONRPCRequest;`
- `use` `codex-rs/app-server/src/message_processor.rs:28` `use codex_app_server_protocol::JSONRPCResponse;`
- `use` `codex-rs/app-server/src/message_processor.rs:29` `use codex_app_server_protocol::ServerNotification;`
- `use` `codex-rs/app-server/src/message_processor.rs:30` `use codex_app_server_protocol::ServerRequestPayload;`
- `use` `codex-rs/app-server/src/message_processor.rs:31` `use codex_app_server_protocol::experimental_required_message;`
- `use` `codex-rs/app-server/src/message_processor.rs:32` `use codex_core::AuthManager;`
- `use` `codex-rs/app-server/src/message_processor.rs:33` `use codex_core::ThreadManager;`
- `use` `codex-rs/app-server/src/message_processor.rs:34` `use codex_core::auth::ExternalAuthRefreshContext;`
- `use` `codex-rs/app-server/src/message_processor.rs:35` `use codex_core::auth::ExternalAuthRefreshReason;`
- `use` `codex-rs/app-server/src/message_processor.rs:36` `use codex_core::auth::ExternalAuthRefresher;`
- `use` `codex-rs/app-server/src/message_processor.rs:37` `use codex_core::auth::ExternalAuthTokens;`
- `use` `codex-rs/app-server/src/message_processor.rs:38` `use codex_core::config::Config;`
- `use` `codex-rs/app-server/src/message_processor.rs:39` `use codex_core::config_loader::CloudRequirementsLoader;`
- `use` `codex-rs/app-server/src/message_processor.rs:40` `use codex_core::config_loader::LoaderOverrides;`
- `use` `codex-rs/app-server/src/message_processor.rs:41` `use codex_core::default_client::SetOriginatorError;`
- `use` `codex-rs/app-server/src/message_processor.rs:42` `use codex_core::default_client::USER_AGENT_SUFFIX;`
- `use` `codex-rs/app-server/src/message_processor.rs:43` `use codex_core::default_client::get_codex_user_agent;`
- `use` `codex-rs/app-server/src/message_processor.rs:44` `use codex_core::default_client::set_default_client_residency_requirement;`
- `use` `codex-rs/app-server/src/message_processor.rs:45` `use codex_core::default_client::set_default_originator;`
- `use` `codex-rs/app-server/src/message_processor.rs:46` `use codex_feedback::CodexFeedback;`
- `use` `codex-rs/app-server/src/message_processor.rs:47` `use codex_protocol::ThreadId;`
- `use` `codex-rs/app-server/src/message_processor.rs:48` `use codex_protocol::protocol::SessionSource;`
- `use` `codex-rs/app-server/src/message_processor.rs:49` `use tokio::sync::broadcast;`
- `use` `codex-rs/app-server/src/message_processor.rs:50` `use tokio::time::Duration;`
- `use` `codex-rs/app-server/src/message_processor.rs:51` `use tokio::time::timeout;`
- `use` `codex-rs/app-server/src/message_processor.rs:52` `use toml::Value as TomlValue;`
- `const` `codex-rs/app-server/src/message_processor.rs:54` `const EXTERNAL_AUTH_REFRESH_TIMEOUT: Duration = Duration::from_secs(10);`
- `struct` `codex-rs/app-server/src/message_processor.rs:57` `struct ExternalAuthRefreshBridge {`
- `impl` `codex-rs/app-server/src/message_processor.rs:61` `impl ExternalAuthRefreshBridge {`
- `fn` `codex-rs/app-server/src/message_processor.rs:62` `fn map_reason(reason: ExternalAuthRefreshReason) -> ChatgptAuthTokensRefreshReason {`
- `impl` `codex-rs/app-server/src/message_processor.rs:70` `impl ExternalAuthRefresher for ExternalAuthRefreshBridge {`
- `fn` `codex-rs/app-server/src/message_processor.rs:71` `async fn refresh(`
- `impl` `codex-rs/app-server/src/message_processor.rs:133` `impl MessageProcessor {`
- `fn` `codex-rs/app-server/src/message_processor.rs:402` `async fn handle_config_read(&self, request_id: ConnectionRequestId, params: ConfigReadParams) {`
- `fn` `codex-rs/app-server/src/message_processor.rs:409` `async fn handle_config_value_write(`
- `fn` `codex-rs/app-server/src/message_processor.rs:420` `async fn handle_config_batch_write(`
- `fn` `codex-rs/app-server/src/message_processor.rs:431` `async fn handle_config_requirements_read(&self, request_id: ConnectionRequestId) {`

## Dependencies (auto sample)
### Imports / Includes
- `use std::path::PathBuf;`
- `use std::sync::Arc;`
- `use std::sync::RwLock;`
- `use crate::codex_message_processor::CodexMessageProcessor;`
- `use crate::codex_message_processor::CodexMessageProcessorArgs;`
- `use crate::config_api::ConfigApi;`
- `use crate::error_code::INVALID_REQUEST_ERROR_CODE;`
- `use crate::outgoing_message::ConnectionId;`
- `use crate::outgoing_message::ConnectionRequestId;`
- `use crate::outgoing_message::OutgoingMessageSender;`
- `use async_trait::async_trait;`
- `use codex_app_server_protocol::ChatgptAuthTokensRefreshParams;`
- `use codex_app_server_protocol::ChatgptAuthTokensRefreshReason;`
- `use codex_app_server_protocol::ChatgptAuthTokensRefreshResponse;`
- `use codex_app_server_protocol::ClientInfo;`
- `use codex_app_server_protocol::ClientRequest;`
- `use codex_app_server_protocol::ConfigBatchWriteParams;`
- `use codex_app_server_protocol::ConfigReadParams;`
- `use codex_app_server_protocol::ConfigValueWriteParams;`
- `use codex_app_server_protocol::ConfigWarningNotification;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- has retry/timeout/backoff logic
- returns structured errors (Result/ErrorKind)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
