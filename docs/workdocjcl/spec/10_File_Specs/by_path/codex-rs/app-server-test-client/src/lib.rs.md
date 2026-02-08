# `codex-rs/app-server-test-client/src/lib.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `36907`
- sha256: `77ed36b57d81677994697e722d5ae0881eacf714577e39367705b58b133036a0`
- generated_utc: `2026-02-08T10:45:14Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server-test-client/src/lib.rs` (read)

### Outputs / Side Effects
- spawns subprocesses
- writes to stdout/stderr

## Public Surface (auto)
- `pub fn run() -> Result<()> {`
- `pub fn send_message_v2(`

## Definitions (auto, per-file)
- `use` `codex-rs/app-server-test-client/src/lib.rs:1` `use std::collections::VecDeque;`
- `use` `codex-rs/app-server-test-client/src/lib.rs:2` `use std::fs;`
- `use` `codex-rs/app-server-test-client/src/lib.rs:3` `use std::io::BufRead;`
- `use` `codex-rs/app-server-test-client/src/lib.rs:4` `use std::io::BufReader;`
- `use` `codex-rs/app-server-test-client/src/lib.rs:5` `use std::io::Write;`
- `use` `codex-rs/app-server-test-client/src/lib.rs:6` `use std::path::Path;`
- `use` `codex-rs/app-server-test-client/src/lib.rs:7` `use std::path::PathBuf;`
- `use` `codex-rs/app-server-test-client/src/lib.rs:8` `use std::process::Child;`
- `use` `codex-rs/app-server-test-client/src/lib.rs:9` `use std::process::ChildStdin;`
- `use` `codex-rs/app-server-test-client/src/lib.rs:10` `use std::process::ChildStdout;`
- `use` `codex-rs/app-server-test-client/src/lib.rs:11` `use std::process::Command;`
- `use` `codex-rs/app-server-test-client/src/lib.rs:12` `use std::process::Stdio;`
- `use` `codex-rs/app-server-test-client/src/lib.rs:13` `use std::thread;`
- `use` `codex-rs/app-server-test-client/src/lib.rs:14` `use std::time::Duration;`
- `use` `codex-rs/app-server-test-client/src/lib.rs:16` `use anyhow::Context;`
- `use` `codex-rs/app-server-test-client/src/lib.rs:17` `use anyhow::Result;`
- `use` `codex-rs/app-server-test-client/src/lib.rs:18` `use anyhow::bail;`
- `use` `codex-rs/app-server-test-client/src/lib.rs:19` `use clap::ArgAction;`
- `use` `codex-rs/app-server-test-client/src/lib.rs:20` `use clap::Parser;`
- `use` `codex-rs/app-server-test-client/src/lib.rs:21` `use clap::Subcommand;`
- `use` `codex-rs/app-server-test-client/src/lib.rs:22` `use codex_app_server_protocol::AddConversationListenerParams;`
- `use` `codex-rs/app-server-test-client/src/lib.rs:23` `use codex_app_server_protocol::AddConversationSubscriptionResponse;`
- `use` `codex-rs/app-server-test-client/src/lib.rs:24` `use codex_app_server_protocol::AskForApproval;`
- `use` `codex-rs/app-server-test-client/src/lib.rs:25` `use codex_app_server_protocol::ClientInfo;`
- `use` `codex-rs/app-server-test-client/src/lib.rs:26` `use codex_app_server_protocol::ClientRequest;`
- `use` `codex-rs/app-server-test-client/src/lib.rs:27` `use codex_app_server_protocol::CommandExecutionApprovalDecision;`
- `use` `codex-rs/app-server-test-client/src/lib.rs:28` `use codex_app_server_protocol::CommandExecutionRequestApprovalParams;`
- `use` `codex-rs/app-server-test-client/src/lib.rs:29` `use codex_app_server_protocol::CommandExecutionRequestApprovalResponse;`
- `use` `codex-rs/app-server-test-client/src/lib.rs:30` `use codex_app_server_protocol::DynamicToolSpec;`
- `use` `codex-rs/app-server-test-client/src/lib.rs:31` `use codex_app_server_protocol::FileChangeApprovalDecision;`
- `use` `codex-rs/app-server-test-client/src/lib.rs:32` `use codex_app_server_protocol::FileChangeRequestApprovalParams;`
- `use` `codex-rs/app-server-test-client/src/lib.rs:33` `use codex_app_server_protocol::FileChangeRequestApprovalResponse;`
- `use` `codex-rs/app-server-test-client/src/lib.rs:34` `use codex_app_server_protocol::GetAccountRateLimitsResponse;`
- `use` `codex-rs/app-server-test-client/src/lib.rs:35` `use codex_app_server_protocol::InitializeCapabilities;`
- `use` `codex-rs/app-server-test-client/src/lib.rs:36` `use codex_app_server_protocol::InitializeParams;`
- `use` `codex-rs/app-server-test-client/src/lib.rs:37` `use codex_app_server_protocol::InitializeResponse;`
- `use` `codex-rs/app-server-test-client/src/lib.rs:38` `use codex_app_server_protocol::InputItem;`
- `use` `codex-rs/app-server-test-client/src/lib.rs:39` `use codex_app_server_protocol::JSONRPCMessage;`
- `use` `codex-rs/app-server-test-client/src/lib.rs:40` `use codex_app_server_protocol::JSONRPCNotification;`
- `use` `codex-rs/app-server-test-client/src/lib.rs:41` `use codex_app_server_protocol::JSONRPCRequest;`
- `use` `codex-rs/app-server-test-client/src/lib.rs:42` `use codex_app_server_protocol::JSONRPCResponse;`
- `use` `codex-rs/app-server-test-client/src/lib.rs:43` `use codex_app_server_protocol::LoginChatGptCompleteNotification;`
- `use` `codex-rs/app-server-test-client/src/lib.rs:44` `use codex_app_server_protocol::LoginChatGptResponse;`
- `use` `codex-rs/app-server-test-client/src/lib.rs:45` `use codex_app_server_protocol::ModelListParams;`
- `use` `codex-rs/app-server-test-client/src/lib.rs:46` `use codex_app_server_protocol::ModelListResponse;`
- `use` `codex-rs/app-server-test-client/src/lib.rs:47` `use codex_app_server_protocol::NewConversationParams;`
- `use` `codex-rs/app-server-test-client/src/lib.rs:48` `use codex_app_server_protocol::NewConversationResponse;`
- `use` `codex-rs/app-server-test-client/src/lib.rs:49` `use codex_app_server_protocol::RequestId;`
- `use` `codex-rs/app-server-test-client/src/lib.rs:50` `use codex_app_server_protocol::SandboxPolicy;`
- `use` `codex-rs/app-server-test-client/src/lib.rs:51` `use codex_app_server_protocol::SendUserMessageParams;`
- `use` `codex-rs/app-server-test-client/src/lib.rs:52` `use codex_app_server_protocol::SendUserMessageResponse;`
- `use` `codex-rs/app-server-test-client/src/lib.rs:53` `use codex_app_server_protocol::ServerNotification;`
- `use` `codex-rs/app-server-test-client/src/lib.rs:54` `use codex_app_server_protocol::ServerRequest;`
- `use` `codex-rs/app-server-test-client/src/lib.rs:55` `use codex_app_server_protocol::ThreadStartParams;`
- `use` `codex-rs/app-server-test-client/src/lib.rs:56` `use codex_app_server_protocol::ThreadStartResponse;`
- `use` `codex-rs/app-server-test-client/src/lib.rs:57` `use codex_app_server_protocol::TurnStartParams;`
- `use` `codex-rs/app-server-test-client/src/lib.rs:58` `use codex_app_server_protocol::TurnStartResponse;`
- `use` `codex-rs/app-server-test-client/src/lib.rs:59` `use codex_app_server_protocol::TurnStatus;`
- `use` `codex-rs/app-server-test-client/src/lib.rs:60` `use codex_app_server_protocol::UserInput as V2UserInput;`
- `use` `codex-rs/app-server-test-client/src/lib.rs:61` `use codex_protocol::ThreadId;`
- `use` `codex-rs/app-server-test-client/src/lib.rs:62` `use codex_protocol::protocol::Event;`
- `use` `codex-rs/app-server-test-client/src/lib.rs:63` `use codex_protocol::protocol::EventMsg;`
- `use` `codex-rs/app-server-test-client/src/lib.rs:64` `use serde::Serialize;`
- `use` `codex-rs/app-server-test-client/src/lib.rs:65` `use serde::de::DeserializeOwned;`
- `use` `codex-rs/app-server-test-client/src/lib.rs:66` `use serde_json::Value;`
- `use` `codex-rs/app-server-test-client/src/lib.rs:67` `use uuid::Uuid;`
- `struct` `codex-rs/app-server-test-client/src/lib.rs:72` `struct Cli {`
- `enum` `codex-rs/app-server-test-client/src/lib.rs:104` `enum CliCommand {`
- `fn` `codex-rs/app-server-test-client/src/lib.rs:146` `pub fn run() -> Result<()> {`
- `fn` `codex-rs/app-server-test-client/src/lib.rs:198` `fn send_message(codex_bin: &Path, config_overrides: &[String], user_message: String) -> Result<()> {`
- `fn` `codex-rs/app-server-test-client/src/lib.rs:220` `pub fn send_message_v2(`
- `fn` `codex-rs/app-server-test-client/src/lib.rs:236` `fn trigger_cmd_approval(`
- `fn` `codex-rs/app-server-test-client/src/lib.rs:255` `fn trigger_patch_approval(`
- `fn` `codex-rs/app-server-test-client/src/lib.rs:274` `fn no_trigger_cmd_approval(`
- `fn` `codex-rs/app-server-test-client/src/lib.rs:290` `fn send_message_v2_with_policies(`
- `fn` `codex-rs/app-server-test-client/src/lib.rs:328` `fn send_follow_up_v2(`
- `fn` `codex-rs/app-server-test-client/src/lib.rs:375` `fn test_login(codex_bin: &Path, config_overrides: &[String]) -> Result<()> {`
- `fn` `codex-rs/app-server-test-client/src/lib.rs:405` `fn get_account_rate_limits(codex_bin: &Path, config_overrides: &[String]) -> Result<()> {`
- `fn` `codex-rs/app-server-test-client/src/lib.rs:417` `fn model_list(codex_bin: &Path, config_overrides: &[String]) -> Result<()> {`
- `fn` `codex-rs/app-server-test-client/src/lib.rs:429` `fn ensure_dynamic_tools_unused(`
- `fn` `codex-rs/app-server-test-client/src/lib.rs:441` `fn parse_dynamic_tools_arg(dynamic_tools: &Option<String>) -> Result<Option<Vec<DynamicToolSpec>>> {`
- `struct` `codex-rs/app-server-test-client/src/lib.rs:463` `struct CodexClient {`
- `impl` `codex-rs/app-server-test-client/src/lib.rs:470` `impl CodexClient {`
- `fn` `codex-rs/app-server-test-client/src/lib.rs:471` `fn spawn(codex_bin: &Path, config_overrides: &[String]) -> Result<Self> {`
- `fn` `codex-rs/app-server-test-client/src/lib.rs:502` `fn initialize(&mut self) -> Result<InitializeResponse> {`
- `fn` `codex-rs/app-server-test-client/src/lib.rs:521` `fn start_thread(&mut self) -> Result<NewConversationResponse> {`
- `fn` `codex-rs/app-server-test-client/src/lib.rs:531` `fn add_conversation_listener(`
- `fn` `codex-rs/app-server-test-client/src/lib.rs:547` `fn remove_thread_listener(&mut self, subscription_id: Uuid) -> Result<()> {`
- `fn` `codex-rs/app-server-test-client/src/lib.rs:563` `fn send_user_message(`
- `fn` `codex-rs/app-server-test-client/src/lib.rs:584` `fn thread_start(&mut self, params: ThreadStartParams) -> Result<ThreadStartResponse> {`
- `fn` `codex-rs/app-server-test-client/src/lib.rs:594` `fn turn_start(&mut self, params: TurnStartParams) -> Result<TurnStartResponse> {`
- `fn` `codex-rs/app-server-test-client/src/lib.rs:604` `fn login_chat_gpt(&mut self) -> Result<LoginChatGptResponse> {`
- `fn` `codex-rs/app-server-test-client/src/lib.rs:614` `fn get_account_rate_limits(&mut self) -> Result<GetAccountRateLimitsResponse> {`
- `fn` `codex-rs/app-server-test-client/src/lib.rs:624` `fn model_list(&mut self, params: ModelListParams) -> Result<ModelListResponse> {`
- `fn` `codex-rs/app-server-test-client/src/lib.rs:634` `fn stream_conversation(&mut self, conversation_id: &ThreadId) -> Result<()> {`
- `fn` `codex-rs/app-server-test-client/src/lib.rs:672` `fn wait_for_login_completion(`
- `fn` `codex-rs/app-server-test-client/src/lib.rs:708` `fn stream_turn(&mut self, thread_id: &str, turn_id: &str) -> Result<()> {`
- `fn` `codex-rs/app-server-test-client/src/lib.rs:768` `fn extract_event(`
- `fn` `codex-rs/app-server-test-client/src/lib.rs:811` `fn write_request(&mut self, request: &ClientRequest) -> Result<()> {`
- `fn` `codex-rs/app-server-test-client/src/lib.rs:857` `fn next_notification(&mut self) -> Result<JSONRPCNotification> {`
- `fn` `codex-rs/app-server-test-client/src/lib.rs:878` `fn read_jsonrpc_message(&mut self) -> Result<JSONRPCMessage> {`
- `fn` `codex-rs/app-server-test-client/src/lib.rs:905` `fn request_id(&self) -> RequestId {`
- `fn` `codex-rs/app-server-test-client/src/lib.rs:909` `fn handle_server_request(&mut self, request: JSONRPCRequest) -> Result<()> {`
- `fn` `codex-rs/app-server-test-client/src/lib.rs:928` `fn handle_command_execution_request_approval(`
- `fn` `codex-rs/app-server-test-client/src/lib.rs:973` `fn approve_file_change_request(`
- `fn` `codex-rs/app-server-test-client/src/lib.rs:1015` `fn write_jsonrpc_message(&mut self, message: JSONRPCMessage) -> Result<()> {`
- `fn` `codex-rs/app-server-test-client/src/lib.rs:1032` `fn print_multiline_with_prefix(prefix: &str, payload: &str) {`
- `impl` `codex-rs/app-server-test-client/src/lib.rs:1038` `impl Drop for CodexClient {`
- `fn` `codex-rs/app-server-test-client/src/lib.rs:1039` `fn drop(&mut self) {`

## Dependencies (auto sample)
### Imports / Includes
- `use std::collections::VecDeque;`
- `use std::fs;`
- `use std::io::BufRead;`
- `use std::io::BufReader;`
- `use std::io::Write;`
- `use std::path::Path;`
- `use std::path::PathBuf;`
- `use std::process::Child;`
- `use std::process::ChildStdin;`
- `use std::process::ChildStdout;`
- `use std::process::Command;`
- `use std::process::Stdio;`
- `use std::thread;`
- `use std::time::Duration;`
- `use anyhow::Context;`
- `use anyhow::Result;`
- `use anyhow::bail;`
- `use clap::ArgAction;`
- `use clap::Parser;`
- `use clap::Subcommand;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
