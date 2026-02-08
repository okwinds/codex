# `codex-rs/rmcp-client/src/logging_client_handler.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `4149`
- sha256: `2a3eafc83517fb132c7929c2e3ec9a1a0a8dbe37daedb343229de4047dae4c7c`
- generated_utc: `2026-02-08T10:45:38Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/rmcp-client/src/logging_client_handler.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `use` `codex-rs/rmcp-client/src/logging_client_handler.rs:1` `use std::sync::Arc;`
- `use` `codex-rs/rmcp-client/src/logging_client_handler.rs:3` `use rmcp::ClientHandler;`
- `use` `codex-rs/rmcp-client/src/logging_client_handler.rs:4` `use rmcp::RoleClient;`
- `use` `codex-rs/rmcp-client/src/logging_client_handler.rs:5` `use rmcp::model::CancelledNotificationParam;`
- `use` `codex-rs/rmcp-client/src/logging_client_handler.rs:6` `use rmcp::model::ClientInfo;`
- `use` `codex-rs/rmcp-client/src/logging_client_handler.rs:7` `use rmcp::model::CreateElicitationRequestParam;`
- `use` `codex-rs/rmcp-client/src/logging_client_handler.rs:8` `use rmcp::model::CreateElicitationResult;`
- `use` `codex-rs/rmcp-client/src/logging_client_handler.rs:9` `use rmcp::model::LoggingLevel;`
- `use` `codex-rs/rmcp-client/src/logging_client_handler.rs:10` `use rmcp::model::LoggingMessageNotificationParam;`
- `use` `codex-rs/rmcp-client/src/logging_client_handler.rs:11` `use rmcp::model::ProgressNotificationParam;`
- `use` `codex-rs/rmcp-client/src/logging_client_handler.rs:12` `use rmcp::model::ResourceUpdatedNotificationParam;`
- `use` `codex-rs/rmcp-client/src/logging_client_handler.rs:13` `use rmcp::service::NotificationContext;`
- `use` `codex-rs/rmcp-client/src/logging_client_handler.rs:14` `use rmcp::service::RequestContext;`
- `use` `codex-rs/rmcp-client/src/logging_client_handler.rs:15` `use tracing::debug;`
- `use` `codex-rs/rmcp-client/src/logging_client_handler.rs:16` `use tracing::error;`
- `use` `codex-rs/rmcp-client/src/logging_client_handler.rs:17` `use tracing::info;`
- `use` `codex-rs/rmcp-client/src/logging_client_handler.rs:18` `use tracing::warn;`
- `use` `codex-rs/rmcp-client/src/logging_client_handler.rs:20` `use crate::rmcp_client::SendElicitation;`
- `impl` `codex-rs/rmcp-client/src/logging_client_handler.rs:28` `impl LoggingClientHandler {`
- `impl` `codex-rs/rmcp-client/src/logging_client_handler.rs:37` `impl ClientHandler for LoggingClientHandler {`
- `fn` `codex-rs/rmcp-client/src/logging_client_handler.rs:38` `async fn create_elicitation(`
- `fn` `codex-rs/rmcp-client/src/logging_client_handler.rs:48` `async fn on_cancelled(`
- `fn` `codex-rs/rmcp-client/src/logging_client_handler.rs:59` `async fn on_progress(`
- `fn` `codex-rs/rmcp-client/src/logging_client_handler.rs:70` `async fn on_resource_updated(`
- `fn` `codex-rs/rmcp-client/src/logging_client_handler.rs:78` `async fn on_resource_list_changed(&self, _context: NotificationContext<RoleClient>) {`
- `fn` `codex-rs/rmcp-client/src/logging_client_handler.rs:82` `async fn on_tool_list_changed(&self, _context: NotificationContext<RoleClient>) {`
- `fn` `codex-rs/rmcp-client/src/logging_client_handler.rs:86` `async fn on_prompt_list_changed(&self, _context: NotificationContext<RoleClient>) {`
- `fn` `codex-rs/rmcp-client/src/logging_client_handler.rs:90` `fn get_info(&self) -> ClientInfo {`
- `fn` `codex-rs/rmcp-client/src/logging_client_handler.rs:94` `async fn on_logging_message(`

## Dependencies (auto sample)
### Imports / Includes
- `use std::sync::Arc;`
- `use rmcp::ClientHandler;`
- `use rmcp::RoleClient;`
- `use rmcp::model::CancelledNotificationParam;`
- `use rmcp::model::ClientInfo;`
- `use rmcp::model::CreateElicitationRequestParam;`
- `use rmcp::model::CreateElicitationResult;`
- `use rmcp::model::LoggingLevel;`
- `use rmcp::model::LoggingMessageNotificationParam;`
- `use rmcp::model::ProgressNotificationParam;`
- `use rmcp::model::ResourceUpdatedNotificationParam;`
- `use rmcp::service::NotificationContext;`
- `use rmcp::service::RequestContext;`
- `use tracing::debug;`
- `use tracing::error;`
- `use tracing::info;`
- `use tracing::warn;`
- `use crate::rmcp_client::SendElicitation;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
