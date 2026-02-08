# Rust Symbol Index

- generated_utc: `2026-02-03T14:49:41Z`
- symbol_count: `3173`

| Kind | Location | Signature |
|---|---|---|
| `pub_fn` | `codex-rs/ansi-escape/src/lib.rs:26` | `pub fn ansi_escape_line(s: &str) -> Line<'static> {` |
| `pub_fn` | `codex-rs/ansi-escape/src/lib.rs:40` | `pub fn ansi_escape(s: &str) -> Text<'static> {` |
| `fn_main` | `codex-rs/app-server-protocol/src/bin/export.rs:19` | `fn main() -> Result<()> {` |
| `fn_main` | `codex-rs/app-server-protocol/src/bin/write_schema_fixtures.rs:22` | `fn main() -> Result<()> {` |
| `pub_trait` | `codex-rs/app-server-protocol/src/experimental_api.rs:2` | `pub trait ExperimentalApi {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/experimental_api.rs:10` | `pub struct ExperimentalField {` |
| `pub_fn` | `codex-rs/app-server-protocol/src/experimental_api.rs:22` | `pub fn experimental_fields() -> Vec<&'static ExperimentalField> {` |
| `pub_fn` | `codex-rs/app-server-protocol/src/experimental_api.rs:27` | `pub fn experimental_required_message(reason: &str) -> String {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/export.rs:41` | `pub struct GeneratedSchema {` |
| `pub_fn` | `codex-rs/app-server-protocol/src/export.rs:63` | `pub fn generate_types(out_dir: &Path, prettier: Option<&Path>) -> Result<()> {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/export.rs:70` | `pub struct GenerateTsOptions {` |
| `pub_fn` | `codex-rs/app-server-protocol/src/export.rs:88` | `pub fn generate_ts(out_dir: &Path, prettier: Option<&Path>) -> Result<()> {` |
| `pub_fn` | `codex-rs/app-server-protocol/src/export.rs:92` | `pub fn generate_ts_with_options(` |
| `pub_fn` | `codex-rs/app-server-protocol/src/export.rs:152` | `pub fn generate_json(out_dir: &Path) -> Result<()> {` |
| `pub_fn` | `codex-rs/app-server-protocol/src/export.rs:156` | `pub fn generate_json_with_experimental(out_dir: &Path, experimental_api: bool) -> Result<()> {` |
| `pub_const` | `codex-rs/app-server-protocol/src/jsonrpc_lite.rs:9` | `pub const JSONRPC_VERSION: &str = "2.0";` |
| `pub_enum` | `codex-rs/app-server-protocol/src/jsonrpc_lite.rs:13` | `pub enum RequestId {` |
| `pub_type` | `codex-rs/app-server-protocol/src/jsonrpc_lite.rs:19` | `pub type Result = serde_json::Value;` |
| `pub_enum` | `codex-rs/app-server-protocol/src/jsonrpc_lite.rs:24` | `pub enum JSONRPCMessage {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/jsonrpc_lite.rs:33` | `pub struct JSONRPCRequest {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/jsonrpc_lite.rs:43` | `pub struct JSONRPCNotification {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/jsonrpc_lite.rs:52` | `pub struct JSONRPCResponse {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/jsonrpc_lite.rs:59` | `pub struct JSONRPCError {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/jsonrpc_lite.rs:65` | `pub struct JSONRPCErrorError {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/common.rs:18` | `pub struct GitSha(pub String);` |
| `pub_fn` | `codex-rs/app-server-protocol/src/protocol/common.rs:21` | `pub fn new(sha: &str) -> Self {` |
| `pub_enum` | `codex-rs/app-server-protocol/src/protocol/common.rs:29` | `pub enum AuthMode {` |
| `pub_enum` | `codex-rs/app-server-protocol/src/protocol/common.rs:99` | `pub enum ClientRequest {` |
| `pub_fn` | `codex-rs/app-server-protocol/src/protocol/common.rs:144` | `pub fn export_client_responses(` |
| `pub_fn` | `codex-rs/app-server-protocol/src/protocol/common.rs:154` | `pub fn export_client_response_schemas(` |
| `pub_fn` | `codex-rs/app-server-protocol/src/protocol/common.rs:165` | `pub fn export_client_param_schemas(` |
| `pub_enum` | `codex-rs/app-server-protocol/src/protocol/common.rs:456` | `pub enum ServerRequest {` |
| `pub_enum` | `codex-rs/app-server-protocol/src/protocol/common.rs:469` | `pub enum ServerRequestPayload {` |
| `pub_fn` | `codex-rs/app-server-protocol/src/protocol/common.rs:474` | `pub fn request_with_id(self, request_id: RequestId) -> ServerRequest {` |
| `pub_fn` | `codex-rs/app-server-protocol/src/protocol/common.rs:481` | `pub fn export_server_responses(` |
| `pub_fn` | `codex-rs/app-server-protocol/src/protocol/common.rs:491` | `pub fn export_server_response_schemas(` |
| `pub_fn` | `codex-rs/app-server-protocol/src/protocol/common.rs:505` | `pub fn export_server_param_schemas(` |
| `pub_enum` | `codex-rs/app-server-protocol/src/protocol/common.rs:533` | `pub enum ServerNotification {` |
| `pub_fn` | `codex-rs/app-server-protocol/src/protocol/common.rs:542` | `pub fn to_params(self) -> Result<serde_json::Value, serde_json::Error> {` |
| `pub_fn` | `codex-rs/app-server-protocol/src/protocol/common.rs:558` | `pub fn export_server_notification_schemas(` |
| `pub_enum` | `codex-rs/app-server-protocol/src/protocol/common.rs:578` | `pub enum ClientNotification {` |
| `pub_fn` | `codex-rs/app-server-protocol/src/protocol/common.rs:585` | `pub fn export_client_notification_schemas(` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/common.rs:654` | `pub struct FuzzyFileSearchParams {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/common.rs:663` | `pub struct FuzzyFileSearchResult {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/common.rs:672` | `pub struct FuzzyFileSearchResponse {` |
| `pub_mod` | `codex-rs/app-server-protocol/src/protocol/mod.rs:4` | `pub mod common;` |
| `pub_mod` | `codex-rs/app-server-protocol/src/protocol/mod.rs:6` | `pub mod thread_history;` |
| `pub_mod` | `codex-rs/app-server-protocol/src/protocol/mod.rs:7` | `pub mod v1;` |
| `pub_mod` | `codex-rs/app-server-protocol/src/protocol/mod.rs:8` | `pub mod v2;` |
| `pub_fn` | `codex-rs/app-server-protocol/src/protocol/thread_history.rs:19` | `pub fn build_turns_from_event_msgs(events: &[EventMsg]) -> Vec<Turn> {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v1.rs:34` | `pub struct InitializeParams {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v1.rs:42` | `pub struct ClientInfo {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v1.rs:51` | `pub struct InitializeCapabilities {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v1.rs:59` | `pub struct InitializeResponse {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v1.rs:65` | `pub struct NewConversationParams {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v1.rs:83` | `pub struct NewConversationResponse {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v1.rs:92` | `pub struct ResumeConversationResponse {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v1.rs:101` | `pub struct ForkConversationResponse {` |
| `pub_enum` | `codex-rs/app-server-protocol/src/protocol/v1.rs:110` | `pub enum GetConversationSummaryParams {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v1.rs:123` | `pub struct GetConversationSummaryResponse {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v1.rs:129` | `pub struct ListConversationsParams {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v1.rs:137` | `pub struct ConversationSummary {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v1.rs:152` | `pub struct ConversationGitInfo {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v1.rs:160` | `pub struct ListConversationsResponse {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v1.rs:167` | `pub struct ResumeConversationParams {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v1.rs:176` | `pub struct ForkConversationParams {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v1.rs:184` | `pub struct AddConversationSubscriptionResponse {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v1.rs:191` | `pub struct ArchiveConversationParams {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v1.rs:198` | `pub struct ArchiveConversationResponse {}` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v1.rs:202` | `pub struct RemoveConversationSubscriptionResponse {}` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v1.rs:206` | `pub struct LoginApiKeyParams {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v1.rs:212` | `pub struct LoginApiKeyResponse {}` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v1.rs:216` | `pub struct LoginChatGptResponse {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v1.rs:224` | `pub struct GitDiffToRemoteResponse {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v1.rs:231` | `pub struct ApplyPatchApprovalParams {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v1.rs:246` | `pub struct ApplyPatchApprovalResponse {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v1.rs:252` | `pub struct ExecCommandApprovalParams {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v1.rs:264` | `pub struct ExecCommandApprovalResponse {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v1.rs:270` | `pub struct CancelLoginChatGptParams {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v1.rs:277` | `pub struct GitDiffToRemoteParams {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v1.rs:283` | `pub struct CancelLoginChatGptResponse {}` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v1.rs:287` | `pub struct LogoutChatGptParams {}` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v1.rs:291` | `pub struct LogoutChatGptResponse {}` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v1.rs:295` | `pub struct GetAuthStatusParams {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v1.rs:302` | `pub struct ExecOneOffCommandParams {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v1.rs:311` | `pub struct ExecOneOffCommandResponse {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v1.rs:319` | `pub struct GetAuthStatusResponse {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v1.rs:327` | `pub struct GetUserAgentResponse {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v1.rs:333` | `pub struct UserInfoResponse {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v1.rs:339` | `pub struct GetUserSavedConfigResponse {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v1.rs:345` | `pub struct SetDefaultModelParams {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v1.rs:352` | `pub struct SetDefaultModelResponse {}` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v1.rs:356` | `pub struct UserSavedConfig {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v1.rs:373` | `pub struct Profile {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v1.rs:385` | `pub struct Tools {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v1.rs:392` | `pub struct SandboxSettings {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v1.rs:402` | `pub struct SendUserMessageParams {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v1.rs:409` | `pub struct SendUserTurnParams {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v1.rs:424` | `pub struct SendUserTurnResponse {}` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v1.rs:428` | `pub struct InterruptConversationParams {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v1.rs:434` | `pub struct InterruptConversationResponse {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v1.rs:440` | `pub struct SendUserMessageResponse {}` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v1.rs:444` | `pub struct AddConversationListenerParams {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v1.rs:452` | `pub struct RemoveConversationListenerParams {` |
| `pub_enum` | `codex-rs/app-server-protocol/src/protocol/v1.rs:460` | `pub enum InputItem {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v1.rs:478` | `pub struct V1ByteRange {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v1.rs:506` | `pub struct V1TextElement {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v1.rs:531` | `pub struct LoginChatGptCompleteNotification {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v1.rs:540` | `pub struct SessionConfiguredNotification {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v1.rs:554` | `pub struct AuthStatusChangeNotification {` |
| `pub_fn` | `codex-rs/app-server-protocol/src/protocol/v2.rs:68` | `pub fn to_core(self) -> $Src {` |
| `pub_enum` | `codex-rs/app-server-protocol/src/protocol/v2.rs:88` | `pub enum CodexErrorInfo {` |
| `pub_enum` | `codex-rs/app-server-protocol/src/protocol/v2.rs:163` | `pub enum AskForApproval {` |
| `pub_fn` | `codex-rs/app-server-protocol/src/protocol/v2.rs:173` | `pub fn to_core(self) -> CoreAskForApproval {` |
| `pub_enum` | `codex-rs/app-server-protocol/src/protocol/v2.rs:197` | `pub enum SandboxMode {` |
| `pub_fn` | `codex-rs/app-server-protocol/src/protocol/v2.rs:204` | `pub fn to_core(self) -> CoreSandboxMode {` |
| `pub_enum` | `codex-rs/app-server-protocol/src/protocol/v2.rs:224` | `pub enum ReviewDelivery from codex_protocol::protocol::ReviewDelivery {` |
| `pub_enum` | `codex-rs/app-server-protocol/src/protocol/v2.rs:230` | `pub enum McpAuthStatus from codex_protocol::protocol::McpAuthStatus {` |
| `pub_enum` | `codex-rs/app-server-protocol/src/protocol/v2.rs:242` | `pub enum ConfigLayerSource {` |
| `pub_fn` | `codex-rs/app-server-protocol/src/protocol/v2.rs:299` | `pub fn precedence(&self) -> i16 {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v2.rs:323` | `pub struct SandboxWorkspaceWrite {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v2.rs:337` | `pub struct ToolsV2 {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v2.rs:346` | `pub struct DynamicToolSpec {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v2.rs:355` | `pub struct ProfileV2 {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v2.rs:371` | `pub struct AnalyticsConfig {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v2.rs:380` | `pub struct Config {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v2.rs:410` | `pub struct ConfigLayerMetadata {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v2.rs:418` | `pub struct ConfigLayer {` |
| `pub_enum` | `codex-rs/app-server-protocol/src/protocol/v2.rs:429` | `pub enum MergeStrategy {` |
| `pub_enum` | `codex-rs/app-server-protocol/src/protocol/v2.rs:437` | `pub enum WriteStatus {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v2.rs:445` | `pub struct OverriddenMetadata {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v2.rs:454` | `pub struct ConfigWriteResponse {` |
| `pub_enum` | `codex-rs/app-server-protocol/src/protocol/v2.rs:465` | `pub enum ConfigWriteErrorCode {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v2.rs:477` | `pub struct ConfigReadParams {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v2.rs:489` | `pub struct ConfigReadResponse {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v2.rs:499` | `pub struct ConfigRequirements {` |
| `pub_enum` | `codex-rs/app-server-protocol/src/protocol/v2.rs:508` | `pub enum ResidencyRequirement {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v2.rs:515` | `pub struct ConfigRequirementsReadResponse {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v2.rs:523` | `pub struct ConfigValueWriteParams {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v2.rs:535` | `pub struct ConfigBatchWriteParams {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v2.rs:545` | `pub struct ConfigEdit {` |
| `pub_enum` | `codex-rs/app-server-protocol/src/protocol/v2.rs:554` | `pub enum CommandExecutionApprovalDecision {` |
| `pub_enum` | `codex-rs/app-server-protocol/src/protocol/v2.rs:573` | `pub enum FileChangeApprovalDecision {` |
| `pub_enum` | `codex-rs/app-server-protocol/src/protocol/v2.rs:587` | `pub enum NetworkAccess {` |
| `pub_enum` | `codex-rs/app-server-protocol/src/protocol/v2.rs:597` | `pub enum SandboxPolicy {` |
| `pub_fn` | `codex-rs/app-server-protocol/src/protocol/v2.rs:621` | `pub fn to_core(&self) -> codex_protocol::protocol::SandboxPolicy {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v2.rs:683` | `pub struct ExecPolicyAmendment {` |
| `pub_fn` | `codex-rs/app-server-protocol/src/protocol/v2.rs:688` | `pub fn into_core(self) -> CoreExecPolicyAmendment {` |
| `pub_enum` | `codex-rs/app-server-protocol/src/protocol/v2.rs:705` | `pub enum CommandAction {` |
| `pub_enum` | `codex-rs/app-server-protocol/src/protocol/v2.rs:729` | `pub enum SessionSource {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v2.rs:771` | `pub struct GitInfo {` |
| `pub_fn` | `codex-rs/app-server-protocol/src/protocol/v2.rs:778` | `pub fn into_core(self) -> CoreParsedCommand {` |
| `pub_enum` | `codex-rs/app-server-protocol/src/protocol/v2.rs:823` | `pub enum Account {` |
| `pub_enum` | `codex-rs/app-server-protocol/src/protocol/v2.rs:837` | `pub enum LoginAccountParams {` |
| `pub_enum` | `codex-rs/app-server-protocol/src/protocol/v2.rs:872` | `pub enum LoginAccountResponse {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v2.rs:893` | `pub struct CancelLoginAccountParams {` |
| `pub_enum` | `codex-rs/app-server-protocol/src/protocol/v2.rs:901` | `pub enum CancelLoginAccountStatus {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v2.rs:909` | `pub struct CancelLoginAccountResponse {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v2.rs:916` | `pub struct LogoutAccountResponse {}` |
| `pub_enum` | `codex-rs/app-server-protocol/src/protocol/v2.rs:921` | `pub enum ChatgptAuthTokensRefreshReason {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v2.rs:929` | `pub struct ChatgptAuthTokensRefreshParams {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v2.rs:944` | `pub struct ChatgptAuthTokensRefreshResponse {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v2.rs:952` | `pub struct GetAccountRateLimitsResponse {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v2.rs:959` | `pub struct GetAccountParams {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v2.rs:972` | `pub struct GetAccountResponse {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v2.rs:980` | `pub struct ModelListParams {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v2.rs:990` | `pub struct Model {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v2.rs:1008` | `pub struct ReasoningEffortOption {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v2.rs:1016` | `pub struct ModelListResponse {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v2.rs:1027` | `pub struct CollaborationModeListParams {}` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v2.rs:1033` | `pub struct CollaborationModeListResponse {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v2.rs:1040` | `pub struct ListMcpServerStatusParams {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v2.rs:1050` | `pub struct McpServerStatus {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v2.rs:1061` | `pub struct ListMcpServerStatusResponse {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v2.rs:1071` | `pub struct AppsListParams {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v2.rs:1081` | `pub struct AppInfo {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v2.rs:1096` | `pub struct AppsListResponse {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v2.rs:1106` | `pub struct McpServerRefreshParams {}` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v2.rs:1111` | `pub struct McpServerRefreshResponse {}` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v2.rs:1116` | `pub struct McpServerOauthLoginParams {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v2.rs:1129` | `pub struct McpServerOauthLoginResponse {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v2.rs:1136` | `pub struct FeedbackUploadParams {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v2.rs:1146` | `pub struct FeedbackUploadResponse {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v2.rs:1153` | `pub struct CommandExecParams {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v2.rs:1164` | `pub struct CommandExecResponse {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v2.rs:1177` | `pub struct ThreadStartParams {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v2.rs:1205` | `pub struct MockExperimentalMethodParams {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v2.rs:1213` | `pub struct MockExperimentalMethodResponse {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v2.rs:1221` | `pub struct ThreadStartResponse {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v2.rs:1243` | `pub struct ThreadResumeParams {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v2.rs:1270` | `pub struct ThreadResumeResponse {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v2.rs:1290` | `pub struct ThreadForkParams {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v2.rs:1311` | `pub struct ThreadForkResponse {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v2.rs:1324` | `pub struct ThreadArchiveParams {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v2.rs:1331` | `pub struct ThreadArchiveResponse {}` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v2.rs:1336` | `pub struct ThreadSetNameParams {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v2.rs:1344` | `pub struct ThreadUnarchiveParams {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v2.rs:1351` | `pub struct ThreadSetNameResponse {}` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v2.rs:1356` | `pub struct ThreadUnarchiveResponse {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v2.rs:1363` | `pub struct ThreadRollbackParams {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v2.rs:1375` | `pub struct ThreadRollbackResponse {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v2.rs:1387` | `pub struct ThreadListParams {` |
| `pub_enum` | `codex-rs/app-server-protocol/src/protocol/v2.rs:1408` | `pub enum ThreadSourceKind {` |
| `pub_enum` | `codex-rs/app-server-protocol/src/protocol/v2.rs:1426` | `pub enum ThreadSortKey {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v2.rs:1434` | `pub struct ThreadListResponse {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v2.rs:1444` | `pub struct ThreadLoadedListParams {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v2.rs:1454` | `pub struct ThreadLoadedListResponse {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v2.rs:1465` | `pub struct ThreadReadParams {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v2.rs:1475` | `pub struct ThreadReadResponse {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v2.rs:1482` | `pub struct SkillsListParams {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v2.rs:1495` | `pub struct SkillsListResponse {` |
| `pub_enum` | `codex-rs/app-server-protocol/src/protocol/v2.rs:1503` | `pub enum SkillScope {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v2.rs:1513` | `pub struct SkillMetadata {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v2.rs:1534` | `pub struct SkillInterface {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v2.rs:1552` | `pub struct SkillDependencies {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v2.rs:1559` | `pub struct SkillToolDependency {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v2.rs:1581` | `pub struct SkillErrorInfo {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v2.rs:1589` | `pub struct SkillsListEntry {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v2.rs:1598` | `pub struct SkillsConfigWriteParams {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v2.rs:1606` | `pub struct SkillsConfigWriteResponse {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v2.rs:1686` | `pub struct Thread {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v2.rs:1718` | `pub struct AccountUpdatedNotification {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v2.rs:1725` | `pub struct ThreadTokenUsageUpdatedNotification {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v2.rs:1734` | `pub struct ThreadTokenUsage {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v2.rs:1755` | `pub struct TokenUsageBreakdown {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v2.rs:1783` | `pub struct Turn {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v2.rs:1798` | `pub struct TurnError {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v2.rs:1808` | `pub struct ErrorNotification {` |
| `pub_enum` | `codex-rs/app-server-protocol/src/protocol/v2.rs:1820` | `pub enum TurnStatus {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v2.rs:1831` | `pub struct TurnStartParams {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v2.rs:1859` | `pub struct ReviewStartParams {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v2.rs:1872` | `pub struct ReviewStartResponse {` |
| `pub_enum` | `codex-rs/app-server-protocol/src/protocol/v2.rs:1884` | `pub enum ReviewTarget {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v2.rs:1911` | `pub struct TurnStartResponse {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v2.rs:1918` | `pub struct TurnInterruptParams {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v2.rs:1926` | `pub struct TurnInterruptResponse {}` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v2.rs:1932` | `pub struct ByteRange {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v2.rs:1958` | `pub struct TextElement {` |
| `pub_fn` | `codex-rs/app-server-protocol/src/protocol/v2.rs:1966` | `pub fn new(byte_range: ByteRange, placeholder: Option<String>) -> Self {` |
| `pub_fn` | `codex-rs/app-server-protocol/src/protocol/v2.rs:1973` | `pub fn set_placeholder(&mut self, placeholder: Option<String>) {` |
| `pub_fn` | `codex-rs/app-server-protocol/src/protocol/v2.rs:1977` | `pub fn placeholder(&self) -> Option<&str> {` |
| `pub_enum` | `codex-rs/app-server-protocol/src/protocol/v2.rs:2001` | `pub enum UserInput {` |
| `pub_fn` | `codex-rs/app-server-protocol/src/protocol/v2.rs:2025` | `pub fn into_core(self) -> CoreUserInput {` |
| `pub_enum` | `codex-rs/app-server-protocol/src/protocol/v2.rs:2065` | `pub enum ThreadItem {` |
| `pub_enum` | `codex-rs/app-server-protocol/src/protocol/v2.rs:2173` | `pub enum WebSearchAction {` |
| `pub_enum` | `codex-rs/app-server-protocol/src/protocol/v2.rs:2247` | `pub enum CommandExecutionStatus {` |
| `pub_enum` | `codex-rs/app-server-protocol/src/protocol/v2.rs:2257` | `pub enum CollabAgentTool {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v2.rs:2267` | `pub struct FileUpdateChange {` |
| `pub_enum` | `codex-rs/app-server-protocol/src/protocol/v2.rs:2277` | `pub enum PatchChangeKind {` |
| `pub_enum` | `codex-rs/app-server-protocol/src/protocol/v2.rs:2286` | `pub enum PatchApplyStatus {` |
| `pub_enum` | `codex-rs/app-server-protocol/src/protocol/v2.rs:2296` | `pub enum McpToolCallStatus {` |
| `pub_enum` | `codex-rs/app-server-protocol/src/protocol/v2.rs:2305` | `pub enum CollabAgentToolCallStatus {` |
| `pub_enum` | `codex-rs/app-server-protocol/src/protocol/v2.rs:2314` | `pub enum CollabAgentStatus {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v2.rs:2326` | `pub struct CollabAgentState {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v2.rs:2365` | `pub struct McpToolCallResult {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v2.rs:2378` | `pub struct McpToolCallError {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v2.rs:2387` | `pub struct ThreadStartedNotification {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v2.rs:2394` | `pub struct ThreadNameUpdatedNotification {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v2.rs:2404` | `pub struct TurnStartedNotification {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v2.rs:2412` | `pub struct Usage {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v2.rs:2421` | `pub struct TurnCompletedNotification {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v2.rs:2431` | `pub struct TurnDiffUpdatedNotification {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v2.rs:2440` | `pub struct TurnPlanUpdatedNotification {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v2.rs:2450` | `pub struct TurnPlanStep {` |
| `pub_enum` | `codex-rs/app-server-protocol/src/protocol/v2.rs:2458` | `pub enum TurnPlanStepStatus {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v2.rs:2486` | `pub struct ItemStartedNotification {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v2.rs:2495` | `pub struct ItemCompletedNotification {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v2.rs:2504` | `pub struct RawResponseItemCompletedNotification {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v2.rs:2514` | `pub struct AgentMessageDeltaNotification {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v2.rs:2526` | `pub struct PlanDeltaNotification {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v2.rs:2536` | `pub struct ReasoningSummaryTextDeltaNotification {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v2.rs:2548` | `pub struct ReasoningSummaryPartAddedNotification {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v2.rs:2559` | `pub struct ReasoningTextDeltaNotification {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v2.rs:2571` | `pub struct TerminalInteractionNotification {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v2.rs:2582` | `pub struct CommandExecutionOutputDeltaNotification {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v2.rs:2592` | `pub struct FileChangeOutputDeltaNotification {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v2.rs:2602` | `pub struct McpToolCallProgressNotification {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v2.rs:2612` | `pub struct McpServerOauthLoginCompletedNotification {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v2.rs:2623` | `pub struct WindowsWorldWritableWarningNotification {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v2.rs:2633` | `pub struct ContextCompactedNotification {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v2.rs:2641` | `pub struct CommandExecutionRequestApprovalParams {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v2.rs:2666` | `pub struct CommandExecutionRequestApprovalResponse {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v2.rs:2673` | `pub struct FileChangeRequestApprovalParams {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v2.rs:2686` | `pub struct FileChangeRequestApprovalResponse {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v2.rs:2693` | `pub struct DynamicToolCallParams {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v2.rs:2704` | `pub struct DynamicToolCallResponse {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v2.rs:2713` | `pub struct ToolRequestUserInputOption {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v2.rs:2722` | `pub struct ToolRequestUserInputQuestion {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v2.rs:2737` | `pub struct ToolRequestUserInputParams {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v2.rs:2748` | `pub struct ToolRequestUserInputAnswer {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v2.rs:2756` | `pub struct ToolRequestUserInputResponse {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v2.rs:2763` | `pub struct AccountRateLimitsUpdatedNotification {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v2.rs:2770` | `pub struct RateLimitSnapshot {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v2.rs:2791` | `pub struct RateLimitWindow {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v2.rs:2812` | `pub struct CreditsSnapshot {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v2.rs:2831` | `pub struct AccountLoginCompletedNotification {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v2.rs:2842` | `pub struct DeprecationNoticeNotification {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v2.rs:2852` | `pub struct TextPosition {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v2.rs:2862` | `pub struct TextRange {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/protocol/v2.rs:2870` | `pub struct ConfigWarningNotification {` |
| `pub_struct` | `codex-rs/app-server-protocol/src/schema_fixtures.rs:11` | `pub struct SchemaFixtureOptions {` |
| `pub_fn` | `codex-rs/app-server-protocol/src/schema_fixtures.rs:15` | `pub fn read_schema_fixture_tree(schema_root: &Path) -> Result<BTreeMap<PathBuf, Vec<u8>>> {` |
| `pub_fn` | `codex-rs/app-server-protocol/src/schema_fixtures.rs:34` | `pub fn write_schema_fixtures(schema_root: &Path, prettier: Option<&Path>) -> Result<()> {` |
| `pub_fn` | `codex-rs/app-server-protocol/src/schema_fixtures.rs:39` | `pub fn write_schema_fixtures_with_options(` |
| `fn_main` | `codex-rs/app-server-test-client/src/main.rs:151` | `fn main() -> Result<()> {` |
| `pub_fn` | `codex-rs/app-server/src/codex_message_processor.rs:326` | `pub fn new(args: CodexMessageProcessorArgs) -> Self {` |
| `pub_fn` | `codex-rs/app-server/src/codex_message_processor.rs:428` | `pub async fn process_request(&mut self, request: ClientRequest) {` |
| `pub_fn` | `codex-rs/app-server/src/lib.rs:170` | `pub async fn run_main(` |
| `fn_main` | `codex-rs/app-server/src/main.rs:11` | `fn main() -> anyhow::Result<()> {` |
| `pub_fn` | `codex-rs/app-server/src/models.rs:11` | `pub async fn supported_models(thread_manager: Arc<ThreadManager>, config: &Config) -> Vec<Model> {` |
| `pub_struct` | `codex-rs/app-server/tests/common/auth_fixtures.rs:19` | `pub struct ChatGptAuthFixture {` |
| `pub_fn` | `codex-rs/app-server/tests/common/auth_fixtures.rs:28` | `pub fn new(access_token: impl Into<String>) -> Self {` |
| `pub_fn` | `codex-rs/app-server/tests/common/auth_fixtures.rs:38` | `pub fn refresh_token(mut self, refresh_token: impl Into<String>) -> Self {` |
| `pub_fn` | `codex-rs/app-server/tests/common/auth_fixtures.rs:43` | `pub fn account_id(mut self, account_id: impl Into<String>) -> Self {` |
| `pub_fn` | `codex-rs/app-server/tests/common/auth_fixtures.rs:48` | `pub fn plan_type(mut self, plan_type: impl Into<String>) -> Self {` |
| `pub_fn` | `codex-rs/app-server/tests/common/auth_fixtures.rs:53` | `pub fn chatgpt_user_id(mut self, chatgpt_user_id: impl Into<String>) -> Self {` |
| `pub_fn` | `codex-rs/app-server/tests/common/auth_fixtures.rs:58` | `pub fn chatgpt_account_id(mut self, chatgpt_account_id: impl Into<String>) -> Self {` |
| `pub_fn` | `codex-rs/app-server/tests/common/auth_fixtures.rs:63` | `pub fn email(mut self, email: impl Into<String>) -> Self {` |
| `pub_fn` | `codex-rs/app-server/tests/common/auth_fixtures.rs:68` | `pub fn last_refresh(mut self, last_refresh: Option<DateTime<Utc>>) -> Self {` |
| `pub_fn` | `codex-rs/app-server/tests/common/auth_fixtures.rs:73` | `pub fn claims(mut self, claims: ChatGptIdTokenClaims) -> Self {` |
| `pub_struct` | `codex-rs/app-server/tests/common/auth_fixtures.rs:80` | `pub struct ChatGptIdTokenClaims {` |
| `pub_fn` | `codex-rs/app-server/tests/common/auth_fixtures.rs:88` | `pub fn new() -> Self {` |
| `pub_fn` | `codex-rs/app-server/tests/common/auth_fixtures.rs:92` | `pub fn email(mut self, email: impl Into<String>) -> Self {` |
| `pub_fn` | `codex-rs/app-server/tests/common/auth_fixtures.rs:97` | `pub fn plan_type(mut self, plan_type: impl Into<String>) -> Self {` |
| `pub_fn` | `codex-rs/app-server/tests/common/auth_fixtures.rs:102` | `pub fn chatgpt_user_id(mut self, chatgpt_user_id: impl Into<String>) -> Self {` |
| `pub_fn` | `codex-rs/app-server/tests/common/auth_fixtures.rs:107` | `pub fn chatgpt_account_id(mut self, chatgpt_account_id: impl Into<String>) -> Self {` |
| `pub_fn` | `codex-rs/app-server/tests/common/auth_fixtures.rs:113` | `pub fn encode_id_token(claims: &ChatGptIdTokenClaims) -> Result<String> {` |
| `pub_fn` | `codex-rs/app-server/tests/common/auth_fixtures.rs:145` | `pub fn write_chatgpt_auth(` |
| `pub_fn` | `codex-rs/app-server/tests/common/config.rs:6` | `pub fn write_mock_responses_config_toml(` |
| `pub_struct` | `codex-rs/app-server/tests/common/mcp_process.rs:66` | `pub struct McpProcess {` |
| `pub_const` | `codex-rs/app-server/tests/common/mcp_process.rs:78` | `pub const DEFAULT_CLIENT_NAME: &str = "codex-app-server-tests";` |
| `pub_fn` | `codex-rs/app-server/tests/common/mcp_process.rs:81` | `pub async fn new(codex_home: &Path) -> anyhow::Result<Self> {` |
| `pub_fn` | `codex-rs/app-server/tests/common/mcp_process.rs:90` | `pub async fn new_with_env(` |
| `pub_fn` | `codex-rs/app-server/tests/common/mcp_process.rs:150` | `pub async fn initialize(&mut self) -> anyhow::Result<()> {` |
| `pub_fn` | `codex-rs/app-server/tests/common/mcp_process.rs:165` | `pub async fn initialize_with_client_info(` |
| `pub_fn` | `codex-rs/app-server/tests/common/mcp_process.rs:178` | `pub async fn initialize_with_capabilities(` |
| `pub_fn` | `codex-rs/app-server/tests/common/mcp_process.rs:233` | `pub async fn send_new_conversation_request(` |
| `pub_fn` | `codex-rs/app-server/tests/common/mcp_process.rs:242` | `pub async fn send_archive_conversation_request(` |
| `pub_fn` | `codex-rs/app-server/tests/common/mcp_process.rs:251` | `pub async fn send_add_conversation_listener_request(` |
| `pub_fn` | `codex-rs/app-server/tests/common/mcp_process.rs:260` | `pub async fn send_send_user_message_request(` |
| `pub_fn` | `codex-rs/app-server/tests/common/mcp_process.rs:270` | `pub async fn send_remove_thread_listener_request(` |
| `pub_fn` | `codex-rs/app-server/tests/common/mcp_process.rs:280` | `pub async fn send_send_user_turn_request(` |
| `pub_fn` | `codex-rs/app-server/tests/common/mcp_process.rs:289` | `pub async fn send_interrupt_conversation_request(` |
| `pub_fn` | `codex-rs/app-server/tests/common/mcp_process.rs:298` | `pub async fn send_get_auth_status_request(` |
| `pub_fn` | `codex-rs/app-server/tests/common/mcp_process.rs:307` | `pub async fn send_get_user_saved_config_request(&mut self) -> anyhow::Result<i64> {` |
| `pub_fn` | `codex-rs/app-server/tests/common/mcp_process.rs:312` | `pub async fn send_get_user_agent_request(&mut self) -> anyhow::Result<i64> {` |
| `pub_fn` | `codex-rs/app-server/tests/common/mcp_process.rs:317` | `pub async fn send_get_account_rate_limits_request(&mut self) -> anyhow::Result<i64> {` |
| `pub_fn` | `codex-rs/app-server/tests/common/mcp_process.rs:322` | `pub async fn send_get_account_request(` |
| `pub_fn` | `codex-rs/app-server/tests/common/mcp_process.rs:331` | `pub async fn send_chatgpt_auth_tokens_login_request(` |
| `pub_fn` | `codex-rs/app-server/tests/common/mcp_process.rs:345` | `pub async fn send_feedback_upload_request(` |
| `pub_fn` | `codex-rs/app-server/tests/common/mcp_process.rs:354` | `pub async fn send_user_info_request(&mut self) -> anyhow::Result<i64> {` |
| `pub_fn` | `codex-rs/app-server/tests/common/mcp_process.rs:359` | `pub async fn send_set_default_model_request(` |
| `pub_fn` | `codex-rs/app-server/tests/common/mcp_process.rs:368` | `pub async fn send_list_conversations_request(` |
| `pub_fn` | `codex-rs/app-server/tests/common/mcp_process.rs:377` | `pub async fn send_thread_start_request(` |
| `pub_fn` | `codex-rs/app-server/tests/common/mcp_process.rs:386` | `pub async fn send_thread_resume_request(` |
| `pub_fn` | `codex-rs/app-server/tests/common/mcp_process.rs:395` | `pub async fn send_thread_fork_request(` |
| `pub_fn` | `codex-rs/app-server/tests/common/mcp_process.rs:404` | `pub async fn send_thread_archive_request(` |
| `pub_fn` | `codex-rs/app-server/tests/common/mcp_process.rs:413` | `pub async fn send_thread_unarchive_request(` |
| `pub_fn` | `codex-rs/app-server/tests/common/mcp_process.rs:422` | `pub async fn send_thread_rollback_request(` |
| `pub_fn` | `codex-rs/app-server/tests/common/mcp_process.rs:431` | `pub async fn send_thread_list_request(` |
| `pub_fn` | `codex-rs/app-server/tests/common/mcp_process.rs:440` | `pub async fn send_thread_loaded_list_request(` |
| `pub_fn` | `codex-rs/app-server/tests/common/mcp_process.rs:449` | `pub async fn send_thread_read_request(` |
| `pub_fn` | `codex-rs/app-server/tests/common/mcp_process.rs:458` | `pub async fn send_list_models_request(` |
| `pub_fn` | `codex-rs/app-server/tests/common/mcp_process.rs:467` | `pub async fn send_apps_list_request(&mut self, params: AppsListParams) -> anyhow::Result<i64> {` |
| `pub_fn` | `codex-rs/app-server/tests/common/mcp_process.rs:473` | `pub async fn send_list_collaboration_modes_request(` |
| `pub_fn` | `codex-rs/app-server/tests/common/mcp_process.rs:482` | `pub async fn send_mock_experimental_method_request(` |
| `pub_fn` | `codex-rs/app-server/tests/common/mcp_process.rs:491` | `pub async fn send_resume_conversation_request(` |
| `pub_fn` | `codex-rs/app-server/tests/common/mcp_process.rs:500` | `pub async fn send_fork_conversation_request(` |
| `pub_fn` | `codex-rs/app-server/tests/common/mcp_process.rs:509` | `pub async fn send_login_api_key_request(` |
| `pub_fn` | `codex-rs/app-server/tests/common/mcp_process.rs:518` | `pub async fn send_login_chat_gpt_request(&mut self) -> anyhow::Result<i64> {` |
| `pub_fn` | `codex-rs/app-server/tests/common/mcp_process.rs:523` | `pub async fn send_turn_start_request(` |
| `pub_fn` | `codex-rs/app-server/tests/common/mcp_process.rs:532` | `pub async fn send_turn_interrupt_request(` |
| `pub_fn` | `codex-rs/app-server/tests/common/mcp_process.rs:541` | `pub async fn send_review_start_request(` |
| `pub_fn` | `codex-rs/app-server/tests/common/mcp_process.rs:550` | `pub async fn send_cancel_login_chat_gpt_request(` |
| `pub_fn` | `codex-rs/app-server/tests/common/mcp_process.rs:559` | `pub async fn send_logout_chat_gpt_request(&mut self) -> anyhow::Result<i64> {` |
| `pub_fn` | `codex-rs/app-server/tests/common/mcp_process.rs:563` | `pub async fn send_config_read_request(` |
| `pub_fn` | `codex-rs/app-server/tests/common/mcp_process.rs:571` | `pub async fn send_config_value_write_request(` |
| `pub_fn` | `codex-rs/app-server/tests/common/mcp_process.rs:579` | `pub async fn send_config_batch_write_request(` |
| `pub_fn` | `codex-rs/app-server/tests/common/mcp_process.rs:588` | `pub async fn send_logout_account_request(&mut self) -> anyhow::Result<i64> {` |
| `pub_fn` | `codex-rs/app-server/tests/common/mcp_process.rs:593` | `pub async fn send_login_account_api_key_request(` |
| `pub_fn` | `codex-rs/app-server/tests/common/mcp_process.rs:605` | `pub async fn send_login_account_chatgpt_request(&mut self) -> anyhow::Result<i64> {` |
| `pub_fn` | `codex-rs/app-server/tests/common/mcp_process.rs:613` | `pub async fn send_cancel_login_account_request(` |
| `pub_fn` | `codex-rs/app-server/tests/common/mcp_process.rs:622` | `pub async fn send_fuzzy_file_search_request(` |
| `pub_fn` | `codex-rs/app-server/tests/common/mcp_process.rs:654` | `pub async fn send_response(` |
| `pub_fn` | `codex-rs/app-server/tests/common/mcp_process.rs:663` | `pub async fn send_error(` |
| `pub_fn` | `codex-rs/app-server/tests/common/mcp_process.rs:672` | `pub async fn send_notification(` |
| `pub_fn` | `codex-rs/app-server/tests/common/mcp_process.rs:705` | `pub async fn read_stream_until_request_message(&mut self) -> anyhow::Result<ServerRequest> {` |
| `pub_fn` | `codex-rs/app-server/tests/common/mcp_process.rs:720` | `pub async fn read_stream_until_response_message(` |
| `pub_fn` | `codex-rs/app-server/tests/common/mcp_process.rs:738` | `pub async fn read_stream_until_error_message(` |
| `pub_fn` | `codex-rs/app-server/tests/common/mcp_process.rs:754` | `pub async fn read_stream_until_notification_message(` |
| `pub_fn` | `codex-rs/app-server/tests/common/mcp_process.rs:775` | `pub async fn read_next_message(&mut self) -> anyhow::Result<JSONRPCMessage> {` |
| `pub_fn` | `codex-rs/app-server/tests/common/mcp_process.rs:783` | `pub fn clear_message_buffer(&mut self) {` |
| `pub_fn` | `codex-rs/app-server/tests/common/mock_model_server.rs:14` | `pub async fn create_mock_responses_server_sequence(responses: Vec<String>) -> MockServer {` |
| `pub_fn` | `codex-rs/app-server/tests/common/mock_model_server.rs:35` | `pub async fn create_mock_responses_server_sequence_unchecked(responses: Vec<String>) -> MockServer {` |
| `pub_fn` | `codex-rs/app-server/tests/common/mock_model_server.rs:68` | `pub async fn create_mock_responses_server_repeating_assistant(message: &str) -> MockServer {` |
| `pub_fn` | `codex-rs/app-server/tests/common/models_cache.rs:50` | `pub fn write_models_cache(codex_home: &Path) -> std::io::Result<()> {` |
| `pub_fn` | `codex-rs/app-server/tests/common/models_cache.rs:73` | `pub fn write_models_cache_with_models(` |
| `pub_fn` | `codex-rs/app-server/tests/common/responses.rs:5` | `pub fn create_shell_command_sse_response(` |
| `pub_fn` | `codex-rs/app-server/tests/common/responses.rs:25` | `pub fn create_final_assistant_message_sse_response(message: &str) -> anyhow::Result<String> {` |
| `pub_fn` | `codex-rs/app-server/tests/common/responses.rs:33` | `pub fn create_apply_patch_sse_response(` |
| `pub_fn` | `codex-rs/app-server/tests/common/responses.rs:44` | `pub fn create_exec_command_sse_response(call_id: &str) -> anyhow::Result<String> {` |
| `pub_fn` | `codex-rs/app-server/tests/common/responses.rs:64` | `pub fn create_request_user_input_sse_response(call_id: &str) -> anyhow::Result<String> {` |
| `pub_fn` | `codex-rs/app-server/tests/common/rollout.rs:14` | `pub fn rollout_path(codex_home: &Path, filename_ts: &str, thread_id: &str) -> PathBuf {` |
| `pub_fn` | `codex-rs/app-server/tests/common/rollout.rs:34` | `pub fn create_fake_rollout(` |
| `pub_fn` | `codex-rs/app-server/tests/common/rollout.rs:54` | `pub fn create_fake_rollout_with_source(` |
| `pub_fn` | `codex-rs/app-server/tests/common/rollout.rs:130` | `pub fn create_fake_rollout_with_text_elements(` |
| `pub_enum` | `codex-rs/apply-patch/src/invocation.rs:35` | `pub enum MaybeApplyPatch {` |
| `pub_enum` | `codex-rs/apply-patch/src/invocation.rs:43` | `pub enum ExtractHeredocError {` |
| `pub_fn` | `codex-rs/apply-patch/src/invocation.rs:103` | `pub fn maybe_parse_apply_patch(argv: &[String]) -> MaybeApplyPatch {` |
| `pub_fn` | `codex-rs/apply-patch/src/invocation.rs:132` | `pub fn maybe_parse_apply_patch_verified(argv: &[String], cwd: &Path) -> MaybeApplyPatchVerified {` |
| `pub_const` | `codex-rs/apply-patch/src/lib.rs:26` | `pub const APPLY_PATCH_TOOL_INSTRUCTIONS: &str = include_str!("../apply_patch_tool_instructions.md");` |
| `pub_enum` | `codex-rs/apply-patch/src/lib.rs:29` | `pub enum ApplyPatchError {` |
| `pub_struct` | `codex-rs/apply-patch/src/lib.rs:64` | `pub struct IoError {` |
| `pub_struct` | `codex-rs/apply-patch/src/lib.rs:79` | `pub struct ApplyPatchArgs {` |
| `pub_enum` | `codex-rs/apply-patch/src/lib.rs:86` | `pub enum ApplyPatchFileChange {` |
| `pub_enum` | `codex-rs/apply-patch/src/lib.rs:102` | `pub enum MaybeApplyPatchVerified {` |
| `pub_struct` | `codex-rs/apply-patch/src/lib.rs:119` | `pub struct ApplyPatchAction {` |
| `pub_fn` | `codex-rs/apply-patch/src/lib.rs:132` | `pub fn is_empty(&self) -> bool {` |
| `pub_fn` | `codex-rs/apply-patch/src/lib.rs:137` | `pub fn changes(&self) -> &HashMap<PathBuf, ApplyPatchFileChange> {` |
| `pub_fn` | `codex-rs/apply-patch/src/lib.rs:143` | `pub fn new_add_for_test(path: &Path, content: String) -> Self {` |
| `pub_fn` | `codex-rs/apply-patch/src/lib.rs:174` | `pub fn apply_patch(` |
| `pub_fn` | `codex-rs/apply-patch/src/lib.rs:207` | `pub fn apply_hunks(` |
| `pub_struct` | `codex-rs/apply-patch/src/lib.rs:262` | `pub struct AffectedPaths {` |
| `pub_struct` | `codex-rs/apply-patch/src/lib.rs:497` | `pub struct ApplyPatchFileUpdate {` |
| `pub_fn` | `codex-rs/apply-patch/src/lib.rs:502` | `pub fn unified_diff_from_chunks(` |
| `pub_fn` | `codex-rs/apply-patch/src/lib.rs:509` | `pub fn unified_diff_from_chunks_with_context(` |
| `pub_fn` | `codex-rs/apply-patch/src/lib.rs:528` | `pub fn print_summary(` |
| `pub_fn` | `codex-rs/apply-patch/src/main.rs:1` | `pub fn main() -> ! {` |
| `pub_enum` | `codex-rs/apply-patch/src/parser.rs:50` | `pub enum ParseError {` |
| `pub_enum` | `codex-rs/apply-patch/src/parser.rs:60` | `pub enum Hunk {` |
| `pub_fn` | `codex-rs/apply-patch/src/parser.rs:79` | `pub fn resolve_path(&self, cwd: &Path) -> PathBuf {` |
| `pub_struct` | `codex-rs/apply-patch/src/parser.rs:91` | `pub struct UpdateFileChunk {` |
| `pub_fn` | `codex-rs/apply-patch/src/parser.rs:106` | `pub fn parse_patch(patch: &str) -> Result<ApplyPatchArgs, ParseError> {` |
| `pub_fn` | `codex-rs/apply-patch/src/standalone_executable.rs:4` | `pub fn main() -> ! {` |
| `pub_fn` | `codex-rs/apply-patch/src/standalone_executable.rs:11` | `pub fn run_main() -> i32 {` |
| `pub_fn` | `codex-rs/arg0/src/lib.rs:14` | `pub fn arg0_dispatch() -> Option<TempDir> {` |
| `pub_fn` | `codex-rs/arg0/src/lib.rs:152` | `pub fn prepend_path_entry_for_codex_aliases() -> std::io::Result<TempDir> {` |
| `pub_enum` | `codex-rs/async-utils/src/lib.rs:6` | `pub enum CancelErr {` |
| `pub_trait` | `codex-rs/async-utils/src/lib.rs:11` | `pub trait OrCancelExt: Sized {` |
| `pub_enum` | `codex-rs/backend-client/src/client.rs:24` | `pub enum PathStyle {` |
| `pub_fn` | `codex-rs/backend-client/src/client.rs:32` | `pub fn from_base_url(base_url: &str) -> Self {` |
| `pub_struct` | `codex-rs/backend-client/src/client.rs:42` | `pub struct Client {` |
| `pub_fn` | `codex-rs/backend-client/src/client.rs:52` | `pub fn new(base_url: impl Into<String>) -> Result<Self> {` |
| `pub_fn` | `codex-rs/backend-client/src/client.rs:77` | `pub fn from_auth(base_url: impl Into<String>, auth: &CodexAuth) -> Result<Self> {` |
| `pub_fn` | `codex-rs/backend-client/src/client.rs:88` | `pub fn with_bearer_token(mut self, token: impl Into<String>) -> Self {` |
| `pub_fn` | `codex-rs/backend-client/src/client.rs:93` | `pub fn with_user_agent(mut self, ua: impl Into<String>) -> Self {` |
| `pub_fn` | `codex-rs/backend-client/src/client.rs:100` | `pub fn with_chatgpt_account_id(mut self, account_id: impl Into<String>) -> Self {` |
| `pub_fn` | `codex-rs/backend-client/src/client.rs:105` | `pub fn with_path_style(mut self, style: PathStyle) -> Self {` |
| `pub_fn` | `codex-rs/backend-client/src/client.rs:162` | `pub async fn get_rate_limits(&self) -> Result<RateLimitSnapshot> {` |
| `pub_fn` | `codex-rs/backend-client/src/client.rs:173` | `pub async fn list_tasks(` |
| `pub_fn` | `codex-rs/backend-client/src/client.rs:209` | `pub async fn get_task_details(&self, task_id: &str) -> Result<CodeTaskDetailsResponse> {` |
| `pub_fn` | `codex-rs/backend-client/src/client.rs:214` | `pub async fn get_task_details_with_body(` |
| `pub_fn` | `codex-rs/backend-client/src/client.rs:228` | `pub async fn list_sibling_turns(` |
| `pub_fn` | `codex-rs/backend-client/src/client.rs:252` | `pub async fn get_config_requirements_file(&self) -> Result<ConfigFileResponse> {` |
| `pub_fn` | `codex-rs/backend-client/src/client.rs:264` | `pub async fn create_task(&self, request_body: serde_json::Value) -> Result<String> {` |
| `pub_mod` | `codex-rs/backend-client/src/lib.rs:2` | `pub mod types;` |
| `pub_struct` | `codex-rs/backend-client/src/types.rs:19` | `pub struct CodeTaskDetailsResponse {` |
| `pub_struct` | `codex-rs/backend-client/src/types.rs:29` | `pub struct Turn {` |
| `pub_struct` | `codex-rs/backend-client/src/types.rs:49` | `pub struct TurnItem {` |
| `pub_enum` | `codex-rs/backend-client/src/types.rs:64` | `pub enum ContentFragment {` |
| `pub_struct` | `codex-rs/backend-client/src/types.rs:70` | `pub struct StructuredContent {` |
| `pub_struct` | `codex-rs/backend-client/src/types.rs:78` | `pub struct DiffPayload {` |
| `pub_struct` | `codex-rs/backend-client/src/types.rs:84` | `pub struct Worklog {` |
| `pub_struct` | `codex-rs/backend-client/src/types.rs:90` | `pub struct WorklogMessage {` |
| `pub_struct` | `codex-rs/backend-client/src/types.rs:98` | `pub struct Author {` |
| `pub_struct` | `codex-rs/backend-client/src/types.rs:104` | `pub struct WorklogContent {` |
| `pub_struct` | `codex-rs/backend-client/src/types.rs:110` | `pub struct TurnError {` |
| `pub_trait` | `codex-rs/backend-client/src/types.rs:259` | `pub trait CodeTaskDetailsResponseExt {` |
| `pub_struct` | `codex-rs/backend-client/src/types.rs:315` | `pub struct TurnAttemptsSiblingTurnsResponse {` |
| `pub_struct` | `codex-rs/chatgpt/src/apply_command.rs:15` | `pub struct ApplyCommand {` |
| `pub_fn` | `codex-rs/chatgpt/src/apply_command.rs:21` | `pub async fn run_apply_command(` |
| `pub_fn` | `codex-rs/chatgpt/src/apply_command.rs:40` | `pub async fn apply_diff_from_task(` |
| `pub_fn` | `codex-rs/chatgpt/src/chatgpt_token.rs:11` | `pub fn get_chatgpt_token_data() -> Option<TokenData> {` |
| `pub_fn` | `codex-rs/chatgpt/src/chatgpt_token.rs:15` | `pub fn set_chatgpt_token_data(value: TokenData) {` |
| `pub_fn` | `codex-rs/chatgpt/src/chatgpt_token.rs:22` | `pub async fn init_chatgpt_token_from_auth(` |
| `pub_fn` | `codex-rs/chatgpt/src/connectors.rs:41` | `pub async fn list_connectors(config: &Config) -> anyhow::Result<Vec<AppInfo>> {` |
| `pub_fn` | `codex-rs/chatgpt/src/connectors.rs:55` | `pub async fn list_all_connectors(config: &Config) -> anyhow::Result<Vec<AppInfo>> {` |
| `pub_struct` | `codex-rs/chatgpt/src/get_task.rs:7` | `pub struct GetTaskResponse {` |
| `pub_struct` | `codex-rs/chatgpt/src/get_task.rs:13` | `pub struct AssistantTurn {` |
| `pub_enum` | `codex-rs/chatgpt/src/get_task.rs:19` | `pub enum OutputItem {` |
| `pub_struct` | `codex-rs/chatgpt/src/get_task.rs:28` | `pub struct PrOutputItem {` |
| `pub_struct` | `codex-rs/chatgpt/src/get_task.rs:33` | `pub struct OutputDiff {` |
| `pub_mod` | `codex-rs/chatgpt/src/lib.rs:1` | `pub mod apply_command;` |
| `pub_mod` | `codex-rs/chatgpt/src/lib.rs:4` | `pub mod connectors;` |
| `pub_mod` | `codex-rs/chatgpt/src/lib.rs:5` | `pub mod get_task;` |
| `pub_struct` | `codex-rs/cli/src/app_cmd.rs:7` | `pub struct AppCommand {` |
| `pub_fn` | `codex-rs/cli/src/app_cmd.rs:18` | `pub async fn run_app(cmd: AppCommand) -> anyhow::Result<()> {` |
| `pub_fn` | `codex-rs/cli/src/debug_sandbox.rs:27` | `pub async fn run_command_under_seatbelt(` |
| `pub_fn` | `codex-rs/cli/src/debug_sandbox.rs:49` | `pub async fn run_command_under_seatbelt(` |
| `pub_fn` | `codex-rs/cli/src/debug_sandbox.rs:56` | `pub async fn run_command_under_landlock(` |
| `pub_fn` | `codex-rs/cli/src/debug_sandbox.rs:76` | `pub async fn run_command_under_windows(` |
| `pub_fn` | `codex-rs/cli/src/debug_sandbox.rs:273` | `pub fn create_sandbox_mode(full_auto: bool) -> SandboxMode {` |
| `pub_struct` | `codex-rs/cli/src/debug_sandbox/seatbelt.rs:8` | `pub struct SandboxDenial {` |
| `pub_struct` | `codex-rs/cli/src/debug_sandbox/seatbelt.rs:13` | `pub struct DenialLogger {` |
| `pub_fn` | `codex-rs/cli/src/desktop_app/mac.rs:7` | `pub async fn run_mac_app_open_or_install(` |
| `pub_fn` | `codex-rs/cli/src/desktop_app/mod.rs:6` | `pub async fn run_app_open_or_install(` |
| `pub_mod` | `codex-rs/cli/src/lib.rs:1` | `pub mod debug_sandbox;` |
| `pub_mod` | `codex-rs/cli/src/lib.rs:3` | `pub mod login;` |
| `pub_struct` | `codex-rs/cli/src/lib.rs:9` | `pub struct SeatbeltCommand {` |
| `pub_struct` | `codex-rs/cli/src/lib.rs:27` | `pub struct LandlockCommand {` |
| `pub_struct` | `codex-rs/cli/src/lib.rs:41` | `pub struct WindowsCommand {` |
| `pub_fn` | `codex-rs/cli/src/login.rs:29` | `pub async fn login_with_chatgpt(` |
| `pub_fn` | `codex-rs/cli/src/login.rs:47` | `pub async fn run_login_with_chatgpt(cli_config_overrides: CliConfigOverrides) -> ! {` |
| `pub_fn` | `codex-rs/cli/src/login.rs:75` | `pub async fn run_login_with_api_key(` |
| `pub_fn` | `codex-rs/cli/src/login.rs:102` | `pub fn read_api_key_from_stdin() -> String {` |
| `pub_fn` | `codex-rs/cli/src/login.rs:130` | `pub async fn run_login_with_device_code(` |
| `pub_fn` | `codex-rs/cli/src/login.rs:166` | `pub async fn run_login_with_device_code_fallback_to_browser(` |
| `pub_fn` | `codex-rs/cli/src/login.rs:224` | `pub async fn run_login_status(cli_config_overrides: CliConfigOverrides) -> ! {` |
| `pub_fn` | `codex-rs/cli/src/login.rs:259` | `pub async fn run_logout(cli_config_overrides: CliConfigOverrides) -> ! {` |
| `fn_main` | `codex-rs/cli/src/main.rs:495` | `fn main() -> anyhow::Result<()> {` |
| `pub_struct` | `codex-rs/cli/src/mcp_cmd.rs:31` | `pub struct McpCli {` |
| `pub_enum` | `codex-rs/cli/src/mcp_cmd.rs:40` | `pub enum McpSubcommand {` |
| `pub_struct` | `codex-rs/cli/src/mcp_cmd.rs:50` | `pub struct ListArgs {` |
| `pub_struct` | `codex-rs/cli/src/mcp_cmd.rs:57` | `pub struct GetArgs {` |
| `pub_struct` | `codex-rs/cli/src/mcp_cmd.rs:68` | `pub struct AddArgs {` |
| `pub_struct` | `codex-rs/cli/src/mcp_cmd.rs:85` | `pub struct AddMcpTransportArgs {` |
| `pub_struct` | `codex-rs/cli/src/mcp_cmd.rs:94` | `pub struct AddMcpStdioArgs {` |
| `pub_struct` | `codex-rs/cli/src/mcp_cmd.rs:114` | `pub struct AddMcpStreamableHttpArgs {` |
| `pub_struct` | `codex-rs/cli/src/mcp_cmd.rs:130` | `pub struct RemoveArgs {` |
| `pub_struct` | `codex-rs/cli/src/mcp_cmd.rs:136` | `pub struct LoginArgs {` |
| `pub_struct` | `codex-rs/cli/src/mcp_cmd.rs:146` | `pub struct LogoutArgs {` |
| `pub_fn` | `codex-rs/cli/src/mcp_cmd.rs:152` | `pub async fn run(self) -> Result<()> {` |
| `pub_fn` | `codex-rs/cli/src/wsl_paths.rs:8` | `pub fn win_path_to_wsl(path: &str) -> Option<String> {` |
| `pub_fn` | `codex-rs/cloud-requirements/src/lib.rs:140` | `pub fn cloud_requirements_loader(` |
| `pub_type` | `codex-rs/cloud-tasks-client/src/api.rs:6` | `pub type Result<T> = std::result::Result<T, CloudTaskError>;` |
| `pub_enum` | `codex-rs/cloud-tasks-client/src/api.rs:9` | `pub enum CloudTaskError {` |
| `pub_struct` | `codex-rs/cloud-tasks-client/src/api.rs:22` | `pub struct TaskId(pub String);` |
| `pub_enum` | `codex-rs/cloud-tasks-client/src/api.rs:26` | `pub enum TaskStatus {` |
| `pub_struct` | `codex-rs/cloud-tasks-client/src/api.rs:34` | `pub struct TaskSummary {` |
| `pub_enum` | `codex-rs/cloud-tasks-client/src/api.rs:53` | `pub enum AttemptStatus {` |
| `pub_struct` | `codex-rs/cloud-tasks-client/src/api.rs:64` | `pub struct TurnAttempt {` |
| `pub_enum` | `codex-rs/cloud-tasks-client/src/api.rs:75` | `pub enum ApplyStatus {` |
| `pub_struct` | `codex-rs/cloud-tasks-client/src/api.rs:82` | `pub struct ApplyOutcome {` |
| `pub_struct` | `codex-rs/cloud-tasks-client/src/api.rs:93` | `pub struct CreatedTask {` |
| `pub_struct` | `codex-rs/cloud-tasks-client/src/api.rs:98` | `pub struct TaskListPage {` |
| `pub_struct` | `codex-rs/cloud-tasks-client/src/api.rs:104` | `pub struct DiffSummary {` |
| `pub_struct` | `codex-rs/cloud-tasks-client/src/api.rs:111` | `pub struct TaskText {` |
| `pub_trait` | `codex-rs/cloud-tasks-client/src/api.rs:134` | `pub trait CloudBackend: Send + Sync {` |
| `pub_struct` | `codex-rs/cloud-tasks-client/src/http.rs:21` | `pub struct HttpClient {` |
| `pub_fn` | `codex-rs/cloud-tasks-client/src/http.rs:27` | `pub fn new(base_url: impl Into<String>) -> anyhow::Result<Self> {` |
| `pub_fn` | `codex-rs/cloud-tasks-client/src/http.rs:33` | `pub fn with_bearer_token(mut self, token: impl Into<String>) -> Self {` |
| `pub_fn` | `codex-rs/cloud-tasks-client/src/http.rs:38` | `pub fn with_user_agent(mut self, ua: impl Into<String>) -> Self {` |
| `pub_fn` | `codex-rs/cloud-tasks-client/src/http.rs:43` | `pub fn with_chatgpt_account_id(mut self, account_id: impl Into<String>) -> Self {` |
| `pub_struct` | `codex-rs/cloud-tasks-client/src/mock.rs:15` | `pub struct MockClient;` |
| `pub_struct` | `codex-rs/cloud-tasks/src/app.rs:6` | `pub struct EnvironmentRow {` |
| `pub_struct` | `codex-rs/cloud-tasks/src/app.rs:14` | `pub struct EnvModalState {` |
| `pub_struct` | `codex-rs/cloud-tasks/src/app.rs:20` | `pub struct BestOfModalState {` |
| `pub_enum` | `codex-rs/cloud-tasks/src/app.rs:25` | `pub enum ApplyResultLevel {` |
| `pub_struct` | `codex-rs/cloud-tasks/src/app.rs:32` | `pub struct ApplyModalState {` |
| `pub_struct` | `codex-rs/cloud-tasks/src/app.rs:47` | `pub struct App {` |
| `pub_fn` | `codex-rs/cloud-tasks/src/app.rs:78` | `pub fn new() -> Self {` |
| `pub_fn` | `codex-rs/cloud-tasks/src/app.rs:104` | `pub fn next(&mut self) {` |
| `pub_fn` | `codex-rs/cloud-tasks/src/app.rs:111` | `pub fn prev(&mut self) {` |
| `pub_fn` | `codex-rs/cloud-tasks/src/app.rs:121` | `pub async fn load_tasks(` |
| `pub_struct` | `codex-rs/cloud-tasks/src/app.rs:136` | `pub struct DiffOverlay {` |
| `pub_struct` | `codex-rs/cloud-tasks/src/app.rs:153` | `pub struct AttemptView {` |
| `pub_fn` | `codex-rs/cloud-tasks/src/app.rs:164` | `pub fn has_diff(&self) -> bool {` |
| `pub_fn` | `codex-rs/cloud-tasks/src/app.rs:168` | `pub fn has_text(&self) -> bool {` |
| `pub_fn` | `codex-rs/cloud-tasks/src/app.rs:174` | `pub fn new(task_id: TaskId, title: String, attempt_total_hint: Option<usize>) -> Self {` |
| `pub_fn` | `codex-rs/cloud-tasks/src/app.rs:194` | `pub fn current_attempt(&self) -> Option<&AttemptView> {` |
| `pub_fn` | `codex-rs/cloud-tasks/src/app.rs:198` | `pub fn base_attempt_mut(&mut self) -> &mut AttemptView {` |
| `pub_fn` | `codex-rs/cloud-tasks/src/app.rs:205` | `pub fn set_view(&mut self, view: DetailView) {` |
| `pub_fn` | `codex-rs/cloud-tasks/src/app.rs:210` | `pub fn expected_attempts(&self) -> Option<usize> {` |
| `pub_fn` | `codex-rs/cloud-tasks/src/app.rs:220` | `pub fn attempt_count(&self) -> usize {` |
| `pub_fn` | `codex-rs/cloud-tasks/src/app.rs:224` | `pub fn attempt_display_total(&self) -> usize {` |
| `pub_fn` | `codex-rs/cloud-tasks/src/app.rs:229` | `pub fn step_attempt(&mut self, delta: isize) -> bool {` |
| `pub_fn` | `codex-rs/cloud-tasks/src/app.rs:244` | `pub fn current_can_apply(&self) -> bool {` |
| `pub_fn` | `codex-rs/cloud-tasks/src/app.rs:253` | `pub fn apply_selection_to_fields(&mut self) {` |
| `pub_enum` | `codex-rs/cloud-tasks/src/app.rs:292` | `pub enum DetailView {` |
| `pub_enum` | `codex-rs/cloud-tasks/src/app.rs:300` | `pub enum AppEvent {` |
| `pub_struct` | `codex-rs/cloud-tasks/src/cli.rs:7` | `pub struct Cli {` |
| `pub_enum` | `codex-rs/cloud-tasks/src/cli.rs:16` | `pub enum Command {` |
| `pub_struct` | `codex-rs/cloud-tasks/src/cli.rs:30` | `pub struct ExecCommand {` |
| `pub_struct` | `codex-rs/cloud-tasks/src/cli.rs:75` | `pub struct StatusCommand {` |
| `pub_struct` | `codex-rs/cloud-tasks/src/cli.rs:82` | `pub struct ListCommand {` |
| `pub_struct` | `codex-rs/cloud-tasks/src/cli.rs:101` | `pub struct ApplyCommand {` |
| `pub_struct` | `codex-rs/cloud-tasks/src/cli.rs:112` | `pub struct DiffCommand {` |
| `pub_struct` | `codex-rs/cloud-tasks/src/env_detect.rs:19` | `pub struct AutodetectSelection {` |
| `pub_fn` | `codex-rs/cloud-tasks/src/env_detect.rs:24` | `pub async fn autodetect_environment_id(` |
| `pub_fn` | `codex-rs/cloud-tasks/src/env_detect.rs:255` | `pub async fn list_environments(` |
| `pub_mod` | `codex-rs/cloud-tasks/src/lib.rs:3` | `pub mod env_detect;` |
| `pub_mod` | `codex-rs/cloud-tasks/src/lib.rs:5` | `pub mod scrollable_diff;` |
| `pub_mod` | `codex-rs/cloud-tasks/src/lib.rs:7` | `pub mod util;` |
| `pub_fn` | `codex-rs/cloud-tasks/src/lib.rs:732` | `pub async fn run_main(cli: Cli, _codex_linux_sandbox_exe: Option<PathBuf>) -> anyhow::Result<()> {` |
| `pub_struct` | `codex-rs/cloud-tasks/src/new_task.rs:3` | `pub struct NewTaskPage {` |
| `pub_fn` | `codex-rs/cloud-tasks/src/new_task.rs:11` | `pub fn new(env_id: Option<String>, best_of_n: usize) -> Self {` |
| `pub_struct` | `codex-rs/cloud-tasks/src/scrollable_diff.rs:6` | `pub struct ScrollViewState {` |
| `pub_fn` | `codex-rs/cloud-tasks/src/scrollable_diff.rs:13` | `pub fn clamp(&mut self) {` |
| `pub_struct` | `codex-rs/cloud-tasks/src/scrollable_diff.rs:26` | `pub struct ScrollableDiff {` |
| `pub_fn` | `codex-rs/cloud-tasks/src/scrollable_diff.rs:35` | `pub fn new() -> Self {` |
| `pub_fn` | `codex-rs/cloud-tasks/src/scrollable_diff.rs:40` | `pub fn set_content(&mut self, lines: Vec<String>) {` |
| `pub_fn` | `codex-rs/cloud-tasks/src/scrollable_diff.rs:50` | `pub fn set_width(&mut self, width: u16) {` |
| `pub_fn` | `codex-rs/cloud-tasks/src/scrollable_diff.rs:60` | `pub fn set_viewport(&mut self, height: u16) {` |
| `pub_fn` | `codex-rs/cloud-tasks/src/scrollable_diff.rs:66` | `pub fn wrapped_lines(&self) -> &[String] {` |
| `pub_fn` | `codex-rs/cloud-tasks/src/scrollable_diff.rs:70` | `pub fn wrapped_src_indices(&self) -> &[usize] {` |
| `pub_fn` | `codex-rs/cloud-tasks/src/scrollable_diff.rs:74` | `pub fn raw_line_at(&self, idx: usize) -> &str {` |
| `pub_fn` | `codex-rs/cloud-tasks/src/scrollable_diff.rs:79` | `pub fn scroll_by(&mut self, delta: i16) {` |
| `pub_fn` | `codex-rs/cloud-tasks/src/scrollable_diff.rs:85` | `pub fn page_by(&mut self, delta: i16) {` |
| `pub_fn` | `codex-rs/cloud-tasks/src/scrollable_diff.rs:89` | `pub fn to_top(&mut self) {` |
| `pub_fn` | `codex-rs/cloud-tasks/src/scrollable_diff.rs:93` | `pub fn to_bottom(&mut self) {` |
| `pub_fn` | `codex-rs/cloud-tasks/src/scrollable_diff.rs:98` | `pub fn percent_scrolled(&self) -> Option<u8> {` |
| `pub_fn` | `codex-rs/cloud-tasks/src/ui.rs:28` | `pub fn draw(frame: &mut Frame, app: &mut App) {` |
| `pub_fn` | `codex-rs/cloud-tasks/src/ui.rs:104` | `pub fn draw_new_task_page(frame: &mut Frame, area: Rect, app: &mut App) {` |
| `pub_fn` | `codex-rs/cloud-tasks/src/ui.rs:469` | `pub fn draw_apply_modal(frame: &mut Frame, area: Rect, app: &mut App) {` |
| `pub_fn` | `codex-rs/cloud-tasks/src/ui.rs:890` | `pub fn draw_env_modal(frame: &mut Frame, area: Rect, app: &mut App) {` |
| `pub_fn` | `codex-rs/cloud-tasks/src/ui.rs:990` | `pub fn draw_best_of_modal(frame: &mut Frame, area: Rect, app: &mut App) {` |
| `pub_fn` | `codex-rs/cloud-tasks/src/util.rs:10` | `pub fn set_user_agent_suffix(suffix: &str) {` |
| `pub_fn` | `codex-rs/cloud-tasks/src/util.rs:16` | `pub fn append_error_log(message: impl AsRef<str>) {` |
| `pub_fn` | `codex-rs/cloud-tasks/src/util.rs:31` | `pub fn normalize_base_url(input: &str) -> String {` |
| `pub_fn` | `codex-rs/cloud-tasks/src/util.rs:46` | `pub fn extract_chatgpt_account_id(token: &str) -> Option<String> {` |
| `pub_fn` | `codex-rs/cloud-tasks/src/util.rs:62` | `pub async fn load_auth_manager() -> Option<AuthManager> {` |
| `pub_fn` | `codex-rs/cloud-tasks/src/util.rs:74` | `pub async fn build_chatgpt_headers() -> HeaderMap {` |
| `pub_fn` | `codex-rs/cloud-tasks/src/util.rs:109` | `pub fn task_url(base_url: &str, task_id: &str) -> String {` |
| `pub_fn` | `codex-rs/cloud-tasks/src/util.rs:123` | `pub fn format_relative_time(reference: DateTime<Utc>, ts: DateTime<Utc>) -> String {` |
| `pub_fn` | `codex-rs/cloud-tasks/src/util.rs:143` | `pub fn format_relative_time_now(ts: DateTime<Utc>) -> String {` |
| `pub_trait` | `codex-rs/codex-api/src/auth.rs:8` | `pub trait AuthProvider: Send + Sync {` |
| `pub_struct` | `codex-rs/codex-api/src/common.rs:18` | `pub struct Prompt {` |
| `pub_struct` | `codex-rs/codex-api/src/common.rs:34` | `pub struct CompactionInput<'a> {` |
| `pub_enum` | `codex-rs/codex-api/src/common.rs:41` | `pub enum ResponseEvent {` |
| `pub_struct` | `codex-rs/codex-api/src/common.rs:70` | `pub struct Reasoning {` |
| `pub_enum` | `codex-rs/codex-api/src/common.rs:79` | `pub enum TextFormatType {` |
| `pub_struct` | `codex-rs/codex-api/src/common.rs:85` | `pub struct TextFormat {` |
| `pub_struct` | `codex-rs/codex-api/src/common.rs:99` | `pub struct TextControls {` |
| `pub_enum` | `codex-rs/codex-api/src/common.rs:108` | `pub enum OpenAiVerbosity {` |
| `pub_struct` | `codex-rs/codex-api/src/common.rs:126` | `pub struct ResponsesApiRequest<'a> {` |
| `pub_struct` | `codex-rs/codex-api/src/common.rs:144` | `pub struct ResponseCreateWsRequest {` |
| `pub_struct` | `codex-rs/codex-api/src/common.rs:162` | `pub struct ResponseAppendWsRequest {` |
| `pub_enum` | `codex-rs/codex-api/src/common.rs:168` | `pub enum ResponsesWsRequest {` |
| `pub_fn` | `codex-rs/codex-api/src/common.rs:175` | `pub fn create_text_param_for_request(` |
| `pub_struct` | `codex-rs/codex-api/src/common.rs:194` | `pub struct ResponseStream {` |
| `pub_struct` | `codex-rs/codex-api/src/endpoint/chat.rs:28` | `pub struct ChatClient<T: HttpTransport, A: AuthProvider> {` |
| `pub_fn` | `codex-rs/codex-api/src/endpoint/chat.rs:33` | `pub fn new(transport: T, provider: Provider, auth: A) -> Self {` |
| `pub_fn` | `codex-rs/codex-api/src/endpoint/chat.rs:39` | `pub fn with_telemetry(` |
| `pub_fn` | `codex-rs/codex-api/src/endpoint/chat.rs:49` | `pub async fn stream_request(&self, request: ChatRequest) -> Result<ResponseStream, ApiError> {` |
| `pub_fn` | `codex-rs/codex-api/src/endpoint/chat.rs:53` | `pub async fn stream_prompt(` |
| `pub_fn` | `codex-rs/codex-api/src/endpoint/chat.rs:78` | `pub async fn stream(` |
| `pub_enum` | `codex-rs/codex-api/src/endpoint/chat.rs:97` | `pub enum AggregateMode {` |
| `pub_struct` | `codex-rs/codex-api/src/endpoint/chat.rs:103` | `pub struct AggregatedStream {` |
| `pub_trait` | `codex-rs/codex-api/src/endpoint/chat.rs:256` | `pub trait AggregateStreamExt {` |
| `pub_struct` | `codex-rs/codex-api/src/endpoint/compact.rs:17` | `pub struct CompactClient<T: HttpTransport, A: AuthProvider> {` |
| `pub_fn` | `codex-rs/codex-api/src/endpoint/compact.rs:25` | `pub fn new(transport: T, provider: Provider, auth: A) -> Self {` |
| `pub_fn` | `codex-rs/codex-api/src/endpoint/compact.rs:34` | `pub fn with_telemetry(mut self, request: Option<Arc<dyn RequestTelemetry>>) -> Self {` |
| `pub_fn` | `codex-rs/codex-api/src/endpoint/compact.rs:48` | `pub async fn compact(` |
| `pub_fn` | `codex-rs/codex-api/src/endpoint/compact.rs:73` | `pub async fn compact_input(` |
| `pub_mod` | `codex-rs/codex-api/src/endpoint/mod.rs:1` | `pub mod chat;` |
| `pub_mod` | `codex-rs/codex-api/src/endpoint/mod.rs:2` | `pub mod compact;` |
| `pub_mod` | `codex-rs/codex-api/src/endpoint/mod.rs:3` | `pub mod models;` |
| `pub_mod` | `codex-rs/codex-api/src/endpoint/mod.rs:4` | `pub mod responses;` |
| `pub_mod` | `codex-rs/codex-api/src/endpoint/mod.rs:5` | `pub mod responses_websocket;` |
| `pub_struct` | `codex-rs/codex-api/src/endpoint/models.rs:15` | `pub struct ModelsClient<T: HttpTransport, A: AuthProvider> {` |
| `pub_fn` | `codex-rs/codex-api/src/endpoint/models.rs:23` | `pub fn new(transport: T, provider: Provider, auth: A) -> Self {` |
| `pub_fn` | `codex-rs/codex-api/src/endpoint/models.rs:32` | `pub fn with_telemetry(mut self, request: Option<Arc<dyn RequestTelemetry>>) -> Self {` |
| `pub_fn` | `codex-rs/codex-api/src/endpoint/models.rs:41` | `pub async fn list_models(` |
| `pub_struct` | `codex-rs/codex-api/src/endpoint/responses.rs:25` | `pub struct ResponsesClient<T: HttpTransport, A: AuthProvider> {` |
| `pub_struct` | `codex-rs/codex-api/src/endpoint/responses.rs:30` | `pub struct ResponsesOptions {` |
| `pub_fn` | `codex-rs/codex-api/src/endpoint/responses.rs:44` | `pub fn new(transport: T, provider: Provider, auth: A) -> Self {` |
| `pub_fn` | `codex-rs/codex-api/src/endpoint/responses.rs:50` | `pub fn with_telemetry(` |
| `pub_fn` | `codex-rs/codex-api/src/endpoint/responses.rs:60` | `pub async fn stream_request(` |
| `pub_fn` | `codex-rs/codex-api/src/endpoint/responses.rs:75` | `pub async fn stream_prompt(` |
| `pub_fn` | `codex-rs/codex-api/src/endpoint/responses.rs:118` | `pub async fn stream(` |
| `pub_struct` | `codex-rs/codex-api/src/endpoint/responses_websocket.rs:38` | `pub struct ResponsesWebsocketConnection {` |
| `pub_fn` | `codex-rs/codex-api/src/endpoint/responses_websocket.rs:61` | `pub async fn is_closed(&self) -> bool {` |
| `pub_fn` | `codex-rs/codex-api/src/endpoint/responses_websocket.rs:65` | `pub async fn stream_request(` |
| `pub_struct` | `codex-rs/codex-api/src/endpoint/responses_websocket.rs:114` | `pub struct ResponsesWebsocketClient<A: AuthProvider> {` |
| `pub_fn` | `codex-rs/codex-api/src/endpoint/responses_websocket.rs:120` | `pub fn new(provider: Provider, auth: A) -> Self {` |
| `pub_fn` | `codex-rs/codex-api/src/endpoint/responses_websocket.rs:124` | `pub async fn connect(` |
| `pub_enum` | `codex-rs/codex-api/src/error.rs:8` | `pub enum ApiError {` |
| `pub_mod` | `codex-rs/codex-api/src/lib.rs:1` | `pub mod auth;` |
| `pub_mod` | `codex-rs/codex-api/src/lib.rs:2` | `pub mod common;` |
| `pub_mod` | `codex-rs/codex-api/src/lib.rs:3` | `pub mod endpoint;` |
| `pub_mod` | `codex-rs/codex-api/src/lib.rs:4` | `pub mod error;` |
| `pub_mod` | `codex-rs/codex-api/src/lib.rs:5` | `pub mod provider;` |
| `pub_mod` | `codex-rs/codex-api/src/lib.rs:6` | `pub mod rate_limits;` |
| `pub_mod` | `codex-rs/codex-api/src/lib.rs:7` | `pub mod requests;` |
| `pub_mod` | `codex-rs/codex-api/src/lib.rs:8` | `pub mod sse;` |
| `pub_mod` | `codex-rs/codex-api/src/lib.rs:9` | `pub mod telemetry;` |
| `pub_enum` | `codex-rs/codex-api/src/provider.rs:13` | `pub enum WireApi {` |
| `pub_struct` | `codex-rs/codex-api/src/provider.rs:24` | `pub struct RetryConfig {` |
| `pub_fn` | `codex-rs/codex-api/src/provider.rs:33` | `pub fn to_policy(&self) -> RetryPolicy {` |
| `pub_struct` | `codex-rs/codex-api/src/provider.rs:51` | `pub struct Provider {` |
| `pub_fn` | `codex-rs/codex-api/src/provider.rs:62` | `pub fn url_for_path(&self, path: &str) -> String {` |
| `pub_fn` | `codex-rs/codex-api/src/provider.rs:86` | `pub fn build_request(&self, method: Method, path: &str) -> Request {` |
| `pub_fn` | `codex-rs/codex-api/src/provider.rs:97` | `pub fn is_azure_responses_endpoint(&self) -> bool {` |
| `pub_fn` | `codex-rs/codex-api/src/provider.rs:101` | `pub fn websocket_url_for_path(&self, path: &str) -> Result<Url, url::ParseError> {` |
| `pub_fn` | `codex-rs/codex-api/src/provider.rs:115` | `pub fn is_azure_responses_wire_base_url(wire: WireApi, name: &str, base_url: Option<&str>) -> bool {` |
| `pub_struct` | `codex-rs/codex-api/src/rate_limits.rs:8` | `pub struct RateLimitError {` |
| `pub_fn` | `codex-rs/codex-api/src/rate_limits.rs:19` | `pub fn parse_rate_limit(headers: &HeaderMap) -> Option<RateLimitSnapshot> {` |
| `pub_fn` | `codex-rs/codex-api/src/rate_limits.rs:45` | `pub fn parse_promo_message(headers: &HeaderMap) -> Option<String> {` |
| `pub_struct` | `codex-rs/codex-api/src/requests/chat.rs:17` | `pub struct ChatRequest {` |
| `pub_struct` | `codex-rs/codex-api/src/requests/chat.rs:22` | `pub struct ChatRequestBuilder<'a> {` |
| `pub_fn` | `codex-rs/codex-api/src/requests/chat.rs:32` | `pub fn new(` |
| `pub_fn` | `codex-rs/codex-api/src/requests/chat.rs:48` | `pub fn conversation_id(mut self, id: Option<String>) -> Self {` |
| `pub_fn` | `codex-rs/codex-api/src/requests/chat.rs:53` | `pub fn session_source(mut self, source: Option<SessionSource>) -> Self {` |
| `pub_fn` | `codex-rs/codex-api/src/requests/chat.rs:58` | `pub fn build(self, _provider: &Provider) -> Result<ChatRequest, ApiError> {` |
| `pub_fn` | `codex-rs/codex-api/src/requests/headers.rs:5` | `pub fn build_conversation_headers(conversation_id: Option<String>) -> HeaderMap {` |
| `pub_mod` | `codex-rs/codex-api/src/requests/mod.rs:1` | `pub mod chat;` |
| `pub_mod` | `codex-rs/codex-api/src/requests/mod.rs:3` | `pub mod responses;` |
| `pub_enum` | `codex-rs/codex-api/src/requests/responses.rs:15` | `pub enum Compression {` |
| `pub_struct` | `codex-rs/codex-api/src/requests/responses.rs:22` | `pub struct ResponsesRequest {` |
| `pub_struct` | `codex-rs/codex-api/src/requests/responses.rs:29` | `pub struct ResponsesRequestBuilder<'a> {` |
| `pub_fn` | `codex-rs/codex-api/src/requests/responses.rs:47` | `pub fn new(model: &'a str, instructions: &'a str, input: &'a [ResponseItem]) -> Self {` |
| `pub_fn` | `codex-rs/codex-api/src/requests/responses.rs:56` | `pub fn tools(mut self, tools: &'a [Value]) -> Self {` |
| `pub_fn` | `codex-rs/codex-api/src/requests/responses.rs:61` | `pub fn parallel_tool_calls(mut self, enabled: bool) -> Self {` |
| `pub_fn` | `codex-rs/codex-api/src/requests/responses.rs:66` | `pub fn reasoning(mut self, reasoning: Option<Reasoning>) -> Self {` |
| `pub_fn` | `codex-rs/codex-api/src/requests/responses.rs:71` | `pub fn include(mut self, include: Vec<String>) -> Self {` |
| `pub_fn` | `codex-rs/codex-api/src/requests/responses.rs:76` | `pub fn prompt_cache_key(mut self, key: Option<String>) -> Self {` |
| `pub_fn` | `codex-rs/codex-api/src/requests/responses.rs:81` | `pub fn text(mut self, text: Option<TextControls>) -> Self {` |
| `pub_fn` | `codex-rs/codex-api/src/requests/responses.rs:86` | `pub fn conversation(mut self, conversation_id: Option<String>) -> Self {` |
| `pub_fn` | `codex-rs/codex-api/src/requests/responses.rs:91` | `pub fn session_source(mut self, source: Option<SessionSource>) -> Self {` |
| `pub_fn` | `codex-rs/codex-api/src/requests/responses.rs:96` | `pub fn store_override(mut self, store: Option<bool>) -> Self {` |
| `pub_fn` | `codex-rs/codex-api/src/requests/responses.rs:101` | `pub fn extra_headers(mut self, headers: HeaderMap) -> Self {` |
| `pub_fn` | `codex-rs/codex-api/src/requests/responses.rs:106` | `pub fn compression(mut self, compression: Compression) -> Self {` |
| `pub_fn` | `codex-rs/codex-api/src/requests/responses.rs:111` | `pub fn build(self, provider: &Provider) -> Result<ResponsesRequest, ApiError> {` |
| `pub_mod` | `codex-rs/codex-api/src/sse/mod.rs:1` | `pub mod chat;` |
| `pub_mod` | `codex-rs/codex-api/src/sse/mod.rs:2` | `pub mod responses;` |
| `pub_fn` | `codex-rs/codex-api/src/sse/responses.rs:31` | `pub fn stream_from_fixture(` |
| `pub_fn` | `codex-rs/codex-api/src/sse/responses.rs:51` | `pub fn spawn_response_stream(` |
| `pub_struct` | `codex-rs/codex-api/src/sse/responses.rs:158` | `pub struct ResponsesStreamEvent {` |
| `pub_enum` | `codex-rs/codex-api/src/sse/responses.rs:169` | `pub enum ResponsesEventError {` |
| `pub_fn` | `codex-rs/codex-api/src/sse/responses.rs:174` | `pub fn into_api_error(self) -> ApiError {` |
| `pub_fn` | `codex-rs/codex-api/src/sse/responses.rs:181` | `pub fn process_responses_event(` |
| `pub_fn` | `codex-rs/codex-api/src/sse/responses.rs:312` | `pub async fn process_sse(` |
| `pub_trait` | `codex-rs/codex-api/src/telemetry.rs:18` | `pub trait SseTelemetry: Send + Sync {` |
| `pub_trait` | `codex-rs/codex-api/src/telemetry.rs:35` | `pub trait WebsocketTelemetry: Send + Sync {` |
| `pub_mod` | `codex-rs/codex-backend-openapi-models/src/lib.rs:6` | `pub mod models;` |
| `pub_struct` | `codex-rs/codex-backend-openapi-models/src/models/code_task_details_response.rs:16` | `pub struct CodeTaskDetailsResponse {` |
| `pub_fn` | `codex-rs/codex-backend-openapi-models/src/models/code_task_details_response.rs:34` | `pub fn new(task: models::TaskResponse) -> CodeTaskDetailsResponse {` |
| `pub_struct` | `codex-rs/codex-backend-openapi-models/src/models/config_file_response.rs:15` | `pub struct ConfigFileResponse {` |
| `pub_fn` | `codex-rs/codex-backend-openapi-models/src/models/config_file_response.rs:27` | `pub fn new(` |
| `pub_struct` | `codex-rs/codex-backend-openapi-models/src/models/credit_status_details.rs:14` | `pub struct CreditStatusDetails {` |
| `pub_fn` | `codex-rs/codex-backend-openapi-models/src/models/credit_status_details.rs:43` | `pub fn new(has_credits: bool, unlimited: bool) -> CreditStatusDetails {` |
| `pub_struct` | `codex-rs/codex-backend-openapi-models/src/models/external_pull_request_response.rs:16` | `pub struct ExternalPullRequestResponse {` |
| `pub_fn` | `codex-rs/codex-backend-openapi-models/src/models/external_pull_request_response.rs:28` | `pub fn new(` |
| `pub_struct` | `codex-rs/codex-backend-openapi-models/src/models/git_pull_request.rs:15` | `pub struct GitPullRequest {` |
| `pub_fn` | `codex-rs/codex-backend-openapi-models/src/models/git_pull_request.rs:51` | `pub fn new(` |
| `pub_mod` | `codex-rs/codex-backend-openapi-models/src/models/mod.rs:7` | `pub mod config_file_response;` |
| `pub_mod` | `codex-rs/codex-backend-openapi-models/src/models/mod.rs:11` | `pub mod code_task_details_response;` |
| `pub_mod` | `codex-rs/codex-backend-openapi-models/src/models/mod.rs:14` | `pub mod task_response;` |
| `pub_mod` | `codex-rs/codex-backend-openapi-models/src/models/mod.rs:17` | `pub mod external_pull_request_response;` |
| `pub_mod` | `codex-rs/codex-backend-openapi-models/src/models/mod.rs:20` | `pub mod git_pull_request;` |
| `pub_mod` | `codex-rs/codex-backend-openapi-models/src/models/mod.rs:23` | `pub mod task_list_item;` |
| `pub_mod` | `codex-rs/codex-backend-openapi-models/src/models/mod.rs:26` | `pub mod paginated_list_task_list_item_;` |
| `pub_mod` | `codex-rs/codex-backend-openapi-models/src/models/mod.rs:30` | `pub mod rate_limit_status_payload;` |
| `pub_mod` | `codex-rs/codex-backend-openapi-models/src/models/mod.rs:34` | `pub mod rate_limit_status_details;` |
| `pub_mod` | `codex-rs/codex-backend-openapi-models/src/models/mod.rs:37` | `pub mod rate_limit_window_snapshot;` |
| `pub_mod` | `codex-rs/codex-backend-openapi-models/src/models/mod.rs:40` | `pub mod credit_status_details;` |
| `pub_struct` | `codex-rs/codex-backend-openapi-models/src/models/paginated_list_task_list_item_.rs:16` | `pub struct PaginatedListTaskListItem {` |
| `pub_fn` | `codex-rs/codex-backend-openapi-models/src/models/paginated_list_task_list_item_.rs:24` | `pub fn new(items: Vec<models::TaskListItem>) -> PaginatedListTaskListItem {` |
| `pub_struct` | `codex-rs/codex-backend-openapi-models/src/models/rate_limit_status_details.rs:16` | `pub struct RateLimitStatusDetails {` |
| `pub_fn` | `codex-rs/codex-backend-openapi-models/src/models/rate_limit_status_details.rs:38` | `pub fn new(allowed: bool, limit_reached: bool) -> RateLimitStatusDetails {` |
| `pub_struct` | `codex-rs/codex-backend-openapi-models/src/models/rate_limit_status_payload.rs:16` | `pub struct RateLimitStatusPayload {` |
| `pub_fn` | `codex-rs/codex-backend-openapi-models/src/models/rate_limit_status_payload.rs:36` | `pub fn new(plan_type: PlanType) -> RateLimitStatusPayload {` |
| `pub_enum` | `codex-rs/codex-backend-openapi-models/src/models/rate_limit_status_payload.rs:48` | `pub enum PlanType {` |
| `pub_struct` | `codex-rs/codex-backend-openapi-models/src/models/rate_limit_window_snapshot.rs:14` | `pub struct RateLimitWindowSnapshot {` |
| `pub_fn` | `codex-rs/codex-backend-openapi-models/src/models/rate_limit_window_snapshot.rs:26` | `pub fn new(` |
| `pub_struct` | `codex-rs/codex-backend-openapi-models/src/models/task_list_item.rs:16` | `pub struct TaskListItem {` |
| `pub_fn` | `codex-rs/codex-backend-openapi-models/src/models/task_list_item.rs:44` | `pub fn new(` |
| `pub_struct` | `codex-rs/codex-backend-openapi-models/src/models/task_response.rs:16` | `pub struct TaskResponse {` |
| `pub_fn` | `codex-rs/codex-backend-openapi-models/src/models/task_response.rs:44` | `pub fn new(` |
| `pub_struct` | `codex-rs/codex-client/src/default_client.rs:17` | `pub struct CodexHttpClient {` |
| `pub_fn` | `codex-rs/codex-client/src/default_client.rs:22` | `pub fn new(inner: reqwest::Client) -> Self {` |
| `pub_struct` | `codex-rs/codex-client/src/default_client.rs:51` | `pub struct CodexRequestBuilder {` |
| `pub_fn` | `codex-rs/codex-client/src/default_client.rs:74` | `pub fn headers(self, headers: HeaderMap) -> Self {` |
| `pub_fn` | `codex-rs/codex-client/src/default_client.rs:95` | `pub fn timeout(self, timeout: Duration) -> Self {` |
| `pub_fn` | `codex-rs/codex-client/src/default_client.rs:113` | `pub async fn send(self) -> Result<Response, reqwest::Error> {` |
| `pub_enum` | `codex-rs/codex-client/src/error.rs:6` | `pub enum TransportError {` |
| `pub_enum` | `codex-rs/codex-client/src/error.rs:25` | `pub enum StreamError {` |
| `pub_enum` | `codex-rs/codex-client/src/request.rs:9` | `pub enum RequestCompression {` |
| `pub_struct` | `codex-rs/codex-client/src/request.rs:16` | `pub struct Request {` |
| `pub_fn` | `codex-rs/codex-client/src/request.rs:26` | `pub fn new(method: Method, url: String) -> Self {` |
| `pub_fn` | `codex-rs/codex-client/src/request.rs:42` | `pub fn with_compression(mut self, compression: RequestCompression) -> Self {` |
| `pub_struct` | `codex-rs/codex-client/src/request.rs:49` | `pub struct Response {` |
| `pub_struct` | `codex-rs/codex-client/src/retry.rs:9` | `pub struct RetryPolicy {` |
| `pub_struct` | `codex-rs/codex-client/src/retry.rs:16` | `pub struct RetryOn {` |
| `pub_fn` | `codex-rs/codex-client/src/retry.rs:23` | `pub fn should_retry(&self, err: &TransportError, attempt: u64, max_attempts: u64) -> bool {` |
| `pub_fn` | `codex-rs/codex-client/src/retry.rs:38` | `pub fn backoff(base: Duration, attempt: u64) -> Duration {` |
| `pub_fn` | `codex-rs/codex-client/src/sse.rs:12` | `pub fn sse_stream(` |
| `pub_trait` | `codex-rs/codex-client/src/telemetry.rs:6` | `pub trait RequestTelemetry: Send + Sync {` |
| `pub_type` | `codex-rs/codex-client/src/transport.rs:18` | `pub type ByteStream = BoxStream<'static, Result<Bytes, TransportError>>;` |
| `pub_struct` | `codex-rs/codex-client/src/transport.rs:20` | `pub struct StreamResponse {` |
| `pub_trait` | `codex-rs/codex-client/src/transport.rs:27` | `pub trait HttpTransport: Send + Sync {` |
| `pub_struct` | `codex-rs/codex-client/src/transport.rs:33` | `pub struct ReqwestTransport {` |
| `pub_fn` | `codex-rs/codex-client/src/transport.rs:38` | `pub fn new(client: reqwest::Client) -> Self {` |
| `pub_fn` | `codex-rs/codex-experimental-api-macros/src/lib.rs:17` | `pub fn derive_experimental_api(input: TokenStream) -> TokenStream {` |
| `pub_enum` | `codex-rs/common/src/approval_mode_cli_arg.rs:10` | `pub enum ApprovalModeCliArg {` |
| `pub_struct` | `codex-rs/common/src/approval_presets.rs:6` | `pub struct ApprovalPreset {` |
| `pub_fn` | `codex-rs/common/src/approval_presets.rs:22` | `pub fn builtin_approval_presets() -> Vec<ApprovalPreset> {` |
| `pub_struct` | `codex-rs/common/src/config_override.rs:19` | `pub struct CliConfigOverrides {` |
| `pub_fn` | `codex-rs/common/src/config_override.rs:42` | `pub fn parse_overrides(&self) -> Result<Vec<(String, Value)>, String> {` |
| `pub_fn` | `codex-rs/common/src/config_override.rs:82` | `pub fn apply_on_value(&self, target: &mut Value) -> Result<(), String> {` |
| `pub_fn` | `codex-rs/common/src/config_summary.rs:7` | `pub fn create_config_summary_entries(config: &Config, model: &str) -> Vec<(&'static str, String)> {` |
| `pub_fn` | `codex-rs/common/src/elapsed.rs:6` | `pub fn format_elapsed(start_time: Instant) -> String {` |
| `pub_fn` | `codex-rs/common/src/elapsed.rs:16` | `pub fn format_duration(duration: Duration) -> String {` |
| `pub_fn` | `codex-rs/common/src/format_env_display.rs:3` | `pub fn format_env_display(env: Option<&HashMap<String, String>>, env_vars: &[String]) -> String {` |
| `pub_fn` | `codex-rs/common/src/fuzzy_match.rs:12` | `pub fn fuzzy_match(haystack: &str, needle: &str) -> Option<(Vec<usize>, i32)> {` |
| `pub_fn` | `codex-rs/common/src/fuzzy_match.rs:72` | `pub fn fuzzy_indices(haystack: &str, needle: &str) -> Option<Vec<usize>> {` |
| `pub_mod` | `codex-rs/common/src/lib.rs:5` | `pub mod elapsed;` |
| `pub_mod` | `codex-rs/common/src/lib.rs:17` | `pub mod format_env_display;` |
| `pub_mod` | `codex-rs/common/src/lib.rs:34` | `pub mod fuzzy_match;` |
| `pub_mod` | `codex-rs/common/src/lib.rs:37` | `pub mod approval_presets;` |
| `pub_mod` | `codex-rs/common/src/lib.rs:39` | `pub mod oss;` |
| `pub_fn` | `codex-rs/common/src/oss.rs:12` | `pub fn get_default_model_for_oss_provider(provider_id: &str) -> Option<&'static str> {` |
| `pub_fn` | `codex-rs/common/src/oss.rs:21` | `pub async fn ollama_chat_deprecation_notice(` |
| `pub_fn` | `codex-rs/common/src/oss.rs:51` | `pub async fn ensure_oss_provider_ready(` |
| `pub_enum` | `codex-rs/common/src/sandbox_mode_cli_arg.rs:14` | `pub enum SandboxModeCliArg {` |
| `pub_fn` | `codex-rs/common/src/sandbox_summary.rs:4` | `pub fn summarize_sandbox_policy(sandbox_policy: &SandboxPolicy) -> String {` |
| `fn_main` | `codex-rs/core/build.rs:4` | `fn main() {` |
| `pub_enum` | `codex-rs/core/src/agent/role.rs:25` | `pub enum AgentRole {` |
| `pub_struct` | `codex-rs/core/src/agent/role.rs:38` | `pub struct AgentProfile {` |
| `pub_fn` | `codex-rs/core/src/agent/role.rs:53` | `pub fn enum_values() -> Vec<String> {` |
| `pub_fn` | `codex-rs/core/src/agent/role.rs:73` | `pub fn profile(self) -> AgentProfile {` |
| `pub_fn` | `codex-rs/core/src/agent/role.rs:112` | `pub fn apply_to_config(self, config: &mut Config) -> Result<(), String> {` |
| `pub_const` | `codex-rs/core/src/apply_patch.rs:12` | `pub const CODEX_APPLY_PATCH_ARG1: &str = "--codex-run-as-apply-patch";` |
| `pub_enum` | `codex-rs/core/src/auth.rs:45` | `pub enum AuthMode {` |
| `pub_enum` | `codex-rs/core/src/auth.rs:52` | `pub enum CodexAuth {` |
| `pub_struct` | `codex-rs/core/src/auth.rs:59` | `pub struct ApiKeyAuth {` |
| `pub_struct` | `codex-rs/core/src/auth.rs:64` | `pub struct ChatgptAuth {` |
| `pub_struct` | `codex-rs/core/src/auth.rs:70` | `pub struct ChatgptAuthTokens {` |
| `pub_const` | `codex-rs/core/src/auth.rs:95` | `pub const REFRESH_TOKEN_URL_OVERRIDE_ENV_VAR: &str = "CODEX_REFRESH_TOKEN_URL_OVERRIDE";` |
| `pub_enum` | `codex-rs/core/src/auth.rs:98` | `pub enum RefreshTokenError {` |
| `pub_struct` | `codex-rs/core/src/auth.rs:106` | `pub struct ExternalAuthTokens {` |
| `pub_enum` | `codex-rs/core/src/auth.rs:112` | `pub enum ExternalAuthRefreshReason {` |
| `pub_struct` | `codex-rs/core/src/auth.rs:117` | `pub struct ExternalAuthRefreshContext {` |
| `pub_trait` | `codex-rs/core/src/auth.rs:123` | `pub trait ExternalAuthRefresher: Send + Sync {` |
| `pub_fn` | `codex-rs/core/src/auth.rs:131` | `pub fn failed_reason(&self) -> Option<RefreshTokenFailedReason> {` |
| `pub_fn` | `codex-rs/core/src/auth.rs:182` | `pub fn from_auth_storage(` |
| `pub_fn` | `codex-rs/core/src/auth.rs:189` | `pub fn internal_auth_mode(&self) -> AuthMode {` |
| `pub_fn` | `codex-rs/core/src/auth.rs:196` | `pub fn api_auth_mode(&self) -> ApiAuthMode {` |
| `pub_fn` | `codex-rs/core/src/auth.rs:204` | `pub fn is_chatgpt_auth(&self) -> bool {` |
| `pub_fn` | `codex-rs/core/src/auth.rs:208` | `pub fn is_external_chatgpt_tokens(&self) -> bool {` |
| `pub_fn` | `codex-rs/core/src/auth.rs:213` | `pub fn api_key(&self) -> Option<&str> {` |
| `pub_fn` | `codex-rs/core/src/auth.rs:221` | `pub fn get_token_data(&self) -> Result<TokenData, std::io::Error> {` |
| `pub_fn` | `codex-rs/core/src/auth.rs:234` | `pub fn get_token(&self) -> Result<String, std::io::Error> {` |
| `pub_fn` | `codex-rs/core/src/auth.rs:245` | `pub fn get_account_id(&self) -> Option<String> {` |
| `pub_fn` | `codex-rs/core/src/auth.rs:250` | `pub fn get_account_email(&self) -> Option<String> {` |
| `pub_fn` | `codex-rs/core/src/auth.rs:258` | `pub fn account_plan_type(&self) -> Option<AccountPlanType> {` |
| `pub_fn` | `codex-rs/core/src/auth.rs:295` | `pub fn create_dummy_chatgpt_auth_for_testing() -> Self {` |
| `pub_fn` | `codex-rs/core/src/auth.rs:323` | `pub fn from_api_key(api_key: &str) -> Self {` |
| `pub_const` | `codex-rs/core/src/auth.rs:347` | `pub const OPENAI_API_KEY_ENV_VAR: &str = "OPENAI_API_KEY";` |
| `pub_const` | `codex-rs/core/src/auth.rs:348` | `pub const CODEX_API_KEY_ENV_VAR: &str = "CODEX_API_KEY";` |
| `pub_fn` | `codex-rs/core/src/auth.rs:350` | `pub fn read_openai_api_key_from_env() -> Option<String> {` |
| `pub_fn` | `codex-rs/core/src/auth.rs:357` | `pub fn read_codex_api_key_from_env() -> Option<String> {` |
| `pub_fn` | `codex-rs/core/src/auth.rs:366` | `pub fn logout(` |
| `pub_fn` | `codex-rs/core/src/auth.rs:375` | `pub fn login_with_api_key(` |
| `pub_fn` | `codex-rs/core/src/auth.rs:390` | `pub fn login_with_chatgpt_auth_tokens(` |
| `pub_fn` | `codex-rs/core/src/auth.rs:404` | `pub fn save_auth(` |
| `pub_fn` | `codex-rs/core/src/auth.rs:418` | `pub fn load_auth_dot_json(` |
| `pub_fn` | `codex-rs/core/src/auth.rs:426` | `pub fn enforce_login_restrictions(config: &Config) -> std::io::Result<()> {` |
| `pub_const` | `codex-rs/core/src/auth.rs:712` | `pub const CLIENT_ID: &str = "app_EMoamEEZ73f0CkXaXp7hrann";` |
| `pub_struct` | `codex-rs/core/src/auth.rs:822` | `pub struct UnauthorizedRecovery {` |
| `pub_fn` | `codex-rs/core/src/auth.rs:853` | `pub fn has_next(&self) -> bool {` |
| `pub_fn` | `codex-rs/core/src/auth.rs:872` | `pub async fn next(&mut self) -> Result<(), RefreshTokenError> {` |
| `pub_struct` | `codex-rs/core/src/auth.rs:920` | `pub struct AuthManager {` |
| `pub_fn` | `codex-rs/core/src/auth.rs:933` | `pub fn new(` |
| `pub_fn` | `codex-rs/core/src/auth.rs:959` | `pub fn from_auth_for_testing(auth: CodexAuth) -> Arc<Self> {` |
| `pub_fn` | `codex-rs/core/src/auth.rs:976` | `pub fn from_auth_for_testing_with_home(auth: CodexAuth, codex_home: PathBuf) -> Arc<Self> {` |
| `pub_fn` | `codex-rs/core/src/auth.rs:991` | `pub fn auth_cached(&self) -> Option<CodexAuth> {` |
| `pub_fn` | `codex-rs/core/src/auth.rs:997` | `pub async fn auth(&self) -> Option<CodexAuth> {` |
| `pub_fn` | `codex-rs/core/src/auth.rs:1008` | `pub fn reload(&self) -> bool {` |
| `pub_fn` | `codex-rs/core/src/auth.rs:1069` | `pub fn set_external_auth_refresher(&self, refresher: Arc<dyn ExternalAuthRefresher>) {` |
| `pub_fn` | `codex-rs/core/src/auth.rs:1075` | `pub fn set_forced_chatgpt_workspace_id(&self, workspace_id: Option<String>) {` |
| `pub_fn` | `codex-rs/core/src/auth.rs:1081` | `pub fn forced_chatgpt_workspace_id(&self) -> Option<String> {` |
| `pub_fn` | `codex-rs/core/src/auth.rs:1088` | `pub fn has_external_auth_refresher(&self) -> bool {` |
| `pub_fn` | `codex-rs/core/src/auth.rs:1096` | `pub fn is_external_auth_active(&self) -> bool {` |
| `pub_fn` | `codex-rs/core/src/auth.rs:1103` | `pub fn shared(` |
| `pub_fn` | `codex-rs/core/src/auth.rs:1115` | `pub fn unauthorized_recovery(self: &Arc<Self>) -> UnauthorizedRecovery {` |
| `pub_fn` | `codex-rs/core/src/auth.rs:1122` | `pub async fn refresh_token(&self) -> Result<(), RefreshTokenError> {` |
| `pub_fn` | `codex-rs/core/src/auth.rs:1154` | `pub fn logout(&self) -> std::io::Result<bool> {` |
| `pub_fn` | `codex-rs/core/src/auth.rs:1161` | `pub fn get_auth_mode(&self) -> Option<ApiAuthMode> {` |
| `pub_fn` | `codex-rs/core/src/auth.rs:1165` | `pub fn get_internal_auth_mode(&self) -> Option<AuthMode> {` |
| `pub_enum` | `codex-rs/core/src/auth/storage.rs:31` | `pub enum AuthCredentialsStoreMode {` |
| `pub_struct` | `codex-rs/core/src/auth/storage.rs:45` | `pub struct AuthDotJson {` |
| `pub_fn` | `codex-rs/core/src/bash.rs:13` | `pub fn try_parse_shell(shell_lc_arg: &str) -> Option<Tree> {` |
| `pub_fn` | `codex-rs/core/src/bash.rs:29` | `pub fn try_parse_word_only_commands_sequence(tree: &Tree, src: &str) -> Option<Vec<Vec<String>>> {` |
| `pub_fn` | `codex-rs/core/src/bash.rs:97` | `pub fn extract_bash_command(command: &[String]) -> Option<(&str, &str)> {` |
| `pub_fn` | `codex-rs/core/src/bash.rs:115` | `pub fn parse_shell_lc_plain_commands(command: &[String]) -> Option<Vec<Vec<String>>> {` |
| `fn_main` | `codex-rs/core/src/bin/config_schema.rs:13` | `fn main() -> Result<()> {` |
| `pub_const` | `codex-rs/core/src/client.rs:76` | `pub const WEB_SEARCH_ELIGIBLE_HEADER: &str = "x-oai-web-search-eligible";` |
| `pub_const` | `codex-rs/core/src/client.rs:77` | `pub const X_CODEX_TURN_STATE_HEADER: &str = "x-codex-turn-state";` |
| `pub_const` | `codex-rs/core/src/client.rs:78` | `pub const X_CODEX_TURN_METADATA_HEADER: &str = "x-codex-turn-metadata";` |
| `pub_struct` | `codex-rs/core/src/client.rs:102` | `pub struct ModelClient {` |
| `pub_struct` | `codex-rs/core/src/client.rs:106` | `pub struct ModelClientSession {` |
| `pub_fn` | `codex-rs/core/src/client.rs:126` | `pub fn new(` |
| `pub_fn` | `codex-rs/core/src/client.rs:155` | `pub fn new_session(&self, turn_metadata_cwd: Option<PathBuf>) -> ModelClientSession {` |
| `pub_fn` | `codex-rs/core/src/client.rs:200` | `pub fn get_model_context_window(&self) -> Option<i64> {` |
| `pub_fn` | `codex-rs/core/src/client.rs:208` | `pub fn config(&self) -> Arc<Config> {` |
| `pub_fn` | `codex-rs/core/src/client.rs:212` | `pub fn provider(&self) -> &ModelProviderInfo {` |
| `pub_fn` | `codex-rs/core/src/client.rs:216` | `pub fn get_provider(&self) -> ModelProviderInfo {` |
| `pub_fn` | `codex-rs/core/src/client.rs:220` | `pub fn get_otel_manager(&self) -> OtelManager {` |
| `pub_fn` | `codex-rs/core/src/client.rs:224` | `pub fn get_session_source(&self) -> SessionSource {` |
| `pub_fn` | `codex-rs/core/src/client.rs:233` | `pub fn get_model(&self) -> String {` |
| `pub_fn` | `codex-rs/core/src/client.rs:237` | `pub fn get_model_info(&self) -> ModelInfo {` |
| `pub_fn` | `codex-rs/core/src/client.rs:242` | `pub fn get_reasoning_effort(&self) -> Option<ReasoningEffortConfig> {` |
| `pub_fn` | `codex-rs/core/src/client.rs:247` | `pub fn get_reasoning_summary(&self) -> ReasoningSummaryConfig {` |
| `pub_fn` | `codex-rs/core/src/client.rs:251` | `pub fn get_auth_manager(&self) -> Option<Arc<AuthManager>> {` |
| `pub_fn` | `codex-rs/core/src/client.rs:259` | `pub async fn compact_conversation_history(&self, prompt: &Prompt) -> Result<Vec<ResponseItem>> {` |
| `pub_fn` | `codex-rs/core/src/client.rs:318` | `pub async fn stream(&mut self, prompt: &Prompt) -> Result<ResponseStream> {` |
| `pub_const` | `codex-rs/core/src/client_common.rs:17` | `pub const REVIEW_PROMPT: &str = include_str!("../review_prompt.md");` |
| `pub_const` | `codex-rs/core/src/client_common.rs:20` | `pub const REVIEW_EXIT_SUCCESS_TMPL: &str = include_str!("../templates/review/exit_success.xml");` |
| `pub_const` | `codex-rs/core/src/client_common.rs:21` | `pub const REVIEW_EXIT_INTERRUPTED_TMPL: &str =` |
| `pub_struct` | `codex-rs/core/src/client_common.rs:26` | `pub struct Prompt {` |
| `pub_struct` | `codex-rs/core/src/client_common.rs:197` | `pub struct FreeformTool {` |
| `pub_struct` | `codex-rs/core/src/client_common.rs:204` | `pub struct FreeformToolFormat {` |
| `pub_struct` | `codex-rs/core/src/client_common.rs:211` | `pub struct ResponsesApiTool {` |
| `pub_struct` | `codex-rs/core/src/client_common.rs:222` | `pub struct ResponseStream {` |
| `pub_struct` | `codex-rs/core/src/codex.rs:225` | `pub struct Codex {` |
| `pub_struct` | `codex-rs/core/src/codex.rs:237` | `pub struct CodexSpawnOk {` |
| `pub_fn` | `codex-rs/core/src/codex.rs:448` | `pub async fn submit(&self, op: Op) -> CodexResult<String> {` |
| `pub_fn` | `codex-rs/core/src/codex.rs:460` | `pub async fn submit_with_id(&self, sub: Submission) -> CodexResult<()> {` |
| `pub_fn` | `codex-rs/core/src/codex.rs:468` | `pub async fn next_event(&self) -> CodexResult<Event> {` |
| `pub_fn` | `codex-rs/core/src/codex.rs:1582` | `pub async fn request_command_approval(` |
| `pub_fn` | `codex-rs/core/src/codex.rs:1623` | `pub async fn request_patch_approval(` |
| `pub_fn` | `codex-rs/core/src/codex.rs:1660` | `pub async fn request_user_input(` |
| `pub_fn` | `codex-rs/core/src/codex.rs:1692` | `pub async fn notify_user_input_response(` |
| `pub_fn` | `codex-rs/core/src/codex.rs:1717` | `pub async fn notify_dynamic_tool_response(&self, call_id: &str, response: DynamicToolResponse) {` |
| `pub_fn` | `codex-rs/core/src/codex.rs:1738` | `pub async fn notify_approval(&self, sub_id: &str, decision: ReviewDecision) {` |
| `pub_fn` | `codex-rs/core/src/codex.rs:1759` | `pub async fn resolve_elicitation(` |
| `pub_fn` | `codex-rs/core/src/codex.rs:1877` | `pub fn enabled(&self, feature: Feature) -> bool {` |
| `pub_fn` | `codex-rs/core/src/codex.rs:2055` | `pub async fn dependency_env(&self) -> HashMap<String, String> {` |
| `pub_fn` | `codex-rs/core/src/codex.rs:2060` | `pub async fn set_dependency_env(&self, values: HashMap<String, String>) {` |
| `pub_fn` | `codex-rs/core/src/codex.rs:2177` | `pub async fn inject_input(&self, input: Vec<UserInput>) -> Result<(), Vec<UserInput>> {` |
| `pub_fn` | `codex-rs/core/src/codex.rs:2190` | `pub async fn inject_response_items(` |
| `pub_fn` | `codex-rs/core/src/codex.rs:2207` | `pub async fn get_pending_input(&self) -> Vec<ResponseInputItem> {` |
| `pub_fn` | `codex-rs/core/src/codex.rs:2218` | `pub async fn has_pending_input(&self) -> bool {` |
| `pub_fn` | `codex-rs/core/src/codex.rs:2229` | `pub async fn list_resources(` |
| `pub_fn` | `codex-rs/core/src/codex.rs:2242` | `pub async fn list_resource_templates(` |
| `pub_fn` | `codex-rs/core/src/codex.rs:2255` | `pub async fn read_resource(` |
| `pub_fn` | `codex-rs/core/src/codex.rs:2268` | `pub async fn call_tool(` |
| `pub_fn` | `codex-rs/core/src/codex.rs:2291` | `pub async fn interrupt_task(self: &Arc<Self>) {` |
| `pub_fn` | `codex-rs/core/src/codex.rs:2594` | `pub async fn interrupt(sess: &Arc<Session>) {` |
| `pub_fn` | `codex-rs/core/src/codex.rs:2598` | `pub async fn override_turn_context(` |
| `pub_fn` | `codex-rs/core/src/codex.rs:2615` | `pub async fn user_input_or_turn(` |
| `pub_fn` | `codex-rs/core/src/codex.rs:2698` | `pub async fn run_user_shell_command(` |
| `pub_fn` | `codex-rs/core/src/codex.rs:2714` | `pub async fn resolve_elicitation(` |
| `pub_fn` | `codex-rs/core/src/codex.rs:2751` | `pub async fn exec_approval(sess: &Arc<Session>, id: String, decision: ReviewDecision) {` |
| `pub_fn` | `codex-rs/core/src/codex.rs:2784` | `pub async fn patch_approval(sess: &Arc<Session>, id: String, decision: ReviewDecision) {` |
| `pub_fn` | `codex-rs/core/src/codex.rs:2793` | `pub async fn request_user_input_response(` |
| `pub_fn` | `codex-rs/core/src/codex.rs:2801` | `pub async fn dynamic_tool_response(` |
| `pub_fn` | `codex-rs/core/src/codex.rs:2809` | `pub async fn add_to_history(sess: &Arc<Session>, config: &Arc<Config>, text: String) {` |
| `pub_fn` | `codex-rs/core/src/codex.rs:2819` | `pub async fn get_history_entry_request(` |
| `pub_fn` | `codex-rs/core/src/codex.rs:2856` | `pub async fn refresh_mcp_servers(sess: &Arc<Session>, refresh_config: McpServerRefreshConfig) {` |
| `pub_fn` | `codex-rs/core/src/codex.rs:2861` | `pub async fn list_mcp_tools(sess: &Session, config: &Arc<Config>, sub_id: String) {` |
| `pub_fn` | `codex-rs/core/src/codex.rs:2878` | `pub async fn list_custom_prompts(sess: &Session, sub_id: String) {` |
| `pub_fn` | `codex-rs/core/src/codex.rs:2895` | `pub async fn list_skills(` |
| `pub_fn` | `codex-rs/core/src/codex.rs:2928` | `pub async fn undo(sess: &Arc<Session>, sub_id: String) {` |
| `pub_fn` | `codex-rs/core/src/codex.rs:2934` | `pub async fn compact(sess: &Arc<Session>, sub_id: String) {` |
| `pub_fn` | `codex-rs/core/src/codex.rs:2949` | `pub async fn thread_rollback(sess: &Arc<Session>, sub_id: String, num_turns: u32) {` |
| `pub_fn` | `codex-rs/core/src/codex.rs:2999` | `pub async fn set_thread_name(sess: &Arc<Session>, sub_id: String, name: String) {` |
| `pub_fn` | `codex-rs/core/src/codex.rs:3058` | `pub async fn shutdown(sess: &Arc<Session>, sub_id: String) -> bool {` |
| `pub_fn` | `codex-rs/core/src/codex.rs:3105` | `pub async fn review(` |
| `pub_struct` | `codex-rs/core/src/codex_thread.rs:18` | `pub struct ThreadConfigSnapshot {` |
| `pub_struct` | `codex-rs/core/src/codex_thread.rs:29` | `pub struct CodexThread {` |
| `pub_fn` | `codex-rs/core/src/codex_thread.rs:44` | `pub async fn submit(&self, op: Op) -> CodexResult<String> {` |
| `pub_fn` | `codex-rs/core/src/codex_thread.rs:49` | `pub async fn submit_with_id(&self, sub: Submission) -> CodexResult<()> {` |
| `pub_fn` | `codex-rs/core/src/codex_thread.rs:53` | `pub async fn next_event(&self) -> CodexResult<Event> {` |
| `pub_fn` | `codex-rs/core/src/codex_thread.rs:57` | `pub async fn agent_status(&self) -> AgentStatus {` |
| `pub_fn` | `codex-rs/core/src/codex_thread.rs:65` | `pub fn rollout_path(&self) -> Option<PathBuf> {` |
| `pub_fn` | `codex-rs/core/src/codex_thread.rs:69` | `pub fn state_db(&self) -> Option<StateDbHandle> {` |
| `pub_fn` | `codex-rs/core/src/codex_thread.rs:73` | `pub async fn config_snapshot(&self) -> ThreadConfigSnapshot {` |
| `pub_fn` | `codex-rs/core/src/command_safety/is_dangerous_command.rs:6` | `pub fn command_might_be_dangerous(command: &[String]) -> bool {` |
| `pub_fn` | `codex-rs/core/src/command_safety/is_safe_command.rs:8` | `pub fn is_known_safe_command(command: &[String]) -> bool {` |
| `pub_mod` | `codex-rs/core/src/command_safety/mod.rs:1` | `pub mod is_dangerous_command;` |
| `pub_mod` | `codex-rs/core/src/command_safety/mod.rs:2` | `pub mod is_safe_command;` |
| `pub_mod` | `codex-rs/core/src/command_safety/mod.rs:3` | `pub mod windows_safe_commands;` |
| `pub_fn` | `codex-rs/core/src/command_safety/windows_dangerous_commands.rs:8` | `pub fn is_dangerous_command_windows(command: &[String]) -> bool {` |
| `pub_fn` | `codex-rs/core/src/command_safety/windows_safe_commands.rs:12` | `pub fn is_safe_command_windows(command: &[String]) -> bool {` |
| `pub_const` | `codex-rs/core/src/compact.rs:32` | `pub const SUMMARIZATION_PROMPT: &str = include_str!("../templates/compact/prompt.md");` |
| `pub_const` | `codex-rs/core/src/compact.rs:33` | `pub const SUMMARY_PREFIX: &str = include_str!("../templates/compact/summary_prefix.md");` |
| `pub_fn` | `codex-rs/core/src/compact.rs:208` | `pub fn content_items_to_text(content: &[ContentItem]) -> Option<String> {` |
| `pub_enum` | `codex-rs/core/src/config/constraint.rs:8` | `pub enum ConstraintError {` |
| `pub_fn` | `codex-rs/core/src/config/constraint.rs:30` | `pub fn empty_field(field_name: impl Into<String>) -> Self {` |
| `pub_type` | `codex-rs/core/src/config/constraint.rs:37` | `pub type ConstraintResult<T> = Result<T, ConstraintError>;` |
| `pub_struct` | `codex-rs/core/src/config/constraint.rs:51` | `pub struct Constrained<T> {` |
| `pub_fn` | `codex-rs/core/src/config/constraint.rs:58` | `pub fn new(` |
| `pub_fn` | `codex-rs/core/src/config/constraint.rs:72` | `pub fn normalized(` |
| `pub_fn` | `codex-rs/core/src/config/constraint.rs:87` | `pub fn allow_any(initial_value: T) -> Self {` |
| `pub_fn` | `codex-rs/core/src/config/constraint.rs:96` | `pub fn allow_any_from_default() -> Self` |
| `pub_fn` | `codex-rs/core/src/config/constraint.rs:103` | `pub fn get(&self) -> &T {` |
| `pub_fn` | `codex-rs/core/src/config/constraint.rs:107` | `pub fn value(&self) -> T` |
| `pub_fn` | `codex-rs/core/src/config/constraint.rs:114` | `pub fn can_set(&self, candidate: &T) -> ConstraintResult<()> {` |
| `pub_fn` | `codex-rs/core/src/config/constraint.rs:118` | `pub fn set(&mut self, value: T) -> ConstraintResult<()> {` |
| `pub_enum` | `codex-rs/core/src/config/edit.rs:22` | `pub enum ConfigEdit {` |
| `pub_fn` | `codex-rs/core/src/config/edit.rs:631` | `pub fn apply_blocking(` |
| `pub_fn` | `codex-rs/core/src/config/edit.rs:685` | `pub async fn apply(` |
| `pub_struct` | `codex-rs/core/src/config/edit.rs:699` | `pub struct ConfigEditsBuilder {` |
| `pub_fn` | `codex-rs/core/src/config/edit.rs:706` | `pub fn new(codex_home: &Path) -> Self {` |
| `pub_fn` | `codex-rs/core/src/config/edit.rs:714` | `pub fn with_profile(mut self, profile: Option<&str>) -> Self {` |
| `pub_fn` | `codex-rs/core/src/config/edit.rs:719` | `pub fn set_model(mut self, model: Option<&str>, effort: Option<ReasoningEffort>) -> Self {` |
| `pub_fn` | `codex-rs/core/src/config/edit.rs:727` | `pub fn set_personality(mut self, personality: Option<Personality>) -> Self {` |
| `pub_fn` | `codex-rs/core/src/config/edit.rs:733` | `pub fn set_hide_full_access_warning(mut self, acknowledged: bool) -> Self {` |
| `pub_fn` | `codex-rs/core/src/config/edit.rs:739` | `pub fn set_hide_world_writable_warning(mut self, acknowledged: bool) -> Self {` |
| `pub_fn` | `codex-rs/core/src/config/edit.rs:745` | `pub fn set_hide_rate_limit_model_nudge(mut self, acknowledged: bool) -> Self {` |
| `pub_fn` | `codex-rs/core/src/config/edit.rs:751` | `pub fn set_hide_model_migration_prompt(mut self, model: &str, acknowledged: bool) -> Self {` |
| `pub_fn` | `codex-rs/core/src/config/edit.rs:760` | `pub fn record_model_migration_seen(mut self, from: &str, to: &str) -> Self {` |
| `pub_fn` | `codex-rs/core/src/config/edit.rs:768` | `pub fn set_windows_wsl_setup_acknowledged(mut self, acknowledged: bool) -> Self {` |
| `pub_fn` | `codex-rs/core/src/config/edit.rs:774` | `pub fn replace_mcp_servers(mut self, servers: &BTreeMap<String, McpServerConfig>) -> Self {` |
| `pub_fn` | `codex-rs/core/src/config/edit.rs:793` | `pub fn set_feature_enabled(mut self, key: &str, enabled: bool) -> Self {` |
| `pub_fn` | `codex-rs/core/src/config/edit.rs:810` | `pub fn apply_blocking(self) -> anyhow::Result<()> {` |
| `pub_fn` | `codex-rs/core/src/config/edit.rs:815` | `pub async fn apply(self) -> anyhow::Result<()> {` |
| `pub_mod` | `codex-rs/core/src/config/mod.rs:78` | `pub mod edit;` |
| `pub_mod` | `codex-rs/core/src/config/mod.rs:79` | `pub mod profile;` |
| `pub_mod` | `codex-rs/core/src/config/mod.rs:80` | `pub mod schema;` |
| `pub_mod` | `codex-rs/core/src/config/mod.rs:81` | `pub mod service;` |
| `pub_mod` | `codex-rs/core/src/config/mod.rs:82` | `pub mod types;` |
| `pub_const` | `codex-rs/core/src/config/mod.rs:98` | `pub const CONFIG_TOML_FILE: &str = "config.toml";` |
| `pub_struct` | `codex-rs/core/src/config/mod.rs:113` | `pub struct Config {` |
| `pub_struct` | `codex-rs/core/src/config/mod.rs:370` | `pub struct ConfigBuilder {` |
| `pub_fn` | `codex-rs/core/src/config/mod.rs:380` | `pub fn codex_home(mut self, codex_home: PathBuf) -> Self {` |
| `pub_fn` | `codex-rs/core/src/config/mod.rs:385` | `pub fn cli_overrides(mut self, cli_overrides: Vec<(String, TomlValue)>) -> Self {` |
| `pub_fn` | `codex-rs/core/src/config/mod.rs:390` | `pub fn harness_overrides(mut self, harness_overrides: ConfigOverrides) -> Self {` |
| `pub_fn` | `codex-rs/core/src/config/mod.rs:395` | `pub fn loader_overrides(mut self, loader_overrides: LoaderOverrides) -> Self {` |
| `pub_fn` | `codex-rs/core/src/config/mod.rs:400` | `pub fn cloud_requirements(mut self, cloud_requirements: CloudRequirementsLoader) -> Self {` |
| `pub_fn` | `codex-rs/core/src/config/mod.rs:405` | `pub fn fallback_cwd(mut self, fallback_cwd: Option<PathBuf>) -> Self {` |
| `pub_fn` | `codex-rs/core/src/config/mod.rs:410` | `pub async fn build(self) -> std::io::Result<Config> {` |
| `pub_fn` | `codex-rs/core/src/config/mod.rs:469` | `pub async fn load_with_cli_overrides(` |
| `pub_fn` | `codex-rs/core/src/config/mod.rs:479` | `pub fn load_default_with_cli_overrides(` |
| `pub_fn` | `codex-rs/core/src/config/mod.rs:507` | `pub async fn load_with_cli_overrides_and_harness_overrides(` |
| `pub_fn` | `codex-rs/core/src/config/mod.rs:522` | `pub async fn load_config_as_toml_with_cli_overrides(` |
| `pub_fn` | `codex-rs/core/src/config/mod.rs:617` | `pub async fn load_global_mcp_servers(` |
| `pub_fn` | `codex-rs/core/src/config/mod.rs:744` | `pub fn set_project_trust_level(` |
| `pub_fn` | `codex-rs/core/src/config/mod.rs:757` | `pub fn set_default_oss_provider(codex_home: &Path, provider: &str) -> std::io::Result<()> {` |
| `pub_struct` | `codex-rs/core/src/config/mod.rs:788` | `pub struct ConfigToml {` |
| `pub_struct` | `codex-rs/core/src/config/mod.rs:1019` | `pub struct ProjectConfig {` |
| `pub_fn` | `codex-rs/core/src/config/mod.rs:1024` | `pub fn is_trusted(&self) -> bool {` |
| `pub_fn` | `codex-rs/core/src/config/mod.rs:1028` | `pub fn is_untrusted(&self) -> bool {` |
| `pub_struct` | `codex-rs/core/src/config/mod.rs:1035` | `pub struct ToolsToml {` |
| `pub_struct` | `codex-rs/core/src/config/mod.rs:1046` | `pub struct AgentsToml {` |
| `pub_struct` | `codex-rs/core/src/config/mod.rs:1064` | `pub struct GhostSnapshotToml {` |
| `pub_struct` | `codex-rs/core/src/config/mod.rs:1077` | `pub struct SandboxPolicyResolution {` |
| `pub_fn` | `codex-rs/core/src/config/mod.rs:1140` | `pub fn get_active_project(&self, resolved_cwd: &Path) -> Option<ProjectConfig> {` |
| `pub_fn` | `codex-rs/core/src/config/mod.rs:1160` | `pub fn get_config_profile(` |
| `pub_struct` | `codex-rs/core/src/config/mod.rs:1184` | `pub struct ConfigOverrides {` |
| `pub_fn` | `codex-rs/core/src/config/mod.rs:1207` | `pub fn resolve_oss_provider(` |
| `pub_fn` | `codex-rs/core/src/config/mod.rs:1720` | `pub fn set_windows_sandbox_enabled(&mut self, value: bool) {` |
| `pub_fn` | `codex-rs/core/src/config/mod.rs:1729` | `pub fn set_windows_elevated_sandbox_enabled(&mut self, value: bool) {` |
| `pub_fn` | `codex-rs/core/src/config/mod.rs:1771` | `pub fn find_codex_home() -> std::io::Result<PathBuf> {` |
| `pub_fn` | `codex-rs/core/src/config/mod.rs:1777` | `pub fn log_dir(cfg: &Config) -> std::io::Result<PathBuf> {` |
| `pub_struct` | `codex-rs/core/src/config/profile.rs:18` | `pub struct ConfigProfile {` |
| `pub_fn` | `codex-rs/core/src/config/schema.rs:56` | `pub fn config_schema() -> RootSchema {` |
| `pub_fn` | `codex-rs/core/src/config/schema.rs:83` | `pub fn config_schema_json() -> anyhow::Result<Vec<u8>> {` |
| `pub_fn` | `codex-rs/core/src/config/schema.rs:92` | `pub fn write_config_schema(out_path: &Path) -> anyhow::Result<()> {` |
| `pub_enum` | `codex-rs/core/src/config/service.rs:40` | `pub enum ConfigServiceError {` |
| `pub_fn` | `codex-rs/core/src/config/service.rs:100` | `pub fn write_error_code(&self) -> Option<ConfigWriteErrorCode> {` |
| `pub_struct` | `codex-rs/core/src/config/service.rs:109` | `pub struct ConfigService {` |
| `pub_fn` | `codex-rs/core/src/config/service.rs:117` | `pub fn new(` |
| `pub_fn` | `codex-rs/core/src/config/service.rs:131` | `pub fn new_with_defaults(codex_home: PathBuf) -> Self {` |
| `pub_fn` | `codex-rs/core/src/config/service.rs:140` | `pub async fn read(` |
| `pub_fn` | `codex-rs/core/src/config/service.rs:189` | `pub async fn read_requirements(` |
| `pub_fn` | `codex-rs/core/src/config/service.rs:205` | `pub async fn write_value(` |
| `pub_fn` | `codex-rs/core/src/config/service.rs:214` | `pub async fn batch_write(` |
| `pub_fn` | `codex-rs/core/src/config/service.rs:228` | `pub async fn load_user_saved_config(` |
| `pub_const` | `codex-rs/core/src/config/types.rs:25` | `pub const DEFAULT_OTEL_ENVIRONMENT: &str = "dev";` |
| `pub_enum` | `codex-rs/core/src/config/types.rs:28` | `pub enum McpServerDisabledReason {` |
| `pub_struct` | `codex-rs/core/src/config/types.rs:45` | `pub struct McpServerConfig {` |
| `pub_enum` | `codex-rs/core/src/config/types.rs:209` | `pub enum McpServerTransportConfig {` |
| `pub_enum` | `codex-rs/core/src/config/types.rs:266` | `pub enum UriBasedFileOpener {` |
| `pub_fn` | `codex-rs/core/src/config/types.rs:285` | `pub fn get_scheme(&self) -> Option<&str> {` |
| `pub_struct` | `codex-rs/core/src/config/types.rs:299` | `pub struct History {` |
| `pub_enum` | `codex-rs/core/src/config/types.rs:310` | `pub enum HistoryPersistence {` |
| `pub_struct` | `codex-rs/core/src/config/types.rs:323` | `pub struct AnalyticsConfigToml {` |
| `pub_struct` | `codex-rs/core/src/config/types.rs:330` | `pub struct FeedbackConfigToml {` |
| `pub_enum` | `codex-rs/core/src/config/types.rs:339` | `pub enum OtelHttpProtocol {` |
| `pub_struct` | `codex-rs/core/src/config/types.rs:349` | `pub struct OtelTlsConfig {` |
| `pub_enum` | `codex-rs/core/src/config/types.rs:359` | `pub enum OtelExporterKind {` |
| `pub_struct` | `codex-rs/core/src/config/types.rs:382` | `pub struct OtelConfigToml {` |
| `pub_struct` | `codex-rs/core/src/config/types.rs:398` | `pub struct OtelConfig {` |
| `pub_enum` | `codex-rs/core/src/config/types.rs:420` | `pub enum Notifications {` |
| `pub_enum` | `codex-rs/core/src/config/types.rs:433` | `pub enum NotificationMethod {` |
| `pub_struct` | `codex-rs/core/src/config/types.rs:453` | `pub struct Tui {` |
| `pub_struct` | `codex-rs/core/src/config/types.rs:499` | `pub struct Notice {` |
| `pub_struct` | `codex-rs/core/src/config/types.rs:523` | `pub struct SkillConfig {` |
| `pub_struct` | `codex-rs/core/src/config/types.rs:530` | `pub struct SkillsConfig {` |
| `pub_struct` | `codex-rs/core/src/config/types.rs:537` | `pub struct SandboxWorkspaceWrite {` |
| `pub_enum` | `codex-rs/core/src/config/types.rs:561` | `pub enum ShellEnvironmentPolicyInherit {` |
| `pub_struct` | `codex-rs/core/src/config/types.rs:578` | `pub struct ShellEnvironmentPolicyToml {` |
| `pub_type` | `codex-rs/core/src/config/types.rs:594` | `pub type EnvironmentVariablePattern = WildMatchPattern<'*', '?'>;` |
| `pub_struct` | `codex-rs/core/src/config/types.rs:604` | `pub struct ShellEnvironmentPolicy {` |
| `pub_struct` | `codex-rs/core/src/config_loader/cloud_requirements.rs:9` | `pub struct CloudRequirementsLoader {` |
| `pub_fn` | `codex-rs/core/src/config_loader/cloud_requirements.rs:24` | `pub async fn get(&self) -> Option<ConfigRequirementsToml> {` |
| `pub_enum` | `codex-rs/core/src/config_loader/config_requirements.rs:15` | `pub enum RequirementSource {` |
| `pub_struct` | `codex-rs/core/src/config_loader/config_requirements.rs:50` | `pub struct ConfigRequirements {` |
| `pub_enum` | `codex-rs/core/src/config_loader/config_requirements.rs:72` | `pub enum McpServerIdentity {` |
| `pub_struct` | `codex-rs/core/src/config_loader/config_requirements.rs:78` | `pub struct McpServerRequirement {` |
| `pub_struct` | `codex-rs/core/src/config_loader/config_requirements.rs:84` | `pub struct ConfigRequirementsToml {` |
| `pub_struct` | `codex-rs/core/src/config_loader/config_requirements.rs:95` | `pub struct Sourced<T> {` |
| `pub_fn` | `codex-rs/core/src/config_loader/config_requirements.rs:101` | `pub fn new(value: T, source: RequirementSource) -> Self {` |
| `pub_struct` | `codex-rs/core/src/config_loader/config_requirements.rs:115` | `pub struct ConfigRequirementsWithSources {` |
| `pub_fn` | `codex-rs/core/src/config_loader/config_requirements.rs:124` | `pub fn merge_unset_fields(&mut self, source: RequirementSource, other: ConfigRequirementsToml) {` |
| `pub_fn` | `codex-rs/core/src/config_loader/config_requirements.rs:158` | `pub fn into_toml(self) -> ConfigRequirementsToml {` |
| `pub_enum` | `codex-rs/core/src/config_loader/config_requirements.rs:179` | `pub enum SandboxModeRequirement {` |
| `pub_enum` | `codex-rs/core/src/config_loader/config_requirements.rs:205` | `pub enum ResidencyRequirement {` |
| `pub_fn` | `codex-rs/core/src/config_loader/config_requirements.rs:210` | `pub fn is_empty(&self) -> bool {` |
| `pub_struct` | `codex-rs/core/src/config_loader/diagnostics.rs:25` | `pub struct TextPosition {` |
| `pub_struct` | `codex-rs/core/src/config_loader/diagnostics.rs:32` | `pub struct TextRange {` |
| `pub_struct` | `codex-rs/core/src/config_loader/diagnostics.rs:38` | `pub struct ConfigError {` |
| `pub_fn` | `codex-rs/core/src/config_loader/diagnostics.rs:45` | `pub fn new(path: PathBuf, range: TextRange, message: impl Into<String>) -> Self {` |
| `pub_struct` | `codex-rs/core/src/config_loader/diagnostics.rs:55` | `pub struct ConfigLoadError {` |
| `pub_fn` | `codex-rs/core/src/config_loader/diagnostics.rs:61` | `pub fn new(error: ConfigError, source: Option<toml::de::Error>) -> Self {` |
| `pub_fn` | `codex-rs/core/src/config_loader/diagnostics.rs:65` | `pub fn config_error(&self) -> &ConfigError {` |
| `pub_fn` | `codex-rs/core/src/config_loader/diagnostics.rs:210` | `pub fn format_config_error(error: &ConfigError, contents: &str) -> String {` |
| `pub_fn` | `codex-rs/core/src/config_loader/diagnostics.rs:246` | `pub fn format_config_error_with_source(error: &ConfigError) -> String {` |
| `pub_fn` | `codex-rs/core/src/config_loader/merge.rs:4` | `pub fn merge_toml_values(base: &mut TomlValue, overlay: &TomlValue) {` |
| `pub_const` | `codex-rs/core/src/config_loader/mod.rs:66` | `pub const SYSTEM_CONFIG_TOML_FILE_UNIX: &str = "/etc/codex/config.toml";` |
| `pub_fn` | `codex-rs/core/src/config_loader/mod.rs:100` | `pub async fn load_config_layers_state(` |
| `pub_fn` | `codex-rs/core/src/config_loader/requirements_exec_policy.rs:18` | `pub fn new(policy: Policy) -> Self {` |
| `pub_struct` | `codex-rs/core/src/config_loader/requirements_exec_policy.rs:50` | `pub struct RequirementsExecPolicyToml {` |
| `pub_struct` | `codex-rs/core/src/config_loader/requirements_exec_policy.rs:58` | `pub struct RequirementsExecPolicyPrefixRuleToml {` |
| `pub_struct` | `codex-rs/core/src/config_loader/requirements_exec_policy.rs:70` | `pub struct RequirementsExecPolicyPatternTokenToml {` |
| `pub_enum` | `codex-rs/core/src/config_loader/requirements_exec_policy.rs:77` | `pub enum RequirementsExecPolicyDecisionToml {` |
| `pub_enum` | `codex-rs/core/src/config_loader/requirements_exec_policy.rs:94` | `pub enum RequirementsExecPolicyParseError {` |
| `pub_fn` | `codex-rs/core/src/config_loader/requirements_exec_policy.rs:125` | `pub fn to_policy(&self) -> Result<Policy, RequirementsExecPolicyParseError> {` |
| `pub_struct` | `codex-rs/core/src/config_loader/state.rs:18` | `pub struct LoaderOverrides {` |
| `pub_struct` | `codex-rs/core/src/config_loader/state.rs:27` | `pub struct ConfigLayerEntry {` |
| `pub_fn` | `codex-rs/core/src/config_loader/state.rs:35` | `pub fn new(name: ConfigLayerSource, config: TomlValue) -> Self {` |
| `pub_fn` | `codex-rs/core/src/config_loader/state.rs:45` | `pub fn new_disabled(` |
| `pub_fn` | `codex-rs/core/src/config_loader/state.rs:59` | `pub fn is_disabled(&self) -> bool {` |
| `pub_fn` | `codex-rs/core/src/config_loader/state.rs:63` | `pub fn metadata(&self) -> ConfigLayerMetadata {` |
| `pub_fn` | `codex-rs/core/src/config_loader/state.rs:70` | `pub fn as_layer(&self) -> ConfigLayer {` |
| `pub_fn` | `codex-rs/core/src/config_loader/state.rs:80` | `pub fn config_folder(&self) -> Option<AbsolutePathBuf> {` |
| `pub_enum` | `codex-rs/core/src/config_loader/state.rs:94` | `pub enum ConfigLayerStackOrdering {` |
| `pub_struct` | `codex-rs/core/src/config_loader/state.rs:100` | `pub struct ConfigLayerStack {` |
| `pub_fn` | `codex-rs/core/src/config_loader/state.rs:119` | `pub fn new(` |
| `pub_fn` | `codex-rs/core/src/config_loader/state.rs:134` | `pub fn get_user_layer(&self) -> Option<&ConfigLayerEntry> {` |
| `pub_fn` | `codex-rs/core/src/config_loader/state.rs:139` | `pub fn requirements(&self) -> &ConfigRequirements {` |
| `pub_fn` | `codex-rs/core/src/config_loader/state.rs:143` | `pub fn requirements_toml(&self) -> &ConfigRequirementsToml {` |
| `pub_fn` | `codex-rs/core/src/config_loader/state.rs:151` | `pub fn with_user_config(&self, config_toml: &AbsolutePathBuf, user_config: TomlValue) -> Self {` |
| `pub_fn` | `codex-rs/core/src/config_loader/state.rs:194` | `pub fn effective_config(&self) -> TomlValue {` |
| `pub_fn` | `codex-rs/core/src/config_loader/state.rs:202` | `pub fn origins(&self) -> HashMap<String, ConfigLayerMetadata> {` |
| `pub_fn` | `codex-rs/core/src/config_loader/state.rs:215` | `pub fn layers_high_to_low(&self) -> Vec<&ConfigLayerEntry> {` |
| `pub_fn` | `codex-rs/core/src/config_loader/state.rs:221` | `pub fn get_layers(` |
| `pub_fn` | `codex-rs/core/src/connectors.rs:20` | `pub async fn list_accessible_connectors_from_mcp_tools(` |
| `pub_fn` | `codex-rs/core/src/connectors.rs:80` | `pub fn connector_display_label(connector: &AppInfo) -> String {` |
| `pub_fn` | `codex-rs/core/src/connectors.rs:84` | `pub fn connector_mention_slug(connector: &AppInfo) -> String {` |
| `pub_fn` | `codex-rs/core/src/connectors.rs:102` | `pub fn merge_connectors(` |
| `pub_fn` | `codex-rs/core/src/connectors.rs:200` | `pub fn connector_install_url(name: &str, connector_id: &str) -> String {` |
| `pub_fn` | `codex-rs/core/src/connectors.rs:205` | `pub fn connector_name_slug(name: &str) -> String {` |
| `pub_fn` | `codex-rs/core/src/custom_prompts.rs:9` | `pub fn default_prompts_dir() -> Option<PathBuf> {` |
| `pub_fn` | `codex-rs/core/src/custom_prompts.rs:17` | `pub async fn discover_prompts_in(dir: &Path) -> Vec<CustomPrompt> {` |
| `pub_fn` | `codex-rs/core/src/custom_prompts.rs:23` | `pub async fn discover_prompts_in_excluding(` |
| `pub_static` | `codex-rs/core/src/default_client.rs:26` | `pub static USER_AGENT_SUFFIX: LazyLock<Mutex<Option<String>>> = LazyLock::new(|| Mutex::new(None));` |
| `pub_const` | `codex-rs/core/src/default_client.rs:27` | `pub const DEFAULT_ORIGINATOR: &str = "codex_cli_rs";` |
| `pub_const` | `codex-rs/core/src/default_client.rs:28` | `pub const CODEX_INTERNAL_ORIGINATOR_OVERRIDE_ENV_VAR: &str = "CODEX_INTERNAL_ORIGINATOR_OVERRIDE";` |
| `pub_const` | `codex-rs/core/src/default_client.rs:29` | `pub const RESIDENCY_HEADER_NAME: &str = "x-openai-internal-codex-residency";` |
| `pub_struct` | `codex-rs/core/src/default_client.rs:32` | `pub struct Originator {` |
| `pub_enum` | `codex-rs/core/src/default_client.rs:41` | `pub enum SetOriginatorError {` |
| `pub_fn` | `codex-rs/core/src/default_client.rs:67` | `pub fn set_default_originator(value: String) -> Result<(), SetOriginatorError> {` |
| `pub_fn` | `codex-rs/core/src/default_client.rs:82` | `pub fn set_default_client_residency_requirement(enforce_residency: Option<ResidencyRequirement>) {` |
| `pub_fn` | `codex-rs/core/src/default_client.rs:90` | `pub fn originator() -> Originator {` |
| `pub_fn` | `codex-rs/core/src/default_client.rs:111` | `pub fn is_first_party_originator(originator_value: &str) -> bool {` |
| `pub_fn` | `codex-rs/core/src/default_client.rs:117` | `pub fn get_codex_user_agent() -> String {` |
| `pub_fn` | `codex-rs/core/src/default_client.rs:176` | `pub fn create_client() -> CodexHttpClient {` |
| `pub_fn` | `codex-rs/core/src/default_client.rs:181` | `pub fn build_reqwest_client() -> reqwest::Client {` |
| `pub_fn` | `codex-rs/core/src/env.rs:8` | `pub fn is_wsl() -> bool {` |
| `pub_fn` | `codex-rs/core/src/env.rs:29` | `pub fn is_headless_environment() -> bool {` |
| `pub_fn` | `codex-rs/core/src/environment_context.rs:19` | `pub fn new(cwd: Option<PathBuf>, shell: Shell) -> Self {` |
| `pub_fn` | `codex-rs/core/src/environment_context.rs:26` | `pub fn equals_except_shell(&self, other: &EnvironmentContext) -> bool {` |
| `pub_fn` | `codex-rs/core/src/environment_context.rs:37` | `pub fn diff(before: &TurnContext, after: &TurnContext, shell: &Shell) -> Self {` |
| `pub_fn` | `codex-rs/core/src/environment_context.rs:46` | `pub fn from_turn_context(turn_context: &TurnContext, shell: &Shell) -> Self {` |
| `pub_fn` | `codex-rs/core/src/environment_context.rs:62` | `pub fn serialize_to_xml(self) -> String {` |
| `pub_type` | `codex-rs/core/src/error.rs:22` | `pub type Result<T> = std::result::Result<T, CodexErr>;` |
| `pub_enum` | `codex-rs/core/src/error.rs:28` | `pub enum SandboxErr {` |
| `pub_enum` | `codex-rs/core/src/error.rs:60` | `pub enum CodexErr {` |
| `pub_fn` | `codex-rs/core/src/error.rs:191` | `pub fn is_retryable(&self) -> bool {` |
| `pub_struct` | `codex-rs/core/src/error.rs:230` | `pub struct ConnectionFailedError {` |
| `pub_struct` | `codex-rs/core/src/error.rs:241` | `pub struct ResponseStreamFailed {` |
| `pub_struct` | `codex-rs/core/src/error.rs:262` | `pub struct RefreshTokenFailedError {` |
| `pub_fn` | `codex-rs/core/src/error.rs:268` | `pub fn new(reason: RefreshTokenFailedReason, message: impl Into<String>) -> Self {` |
| `pub_enum` | `codex-rs/core/src/error.rs:277` | `pub enum RefreshTokenFailedReason {` |
| `pub_struct` | `codex-rs/core/src/error.rs:285` | `pub struct UnexpectedResponseError {` |
| `pub_struct` | `codex-rs/core/src/error.rs:339` | `pub struct RetryLimitReachedError {` |
| `pub_struct` | `codex-rs/core/src/error.rs:359` | `pub struct UsageLimitReachedError {` |
| `pub_struct` | `codex-rs/core/src/error.rs:413` | `pub struct ModelCapError {` |
| `pub_struct` | `codex-rs/core/src/error.rs:508` | `pub struct EnvVarError {` |
| `pub_fn` | `codex-rs/core/src/error.rs:536` | `pub fn to_codex_protocol_error(&self) -> CodexErrorInfo {` |
| `pub_fn` | `codex-rs/core/src/error.rs:567` | `pub fn to_error_event(&self, message_prefix: Option<String>) -> ErrorEvent {` |
| `pub_fn` | `codex-rs/core/src/error.rs:579` | `pub fn http_status_code_value(&self) -> Option<u16> {` |
| `pub_fn` | `codex-rs/core/src/error.rs:591` | `pub fn get_error_message_ui(e: &CodexErr) -> String {` |
| `pub_fn` | `codex-rs/core/src/event_mapping.rs:91` | `pub fn parse_turn_item(item: &ResponseItem) -> Option<TurnItem> {` |
| `pub_const` | `codex-rs/core/src/exec.rs:37` | `pub const DEFAULT_EXEC_COMMAND_TIMEOUT_MS: u64 = 10_000;` |
| `pub_struct` | `codex-rs/core/src/exec.rs:61` | `pub struct ExecParams {` |
| `pub_enum` | `codex-rs/core/src/exec.rs:74` | `pub enum ExecExpiration {` |
| `pub_enum` | `codex-rs/core/src/exec.rs:118` | `pub enum SandboxType {` |
| `pub_struct` | `codex-rs/core/src/exec.rs:132` | `pub struct StdoutStream {` |
| `pub_fn` | `codex-rs/core/src/exec.rs:138` | `pub async fn process_exec_tool_call(` |
| `pub_struct` | `codex-rs/core/src/exec.rs:550` | `pub struct StreamOutput<T: Clone> {` |
| `pub_fn` | `codex-rs/core/src/exec.rs:565` | `pub fn new(text: String) -> Self {` |
| `pub_fn` | `codex-rs/core/src/exec.rs:574` | `pub fn from_utf8_lossy(&self) -> StreamOutput<String> {` |
| `pub_struct` | `codex-rs/core/src/exec.rs:626` | `pub struct ExecToolCallOutput {` |
| `pub_fn` | `codex-rs/core/src/exec_env.rs:14` | `pub fn create_env(policy: &ShellEnvironmentPolicy) -> HashMap<String, String> {` |
| `pub_enum` | `codex-rs/core/src/exec_policy.rs:48` | `pub enum ExecPolicyError {` |
| `pub_enum` | `codex-rs/core/src/exec_policy.rs:69` | `pub enum ExecPolicyUpdateError {` |
| `pub_fn` | `codex-rs/core/src/exec_policy.rs:223` | `pub async fn check_execpolicy_for_warnings(` |
| `pub_fn` | `codex-rs/core/src/exec_policy.rs:246` | `pub async fn load_exec_policy(config_stack: &ConfigLayerStack) -> Result<Policy, ExecPolicyError> {` |
| `pub_fn` | `codex-rs/core/src/exec_policy.rs:298` | `pub fn render_decision_for_unmatched_command(` |
| `pub_enum` | `codex-rs/core/src/features.rs:29` | `pub enum Stage {` |
| `pub_fn` | `codex-rs/core/src/features.rs:47` | `pub fn experimental_menu_name(self) -> Option<&'static str> {` |
| `pub_fn` | `codex-rs/core/src/features.rs:54` | `pub fn experimental_menu_description(self) -> Option<&'static str> {` |
| `pub_fn` | `codex-rs/core/src/features.rs:63` | `pub fn experimental_announcement(self) -> Option<&'static str> {` |
| `pub_enum` | `codex-rs/core/src/features.rs:73` | `pub enum Feature {` |
| `pub_fn` | `codex-rs/core/src/features.rs:133` | `pub fn key(self) -> &'static str {` |
| `pub_fn` | `codex-rs/core/src/features.rs:137` | `pub fn stage(self) -> Stage {` |
| `pub_fn` | `codex-rs/core/src/features.rs:141` | `pub fn default_enabled(self) -> bool {` |
| `pub_struct` | `codex-rs/core/src/features.rs:154` | `pub struct LegacyFeatureUsage {` |
| `pub_struct` | `codex-rs/core/src/features.rs:163` | `pub struct Features {` |
| `pub_struct` | `codex-rs/core/src/features.rs:169` | `pub struct FeatureOverrides {` |
| `pub_fn` | `codex-rs/core/src/features.rs:187` | `pub fn with_defaults() -> Self {` |
| `pub_fn` | `codex-rs/core/src/features.rs:200` | `pub fn enabled(&self, f: Feature) -> bool {` |
| `pub_fn` | `codex-rs/core/src/features.rs:204` | `pub fn enable(&mut self, f: Feature) -> &mut Self {` |
| `pub_fn` | `codex-rs/core/src/features.rs:209` | `pub fn disable(&mut self, f: Feature) -> &mut Self {` |
| `pub_fn` | `codex-rs/core/src/features.rs:214` | `pub fn record_legacy_usage_force(&mut self, alias: &str, feature: Feature) {` |
| `pub_fn` | `codex-rs/core/src/features.rs:224` | `pub fn record_legacy_usage(&mut self, alias: &str, feature: Feature) {` |
| `pub_fn` | `codex-rs/core/src/features.rs:231` | `pub fn legacy_feature_usages(&self) -> impl Iterator<Item = &LegacyFeatureUsage> + '_ {` |
| `pub_fn` | `codex-rs/core/src/features.rs:235` | `pub fn emit_metrics(&self, otel: &OtelManager) {` |
| `pub_fn` | `codex-rs/core/src/features.rs:251` | `pub fn apply_map(&mut self, m: &BTreeMap<String, bool>) {` |
| `pub_fn` | `codex-rs/core/src/features.rs:286` | `pub fn from_config(` |
| `pub_fn` | `codex-rs/core/src/features.rs:323` | `pub fn enabled_features(&self) -> Vec<Feature> {` |
| `pub_fn` | `codex-rs/core/src/features.rs:375` | `pub fn is_known_feature_key(key: &str) -> bool {` |
| `pub_struct` | `codex-rs/core/src/features.rs:381` | `pub struct FeaturesToml {` |
| `pub_struct` | `codex-rs/core/src/features.rs:388` | `pub struct FeatureSpec {` |
| `pub_const` | `codex-rs/core/src/features.rs:395` | `pub const FEATURES: &[FeatureSpec] = &[` |
| `pub_fn` | `codex-rs/core/src/features.rs:583` | `pub fn maybe_push_unstable_features_warning(` |
| `pub_struct` | `codex-rs/core/src/features/legacy.rs:53` | `pub struct LegacyFeatureToggles {` |
| `pub_fn` | `codex-rs/core/src/features/legacy.rs:61` | `pub fn apply(self, features: &mut Features) {` |
| `pub_enum` | `codex-rs/core/src/function_tool.rs:4` | `pub enum FunctionCallError {` |
| `pub_fn` | `codex-rs/core/src/git_info.rs:28` | `pub fn get_git_repo_root(base_dir: &Path) -> Option<PathBuf> {` |
| `pub_struct` | `codex-rs/core/src/git_info.rs:50` | `pub struct GitDiffToRemote {` |
| `pub_fn` | `codex-rs/core/src/git_info.rs:59` | `pub async fn collect_git_info(cwd: &Path) -> Option<GitInfo> {` |
| `pub_fn` | `codex-rs/core/src/git_info.rs:114` | `pub async fn get_git_remote_urls(cwd: &Path) -> Option<BTreeMap<String, String>> {` |
| `pub_fn` | `codex-rs/core/src/git_info.rs:127` | `pub async fn get_git_remote_urls_assume_git_repo(cwd: &Path) -> Option<BTreeMap<String, String>> {` |
| `pub_fn` | `codex-rs/core/src/git_info.rs:138` | `pub async fn get_head_commit_hash(cwd: &Path) -> Option<String> {` |
| `pub_struct` | `codex-rs/core/src/git_info.rs:182` | `pub struct CommitLogEntry {` |
| `pub_fn` | `codex-rs/core/src/git_info.rs:193` | `pub async fn recent_commits(cwd: &Path, limit: usize) -> Vec<CommitLogEntry> {` |
| `pub_fn` | `codex-rs/core/src/git_info.rs:240` | `pub async fn git_diff_to_remote(cwd: &Path) -> Option<GitDiffToRemote> {` |
| `pub_fn` | `codex-rs/core/src/git_info.rs:340` | `pub async fn default_branch_name(cwd: &Path) -> Option<String> {` |
| `pub_fn` | `codex-rs/core/src/git_info.rs:600` | `pub fn resolve_root_git_project_for_trust(cwd: &Path) -> Option<PathBuf> {` |
| `pub_fn` | `codex-rs/core/src/git_info.rs:627` | `pub async fn local_git_branches(cwd: &Path) -> Vec<String> {` |
| `pub_fn` | `codex-rs/core/src/git_info.rs:654` | `pub async fn current_branch_name(cwd: &Path) -> Option<String> {` |
| `pub_const` | `codex-rs/core/src/instructions/user_instructions.rs:7` | `pub const USER_INSTRUCTIONS_OPEN_TAG_LEGACY: &str = "<user_instructions>";` |
| `pub_const` | `codex-rs/core/src/instructions/user_instructions.rs:8` | `pub const USER_INSTRUCTIONS_PREFIX: &str = "# AGENTS.md instructions for ";` |
| `pub_const` | `codex-rs/core/src/instructions/user_instructions.rs:9` | `pub const SKILL_INSTRUCTIONS_PREFIX: &str = "<skill";` |
| `pub_fn` | `codex-rs/core/src/instructions/user_instructions.rs:19` | `pub fn is_user_instructions(message: &[ContentItem]) -> bool {` |
| `pub_fn` | `codex-rs/core/src/instructions/user_instructions.rs:56` | `pub fn is_skill_instructions(message: &[ContentItem]) -> bool {` |
| `pub_mod` | `codex-rs/core/src/lib.rs:9` | `pub mod api_bridge;` |
| `pub_mod` | `codex-rs/core/src/lib.rs:11` | `pub mod auth;` |
| `pub_mod` | `codex-rs/core/src/lib.rs:12` | `pub mod bash;` |
| `pub_mod` | `codex-rs/core/src/lib.rs:15` | `pub mod codex;` |
| `pub_mod` | `codex-rs/core/src/lib.rs:23` | `pub mod config;` |
| `pub_mod` | `codex-rs/core/src/lib.rs:24` | `pub mod config_loader;` |
| `pub_mod` | `codex-rs/core/src/lib.rs:25` | `pub mod connectors;` |
| `pub_mod` | `codex-rs/core/src/lib.rs:27` | `pub mod custom_prompts;` |
| `pub_mod` | `codex-rs/core/src/lib.rs:28` | `pub mod env;` |
| `pub_mod` | `codex-rs/core/src/lib.rs:30` | `pub mod error;` |
| `pub_mod` | `codex-rs/core/src/lib.rs:31` | `pub mod exec;` |
| `pub_mod` | `codex-rs/core/src/lib.rs:32` | `pub mod exec_env;` |
| `pub_mod` | `codex-rs/core/src/lib.rs:34` | `pub mod features;` |
| `pub_mod` | `codex-rs/core/src/lib.rs:36` | `pub mod git_info;` |
| `pub_mod` | `codex-rs/core/src/lib.rs:37` | `pub mod instructions;` |
| `pub_mod` | `codex-rs/core/src/lib.rs:38` | `pub mod landlock;` |
| `pub_mod` | `codex-rs/core/src/lib.rs:39` | `pub mod mcp;` |
| `pub_mod` | `codex-rs/core/src/lib.rs:41` | `pub mod models_manager;` |
| `pub_mod` | `codex-rs/core/src/lib.rs:50` | `pub mod parse_command;` |
| `pub_mod` | `codex-rs/core/src/lib.rs:51` | `pub mod path_utils;` |
| `pub_mod` | `codex-rs/core/src/lib.rs:52` | `pub mod personality_migration;` |
| `pub_mod` | `codex-rs/core/src/lib.rs:53` | `pub mod powershell;` |
| `pub_mod` | `codex-rs/core/src/lib.rs:55` | `pub mod sandboxing;` |
| `pub_mod` | `codex-rs/core/src/lib.rs:60` | `pub mod token_data;` |
| `pub_mod` | `codex-rs/core/src/lib.rs:63` | `pub mod windows_sandbox;` |
| `pub_mod` | `codex-rs/core/src/lib.rs:75` | `pub mod review_format;` |
| `pub_mod` | `codex-rs/core/src/lib.rs:76` | `pub mod review_prompts;` |
| `pub_mod` | `codex-rs/core/src/lib.rs:78` | `pub mod web_search;` |
| `pub_type` | `codex-rs/core/src/lib.rs:83` | `pub type ConversationManager = ThreadManager;` |
| `pub_type` | `codex-rs/core/src/lib.rs:85` | `pub type NewConversation = NewThread;` |
| `pub_type` | `codex-rs/core/src/lib.rs:87` | `pub type CodexConversation = CodexThread;` |
| `pub_mod` | `codex-rs/core/src/lib.rs:91` | `pub mod default_client;` |
| `pub_mod` | `codex-rs/core/src/lib.rs:92` | `pub mod project_doc;` |
| `pub_mod` | `codex-rs/core/src/lib.rs:95` | `pub mod seatbelt;` |
| `pub_mod` | `codex-rs/core/src/lib.rs:96` | `pub mod shell;` |
| `pub_mod` | `codex-rs/core/src/lib.rs:97` | `pub mod shell_snapshot;` |
| `pub_mod` | `codex-rs/core/src/lib.rs:98` | `pub mod skills;` |
| `pub_mod` | `codex-rs/core/src/lib.rs:99` | `pub mod spawn;` |
| `pub_mod` | `codex-rs/core/src/lib.rs:100` | `pub mod state_db;` |
| `pub_mod` | `codex-rs/core/src/lib.rs:101` | `pub mod terminal;` |
| `pub_mod` | `codex-rs/core/src/lib.rs:103` | `pub mod turn_diff_tracker;` |
| `pub_mod` | `codex-rs/core/src/lib.rs:131` | `pub mod util;` |
| `pub_mod` | `codex-rs/core/src/lib.rs:163` | `pub mod compact;` |
| `pub_mod` | `codex-rs/core/src/lib.rs:164` | `pub mod otel_init;` |
| `pub_struct` | `codex-rs/core/src/mcp/auth.rs:15` | `pub struct McpOAuthLoginConfig {` |
| `pub_enum` | `codex-rs/core/src/mcp/auth.rs:22` | `pub enum McpOAuthLoginSupport {` |
| `pub_fn` | `codex-rs/core/src/mcp/auth.rs:28` | `pub async fn oauth_login_support(transport: &McpServerTransportConfig) -> McpOAuthLoginSupport {` |
| `pub_struct` | `codex-rs/core/src/mcp/auth.rs:55` | `pub struct McpAuthStatusEntry {` |
| `pub_mod` | `codex-rs/core/src/mcp/mod.rs:1` | `pub mod auth;` |
| `pub_fn` | `codex-rs/core/src/mcp/mod.rs:140` | `pub async fn collect_mcp_snapshot(config: &Config) -> McpListToolsResponseEvent {` |
| `pub_fn` | `codex-rs/core/src/mcp/mod.rs:191` | `pub fn split_qualified_tool_name(qualified_name: &str) -> Option<(String, String)> {` |
| `pub_fn` | `codex-rs/core/src/mcp/mod.rs:205` | `pub fn group_tools_by_server(` |
| `pub_const` | `codex-rs/core/src/mcp_connection_manager.rs:81` | `pub const DEFAULT_STARTUP_TIMEOUT: Duration = Duration::from_secs(10);` |
| `pub_const` | `codex-rs/core/src/mcp_connection_manager.rs:304` | `pub const MCP_SANDBOX_STATE_CAPABILITY: &str = "codex/sandbox-state";` |
| `pub_const` | `codex-rs/core/src/mcp_connection_manager.rs:308` | `pub const MCP_SANDBOX_STATE_METHOD: &str = "codex/sandbox-state/update";` |
| `pub_struct` | `codex-rs/core/src/mcp_connection_manager.rs:312` | `pub struct SandboxState {` |
| `pub_fn` | `codex-rs/core/src/mcp_connection_manager.rs:326` | `pub async fn initialize(` |
| `pub_fn` | `codex-rs/core/src/mcp_connection_manager.rs:439` | `pub async fn resolve_elicitation(` |
| `pub_fn` | `codex-rs/core/src/mcp_connection_manager.rs:464` | `pub async fn list_all_tools(&self) -> HashMap<String, ToolInfo> {` |
| `pub_fn` | `codex-rs/core/src/mcp_connection_manager.rs:488` | `pub async fn list_all_resources(&self) -> HashMap<String, Vec<Resource>> {` |
| `pub_fn` | `codex-rs/core/src/mcp_connection_manager.rs:553` | `pub async fn list_all_resource_templates(&self) -> HashMap<String, Vec<ResourceTemplate>> {` |
| `pub_fn` | `codex-rs/core/src/mcp_connection_manager.rs:621` | `pub async fn call_tool(` |
| `pub_fn` | `codex-rs/core/src/mcp_connection_manager.rs:658` | `pub async fn list_resources(` |
| `pub_fn` | `codex-rs/core/src/mcp_connection_manager.rs:674` | `pub async fn list_resource_templates(` |
| `pub_fn` | `codex-rs/core/src/mcp_connection_manager.rs:690` | `pub async fn read_resource(` |
| `pub_fn` | `codex-rs/core/src/mcp_connection_manager.rs:706` | `pub async fn parse_tool_name(&self, tool_name: &str) -> Option<(String, String)> {` |
| `pub_fn` | `codex-rs/core/src/mcp_connection_manager.rs:713` | `pub async fn notify_sandbox_state_change(&self, sandbox_state: &SandboxState) -> Result<()> {` |
| `pub_struct` | `codex-rs/core/src/message_history.rs:57` | `pub struct HistoryEntry {` |
| `pub_const` | `codex-rs/core/src/model_provider_info.rs:31` | `pub const CHAT_WIRE_API_DEPRECATION_SUMMARY: &str = r#"Support for the "chat" wire API is deprecated and will soon be removed. Update your model provider definition in config.toml to use wire_api = "responses"."#;` |
| `pub_enum` | `codex-rs/core/src/model_provider_info.rs:43` | `pub enum WireApi {` |
| `pub_struct` | `codex-rs/core/src/model_provider_info.rs:55` | `pub struct ModelProviderInfo {` |
| `pub_fn` | `codex-rs/core/src/model_provider_info.rs:186` | `pub fn api_key(&self) -> crate::error::Result<Option<String>> {` |
| `pub_fn` | `codex-rs/core/src/model_provider_info.rs:210` | `pub fn request_max_retries(&self) -> u64 {` |
| `pub_fn` | `codex-rs/core/src/model_provider_info.rs:217` | `pub fn stream_max_retries(&self) -> u64 {` |
| `pub_fn` | `codex-rs/core/src/model_provider_info.rs:224` | `pub fn stream_idle_timeout(&self) -> Duration {` |
| `pub_fn` | `codex-rs/core/src/model_provider_info.rs:229` | `pub fn create_openai_provider() -> ModelProviderInfo {` |
| `pub_fn` | `codex-rs/core/src/model_provider_info.rs:270` | `pub fn is_openai(&self) -> bool {` |
| `pub_const` | `codex-rs/core/src/model_provider_info.rs:275` | `pub const DEFAULT_LMSTUDIO_PORT: u16 = 1234;` |
| `pub_const` | `codex-rs/core/src/model_provider_info.rs:276` | `pub const DEFAULT_OLLAMA_PORT: u16 = 11434;` |
| `pub_const` | `codex-rs/core/src/model_provider_info.rs:278` | `pub const LMSTUDIO_OSS_PROVIDER_ID: &str = "lmstudio";` |
| `pub_const` | `codex-rs/core/src/model_provider_info.rs:279` | `pub const OLLAMA_OSS_PROVIDER_ID: &str = "ollama";` |
| `pub_const` | `codex-rs/core/src/model_provider_info.rs:280` | `pub const OLLAMA_CHAT_PROVIDER_ID: &str = "ollama-chat";` |
| `pub_fn` | `codex-rs/core/src/model_provider_info.rs:283` | `pub fn built_in_model_providers() -> HashMap<String, ModelProviderInfo> {` |
| `pub_fn` | `codex-rs/core/src/model_provider_info.rs:310` | `pub fn create_oss_provider(default_provider_port: u16, wire_api: WireApi) -> ModelProviderInfo {` |
| `pub_fn` | `codex-rs/core/src/model_provider_info.rs:330` | `pub fn create_oss_provider_with_base_url(base_url: &str, wire_api: WireApi) -> ModelProviderInfo {` |
| `pub_fn` | `codex-rs/core/src/models_manager/collaboration_mode_presets.rs:22` | `pub fn test_builtin_collaboration_mode_presets() -> Vec<CollaborationModeMask> {` |
| `pub_enum` | `codex-rs/core/src/models_manager/manager.rs:36` | `pub enum RefreshStrategy {` |
| `pub_struct` | `codex-rs/core/src/models_manager/manager.rs:47` | `pub struct ModelsManager {` |
| `pub_fn` | `codex-rs/core/src/models_manager/manager.rs:60` | `pub fn new(codex_home: PathBuf, auth_manager: Arc<AuthManager>) -> Self {` |
| `pub_fn` | `codex-rs/core/src/models_manager/manager.rs:76` | `pub async fn list_models(` |
| `pub_fn` | `codex-rs/core/src/models_manager/manager.rs:94` | `pub fn list_collaboration_modes(&self) -> Vec<CollaborationModeMask> {` |
| `pub_fn` | `codex-rs/core/src/models_manager/manager.rs:101` | `pub fn try_list_models(&self, config: &Config) -> Result<Vec<ModelPreset>, TryLockError> {` |
| `pub_fn` | `codex-rs/core/src/models_manager/manager.rs:111` | `pub async fn get_default_model(` |
| `pub_fn` | `codex-rs/core/src/models_manager/manager.rs:138` | `pub async fn get_model_info(&self, model: &str, config: &Config) -> ModelInfo {` |
| `pub_fn` | `codex-rs/core/src/models_manager/manager.rs:317` | `pub fn with_provider(` |
| `pub_fn` | `codex-rs/core/src/models_manager/manager.rs:336` | `pub fn get_model_offline(model: Option<&str>) -> String {` |
| `pub_fn` | `codex-rs/core/src/models_manager/manager.rs:351` | `pub fn construct_model_info_offline(model: &str, config: &Config) -> ModelInfo {` |
| `pub_mod` | `codex-rs/core/src/models_manager/mod.rs:1` | `pub mod cache;` |
| `pub_mod` | `codex-rs/core/src/models_manager/mod.rs:2` | `pub mod collaboration_mode_presets;` |
| `pub_mod` | `codex-rs/core/src/models_manager/mod.rs:3` | `pub mod manager;` |
| `pub_mod` | `codex-rs/core/src/models_manager/mod.rs:4` | `pub mod model_info;` |
| `pub_mod` | `codex-rs/core/src/models_manager/mod.rs:5` | `pub mod model_presets;` |
| `pub_fn` | `codex-rs/core/src/models_manager/mod.rs:11` | `pub fn client_version_to_whole() -> String {` |
| `pub_const` | `codex-rs/core/src/models_manager/model_info.rs:19` | `pub const BASE_INSTRUCTIONS: &str = include_str!("../../prompt.md");` |
| `pub_const` | `codex-rs/core/src/models_manager/model_presets.rs:10` | `pub const HIDE_GPT5_1_MIGRATION_PROMPT_CONFIG: &str = "hide_gpt5_1_migration_prompt";` |
| `pub_const` | `codex-rs/core/src/models_manager/model_presets.rs:11` | `pub const HIDE_GPT_5_1_CODEX_MAX_MIGRATION_PROMPT_CONFIG: &str =` |
| `pub_fn` | `codex-rs/core/src/models_manager/model_presets.rs:363` | `pub fn all_model_presets() -> &'static Vec<ModelPreset> {` |
| `pub_fn` | `codex-rs/core/src/otel_init.rs:16` | `pub fn build_provider(` |
| `pub_fn` | `codex-rs/core/src/otel_init.rs:97` | `pub fn codex_export_filter(meta: &tracing::Metadata<'_>) -> bool {` |
| `pub_fn` | `codex-rs/core/src/parse_command.rs:10` | `pub fn shlex_join(tokens: &[String]) -> String {` |
| `pub_fn` | `codex-rs/core/src/parse_command.rs:16` | `pub fn extract_shell_command(command: &[String]) -> Option<(&str, &str)> {` |
| `pub_fn` | `codex-rs/core/src/parse_command.rs:30` | `pub fn parse_command(command: &[String]) -> Vec<ParsedCommand> {` |
| `pub_fn` | `codex-rs/core/src/parse_command.rs:1333` | `pub fn parse_command_impl(command: &[String]) -> Vec<ParsedCommand> {` |
| `pub_fn` | `codex-rs/core/src/path_utils.rs:10` | `pub fn normalize_for_path_comparison(path: impl AsRef<Path>) -> std::io::Result<PathBuf> {` |
| `pub_struct` | `codex-rs/core/src/path_utils.rs:15` | `pub struct SymlinkWritePaths {` |
| `pub_fn` | `codex-rs/core/src/path_utils.rs:26` | `pub fn resolve_symlink_write_paths(path: &Path) -> io::Result<SymlinkWritePaths> {` |
| `pub_fn` | `codex-rs/core/src/path_utils.rs:101` | `pub fn write_atomically(write_path: &Path, contents: &str) -> io::Result<()> {` |
| `pub_const` | `codex-rs/core/src/personality_migration.rs:17` | `pub const PERSONALITY_MIGRATION_FILENAME: &str = ".personality_migration";` |
| `pub_enum` | `codex-rs/core/src/personality_migration.rs:20` | `pub enum PersonalityMigrationStatus {` |
| `pub_fn` | `codex-rs/core/src/personality_migration.rs:27` | `pub async fn maybe_migrate_personality(` |
| `pub_fn` | `codex-rs/core/src/powershell.rs:43` | `pub fn extract_powershell_command(command: &[String]) -> Option<(&str, &str)> {` |
| `pub_const` | `codex-rs/core/src/project_doc.rs:29` | `pub const DEFAULT_PROJECT_DOC_FILENAME: &str = "AGENTS.md";` |
| `pub_const` | `codex-rs/core/src/project_doc.rs:31` | `pub const LOCAL_PROJECT_DOC_FILENAME: &str = "AGENTS.override.md";` |
| `pub_fn` | `codex-rs/core/src/project_doc.rs:92` | `pub async fn read_project_docs(config: &Config) -> std::io::Result<Option<String>> {` |
| `pub_fn` | `codex-rs/core/src/project_doc.rs:150` | `pub fn discover_project_doc_paths(config: &Config) -> std::io::Result<Vec<PathBuf>> {` |
| `pub_fn` | `codex-rs/core/src/review_format.rs:23` | `pub fn format_review_findings_block(` |
| `pub_fn` | `codex-rs/core/src/review_format.rs:64` | `pub fn render_review_output_text(output: &ReviewOutputEvent) -> String {` |
| `pub_struct` | `codex-rs/core/src/review_prompts.rs:7` | `pub struct ResolvedReviewRequest {` |
| `pub_fn` | `codex-rs/core/src/review_prompts.rs:22` | `pub fn resolve_review_request(` |
| `pub_fn` | `codex-rs/core/src/review_prompts.rs:39` | `pub fn review_prompt(target: &ReviewTarget, cwd: &Path) -> anyhow::Result<String> {` |
| `pub_fn` | `codex-rs/core/src/review_prompts.rs:70` | `pub fn user_facing_hint(target: &ReviewTarget) -> String {` |
| `pub_struct` | `codex-rs/core/src/rollout/list.rs:31` | `pub struct ThreadsPage {` |
| `pub_struct` | `codex-rs/core/src/rollout/list.rs:44` | `pub struct ThreadItem {` |
| `pub_type` | `codex-rs/core/src/rollout/list.rs:59` | `pub type ConversationItem = ThreadItem;` |
| `pub_type` | `codex-rs/core/src/rollout/list.rs:62` | `pub type ConversationsPage = ThreadsPage;` |
| `pub_enum` | `codex-rs/core/src/rollout/list.rs:81` | `pub enum ThreadSortKey {` |
| `pub_struct` | `codex-rs/core/src/rollout/list.rs:101` | `pub struct Cursor {` |
| `pub_fn` | `codex-rs/core/src/rollout/list.rs:624` | `pub fn parse_cursor(token: &str) -> Option<Cursor> {` |
| `pub_fn` | `codex-rs/core/src/rollout/list.rs:1024` | `pub async fn read_head_for_summary(path: &Path) -> io::Result<Vec<serde_json::Value>> {` |
| `pub_fn` | `codex-rs/core/src/rollout/list.rs:1031` | `pub async fn read_session_meta_line(path: &Path) -> io::Result<SessionMetaLine> {` |
| `pub_fn` | `codex-rs/core/src/rollout/list.rs:1129` | `pub async fn find_thread_path_by_id_str(` |
| `pub_fn` | `codex-rs/core/src/rollout/list.rs:1137` | `pub async fn find_archived_thread_path_by_id_str(` |
| `pub_fn` | `codex-rs/core/src/rollout/list.rs:1145` | `pub fn rollout_date_parts(file_name: &OsStr) -> Option<(String, String, String)> {` |
| `pub_const` | `codex-rs/core/src/rollout/mod.rs:5` | `pub const SESSIONS_SUBDIR: &str = "sessions";` |
| `pub_const` | `codex-rs/core/src/rollout/mod.rs:6` | `pub const ARCHIVED_SESSIONS_SUBDIR: &str = "archived_sessions";` |
| `pub_const` | `codex-rs/core/src/rollout/mod.rs:7` | `pub const INTERACTIVE_SESSION_SOURCES: &[SessionSource] =` |
| `pub_mod` | `codex-rs/core/src/rollout/mod.rs:11` | `pub mod list;` |
| `pub_mod` | `codex-rs/core/src/rollout/mod.rs:14` | `pub mod recorder;` |
| `pub_mod` | `codex-rs/core/src/rollout/mod.rs:30` | `pub mod tests;` |
| `pub_struct` | `codex-rs/core/src/rollout/recorder.rs:59` | `pub struct RolloutRecorder {` |
| `pub_enum` | `codex-rs/core/src/rollout/recorder.rs:66` | `pub enum RolloutRecorderParams {` |
| `pub_fn` | `codex-rs/core/src/rollout/recorder.rs:91` | `pub fn new(` |
| `pub_fn` | `codex-rs/core/src/rollout/recorder.rs:107` | `pub fn resume(path: PathBuf) -> Self {` |
| `pub_fn` | `codex-rs/core/src/rollout/recorder.rs:114` | `pub async fn list_threads(` |
| `pub_fn` | `codex-rs/core/src/rollout/recorder.rs:164` | `pub async fn list_archived_threads(` |
| `pub_fn` | `codex-rs/core/src/rollout/recorder.rs:219` | `pub async fn find_latest_thread_path(` |
| `pub_fn` | `codex-rs/core/src/rollout/recorder.rs:254` | `pub async fn new(` |
| `pub_fn` | `codex-rs/core/src/rollout/recorder.rs:343` | `pub fn rollout_path(&self) -> &Path {` |
| `pub_fn` | `codex-rs/core/src/rollout/recorder.rs:347` | `pub fn state_db(&self) -> Option<StateDbHandle> {` |
| `pub_fn` | `codex-rs/core/src/rollout/recorder.rs:371` | `pub async fn flush(&self) -> std::io::Result<()> {` |
| `pub_fn` | `codex-rs/core/src/rollout/recorder.rs:446` | `pub async fn get_rollout_history(path: &Path) -> std::io::Result<InitialHistory> {` |
| `pub_fn` | `codex-rs/core/src/rollout/recorder.rs:463` | `pub async fn shutdown(&self) -> std::io::Result<()> {` |
| `pub_struct` | `codex-rs/core/src/rollout/session_index.rs:20` | `pub struct SessionIndexEntry {` |
| `pub_fn` | `codex-rs/core/src/rollout/session_index.rs:28` | `pub async fn append_thread_name(` |
| `pub_fn` | `codex-rs/core/src/rollout/session_index.rs:49` | `pub async fn append_session_index_entry(` |
| `pub_fn` | `codex-rs/core/src/rollout/session_index.rs:67` | `pub async fn find_thread_name_by_id(` |
| `pub_fn` | `codex-rs/core/src/rollout/session_index.rs:83` | `pub async fn find_thread_names_by_ids(` |
| `pub_fn` | `codex-rs/core/src/rollout/session_index.rs:115` | `pub async fn find_thread_id_by_name(` |
| `pub_fn` | `codex-rs/core/src/rollout/session_index.rs:135` | `pub async fn find_thread_path_by_name_str(` |
| `pub_enum` | `codex-rs/core/src/safety.rs:16` | `pub enum SafetyCheck {` |
| `pub_fn` | `codex-rs/core/src/safety.rs:27` | `pub fn assess_patch_safety(` |
| `pub_fn` | `codex-rs/core/src/safety.rs:88` | `pub fn get_platform_sandbox(windows_sandbox_enabled: bool) -> Option<SandboxType> {` |
| `pub_struct` | `codex-rs/core/src/sandboxing/mod.rs:31` | `pub struct CommandSpec {` |
| `pub_struct` | `codex-rs/core/src/sandboxing/mod.rs:42` | `pub struct ExecEnv {` |
| `pub_enum` | `codex-rs/core/src/sandboxing/mod.rs:54` | `pub enum SandboxPreference {` |
| `pub_struct` | `codex-rs/core/src/sandboxing/mod.rs:70` | `pub struct SandboxManager;` |
| `pub_fn` | `codex-rs/core/src/sandboxing/mod.rs:73` | `pub fn new() -> Self {` |
| `pub_fn` | `codex-rs/core/src/sandboxing/mod.rs:180` | `pub fn denied(&self, sandbox: SandboxType, out: &ExecToolCallOutput) -> bool {` |
| `pub_fn` | `codex-rs/core/src/sandboxing/mod.rs:185` | `pub async fn execute_env(` |
| `pub_fn` | `codex-rs/core/src/seatbelt.rs:23` | `pub async fn spawn_command_under_seatbelt(` |
| `pub_enum` | `codex-rs/core/src/shell.rs:9` | `pub enum ShellType {` |
| `pub_struct` | `codex-rs/core/src/shell.rs:18` | `pub struct Shell {` |
| `pub_fn` | `codex-rs/core/src/shell.rs:30` | `pub fn name(&self) -> &'static str {` |
| `pub_fn` | `codex-rs/core/src/shell.rs:42` | `pub fn derive_exec_args(&self, command: &str, use_login_shell: bool) -> Vec<String> {` |
| `pub_fn` | `codex-rs/core/src/shell.rs:72` | `pub fn shell_snapshot(&self) -> Option<Arc<ShellSnapshot>> {` |
| `pub_fn` | `codex-rs/core/src/shell.rs:231` | `pub fn get_shell_by_model_provided_path(shell_path: &PathBuf) -> Shell {` |
| `pub_fn` | `codex-rs/core/src/shell.rs:237` | `pub fn get_shell(shell_type: ShellType, path: Option<&PathBuf>) -> Option<Shell> {` |
| `pub_fn` | `codex-rs/core/src/shell.rs:247` | `pub fn detect_shell_type(shell_path: &PathBuf) -> Option<ShellType> {` |
| `pub_fn` | `codex-rs/core/src/shell.rs:268` | `pub fn default_user_shell() -> Shell {` |
| `pub_struct` | `codex-rs/core/src/shell_snapshot.rs:27` | `pub struct ShellSnapshot {` |
| `pub_fn` | `codex-rs/core/src/shell_snapshot.rs:37` | `pub fn start_snapshotting(` |
| `pub_fn` | `codex-rs/core/src/shell_snapshot.rs:402` | `pub async fn cleanup_stale_snapshots(codex_home: &Path, active_session_id: ThreadId) -> Result<()> {` |
| `pub_fn` | `codex-rs/core/src/skills/loader.rs:125` | `pub fn load_skills(config: &Config) -> SkillLoadOutcome {` |
| `pub_struct` | `codex-rs/core/src/skills/manager.rs:21` | `pub struct SkillsManager {` |
| `pub_fn` | `codex-rs/core/src/skills/manager.rs:27` | `pub fn new(codex_home: PathBuf) -> Self {` |
| `pub_fn` | `codex-rs/core/src/skills/manager.rs:40` | `pub fn skills_for_config(&self, config: &Config) -> SkillLoadOutcome {` |
| `pub_fn` | `codex-rs/core/src/skills/manager.rs:65` | `pub async fn skills_for_cwd(&self, cwd: &Path, force_reload: bool) -> SkillLoadOutcome {` |
| `pub_fn` | `codex-rs/core/src/skills/manager.rs:123` | `pub fn clear_cache(&self) {` |
| `pub_mod` | `codex-rs/core/src/skills/mod.rs:2` | `pub mod injection;` |
| `pub_mod` | `codex-rs/core/src/skills/mod.rs:3` | `pub mod loader;` |
| `pub_mod` | `codex-rs/core/src/skills/mod.rs:4` | `pub mod manager;` |
| `pub_mod` | `codex-rs/core/src/skills/mod.rs:5` | `pub mod model;` |
| `pub_mod` | `codex-rs/core/src/skills/mod.rs:6` | `pub mod render;` |
| `pub_mod` | `codex-rs/core/src/skills/mod.rs:7` | `pub mod system;` |
| `pub_struct` | `codex-rs/core/src/skills/model.rs:7` | `pub struct SkillMetadata {` |
| `pub_struct` | `codex-rs/core/src/skills/model.rs:18` | `pub struct SkillInterface {` |
| `pub_struct` | `codex-rs/core/src/skills/model.rs:28` | `pub struct SkillDependencies {` |
| `pub_struct` | `codex-rs/core/src/skills/model.rs:33` | `pub struct SkillToolDependency {` |
| `pub_struct` | `codex-rs/core/src/skills/model.rs:43` | `pub struct SkillError {` |
| `pub_struct` | `codex-rs/core/src/skills/model.rs:49` | `pub struct SkillLoadOutcome {` |
| `pub_fn` | `codex-rs/core/src/skills/model.rs:56` | `pub fn is_skill_enabled(&self, skill: &SkillMetadata) -> bool {` |
| `pub_fn` | `codex-rs/core/src/skills/model.rs:60` | `pub fn enabled_skills(&self) -> Vec<SkillMetadata> {` |
| `pub_fn` | `codex-rs/core/src/skills/model.rs:68` | `pub fn skills_with_enabled(&self) -> impl Iterator<Item = (&SkillMetadata, bool)> {` |
| `pub_fn` | `codex-rs/core/src/skills/render.rs:3` | `pub fn render_skills_section(skills: &[SkillMetadata]) -> Option<String> {` |
| `pub_const` | `codex-rs/core/src/spawn.rs:18` | `pub const CODEX_SANDBOX_NETWORK_DISABLED_ENV_VAR: &str = "CODEX_SANDBOX_NETWORK_DISABLED";` |
| `pub_const` | `codex-rs/core/src/spawn.rs:23` | `pub const CODEX_SANDBOX_ENV_VAR: &str = "CODEX_SANDBOX";` |
| `pub_enum` | `codex-rs/core/src/spawn.rs:26` | `pub enum StdioPolicy {` |
| `pub_type` | `codex-rs/core/src/state_db.rs:27` | `pub type StateDbHandle = Arc<codex_state::StateRuntime>;` |
| `pub_fn` | `codex-rs/core/src/state_db.rs:76` | `pub async fn get_state_db(config: &Config, otel: Option<&OtelManager>) -> Option<StateDbHandle> {` |
| `pub_fn` | `codex-rs/core/src/state_db.rs:95` | `pub async fn open_if_present(codex_home: &Path, default_provider: &str) -> Option<StateDbHandle> {` |
| `pub_fn` | `codex-rs/core/src/state_db.rs:132` | `pub async fn list_thread_ids_db(` |
| `pub_fn` | `codex-rs/core/src/state_db.rs:185` | `pub async fn find_rollout_path_by_id(` |
| `pub_fn` | `codex-rs/core/src/state_db.rs:201` | `pub async fn get_dynamic_tools(` |
| `pub_fn` | `codex-rs/core/src/state_db.rs:217` | `pub async fn persist_dynamic_tools(` |
| `pub_fn` | `codex-rs/core/src/state_db.rs:232` | `pub async fn reconcile_rollout(` |
| `pub_fn` | `codex-rs/core/src/state_db.rs:289` | `pub async fn apply_rollout_items(` |
| `pub_fn` | `codex-rs/core/src/state_db.rs:324` | `pub fn record_discrepancy(stage: &str, reason: &str) {` |
| `pub_fn` | `codex-rs/core/src/tasks/mod.rs:178` | `pub async fn abort_all_tasks(self: &Arc<Self>, reason: TurnAbortReason) {` |
| `pub_fn` | `codex-rs/core/src/tasks/mod.rs:185` | `pub async fn on_task_finished(` |
| `pub_struct` | `codex-rs/core/src/terminal.rs:10` | `pub struct TerminalInfo {` |
| `pub_enum` | `codex-rs/core/src/terminal.rs:25` | `pub enum TerminalName {` |
| `pub_enum` | `codex-rs/core/src/terminal.rs:58` | `pub enum Multiplexer {` |
| `pub_fn` | `codex-rs/core/src/terminal.rs:234` | `pub fn user_agent() -> String {` |
| `pub_fn` | `codex-rs/core/src/terminal.rs:239` | `pub fn terminal_info() -> TerminalInfo {` |
| `pub_fn` | `codex-rs/core/src/text_encoding.rs:15` | `pub fn bytes_to_string_smart(bytes: &[u8]) -> String {` |
| `pub_struct` | `codex-rs/core/src/thread_manager.rs:42` | `pub struct NewThread {` |
| `pub_struct` | `codex-rs/core/src/thread_manager.rs:50` | `pub struct ThreadManager {` |
| `pub_fn` | `codex-rs/core/src/thread_manager.rs:73` | `pub fn new(` |
| `pub_fn` | `codex-rs/core/src/thread_manager.rs:101` | `pub fn with_models_provider(auth: CodexAuth, provider: ModelProviderInfo) -> Self {` |
| `pub_fn` | `codex-rs/core/src/thread_manager.rs:112` | `pub fn with_models_provider_and_home(` |
| `pub_fn` | `codex-rs/core/src/thread_manager.rs:138` | `pub fn session_source(&self) -> SessionSource {` |
| `pub_fn` | `codex-rs/core/src/thread_manager.rs:142` | `pub fn skills_manager(&self) -> Arc<SkillsManager> {` |
| `pub_fn` | `codex-rs/core/src/thread_manager.rs:146` | `pub fn get_models_manager(&self) -> Arc<ModelsManager> {` |
| `pub_fn` | `codex-rs/core/src/thread_manager.rs:150` | `pub async fn list_models(` |
| `pub_fn` | `codex-rs/core/src/thread_manager.rs:161` | `pub fn list_collaboration_modes(&self) -> Vec<CollaborationModeMask> {` |
| `pub_fn` | `codex-rs/core/src/thread_manager.rs:165` | `pub async fn list_thread_ids(&self) -> Vec<ThreadId> {` |
| `pub_fn` | `codex-rs/core/src/thread_manager.rs:169` | `pub async fn refresh_mcp_servers(&self, refresh_config: McpServerRefreshConfig) {` |
| `pub_fn` | `codex-rs/core/src/thread_manager.rs:190` | `pub fn subscribe_thread_created(&self) -> broadcast::Receiver<ThreadId> {` |
| `pub_fn` | `codex-rs/core/src/thread_manager.rs:194` | `pub async fn get_thread(&self, thread_id: ThreadId) -> CodexResult<Arc<CodexThread>> {` |
| `pub_fn` | `codex-rs/core/src/thread_manager.rs:198` | `pub async fn start_thread(&self, config: Config) -> CodexResult<NewThread> {` |
| `pub_fn` | `codex-rs/core/src/thread_manager.rs:202` | `pub async fn start_thread_with_tools(` |
| `pub_fn` | `codex-rs/core/src/thread_manager.rs:218` | `pub async fn resume_thread_from_rollout(` |
| `pub_fn` | `codex-rs/core/src/thread_manager.rs:229` | `pub async fn resume_thread_with_history(` |
| `pub_fn` | `codex-rs/core/src/thread_manager.rs:249` | `pub async fn remove_thread(&self, thread_id: &ThreadId) -> Option<Arc<CodexThread>> {` |
| `pub_fn` | `codex-rs/core/src/thread_manager.rs:254` | `pub async fn remove_and_close_all_threads(&self) -> CodexResult<()> {` |
| `pub_fn` | `codex-rs/core/src/thread_manager.rs:266` | `pub async fn fork_thread(` |
| `pub_struct` | `codex-rs/core/src/token_data.rs:7` | `pub struct TokenData {` |
| `pub_struct` | `codex-rs/core/src/token_data.rs:25` | `pub struct IdTokenInfo {` |
| `pub_fn` | `codex-rs/core/src/token_data.rs:39` | `pub fn get_chatgpt_plan_type(&self) -> Option<String> {` |
| `pub_fn` | `codex-rs/core/src/token_data.rs:46` | `pub fn is_workspace_account(&self) -> bool {` |
| `pub_enum` | `codex-rs/core/src/token_data.rs:105` | `pub enum IdTokenInfoError {` |
| `pub_fn` | `codex-rs/core/src/token_data.rs:114` | `pub fn parse_id_token(id_token: &str) -> Result<IdTokenInfo, IdTokenInfoError> {` |
| `pub_type` | `codex-rs/core/src/tools/context.rs:17` | `pub type SharedTurnDiffTracker = Arc<Mutex<TurnDiffTracker>>;` |
| `pub_struct` | `codex-rs/core/src/tools/context.rs:20` | `pub struct ToolInvocation {` |
| `pub_enum` | `codex-rs/core/src/tools/context.rs:30` | `pub enum ToolPayload {` |
| `pub_fn` | `codex-rs/core/src/tools/context.rs:48` | `pub fn log_payload(&self) -> Cow<'_, str> {` |
| `pub_enum` | `codex-rs/core/src/tools/context.rs:59` | `pub enum ToolOutput {` |
| `pub_fn` | `codex-rs/core/src/tools/context.rs:73` | `pub fn log_preview(&self) -> String {` |
| `pub_fn` | `codex-rs/core/src/tools/context.rs:80` | `pub fn success_for_logging(&self) -> bool {` |
| `pub_fn` | `codex-rs/core/src/tools/context.rs:87` | `pub fn into_response(self, call_id: &str, payload: &ToolPayload) -> ResponseInputItem {` |
| `pub_fn` | `codex-rs/core/src/tools/events.rs:35` | `pub fn new(` |
| `pub_fn` | `codex-rs/core/src/tools/events.rs:109` | `pub fn shell(` |
| `pub_fn` | `codex-rs/core/src/tools/events.rs:125` | `pub fn apply_patch(changes: HashMap<PathBuf, FileChange>, auto_approved: bool) -> Self {` |
| `pub_fn` | `codex-rs/core/src/tools/events.rs:132` | `pub fn unified_exec(` |
| `pub_fn` | `codex-rs/core/src/tools/events.rs:148` | `pub async fn emit(&self, ctx: ToolEventCtx<'_>, stage: ToolEventStage) {` |
| `pub_fn` | `codex-rs/core/src/tools/events.rs:254` | `pub async fn begin(&self, ctx: ToolEventCtx<'_>) {` |
| `pub_fn` | `codex-rs/core/src/tools/events.rs:271` | `pub async fn finish(` |
| `pub_struct` | `codex-rs/core/src/tools/handlers/apply_patch.rs:34` | `pub struct ApplyPatchHandler;` |
| `pub_struct` | `codex-rs/core/src/tools/handlers/collab.rs:29` | `pub struct CollabHandler;` |
| `pub_fn` | `codex-rs/core/src/tools/handlers/collab.rs:103` | `pub async fn handle(` |
| `pub_fn` | `codex-rs/core/src/tools/handlers/collab.rs:211` | `pub async fn handle(` |
| `pub_fn` | `codex-rs/core/src/tools/handlers/collab.rs:309` | `pub async fn handle(` |
| `pub_mod` | `codex-rs/core/src/tools/handlers/collab.rs:473` | `pub mod close_agent {` |
| `pub_fn` | `codex-rs/core/src/tools/handlers/collab.rs:482` | `pub async fn handle(` |
| `pub_struct` | `codex-rs/core/src/tools/handlers/dynamic.rs:18` | `pub struct DynamicToolHandler;` |
| `pub_struct` | `codex-rs/core/src/tools/handlers/grep_files.rs:17` | `pub struct GrepFilesHandler;` |
| `pub_struct` | `codex-rs/core/src/tools/handlers/list_dir.rs:20` | `pub struct ListDirHandler;` |
| `pub_struct` | `codex-rs/core/src/tools/handlers/mcp.rs:12` | `pub struct McpHandler;` |
| `pub_struct` | `codex-rs/core/src/tools/handlers/mcp_resource.rs:33` | `pub struct McpResourceHandler;` |
| `pub_mod` | `codex-rs/core/src/tools/handlers/mod.rs:1` | `pub mod apply_patch;` |
| `pub_struct` | `codex-rs/core/src/tools/handlers/plan.rs:19` | `pub struct PlanHandler;` |
| `pub_static` | `codex-rs/core/src/tools/handlers/plan.rs:21` | `pub static PLAN_TOOL: LazyLock<ToolSpec> = LazyLock::new(|| {` |
| `pub_struct` | `codex-rs/core/src/tools/handlers/read_file.rs:16` | `pub struct ReadFileHandler;` |
| `pub_fn` | `codex-rs/core/src/tools/handlers/read_file.rs:164` | `pub async fn read(` |
| `pub_fn` | `codex-rs/core/src/tools/handlers/read_file.rs:236` | `pub async fn read_block(` |
| `pub_fn` | `codex-rs/core/src/tools/handlers/read_file.rs:465` | `pub fn offset() -> usize {` |
| `pub_fn` | `codex-rs/core/src/tools/handlers/read_file.rs:469` | `pub fn limit() -> usize {` |
| `pub_fn` | `codex-rs/core/src/tools/handlers/read_file.rs:473` | `pub fn max_levels() -> usize {` |
| `pub_fn` | `codex-rs/core/src/tools/handlers/read_file.rs:477` | `pub fn include_siblings() -> bool {` |
| `pub_fn` | `codex-rs/core/src/tools/handlers/read_file.rs:481` | `pub fn include_header() -> bool {` |
| `pub_struct` | `codex-rs/core/src/tools/handlers/request_user_input.rs:13` | `pub struct RequestUserInputHandler;` |
| `pub_struct` | `codex-rs/core/src/tools/handlers/shell.rs:28` | `pub struct ShellHandler;` |
| `pub_struct` | `codex-rs/core/src/tools/handlers/shell.rs:30` | `pub struct ShellCommandHandler;` |
| `pub_struct` | `codex-rs/core/src/tools/handlers/test_sync.rs:20` | `pub struct TestSyncHandler;` |
| `pub_struct` | `codex-rs/core/src/tools/handlers/unified_exec.rs:25` | `pub struct UnifiedExecHandler;` |
| `pub_struct` | `codex-rs/core/src/tools/handlers/view_image.rs:18` | `pub struct ViewImageHandler;` |
| `pub_mod` | `codex-rs/core/src/tools/mod.rs:1` | `pub mod context;` |
| `pub_mod` | `codex-rs/core/src/tools/mod.rs:2` | `pub mod events;` |
| `pub_mod` | `codex-rs/core/src/tools/mod.rs:4` | `pub mod orchestrator;` |
| `pub_mod` | `codex-rs/core/src/tools/mod.rs:5` | `pub mod parallel;` |
| `pub_mod` | `codex-rs/core/src/tools/mod.rs:6` | `pub mod registry;` |
| `pub_mod` | `codex-rs/core/src/tools/mod.rs:7` | `pub mod router;` |
| `pub_mod` | `codex-rs/core/src/tools/mod.rs:8` | `pub mod runtimes;` |
| `pub_mod` | `codex-rs/core/src/tools/mod.rs:9` | `pub mod sandboxing;` |
| `pub_mod` | `codex-rs/core/src/tools/mod.rs:10` | `pub mod spec;` |
| `pub_fn` | `codex-rs/core/src/tools/mod.rs:27` | `pub fn format_exec_output_for_model_structured(` |
| `pub_fn` | `codex-rs/core/src/tools/mod.rs:66` | `pub fn format_exec_output_for_model_freeform(` |
| `pub_fn` | `codex-rs/core/src/tools/mod.rs:93` | `pub fn format_exec_output_str(` |
| `pub_fn` | `codex-rs/core/src/tools/orchestrator.rs:29` | `pub fn new() -> Self {` |
| `pub_enum` | `codex-rs/core/src/tools/registry.rs:16` | `pub enum ToolKind {` |
| `pub_trait` | `codex-rs/core/src/tools/registry.rs:22` | `pub trait ToolHandler: Send + Sync {` |
| `pub_struct` | `codex-rs/core/src/tools/registry.rs:46` | `pub struct ToolRegistry {` |
| `pub_fn` | `codex-rs/core/src/tools/registry.rs:51` | `pub fn new(handlers: HashMap<String, Arc<dyn ToolHandler>>) -> Self {` |
| `pub_fn` | `codex-rs/core/src/tools/registry.rs:55` | `pub fn handler(&self, name: &str) -> Option<Arc<dyn ToolHandler>> {` |
| `pub_fn` | `codex-rs/core/src/tools/registry.rs:67` | `pub async fn dispatch(` |
| `pub_struct` | `codex-rs/core/src/tools/registry.rs:153` | `pub struct ConfiguredToolSpec {` |
| `pub_fn` | `codex-rs/core/src/tools/registry.rs:159` | `pub fn new(spec: ToolSpec, supports_parallel_tool_calls: bool) -> Self {` |
| `pub_struct` | `codex-rs/core/src/tools/registry.rs:167` | `pub struct ToolRegistryBuilder {` |
| `pub_fn` | `codex-rs/core/src/tools/registry.rs:173` | `pub fn new() -> Self {` |
| `pub_fn` | `codex-rs/core/src/tools/registry.rs:180` | `pub fn push_spec(&mut self, spec: ToolSpec) {` |
| `pub_fn` | `codex-rs/core/src/tools/registry.rs:184` | `pub fn push_spec_with_parallel_support(` |
| `pub_fn` | `codex-rs/core/src/tools/registry.rs:193` | `pub fn register_handler(&mut self, name: impl Into<String>, handler: Arc<dyn ToolHandler>) {` |
| `pub_fn` | `codex-rs/core/src/tools/registry.rs:222` | `pub fn build(self) -> (Vec<ConfiguredToolSpec>, ToolRegistry) {` |
| `pub_struct` | `codex-rs/core/src/tools/router.rs:24` | `pub struct ToolCall {` |
| `pub_struct` | `codex-rs/core/src/tools/router.rs:30` | `pub struct ToolRouter {` |
| `pub_fn` | `codex-rs/core/src/tools/router.rs:36` | `pub fn from_config(` |
| `pub_fn` | `codex-rs/core/src/tools/router.rs:47` | `pub fn specs(&self) -> Vec<ToolSpec> {` |
| `pub_fn` | `codex-rs/core/src/tools/router.rs:54` | `pub fn tool_supports_parallel(&self, tool_name: &str) -> bool {` |
| `pub_fn` | `codex-rs/core/src/tools/router.rs:62` | `pub async fn build_tool_call(` |
| `pub_fn` | `codex-rs/core/src/tools/router.rs:134` | `pub async fn dispatch_tool_call(` |
| `pub_struct` | `codex-rs/core/src/tools/runtimes/apply_patch.rs:32` | `pub struct ApplyPatchRequest {` |
| `pub_struct` | `codex-rs/core/src/tools/runtimes/apply_patch.rs:42` | `pub struct ApplyPatchRuntime;` |
| `pub_fn` | `codex-rs/core/src/tools/runtimes/apply_patch.rs:45` | `pub fn new() -> Self {` |
| `pub_mod` | `codex-rs/core/src/tools/runtimes/mod.rs:15` | `pub mod apply_patch;` |
| `pub_mod` | `codex-rs/core/src/tools/runtimes/mod.rs:16` | `pub mod shell;` |
| `pub_mod` | `codex-rs/core/src/tools/runtimes/mod.rs:17` | `pub mod unified_exec;` |
| `pub_struct` | `codex-rs/core/src/tools/runtimes/shell.rs:31` | `pub struct ShellRequest {` |
| `pub_struct` | `codex-rs/core/src/tools/runtimes/shell.rs:42` | `pub struct ShellRuntime;` |
| `pub_fn` | `codex-rs/core/src/tools/runtimes/shell.rs:52` | `pub fn new() -> Self {` |
| `pub_struct` | `codex-rs/core/src/tools/runtimes/unified_exec.rs:36` | `pub struct UnifiedExecRequest {` |
| `pub_struct` | `codex-rs/core/src/tools/runtimes/unified_exec.rs:47` | `pub struct UnifiedExecApprovalKey {` |
| `pub_struct` | `codex-rs/core/src/tools/runtimes/unified_exec.rs:54` | `pub struct UnifiedExecRuntime<'a> {` |
| `pub_fn` | `codex-rs/core/src/tools/runtimes/unified_exec.rs:59` | `pub fn new(` |
| `pub_fn` | `codex-rs/core/src/tools/runtimes/unified_exec.rs:81` | `pub fn new(manager: &'a UnifiedExecProcessManager) -> Self {` |
| `pub_fn` | `codex-rs/core/src/tools/sandboxing.rs:138` | `pub fn proposed_execpolicy_amendment(&self) -> Option<&ExecPolicyAmendment> {` |
| `pub_fn` | `codex-rs/core/src/tools/sandboxing.rs:281` | `pub fn env_for(` |
| `pub_fn` | `codex-rs/core/src/tools/spec.rs:44` | `pub fn new(params: &ToolsConfigParams) -> Self {` |
| `pub_enum` | `codex-rs/core/src/tools/spec.rs:95` | `pub enum JsonSchema {` |
| `pub_enum` | `codex-rs/core/src/tools/spec.rs:131` | `pub enum AdditionalProperties {` |
| `pub_fn` | `codex-rs/core/src/tools/spec.rs:1039` | `pub fn create_tools_json_for_responses_api(` |
| `pub_fn` | `codex-rs/core/src/tools/spec.rs:1142` | `pub fn parse_tool_input_schema(input_schema: &JsonValue) -> Result<JsonSchema, serde_json::Error> {` |
| `pub_struct` | `codex-rs/core/src/transport_manager.rs:6` | `pub struct TransportManager {` |
| `pub_fn` | `codex-rs/core/src/transport_manager.rs:11` | `pub fn new() -> Self {` |
| `pub_fn` | `codex-rs/core/src/transport_manager.rs:15` | `pub fn disable_websockets(&self) -> bool {` |
| `pub_fn` | `codex-rs/core/src/transport_manager.rs:19` | `pub fn activate_http_fallback(&self, websocket_enabled: bool) -> bool {` |
| `pub_enum` | `codex-rs/core/src/truncate.rs:13` | `pub enum TruncationPolicy {` |
| `pub_fn` | `codex-rs/core/src/truncate.rs:42` | `pub fn token_budget(&self) -> usize {` |
| `pub_fn` | `codex-rs/core/src/truncate.rs:56` | `pub fn byte_budget(&self) -> usize {` |
| `pub_struct` | `codex-rs/core/src/turn_diff_tracker.rs:33` | `pub struct TurnDiffTracker {` |
| `pub_fn` | `codex-rs/core/src/turn_diff_tracker.rs:46` | `pub fn new() -> Self {` |
| `pub_fn` | `codex-rs/core/src/turn_diff_tracker.rs:54` | `pub fn on_patch_begin(&mut self, changes: &HashMap<PathBuf, FileChange>) {` |
| `pub_fn` | `codex-rs/core/src/turn_diff_tracker.rs:225` | `pub fn get_unified_diff(&mut self) -> Result<Option<String>> {` |
| `pub_fn` | `codex-rs/core/src/unified_exec/mod.rs:66` | `pub fn new(session: Arc<Session>, turn: Arc<TurnContext>, call_id: String) -> Self {` |
| `pub_const` | `codex-rs/core/src/user_shell_command.rs:10` | `pub const USER_SHELL_COMMAND_OPEN: &str = "<user_shell_command>";` |
| `pub_const` | `codex-rs/core/src/user_shell_command.rs:11` | `pub const USER_SHELL_COMMAND_CLOSE: &str = "</user_shell_command>";` |
| `pub_fn` | `codex-rs/core/src/user_shell_command.rs:13` | `pub fn is_user_shell_command_text(text: &str) -> bool {` |
| `pub_fn` | `codex-rs/core/src/user_shell_command.rs:45` | `pub fn format_user_shell_command_record(` |
| `pub_fn` | `codex-rs/core/src/user_shell_command.rs:54` | `pub fn user_shell_command_record_item(` |
| `pub_fn` | `codex-rs/core/src/util.rs:70` | `pub fn resolve_path(base: &Path, path: &PathBuf) -> PathBuf {` |
| `pub_fn` | `codex-rs/core/src/util.rs:79` | `pub fn normalize_thread_name(name: &str) -> Option<String> {` |
| `pub_fn` | `codex-rs/core/src/util.rs:88` | `pub fn resume_command(thread_name: Option<&str>, thread_id: Option<ThreadId>) -> Option<String> {` |
| `pub_fn` | `codex-rs/core/src/web_search.rs:18` | `pub fn web_search_action_detail(action: &WebSearchAction) -> String {` |
| `pub_fn` | `codex-rs/core/src/web_search.rs:32` | `pub fn web_search_detail(action: Option<&WebSearchAction>, query: &str) -> String {` |
| `pub_const` | `codex-rs/core/src/windows_sandbox.rs:13` | `pub const ELEVATED_SANDBOX_NUX_ENABLED: bool = true;` |
| `pub_trait` | `codex-rs/core/src/windows_sandbox.rs:15` | `pub trait WindowsSandboxLevelExt {` |
| `pub_fn` | `codex-rs/core/src/windows_sandbox.rs:37` | `pub fn windows_sandbox_level_from_config(config: &Config) -> WindowsSandboxLevel {` |
| `pub_fn` | `codex-rs/core/src/windows_sandbox.rs:41` | `pub fn windows_sandbox_level_from_features(features: &Features) -> WindowsSandboxLevel {` |
| `pub_fn` | `codex-rs/core/src/windows_sandbox.rs:46` | `pub fn sandbox_setup_is_complete(codex_home: &Path) -> bool {` |
| `pub_fn` | `codex-rs/core/src/windows_sandbox.rs:51` | `pub fn sandbox_setup_is_complete(_codex_home: &Path) -> bool {` |
| `pub_fn` | `codex-rs/core/src/windows_sandbox.rs:56` | `pub fn elevated_setup_failure_details(err: &anyhow::Error) -> Option<(String, String)> {` |
| `pub_fn` | `codex-rs/core/src/windows_sandbox.rs:64` | `pub fn elevated_setup_failure_details(_err: &anyhow::Error) -> Option<(String, String)> {` |
| `pub_fn` | `codex-rs/core/src/windows_sandbox.rs:69` | `pub fn elevated_setup_failure_metric_name(err: &anyhow::Error) -> &'static str {` |
| `pub_fn` | `codex-rs/core/src/windows_sandbox.rs:83` | `pub fn elevated_setup_failure_metric_name(_err: &anyhow::Error) -> &'static str {` |
| `pub_fn` | `codex-rs/core/src/windows_sandbox.rs:88` | `pub fn run_elevated_setup(` |
| `pub_fn` | `codex-rs/core/src/windows_sandbox.rs:107` | `pub fn run_elevated_setup(` |
| `pub_mod` | `codex-rs/core/tests/common/lib.rs:15` | `pub mod process;` |
| `pub_mod` | `codex-rs/core/tests/common/lib.rs:16` | `pub mod responses;` |
| `pub_mod` | `codex-rs/core/tests/common/lib.rs:17` | `pub mod streaming_sse;` |
| `pub_mod` | `codex-rs/core/tests/common/lib.rs:18` | `pub mod test_codex;` |
| `pub_mod` | `codex-rs/core/tests/common/lib.rs:19` | `pub mod test_codex_exec;` |
| `pub_fn` | `codex-rs/core/tests/common/lib.rs:31` | `pub fn test_path_buf_with_windows(unix_path: &str, windows_path: Option<&str>) -> PathBuf {` |
| `pub_fn` | `codex-rs/core/tests/common/lib.rs:50` | `pub fn test_path_buf(unix_path: &str) -> PathBuf {` |
| `pub_fn` | `codex-rs/core/tests/common/lib.rs:54` | `pub fn test_absolute_path_with_windows(` |
| `pub_fn` | `codex-rs/core/tests/common/lib.rs:62` | `pub fn test_absolute_path(unix_path: &str) -> AbsolutePathBuf {` |
| `pub_fn` | `codex-rs/core/tests/common/lib.rs:66` | `pub fn test_tmp_path() -> AbsolutePathBuf {` |
| `pub_fn` | `codex-rs/core/tests/common/lib.rs:70` | `pub fn test_tmp_path_buf() -> PathBuf {` |
| `pub_fn` | `codex-rs/core/tests/common/lib.rs:77` | `pub async fn load_default_config_for_test(codex_home: &TempDir) -> Config {` |
| `pub_fn` | `codex-rs/core/tests/common/lib.rs:110` | `pub fn load_sse_fixture(path: impl AsRef<std::path::Path>) -> String {` |
| `pub_fn` | `codex-rs/core/tests/common/lib.rs:130` | `pub fn load_sse_fixture_with_id_from_str(raw: &str, id: &str) -> String {` |
| `pub_fn` | `codex-rs/core/tests/common/lib.rs:154` | `pub fn load_sse_fixture_with_id(path: impl AsRef<std::path::Path>, id: &str) -> String {` |
| `pub_fn` | `codex-rs/core/tests/common/lib.rs:222` | `pub fn sandbox_env_var() -> &'static str {` |
| `pub_fn` | `codex-rs/core/tests/common/lib.rs:226` | `pub fn sandbox_network_env_var() -> &'static str {` |
| `pub_fn` | `codex-rs/core/tests/common/lib.rs:230` | `pub fn format_with_current_shell(command: &str) -> Vec<String> {` |
| `pub_fn` | `codex-rs/core/tests/common/lib.rs:234` | `pub fn format_with_current_shell_display(command: &str) -> String {` |
| `pub_fn` | `codex-rs/core/tests/common/lib.rs:239` | `pub fn format_with_current_shell_non_login(command: &str) -> Vec<String> {` |
| `pub_fn` | `codex-rs/core/tests/common/lib.rs:243` | `pub fn format_with_current_shell_display_non_login(command: &str) -> String {` |
| `pub_fn` | `codex-rs/core/tests/common/lib.rs:249` | `pub fn stdio_server_bin() -> Result<String, CargoBinError> {` |
| `pub_mod` | `codex-rs/core/tests/common/lib.rs:253` | `pub mod fs_wait {` |
| `pub_fn` | `codex-rs/core/tests/common/lib.rs:267` | `pub async fn wait_for_path_exists(` |
| `pub_fn` | `codex-rs/core/tests/common/lib.rs:275` | `pub async fn wait_for_matching_file(` |
| `pub_fn` | `codex-rs/core/tests/common/process.rs:6` | `pub async fn wait_for_pid_file(path: &Path) -> anyhow::Result<String> {` |
| `pub_fn` | `codex-rs/core/tests/common/process.rs:24` | `pub fn process_is_alive(pid: &str) -> anyhow::Result<bool> {` |
| `pub_fn` | `codex-rs/core/tests/common/process.rs:41` | `pub async fn wait_for_process_exit(pid: &str) -> anyhow::Result<()> {` |
| `pub_struct` | `codex-rs/core/tests/common/responses.rs:32` | `pub struct ResponseMock {` |
| `pub_fn` | `codex-rs/core/tests/common/responses.rs:43` | `pub fn single_request(&self) -> ResponsesRequest {` |
| `pub_fn` | `codex-rs/core/tests/common/responses.rs:51` | `pub fn requests(&self) -> Vec<ResponsesRequest> {` |
| `pub_fn` | `codex-rs/core/tests/common/responses.rs:55` | `pub fn last_request(&self) -> Option<ResponsesRequest> {` |
| `pub_fn` | `codex-rs/core/tests/common/responses.rs:61` | `pub fn saw_function_call(&self, call_id: &str) -> bool {` |
| `pub_fn` | `codex-rs/core/tests/common/responses.rs:69` | `pub fn function_call_output_text(&self, call_id: &str) -> Option<String> {` |
| `pub_struct` | `codex-rs/core/tests/common/responses.rs:77` | `pub struct ResponsesRequest(wiremock::Request);` |
| `pub_fn` | `codex-rs/core/tests/common/responses.rs:96` | `pub fn body_json(&self) -> Value {` |
| `pub_fn` | `codex-rs/core/tests/common/responses.rs:107` | `pub fn body_bytes(&self) -> Vec<u8> {` |
| `pub_fn` | `codex-rs/core/tests/common/responses.rs:111` | `pub fn instructions_text(&self) -> String {` |
| `pub_fn` | `codex-rs/core/tests/common/responses.rs:119` | `pub fn message_input_texts(&self, role: &str) -> Vec<String> {` |
| `pub_fn` | `codex-rs/core/tests/common/responses.rs:130` | `pub fn input(&self) -> Vec<Value> {` |
| `pub_fn` | `codex-rs/core/tests/common/responses.rs:137` | `pub fn inputs_of_type(&self, ty: &str) -> Vec<Value> {` |
| `pub_fn` | `codex-rs/core/tests/common/responses.rs:145` | `pub fn function_call_output(&self, call_id: &str) -> Value {` |
| `pub_fn` | `codex-rs/core/tests/common/responses.rs:149` | `pub fn custom_tool_call_output(&self, call_id: &str) -> Value {` |
| `pub_fn` | `codex-rs/core/tests/common/responses.rs:153` | `pub fn call_output(&self, call_id: &str, call_type: &str) -> Value {` |
| `pub_fn` | `codex-rs/core/tests/common/responses.rs:165` | `pub fn has_function_call(&self, call_id: &str) -> bool {` |
| `pub_fn` | `codex-rs/core/tests/common/responses.rs:174` | `pub fn function_call_output_text(&self, call_id: &str) -> Option<String> {` |
| `pub_fn` | `codex-rs/core/tests/common/responses.rs:185` | `pub fn function_call_output_content_and_success(` |
| `pub_fn` | `codex-rs/core/tests/common/responses.rs:192` | `pub fn custom_tool_call_output_content_and_success(` |
| `pub_fn` | `codex-rs/core/tests/common/responses.rs:221` | `pub fn header(&self, name: &str) -> Option<String> {` |
| `pub_fn` | `codex-rs/core/tests/common/responses.rs:229` | `pub fn path(&self) -> String {` |
| `pub_fn` | `codex-rs/core/tests/common/responses.rs:233` | `pub fn query_param(&self, name: &str) -> Option<String> {` |
| `pub_struct` | `codex-rs/core/tests/common/responses.rs:243` | `pub struct WebSocketRequest {` |
| `pub_fn` | `codex-rs/core/tests/common/responses.rs:248` | `pub fn body_json(&self) -> Value {` |
| `pub_struct` | `codex-rs/core/tests/common/responses.rs:254` | `pub struct WebSocketHandshake {` |
| `pub_fn` | `codex-rs/core/tests/common/responses.rs:259` | `pub fn header(&self, name: &str) -> Option<String> {` |
| `pub_struct` | `codex-rs/core/tests/common/responses.rs:268` | `pub struct WebSocketConnectionConfig {` |
| `pub_struct` | `codex-rs/core/tests/common/responses.rs:273` | `pub struct WebSocketTestServer {` |
| `pub_fn` | `codex-rs/core/tests/common/responses.rs:282` | `pub fn uri(&self) -> &str {` |
| `pub_fn` | `codex-rs/core/tests/common/responses.rs:286` | `pub fn connections(&self) -> Vec<Vec<WebSocketRequest>> {` |
| `pub_fn` | `codex-rs/core/tests/common/responses.rs:290` | `pub fn single_connection(&self) -> Vec<WebSocketRequest> {` |
| `pub_fn` | `codex-rs/core/tests/common/responses.rs:298` | `pub fn handshakes(&self) -> Vec<WebSocketHandshake> {` |
| `pub_fn` | `codex-rs/core/tests/common/responses.rs:302` | `pub fn single_handshake(&self) -> WebSocketHandshake {` |
| `pub_fn` | `codex-rs/core/tests/common/responses.rs:310` | `pub async fn shutdown(self) {` |
| `pub_struct` | `codex-rs/core/tests/common/responses.rs:317` | `pub struct ModelsMock {` |
| `pub_fn` | `codex-rs/core/tests/common/responses.rs:328` | `pub fn requests(&self) -> Vec<wiremock::Request> {` |
| `pub_fn` | `codex-rs/core/tests/common/responses.rs:332` | `pub fn single_request_path(&self) -> String {` |
| `pub_fn` | `codex-rs/core/tests/common/responses.rs:363` | `pub fn sse(events: Vec<Value>) -> String {` |
| `pub_fn` | `codex-rs/core/tests/common/responses.rs:379` | `pub fn ev_completed(id: &str) -> Value {` |
| `pub_fn` | `codex-rs/core/tests/common/responses.rs:389` | `pub fn ev_done() -> Value {` |
| `pub_fn` | `codex-rs/core/tests/common/responses.rs:399` | `pub fn ev_response_created(id: &str) -> Value {` |
| `pub_fn` | `codex-rs/core/tests/common/responses.rs:408` | `pub fn ev_completed_with_tokens(id: &str, total_tokens: i64) -> Value {` |
| `pub_fn` | `codex-rs/core/tests/common/responses.rs:425` | `pub fn ev_assistant_message(id: &str, text: &str) -> Value {` |
| `pub_fn` | `codex-rs/core/tests/common/responses.rs:437` | `pub fn ev_message_item_added(id: &str, text: &str) -> Value {` |
| `pub_fn` | `codex-rs/core/tests/common/responses.rs:449` | `pub fn ev_output_text_delta(delta: &str) -> Value {` |
| `pub_fn` | `codex-rs/core/tests/common/responses.rs:456` | `pub fn ev_reasoning_item(id: &str, summary: &[&str], raw_content: &[&str]) -> Value {` |
| `pub_fn` | `codex-rs/core/tests/common/responses.rs:488` | `pub fn ev_reasoning_item_added(id: &str, summary: &[&str]) -> Value {` |
| `pub_fn` | `codex-rs/core/tests/common/responses.rs:504` | `pub fn ev_reasoning_summary_text_delta(delta: &str) -> Value {` |
| `pub_fn` | `codex-rs/core/tests/common/responses.rs:512` | `pub fn ev_reasoning_text_delta(delta: &str) -> Value {` |
| `pub_fn` | `codex-rs/core/tests/common/responses.rs:520` | `pub fn ev_web_search_call_added_partial(id: &str, status: &str) -> Value {` |
| `pub_fn` | `codex-rs/core/tests/common/responses.rs:531` | `pub fn ev_web_search_call_done(id: &str, status: &str, query: &str) -> Value {` |
| `pub_fn` | `codex-rs/core/tests/common/responses.rs:543` | `pub fn ev_function_call(call_id: &str, name: &str, arguments: &str) -> Value {` |
| `pub_fn` | `codex-rs/core/tests/common/responses.rs:555` | `pub fn ev_custom_tool_call(call_id: &str, name: &str, input: &str) -> Value {` |
| `pub_fn` | `codex-rs/core/tests/common/responses.rs:567` | `pub fn ev_local_shell_call(call_id: &str, status: &str, command: Vec<&str>) -> Value {` |
| `pub_fn` | `codex-rs/core/tests/common/responses.rs:582` | `pub fn ev_apply_patch_call(` |
| `pub_fn` | `codex-rs/core/tests/common/responses.rs:603` | `pub fn ev_apply_patch_custom_tool_call(call_id: &str, patch: &str) -> Value {` |
| `pub_fn` | `codex-rs/core/tests/common/responses.rs:618` | `pub fn ev_apply_patch_function_call(call_id: &str, patch: &str) -> Value {` |
| `pub_fn` | `codex-rs/core/tests/common/responses.rs:633` | `pub fn ev_shell_command_call(call_id: &str, command: &str) -> Value {` |
| `pub_fn` | `codex-rs/core/tests/common/responses.rs:638` | `pub fn ev_shell_command_call_with_args(call_id: &str, args: &serde_json::Value) -> Value {` |
| `pub_fn` | `codex-rs/core/tests/common/responses.rs:643` | `pub fn ev_apply_patch_shell_call(call_id: &str, patch: &str) -> Value {` |
| `pub_fn` | `codex-rs/core/tests/common/responses.rs:650` | `pub fn ev_apply_patch_shell_call_via_heredoc(call_id: &str, patch: &str) -> Value {` |
| `pub_fn` | `codex-rs/core/tests/common/responses.rs:658` | `pub fn ev_apply_patch_shell_command_call_via_heredoc(call_id: &str, patch: &str) -> Value {` |
| `pub_fn` | `codex-rs/core/tests/common/responses.rs:665` | `pub fn sse_failed(id: &str, code: &str, message: &str) -> String {` |
| `pub_fn` | `codex-rs/core/tests/common/responses.rs:675` | `pub fn sse_response(body: String) -> ResponseTemplate {` |
| `pub_fn` | `codex-rs/core/tests/common/responses.rs:681` | `pub async fn mount_response_once(server: &MockServer, response: ResponseTemplate) -> ResponseMock {` |
| `pub_fn` | `codex-rs/core/tests/common/responses.rs:744` | `pub async fn mount_sse_once(server: &MockServer, body: String) -> ResponseMock {` |
| `pub_fn` | `codex-rs/core/tests/common/responses.rs:774` | `pub async fn mount_compact_json_once(server: &MockServer, body: serde_json::Value) -> ResponseMock {` |
| `pub_fn` | `codex-rs/core/tests/common/responses.rs:787` | `pub async fn mount_models_once(server: &MockServer, body: ModelsResponse) -> ModelsMock {` |
| `pub_fn` | `codex-rs/core/tests/common/responses.rs:800` | `pub async fn mount_models_once_with_delay(` |
| `pub_fn` | `codex-rs/core/tests/common/responses.rs:818` | `pub async fn mount_models_once_with_etag(` |
| `pub_fn` | `codex-rs/core/tests/common/responses.rs:837` | `pub async fn start_mock_server() -> MockServer {` |
| `pub_fn` | `codex-rs/core/tests/common/responses.rs:854` | `pub async fn start_websocket_server(connections: Vec<Vec<Vec<Value>>>) -> WebSocketTestServer {` |
| `pub_fn` | `codex-rs/core/tests/common/responses.rs:865` | `pub async fn start_websocket_server_with_headers(` |
| `pub_struct` | `codex-rs/core/tests/common/responses.rs:987` | `pub struct FunctionCallResponseMocks {` |
| `pub_fn` | `codex-rs/core/tests/common/responses.rs:992` | `pub async fn mount_function_call_agent_response(` |
| `pub_fn` | `codex-rs/core/tests/common/responses.rs:1020` | `pub async fn mount_sse_sequence(server: &MockServer, bodies: Vec<String>) -> ResponseMock {` |
| `pub_fn` | `codex-rs/core/tests/common/responses.rs:1059` | `pub async fn mount_response_sequence(` |
| `pub_struct` | `codex-rs/core/tests/common/streaming_sse.rs:14` | `pub struct StreamingSseChunk {` |
| `pub_struct` | `codex-rs/core/tests/common/streaming_sse.rs:20` | `pub struct StreamingSseServer {` |
| `pub_fn` | `codex-rs/core/tests/common/streaming_sse.rs:28` | `pub fn uri(&self) -> &str {` |
| `pub_fn` | `codex-rs/core/tests/common/streaming_sse.rs:32` | `pub async fn requests(&self) -> Vec<Vec<u8>> {` |
| `pub_fn` | `codex-rs/core/tests/common/streaming_sse.rs:36` | `pub async fn shutdown(self) {` |
| `pub_fn` | `codex-rs/core/tests/common/streaming_sse.rs:48` | `pub async fn start_streaming_sse_server(` |
| `pub_enum` | `codex-rs/core/tests/common/test_codex.rs:38` | `pub enum ApplyPatchModelOutput {` |
| `pub_enum` | `codex-rs/core/tests/common/test_codex.rs:48` | `pub enum ShellModelOutput {` |
| `pub_struct` | `codex-rs/core/tests/common/test_codex.rs:55` | `pub struct TestCodexBuilder {` |
| `pub_fn` | `codex-rs/core/tests/common/test_codex.rs:71` | `pub fn with_auth(mut self, auth: CodexAuth) -> Self {` |
| `pub_fn` | `codex-rs/core/tests/common/test_codex.rs:76` | `pub fn with_model(self, model: &str) -> Self {` |
| `pub_fn` | `codex-rs/core/tests/common/test_codex.rs:91` | `pub fn with_home(mut self, home: Arc<TempDir>) -> Self {` |
| `pub_fn` | `codex-rs/core/tests/common/test_codex.rs:96` | `pub async fn build(&mut self, server: &wiremock::MockServer) -> anyhow::Result<TestCodex> {` |
| `pub_fn` | `codex-rs/core/tests/common/test_codex.rs:104` | `pub async fn build_with_streaming_server(` |
| `pub_fn` | `codex-rs/core/tests/common/test_codex.rs:117` | `pub async fn build_with_websocket_server(` |
| `pub_fn` | `codex-rs/core/tests/common/test_codex.rs:135` | `pub async fn resume(` |
| `pub_struct` | `codex-rs/core/tests/common/test_codex.rs:236` | `pub struct TestCodex {` |
| `pub_fn` | `codex-rs/core/tests/common/test_codex.rs:246` | `pub fn cwd_path(&self) -> &Path {` |
| `pub_fn` | `codex-rs/core/tests/common/test_codex.rs:250` | `pub fn codex_home_path(&self) -> &Path {` |
| `pub_fn` | `codex-rs/core/tests/common/test_codex.rs:254` | `pub fn workspace_path(&self, rel: impl AsRef<Path>) -> PathBuf {` |
| `pub_fn` | `codex-rs/core/tests/common/test_codex.rs:258` | `pub async fn submit_turn(&self, prompt: &str) -> Result<()> {` |
| `pub_fn` | `codex-rs/core/tests/common/test_codex.rs:267` | `pub async fn submit_turn_with_policy(` |
| `pub_fn` | `codex-rs/core/tests/common/test_codex.rs:276` | `pub async fn submit_turn_with_policies(` |
| `pub_struct` | `codex-rs/core/tests/common/test_codex.rs:309` | `pub struct TestCodexHarness {` |
| `pub_fn` | `codex-rs/core/tests/common/test_codex.rs:315` | `pub async fn new() -> Result<Self> {` |
| `pub_fn` | `codex-rs/core/tests/common/test_codex.rs:319` | `pub async fn with_config(mutator: impl FnOnce(&mut Config) + Send + 'static) -> Result<Self> {` |
| `pub_fn` | `codex-rs/core/tests/common/test_codex.rs:323` | `pub async fn with_builder(mut builder: TestCodexBuilder) -> Result<Self> {` |
| `pub_fn` | `codex-rs/core/tests/common/test_codex.rs:329` | `pub fn server(&self) -> &MockServer {` |
| `pub_fn` | `codex-rs/core/tests/common/test_codex.rs:333` | `pub fn test(&self) -> &TestCodex {` |
| `pub_fn` | `codex-rs/core/tests/common/test_codex.rs:337` | `pub fn cwd(&self) -> &Path {` |
| `pub_fn` | `codex-rs/core/tests/common/test_codex.rs:341` | `pub fn path(&self, rel: impl AsRef<Path>) -> PathBuf {` |
| `pub_fn` | `codex-rs/core/tests/common/test_codex.rs:345` | `pub async fn submit(&self, prompt: &str) -> Result<()> {` |
| `pub_fn` | `codex-rs/core/tests/common/test_codex.rs:349` | `pub async fn submit_with_policy(` |
| `pub_fn` | `codex-rs/core/tests/common/test_codex.rs:359` | `pub async fn request_bodies(&self) -> Vec<Value> {` |
| `pub_fn` | `codex-rs/core/tests/common/test_codex.rs:374` | `pub async fn function_call_output_value(&self, call_id: &str) -> Value {` |
| `pub_fn` | `codex-rs/core/tests/common/test_codex.rs:379` | `pub async fn function_call_stdout(&self, call_id: &str) -> String {` |
| `pub_fn` | `codex-rs/core/tests/common/test_codex.rs:388` | `pub async fn custom_tool_call_output(&self, call_id: &str) -> String {` |
| `pub_fn` | `codex-rs/core/tests/common/test_codex.rs:397` | `pub async fn apply_patch_output(` |
| `pub_fn` | `codex-rs/core/tests/common/test_codex.rs:444` | `pub fn test_codex() -> TestCodexBuilder {` |
| `pub_struct` | `codex-rs/core/tests/common/test_codex_exec.rs:7` | `pub struct TestCodexExecBuilder {` |
| `pub_fn` | `codex-rs/core/tests/common/test_codex_exec.rs:13` | `pub fn cmd(&self) -> assert_cmd::Command {` |
| `pub_fn` | `codex-rs/core/tests/common/test_codex_exec.rs:23` | `pub fn cmd_with_server(&self, server: &MockServer) -> assert_cmd::Command {` |
| `pub_fn` | `codex-rs/core/tests/common/test_codex_exec.rs:30` | `pub fn cwd_path(&self) -> &Path {` |
| `pub_fn` | `codex-rs/core/tests/common/test_codex_exec.rs:33` | `pub fn home_path(&self) -> &Path {` |
| `pub_fn` | `codex-rs/core/tests/common/test_codex_exec.rs:38` | `pub fn test_codex_exec() -> TestCodexExecBuilder {` |
| `pub_fn` | `codex-rs/core/tests/suite/apply_patch_cli.rs:41` | `pub async fn apply_patch_harness() -> Result<TestCodexHarness> {` |
| `pub_fn` | `codex-rs/core/tests/suite/apply_patch_cli.rs:54` | `pub async fn mount_apply_patch(` |
| `pub_static` | `codex-rs/core/tests/suite/mod.rs:11` | `pub static CODEX_ALIASES_TEMP_DIR: TempDir = unsafe {` |
| `pub_struct` | `codex-rs/debug-client/src/client.rs:43` | `pub struct AppServerClient {` |
| `pub_fn` | `codex-rs/debug-client/src/client.rs:54` | `pub fn spawn(` |
| `pub_fn` | `codex-rs/debug-client/src/client.rs:93` | `pub fn initialize(&mut self) -> Result<()> {` |
| `pub_fn` | `codex-rs/debug-client/src/client.rs:118` | `pub fn start_thread(&mut self, params: ThreadStartParams) -> Result<String> {` |
| `pub_fn` | `codex-rs/debug-client/src/client.rs:133` | `pub fn resume_thread(&mut self, params: ThreadResumeParams) -> Result<String> {` |
| `pub_fn` | `codex-rs/debug-client/src/client.rs:148` | `pub fn request_thread_start(&self, params: ThreadStartParams) -> Result<RequestId> {` |
| `pub_fn` | `codex-rs/debug-client/src/client.rs:159` | `pub fn request_thread_resume(&self, params: ThreadResumeParams) -> Result<RequestId> {` |
| `pub_fn` | `codex-rs/debug-client/src/client.rs:170` | `pub fn request_thread_list(&self, cursor: Option<String>) -> Result<RequestId> {` |
| `pub_fn` | `codex-rs/debug-client/src/client.rs:188` | `pub fn send_turn(&self, thread_id: &str, text: String) -> Result<RequestId> {` |
| `pub_fn` | `codex-rs/debug-client/src/client.rs:206` | `pub fn start_reader(` |
| `pub_fn` | `codex-rs/debug-client/src/client.rs:225` | `pub fn thread_id(&self) -> Option<String> {` |
| `pub_fn` | `codex-rs/debug-client/src/client.rs:230` | `pub fn set_thread_id(&self, thread_id: String) {` |
| `pub_fn` | `codex-rs/debug-client/src/client.rs:236` | `pub fn use_thread(&self, thread_id: String) -> bool {` |
| `pub_fn` | `codex-rs/debug-client/src/client.rs:244` | `pub fn shutdown(&mut self) {` |
| `pub_fn` | `codex-rs/debug-client/src/client.rs:378` | `pub fn build_thread_start_params(` |
| `pub_fn` | `codex-rs/debug-client/src/client.rs:394` | `pub fn build_thread_resume_params(` |
| `pub_enum` | `codex-rs/debug-client/src/commands.rs:2` | `pub enum InputAction {` |
| `pub_enum` | `codex-rs/debug-client/src/commands.rs:8` | `pub enum UserCommand {` |
| `pub_enum` | `codex-rs/debug-client/src/commands.rs:18` | `pub enum ParseError {` |
| `pub_fn` | `codex-rs/debug-client/src/commands.rs:25` | `pub fn message(&self) -> String {` |
| `pub_fn` | `codex-rs/debug-client/src/commands.rs:36` | `pub fn parse_input(line: &str) -> Result<Option<InputAction>, ParseError> {` |
| `fn_main` | `codex-rs/debug-client/src/main.rs:66` | `fn main() -> Result<()> {` |
| `pub_enum` | `codex-rs/debug-client/src/output.rs:8` | `pub enum LabelColor {` |
| `pub_struct` | `codex-rs/debug-client/src/output.rs:22` | `pub struct Output {` |
| `pub_fn` | `codex-rs/debug-client/src/output.rs:29` | `pub fn new() -> Self {` |
| `pub_fn` | `codex-rs/debug-client/src/output.rs:39` | `pub fn server_line(&self, line: &str) -> io::Result<()> {` |
| `pub_fn` | `codex-rs/debug-client/src/output.rs:48` | `pub fn client_line(&self, line: &str) -> io::Result<()> {` |
| `pub_fn` | `codex-rs/debug-client/src/output.rs:56` | `pub fn prompt(&self, thread_id: &str) -> io::Result<()> {` |
| `pub_fn` | `codex-rs/debug-client/src/output.rs:62` | `pub fn set_prompt(&self, thread_id: &str) {` |
| `pub_fn` | `codex-rs/debug-client/src/output.rs:67` | `pub fn format_label(&self, label: &str, color: LabelColor) -> String {` |
| `pub_fn` | `codex-rs/debug-client/src/reader.rs:34` | `pub fn start_reader(` |
| `pub_struct` | `codex-rs/debug-client/src/state.rs:6` | `pub struct State {` |
| `pub_enum` | `codex-rs/debug-client/src/state.rs:13` | `pub enum PendingRequest {` |
| `pub_enum` | `codex-rs/debug-client/src/state.rs:20` | `pub enum ReaderEvent {` |
| `fn_main` | `codex-rs/exec-server/src/bin/main_execve_wrapper.rs:2` | `fn main() {` |
| `fn_main` | `codex-rs/exec-server/src/bin/main_mcp_server.rs:2` | `fn main() {` |
| `pub_fn` | `codex-rs/exec-server/src/posix.rs:110` | `pub async fn main_mcp_server() -> anyhow::Result<()> {` |
| `pub_struct` | `codex-rs/exec-server/src/posix.rs:152` | `pub struct ExecveWrapperCli {` |
| `pub_fn` | `codex-rs/exec-server/src/posix.rs:160` | `pub async fn main_execve_wrapper() -> anyhow::Result<()> {` |
| `pub_fn` | `codex-rs/exec-server/src/posix/escalate_server.rs:49` | `pub async fn exec(` |
| `pub_struct` | `codex-rs/exec-server/src/posix/mcp.rs:48` | `pub struct ExecParams {` |
| `pub_struct` | `codex-rs/exec-server/src/posix/mcp.rs:60` | `pub struct ExecResult {` |
| `pub_struct` | `codex-rs/exec-server/src/posix/mcp.rs:79` | `pub struct ExecTool {` |
| `pub_fn` | `codex-rs/exec-server/src/posix/mcp.rs:90` | `pub fn new(` |
| `pub_struct` | `codex-rs/exec-server/src/posix/mcp.rs:152` | `pub struct CodexSandboxStateUpdateMethod;` |
| `pub_fn` | `codex-rs/exec-server/src/posix/socket.rs:259` | `pub fn from_fd(fd: OwnedFd) -> std::io::Result<AsyncSocket> {` |
| `pub_fn` | `codex-rs/exec-server/src/posix/socket.rs:263` | `pub fn pair() -> std::io::Result<(AsyncSocket, AsyncSocket)> {` |
| `pub_fn` | `codex-rs/exec-server/src/posix/socket.rs:303` | `pub fn into_inner(self) -> Socket {` |
| `pub_fn` | `codex-rs/exec-server/src/posix/socket.rs:372` | `pub fn pair() -> std::io::Result<(Self, Self)> {` |
| `pub_fn` | `codex-rs/exec-server/src/posix/socket.rs:377` | `pub async fn send_with_fds(&self, data: &[u8], fds: &[OwnedFd]) -> std::io::Result<()> {` |
| `pub_fn` | `codex-rs/exec-server/src/posix/socket.rs:385` | `pub async fn receive_with_fds(&self) -> std::io::Result<(Vec<u8>, Vec<OwnedFd>)> {` |
| `pub_fn` | `codex-rs/exec-server/src/posix/socket.rs:391` | `pub fn into_inner(self) -> Socket {` |
| `pub_struct` | `codex-rs/exec-server/tests/common/lib.rs:141` | `pub struct InteractiveClient {` |
| `pub_struct` | `codex-rs/exec/src/cli.rs:10` | `pub struct Cli {` |
| `pub_enum` | `codex-rs/exec/src/cli.rs:105` | `pub enum Command {` |
| `pub_struct` | `codex-rs/exec/src/cli.rs:146` | `pub struct ResumeArgs {` |
| `pub_struct` | `codex-rs/exec/src/cli.rs:205` | `pub struct ReviewArgs {` |
| `pub_enum` | `codex-rs/exec/src/cli.rs:241` | `pub enum Color {` |
| `pub_struct` | `codex-rs/exec/src/event_processor_with_jsonl_output.rs:59` | `pub struct EventProcessorWithJsonOutput {` |
| `pub_fn` | `codex-rs/exec/src/event_processor_with_jsonl_output.rs:103` | `pub fn new(last_message_path: Option<PathBuf>) -> Self {` |
| `pub_fn` | `codex-rs/exec/src/event_processor_with_jsonl_output.rs:119` | `pub fn collect_thread_events(&mut self, event: &protocol::Event) -> Vec<ThreadEvent> {` |
| `pub_enum` | `codex-rs/exec/src/exec_events.rs:11` | `pub enum ThreadEvent {` |
| `pub_struct` | `codex-rs/exec/src/exec_events.rs:40` | `pub struct ThreadStartedEvent {` |
| `pub_struct` | `codex-rs/exec/src/exec_events.rs:47` | `pub struct TurnStartedEvent {}` |
| `pub_struct` | `codex-rs/exec/src/exec_events.rs:50` | `pub struct TurnCompletedEvent {` |
| `pub_struct` | `codex-rs/exec/src/exec_events.rs:55` | `pub struct TurnFailedEvent {` |
| `pub_struct` | `codex-rs/exec/src/exec_events.rs:61` | `pub struct Usage {` |
| `pub_struct` | `codex-rs/exec/src/exec_events.rs:71` | `pub struct ItemStartedEvent {` |
| `pub_struct` | `codex-rs/exec/src/exec_events.rs:76` | `pub struct ItemCompletedEvent {` |
| `pub_struct` | `codex-rs/exec/src/exec_events.rs:81` | `pub struct ItemUpdatedEvent {` |
| `pub_struct` | `codex-rs/exec/src/exec_events.rs:87` | `pub struct ThreadErrorEvent {` |
| `pub_struct` | `codex-rs/exec/src/exec_events.rs:93` | `pub struct ThreadItem {` |
| `pub_enum` | `codex-rs/exec/src/exec_events.rs:102` | `pub enum ThreadItemDetails {` |
| `pub_struct` | `codex-rs/exec/src/exec_events.rs:133` | `pub struct AgentMessageItem {` |
| `pub_struct` | `codex-rs/exec/src/exec_events.rs:139` | `pub struct ReasoningItem {` |
| `pub_enum` | `codex-rs/exec/src/exec_events.rs:146` | `pub enum CommandExecutionStatus {` |
| `pub_struct` | `codex-rs/exec/src/exec_events.rs:156` | `pub struct CommandExecutionItem {` |
| `pub_struct` | `codex-rs/exec/src/exec_events.rs:165` | `pub struct FileUpdateChange {` |
| `pub_enum` | `codex-rs/exec/src/exec_events.rs:173` | `pub enum PatchApplyStatus {` |
| `pub_struct` | `codex-rs/exec/src/exec_events.rs:181` | `pub struct FileChangeItem {` |
| `pub_enum` | `codex-rs/exec/src/exec_events.rs:189` | `pub enum PatchChangeKind {` |
| `pub_enum` | `codex-rs/exec/src/exec_events.rs:198` | `pub enum McpToolCallStatus {` |
| `pub_enum` | `codex-rs/exec/src/exec_events.rs:208` | `pub enum CollabToolCallStatus {` |
| `pub_enum` | `codex-rs/exec/src/exec_events.rs:218` | `pub enum CollabTool {` |
| `pub_enum` | `codex-rs/exec/src/exec_events.rs:228` | `pub enum CollabAgentStatus {` |
| `pub_struct` | `codex-rs/exec/src/exec_events.rs:239` | `pub struct CollabAgentState {` |
| `pub_struct` | `codex-rs/exec/src/exec_events.rs:246` | `pub struct CollabToolCallItem {` |
| `pub_struct` | `codex-rs/exec/src/exec_events.rs:257` | `pub struct McpToolCallItemResult {` |
| `pub_struct` | `codex-rs/exec/src/exec_events.rs:271` | `pub struct McpToolCallItemError {` |
| `pub_struct` | `codex-rs/exec/src/exec_events.rs:277` | `pub struct McpToolCallItem {` |
| `pub_struct` | `codex-rs/exec/src/exec_events.rs:289` | `pub struct WebSearchItem {` |
| `pub_struct` | `codex-rs/exec/src/exec_events.rs:297` | `pub struct ErrorItem {` |
| `pub_struct` | `codex-rs/exec/src/exec_events.rs:303` | `pub struct TodoItem {` |
| `pub_struct` | `codex-rs/exec/src/exec_events.rs:309` | `pub struct TodoListItem {` |
| `pub_mod` | `codex-rs/exec/src/lib.rs:10` | `pub mod event_processor_with_jsonl_output;` |
| `pub_mod` | `codex-rs/exec/src/lib.rs:11` | `pub mod exec_events;` |
| `pub_fn` | `codex-rs/exec/src/lib.rs:91` | `pub async fn run_main(cli: Cli, codex_linux_sandbox_exe: Option<PathBuf>) -> anyhow::Result<()> {` |
| `fn_main` | `codex-rs/exec/src/main.rs:27` | `fn main() -> anyhow::Result<()> {` |
| `fn_main` | `codex-rs/execpolicy-legacy/build.rs:1` | `fn main() {` |
| `pub_enum` | `codex-rs/execpolicy-legacy/src/arg_matcher.rs:20` | `pub enum ArgMatcher {` |
| `pub_fn` | `codex-rs/execpolicy-legacy/src/arg_matcher.rs:51` | `pub fn cardinality(&self) -> ArgMatcherCardinality {` |
| `pub_fn` | `codex-rs/execpolicy-legacy/src/arg_matcher.rs:66` | `pub fn arg_type(&self) -> ArgType {` |
| `pub_enum` | `codex-rs/execpolicy-legacy/src/arg_matcher.rs:81` | `pub enum ArgMatcherCardinality {` |
| `pub_fn` | `codex-rs/execpolicy-legacy/src/arg_matcher.rs:88` | `pub fn is_exact(&self) -> Option<usize> {` |
| `pub_struct` | `codex-rs/execpolicy-legacy/src/arg_resolver.rs:10` | `pub struct PositionalArg {` |
| `pub_fn` | `codex-rs/execpolicy-legacy/src/arg_resolver.rs:15` | `pub fn resolve_observed_args_with_patterns(` |
| `pub_enum` | `codex-rs/execpolicy-legacy/src/arg_type.rs:15` | `pub enum ArgType {` |
| `pub_fn` | `codex-rs/execpolicy-legacy/src/arg_type.rs:32` | `pub fn validate(&self, value: &str) -> Result<()> {` |
| `pub_fn` | `codex-rs/execpolicy-legacy/src/arg_type.rs:72` | `pub fn might_write_file(&self) -> bool {` |
| `pub_type` | `codex-rs/execpolicy-legacy/src/error.rs:10` | `pub type Result<T> = std::result::Result<T, Error>;` |
| `pub_enum` | `codex-rs/execpolicy-legacy/src/error.rs:15` | `pub enum Error {` |
| `pub_struct` | `codex-rs/execpolicy-legacy/src/exec_call.rs:6` | `pub struct ExecCall {` |
| `pub_fn` | `codex-rs/execpolicy-legacy/src/exec_call.rs:12` | `pub fn new(program: &str, args: &[&str]) -> Self {` |
| `pub_struct` | `codex-rs/execpolicy-legacy/src/execv_checker.rs:29` | `pub struct ExecvChecker {` |
| `pub_fn` | `codex-rs/execpolicy-legacy/src/execv_checker.rs:34` | `pub fn new(execv_policy: Policy) -> Self {` |
| `pub_fn` | `codex-rs/execpolicy-legacy/src/execv_checker.rs:44` | `pub fn check(` |
| `pub_fn` | `codex-rs/execpolicy-legacy/src/lib.rs:42` | `pub fn get_default_policy() -> starlark::Result<Policy> {` |
| `pub_struct` | `codex-rs/execpolicy-legacy/src/main.rs:23` | `pub struct Args {` |
| `pub_enum` | `codex-rs/execpolicy-legacy/src/main.rs:38` | `pub enum Command {` |
| `pub_struct` | `codex-rs/execpolicy-legacy/src/main.rs:55` | `pub struct ExecArg {` |
| `fn_main` | `codex-rs/execpolicy-legacy/src/main.rs:62` | `fn main() -> Result<()> {` |
| `pub_enum` | `codex-rs/execpolicy-legacy/src/main.rs:129` | `pub enum Output {` |
| `pub_struct` | `codex-rs/execpolicy-legacy/src/opt.rs:19` | `pub struct Opt {` |
| `pub_enum` | `codex-rs/execpolicy-legacy/src/opt.rs:31` | `pub enum OptMeta {` |
| `pub_fn` | `codex-rs/execpolicy-legacy/src/opt.rs:40` | `pub fn new(opt: String, meta: OptMeta, required: bool) -> Self {` |
| `pub_fn` | `codex-rs/execpolicy-legacy/src/opt.rs:48` | `pub fn name(&self) -> &str {` |
| `pub_struct` | `codex-rs/execpolicy-legacy/src/policy.rs:15` | `pub struct Policy {` |
| `pub_fn` | `codex-rs/execpolicy-legacy/src/policy.rs:22` | `pub fn new(` |
| `pub_fn` | `codex-rs/execpolicy-legacy/src/policy.rs:44` | `pub fn check(&self, exec_call: &ExecCall) -> Result<MatchedExec> {` |
| `pub_fn` | `codex-rs/execpolicy-legacy/src/policy.rs:88` | `pub fn check_each_good_list_individually(&self) -> Vec<PositiveExampleFailedCheck> {` |
| `pub_fn` | `codex-rs/execpolicy-legacy/src/policy.rs:96` | `pub fn check_each_bad_list_individually(&self) -> Vec<NegativeExamplePassedCheck> {` |
| `pub_struct` | `codex-rs/execpolicy-legacy/src/policy_parser.rs:24` | `pub struct PolicyParser {` |
| `pub_fn` | `codex-rs/execpolicy-legacy/src/policy_parser.rs:30` | `pub fn new(policy_source: &str, unparsed_policy: &str) -> Self {` |
| `pub_fn` | `codex-rs/execpolicy-legacy/src/policy_parser.rs:37` | `pub fn parse(&self) -> starlark::Result<Policy> {` |
| `pub_struct` | `codex-rs/execpolicy-legacy/src/policy_parser.rs:75` | `pub struct ForbiddenProgramRegex {` |
| `pub_struct` | `codex-rs/execpolicy-legacy/src/program.rs:19` | `pub struct ProgramSpec {` |
| `pub_fn` | `codex-rs/execpolicy-legacy/src/program.rs:33` | `pub fn new(` |
| `pub_enum` | `codex-rs/execpolicy-legacy/src/program.rs:70` | `pub enum MatchedExec {` |
| `pub_enum` | `codex-rs/execpolicy-legacy/src/program.rs:76` | `pub enum Forbidden {` |
| `pub_fn` | `codex-rs/execpolicy-legacy/src/program.rs:94` | `pub fn check(&self, exec_call: &ExecCall) -> Result<MatchedExec> {` |
| `pub_fn` | `codex-rs/execpolicy-legacy/src/program.rs:197` | `pub fn verify_should_match_list(&self) -> Vec<PositiveExampleFailedCheck> {` |
| `pub_fn` | `codex-rs/execpolicy-legacy/src/program.rs:218` | `pub fn verify_should_not_match_list(&self) -> Vec<NegativeExamplePassedCheck> {` |
| `pub_struct` | `codex-rs/execpolicy-legacy/src/program.rs:237` | `pub struct PositiveExampleFailedCheck {` |
| `pub_struct` | `codex-rs/execpolicy-legacy/src/program.rs:244` | `pub struct NegativeExamplePassedCheck {` |
| `pub_fn` | `codex-rs/execpolicy-legacy/src/sed_command.rs:4` | `pub fn parse_sed_command(sed_command: &str) -> Result<()> {` |
| `pub_struct` | `codex-rs/execpolicy-legacy/src/valid_exec.rs:7` | `pub struct ValidExec {` |
| `pub_fn` | `codex-rs/execpolicy-legacy/src/valid_exec.rs:21` | `pub fn new(program: &str, args: Vec<MatchedArg>, system_path: &[&str]) -> Self {` |
| `pub_fn` | `codex-rs/execpolicy-legacy/src/valid_exec.rs:33` | `pub fn might_write_files(&self) -> bool {` |
| `pub_struct` | `codex-rs/execpolicy-legacy/src/valid_exec.rs:40` | `pub struct MatchedArg {` |
| `pub_fn` | `codex-rs/execpolicy-legacy/src/valid_exec.rs:47` | `pub fn new(index: usize, r#type: ArgType, value: &str) -> Result<Self> {` |
| `pub_struct` | `codex-rs/execpolicy-legacy/src/valid_exec.rs:59` | `pub struct MatchedOpt {` |
| `pub_fn` | `codex-rs/execpolicy-legacy/src/valid_exec.rs:69` | `pub fn new(name: &str, value: &str, r#type: ArgType) -> Result<Self> {` |
| `pub_fn` | `codex-rs/execpolicy-legacy/src/valid_exec.rs:78` | `pub fn name(&self) -> &str {` |
| `pub_struct` | `codex-rs/execpolicy-legacy/src/valid_exec.rs:84` | `pub struct MatchedFlag {` |
| `pub_fn` | `codex-rs/execpolicy-legacy/src/valid_exec.rs:90` | `pub fn new(name: &str) -> Self {` |
| `pub_enum` | `codex-rs/execpolicy/src/amend.rs:13` | `pub enum AmendError {` |
| `pub_fn` | `codex-rs/execpolicy/src/amend.rs:59` | `pub fn blocking_append_allow_prefix_rule(` |
| `pub_enum` | `codex-rs/execpolicy/src/decision.rs:9` | `pub enum Decision {` |
| `pub_fn` | `codex-rs/execpolicy/src/decision.rs:19` | `pub fn parse(raw: &str) -> Result<Self> {` |
| `pub_type` | `codex-rs/execpolicy/src/error.rs:4` | `pub type Result<T> = std::result::Result<T, Error>;` |
| `pub_struct` | `codex-rs/execpolicy/src/error.rs:7` | `pub struct TextPosition {` |
| `pub_struct` | `codex-rs/execpolicy/src/error.rs:13` | `pub struct TextRange {` |
| `pub_struct` | `codex-rs/execpolicy/src/error.rs:19` | `pub struct ErrorLocation {` |
| `pub_enum` | `codex-rs/execpolicy/src/error.rs:25` | `pub enum Error {` |
| `pub_fn` | `codex-rs/execpolicy/src/error.rs:49` | `pub fn location(&self) -> Option<ErrorLocation> {` |
| `pub_struct` | `codex-rs/execpolicy/src/execpolicycheck.rs:16` | `pub struct ExecPolicyCheckCommand {` |
| `pub_fn` | `codex-rs/execpolicy/src/execpolicycheck.rs:37` | `pub fn run(&self) -> Result<()> {` |
| `pub_fn` | `codex-rs/execpolicy/src/execpolicycheck.rs:48` | `pub fn format_matches_json(matched_rules: &[RuleMatch], pretty: bool) -> Result<String> {` |
| `pub_fn` | `codex-rs/execpolicy/src/execpolicycheck.rs:61` | `pub fn load_policies(policy_paths: &[PathBuf]) -> Result<Policy> {` |
| `pub_mod` | `codex-rs/execpolicy/src/lib.rs:1` | `pub mod amend;` |
| `pub_mod` | `codex-rs/execpolicy/src/lib.rs:2` | `pub mod decision;` |
| `pub_mod` | `codex-rs/execpolicy/src/lib.rs:3` | `pub mod error;` |
| `pub_mod` | `codex-rs/execpolicy/src/lib.rs:4` | `pub mod execpolicycheck;` |
| `pub_mod` | `codex-rs/execpolicy/src/lib.rs:5` | `pub mod parser;` |
| `pub_mod` | `codex-rs/execpolicy/src/lib.rs:6` | `pub mod policy;` |
| `pub_mod` | `codex-rs/execpolicy/src/lib.rs:7` | `pub mod rule;` |
| `fn_main` | `codex-rs/execpolicy/src/main.rs:13` | `fn main() -> Result<()> {` |
| `pub_struct` | `codex-rs/execpolicy/src/parser.rs:28` | `pub struct PolicyParser {` |
| `pub_fn` | `codex-rs/execpolicy/src/parser.rs:39` | `pub fn new() -> Self {` |
| `pub_fn` | `codex-rs/execpolicy/src/parser.rs:47` | `pub fn parse(&mut self, policy_identifier: &str, policy_file_contents: &str) -> Result<()> {` |
| `pub_fn` | `codex-rs/execpolicy/src/parser.rs:66` | `pub fn build(self) -> crate::policy::Policy {` |
| `pub_struct` | `codex-rs/execpolicy/src/policy.rs:17` | `pub struct Policy {` |
| `pub_fn` | `codex-rs/execpolicy/src/policy.rs:22` | `pub fn new(rules_by_program: MultiMap<String, RuleRef>) -> Self {` |
| `pub_fn` | `codex-rs/execpolicy/src/policy.rs:26` | `pub fn empty() -> Self {` |
| `pub_fn` | `codex-rs/execpolicy/src/policy.rs:30` | `pub fn rules(&self) -> &MultiMap<String, RuleRef> {` |
| `pub_fn` | `codex-rs/execpolicy/src/policy.rs:34` | `pub fn get_allowed_prefixes(&self) -> Vec<Vec<String>> {` |
| `pub_fn` | `codex-rs/execpolicy/src/policy.rs:58` | `pub fn add_prefix_rule(&mut self, prefix: &[String], decision: Decision) -> Result<()> {` |
| `pub_fn` | `codex-rs/execpolicy/src/policy.rs:116` | `pub fn matches_for_command(` |
| `pub_struct` | `codex-rs/execpolicy/src/policy.rs:152` | `pub struct Evaluation {` |
| `pub_fn` | `codex-rs/execpolicy/src/policy.rs:159` | `pub fn is_match(&self) -> bool {` |
| `pub_enum` | `codex-rs/execpolicy/src/rule.rs:13` | `pub enum PatternToken {` |
| `pub_fn` | `codex-rs/execpolicy/src/rule.rs:26` | `pub fn alternatives(&self) -> &[String] {` |
| `pub_struct` | `codex-rs/execpolicy/src/rule.rs:37` | `pub struct PrefixPattern {` |
| `pub_fn` | `codex-rs/execpolicy/src/rule.rs:43` | `pub fn matches_prefix(&self, cmd: &[String]) -> Option<Vec<String>> {` |
| `pub_enum` | `codex-rs/execpolicy/src/rule.rs:61` | `pub enum RuleMatch {` |
| `pub_fn` | `codex-rs/execpolicy/src/rule.rs:80` | `pub fn decision(&self) -> Decision {` |
| `pub_struct` | `codex-rs/execpolicy/src/rule.rs:89` | `pub struct PrefixRule {` |
| `pub_trait` | `codex-rs/execpolicy/src/rule.rs:95` | `pub trait Rule: Any + Debug + Send + Sync {` |
| `pub_type` | `codex-rs/execpolicy/src/rule.rs:103` | `pub type RuleRef = Arc<dyn Rule>;` |
| `pub_struct` | `codex-rs/feedback/src/lib.rs:32` | `pub struct CodexFeedback {` |
| `pub_fn` | `codex-rs/feedback/src/lib.rs:43` | `pub fn new() -> Self {` |
| `pub_fn` | `codex-rs/feedback/src/lib.rs:53` | `pub fn make_writer(&self) -> FeedbackMakeWriter {` |
| `pub_fn` | `codex-rs/feedback/src/lib.rs:91` | `pub fn snapshot(&self, session_id: Option<ThreadId>) -> CodexLogSnapshot {` |
| `pub_struct` | `codex-rs/feedback/src/lib.rs:125` | `pub struct FeedbackMakeWriter {` |
| `pub_struct` | `codex-rs/feedback/src/lib.rs:139` | `pub struct FeedbackWriter {` |
| `pub_struct` | `codex-rs/feedback/src/lib.rs:202` | `pub struct CodexLogSnapshot {` |
| `pub_fn` | `codex-rs/feedback/src/lib.rs:213` | `pub fn save_to_temp_file(&self) -> io::Result<PathBuf> {` |
| `pub_fn` | `codex-rs/feedback/src/lib.rs:222` | `pub fn upload_feedback(` |
| `pub_struct` | `codex-rs/file-search/src/cli.rs:10` | `pub struct Cli {` |
| `pub_struct` | `codex-rs/file-search/src/lib.rs:52` | `pub struct FileMatch {` |
| `pub_fn` | `codex-rs/file-search/src/lib.rs:61` | `pub fn full_path(&self) -> PathBuf {` |
| `pub_fn` | `codex-rs/file-search/src/lib.rs:67` | `pub fn file_name_from_path(path: &str) -> String {` |
| `pub_struct` | `codex-rs/file-search/src/lib.rs:75` | `pub struct FileSearchResults {` |
| `pub_struct` | `codex-rs/file-search/src/lib.rs:81` | `pub struct FileSearchSnapshot {` |
| `pub_struct` | `codex-rs/file-search/src/lib.rs:90` | `pub struct FileSearchOptions {` |
| `pub_trait` | `codex-rs/file-search/src/lib.rs:112` | `pub trait SessionReporter: Send + Sync + 'static {` |
| `pub_struct` | `codex-rs/file-search/src/lib.rs:120` | `pub struct FileSearchSession {` |
| `pub_fn` | `codex-rs/file-search/src/lib.rs:126` | `pub fn update_query(&self, pattern_text: &str) {` |
| `pub_fn` | `codex-rs/file-search/src/lib.rs:141` | `pub fn create_session(` |
| `pub_trait` | `codex-rs/file-search/src/lib.rs:209` | `pub trait Reporter {` |
| `pub_fn` | `codex-rs/file-search/src/lib.rs:287` | `pub fn run(` |
| `pub_enum` | `codex-rs/keyring-store/src/lib.rs:9` | `pub enum CredentialStoreError {` |
| `pub_fn` | `codex-rs/keyring-store/src/lib.rs:14` | `pub fn new(error: KeyringError) -> Self {` |
| `pub_fn` | `codex-rs/keyring-store/src/lib.rs:18` | `pub fn message(&self) -> String {` |
| `pub_fn` | `codex-rs/keyring-store/src/lib.rs:24` | `pub fn into_error(self) -> KeyringError {` |
| `pub_trait` | `codex-rs/keyring-store/src/lib.rs:42` | `pub trait KeyringStore: Debug + Send + Sync {` |
| `pub_struct` | `codex-rs/keyring-store/src/lib.rs:49` | `pub struct DefaultKeyringStore;` |
| `pub_mod` | `codex-rs/keyring-store/src/lib.rs:109` | `pub mod tests {` |
| `pub_struct` | `codex-rs/keyring-store/src/lib.rs:121` | `pub struct MockKeyringStore {` |
| `pub_fn` | `codex-rs/keyring-store/src/lib.rs:126` | `pub fn credential(&self, account: &str) -> Arc<MockCredential> {` |
| `pub_fn` | `codex-rs/keyring-store/src/lib.rs:137` | `pub fn saved_value(&self, account: &str) -> Option<String> {` |
| `pub_fn` | `codex-rs/keyring-store/src/lib.rs:148` | `pub fn set_error(&self, account: &str, error: KeyringError) {` |
| `pub_fn` | `codex-rs/keyring-store/src/lib.rs:153` | `pub fn contains(&self, account: &str) -> bool {` |
| `pub_fn` | `codex-rs/linux-sandbox/src/lib.rs:9` | `pub fn run_main() -> ! {` |
| `pub_fn` | `codex-rs/linux-sandbox/src/lib.rs:14` | `pub fn run_main() -> ! {` |
| `pub_struct` | `codex-rs/linux-sandbox/src/linux_run_main.rs:8` | `pub struct LandlockCommand {` |
| `pub_fn` | `codex-rs/linux-sandbox/src/linux_run_main.rs:22` | `pub fn run_main() -> ! {` |
| `fn_main` | `codex-rs/linux-sandbox/src/main.rs:4` | `fn main() -> ! {` |
| `pub_struct` | `codex-rs/lmstudio/src/client.rs:7` | `pub struct LMStudioClient {` |
| `pub_fn` | `codex-rs/lmstudio/src/client.rs:15` | `pub async fn try_from_provider(config: &Config) -> std::io::Result<Self> {` |
| `pub_fn` | `codex-rs/lmstudio/src/client.rs:65` | `pub async fn load_model(&self, model: &str) -> io::Result<()> {` |
| `pub_fn` | `codex-rs/lmstudio/src/client.rs:95` | `pub async fn fetch_models(&self) -> io::Result<Vec<String>> {` |
| `pub_fn` | `codex-rs/lmstudio/src/client.rs:168` | `pub async fn download_model(&self, model: &str) -> std::io::Result<()> {` |
| `pub_const` | `codex-rs/lmstudio/src/lib.rs:7` | `pub const DEFAULT_OSS_MODEL: &str = "openai/gpt-oss-20b";` |
| `pub_fn` | `codex-rs/lmstudio/src/lib.rs:13` | `pub async fn ensure_oss_ready(config: &Config) -> std::io::Result<()> {` |
| `pub_struct` | `codex-rs/login/src/device_code_auth.rs:18` | `pub struct DeviceCode {` |
| `pub_fn` | `codex-rs/login/src/device_code_auth.rs:160` | `pub async fn request_device_code(opts: &ServerOptions) -> std::io::Result<DeviceCode> {` |
| `pub_fn` | `codex-rs/login/src/device_code_auth.rs:174` | `pub async fn complete_device_code_login(` |
| `pub_fn` | `codex-rs/login/src/device_code_auth.rs:226` | `pub async fn run_device_code_login(opts: ServerOptions) -> std::io::Result<()> {` |
| `pub_struct` | `codex-rs/login/src/pkce.rs:7` | `pub struct PkceCodes {` |
| `pub_fn` | `codex-rs/login/src/pkce.rs:12` | `pub fn generate_pkce() -> PkceCodes {` |
| `pub_struct` | `codex-rs/login/src/server.rs:36` | `pub struct ServerOptions {` |
| `pub_fn` | `codex-rs/login/src/server.rs:48` | `pub fn new(` |
| `pub_struct` | `codex-rs/login/src/server.rs:67` | `pub struct LoginServer {` |
| `pub_fn` | `codex-rs/login/src/server.rs:75` | `pub async fn block_until_done(self) -> io::Result<()> {` |
| `pub_fn` | `codex-rs/login/src/server.rs:81` | `pub fn cancel(&self) {` |
| `pub_fn` | `codex-rs/login/src/server.rs:85` | `pub fn cancel_handle(&self) -> ShutdownHandle {` |
| `pub_struct` | `codex-rs/login/src/server.rs:91` | `pub struct ShutdownHandle {` |
| `pub_fn` | `codex-rs/login/src/server.rs:96` | `pub fn shutdown(&self) {` |
| `pub_fn` | `codex-rs/login/src/server.rs:101` | `pub fn run_login_server(opts: ServerOptions) -> io::Result<LoginServer> {` |
| `pub_struct` | `codex-rs/mcp-server/src/codex_tool_config.rs:22` | `pub struct CodexToolCallParam {` |
| `pub_enum` | `codex-rs/mcp-server/src/codex_tool_config.rs:70` | `pub enum CodexToolCallApprovalPolicy {` |
| `pub_enum` | `codex-rs/mcp-server/src/codex_tool_config.rs:92` | `pub enum CodexToolCallSandboxMode {` |
| `pub_fn` | `codex-rs/mcp-server/src/codex_tool_config.rs:153` | `pub async fn into_config(` |
| `pub_struct` | `codex-rs/mcp-server/src/codex_tool_config.rs:199` | `pub struct CodexToolCallReplyParam {` |
| `pub_fn` | `codex-rs/mcp-server/src/codex_tool_runner.rs:59` | `pub async fn run_codex_tool_session(` |
| `pub_fn` | `codex-rs/mcp-server/src/codex_tool_runner.rs:143` | `pub async fn run_codex_tool_session_reply(` |
| `pub_struct` | `codex-rs/mcp-server/src/exec_approval.rs:20` | `pub struct ExecApprovalElicitRequestParams {` |
| `pub_struct` | `codex-rs/mcp-server/src/exec_approval.rs:46` | `pub struct ExecApprovalResponse {` |
| `pub_fn` | `codex-rs/mcp-server/src/lib.rs:51` | `pub async fn run_main(` |
| `fn_main` | `codex-rs/mcp-server/src/main.rs:5` | `fn main() -> anyhow::Result<()> {` |
| `pub_struct` | `codex-rs/mcp-server/src/patch_approval.rs:21` | `pub struct PatchApprovalElicitRequestParams {` |
| `pub_struct` | `codex-rs/mcp-server/src/patch_approval.rs:39` | `pub struct PatchApprovalResponse {` |
| `pub_struct` | `codex-rs/mcp-server/tests/common/mcp_process.rs:33` | `pub struct McpProcess {` |
| `pub_fn` | `codex-rs/mcp-server/tests/common/mcp_process.rs:45` | `pub async fn new(codex_home: &Path) -> anyhow::Result<Self> {` |
| `pub_fn` | `codex-rs/mcp-server/tests/common/mcp_process.rs:54` | `pub async fn new_with_env(` |
| `pub_fn` | `codex-rs/mcp-server/tests/common/mcp_process.rs:112` | `pub async fn initialize(&mut self) -> anyhow::Result<()> {` |
| `pub_fn` | `codex-rs/mcp-server/tests/common/mcp_process.rs:193` | `pub async fn send_codex_tool_call(` |
| `pub_fn` | `codex-rs/mcp-server/tests/common/mcp_process.rs:227` | `pub async fn send_response(` |
| `pub_fn` | `codex-rs/mcp-server/tests/common/mcp_process.rs:264` | `pub async fn read_stream_until_request_message(` |
| `pub_fn` | `codex-rs/mcp-server/tests/common/mcp_process.rs:289` | `pub async fn read_stream_until_response_message(` |
| `pub_fn` | `codex-rs/mcp-server/tests/common/mcp_process.rs:318` | `pub async fn read_stream_until_legacy_task_complete_notification(` |
| `pub_fn` | `codex-rs/mcp-server/tests/common/mock_model_server.rs:13` | `pub async fn create_mock_chat_completions_server(responses: Vec<String>) -> MockServer {` |
| `pub_fn` | `codex-rs/mcp-server/tests/common/responses.rs:4` | `pub fn create_shell_command_sse_response(` |
| `pub_fn` | `codex-rs/mcp-server/tests/common/responses.rs:43` | `pub fn create_final_assistant_message_sse_response(message: &str) -> anyhow::Result<String> {` |
| `pub_fn` | `codex-rs/mcp-server/tests/common/responses.rs:62` | `pub fn create_apply_patch_sse_response(` |
| `pub_struct` | `codex-rs/mcp-server/tests/suite/codex_tool.rs:461` | `pub struct McpHandle {` |
| `pub_fn` | `codex-rs/network-proxy/src/admin.rs:23` | `pub async fn run_admin_api(state: Arc<NetworkProxyState>, addr: SocketAddr) -> Result<()> {` |
| `pub_struct` | `codex-rs/network-proxy/src/config.rs:12` | `pub struct NetworkProxyConfig {` |
| `pub_struct` | `codex-rs/network-proxy/src/config.rs:18` | `pub struct NetworkProxySettings {` |
| `pub_struct` | `codex-rs/network-proxy/src/config.rs:62` | `pub struct NetworkPolicy {` |
| `pub_enum` | `codex-rs/network-proxy/src/config.rs:75` | `pub enum NetworkMode {` |
| `pub_fn` | `codex-rs/network-proxy/src/config.rs:86` | `pub fn allows_method(self, method: &str) -> bool {` |
| `pub_struct` | `codex-rs/network-proxy/src/config.rs:175` | `pub struct RuntimeConfig {` |
| `pub_fn` | `codex-rs/network-proxy/src/config.rs:181` | `pub fn resolve_runtime(cfg: &NetworkProxyConfig) -> Result<RuntimeConfig> {` |
| `pub_fn` | `codex-rs/network-proxy/src/http_proxy.rs:66` | `pub async fn run_http_proxy(` |
| `pub_fn` | `codex-rs/network-proxy/src/lib.rs:27` | `pub async fn run_main(args: Args) -> Result<()> {` |
| `pub_enum` | `codex-rs/network-proxy/src/network_policy.rs:11` | `pub enum NetworkProtocol {` |
| `pub_struct` | `codex-rs/network-proxy/src/network_policy.rs:19` | `pub struct NetworkPolicyRequest {` |
| `pub_struct` | `codex-rs/network-proxy/src/network_policy.rs:29` | `pub struct NetworkPolicyRequestArgs {` |
| `pub_fn` | `codex-rs/network-proxy/src/network_policy.rs:40` | `pub fn new(args: NetworkPolicyRequestArgs) -> Self {` |
| `pub_enum` | `codex-rs/network-proxy/src/network_policy.rs:63` | `pub enum NetworkDecision {` |
| `pub_fn` | `codex-rs/network-proxy/src/network_policy.rs:69` | `pub fn deny(reason: impl Into<String>) -> Self {` |
| `pub_trait` | `codex-rs/network-proxy/src/network_policy.rs:86` | `pub trait NetworkPolicyDecider: Send + Sync + 'static {` |
| `pub_struct` | `codex-rs/network-proxy/src/policy.rs:17` | `pub struct Host(String);` |
| `pub_fn` | `codex-rs/network-proxy/src/policy.rs:20` | `pub fn parse(input: &str) -> Result<Self> {` |
| `pub_fn` | `codex-rs/network-proxy/src/policy.rs:26` | `pub fn as_str(&self) -> &str {` |
| `pub_fn` | `codex-rs/network-proxy/src/policy.rs:32` | `pub fn is_loopback_host(host: &Host) -> bool {` |
| `pub_fn` | `codex-rs/network-proxy/src/policy.rs:44` | `pub fn is_non_public_ip(ip: IpAddr) -> bool {` |
| `pub_fn` | `codex-rs/network-proxy/src/policy.rs:100` | `pub fn normalize_host(host: &str) -> String {` |
| `pub_struct` | `codex-rs/network-proxy/src/proxy.rs:18` | `pub struct Args {}` |
| `pub_struct` | `codex-rs/network-proxy/src/proxy.rs:21` | `pub struct NetworkProxyBuilder {` |
| `pub_fn` | `codex-rs/network-proxy/src/proxy.rs:29` | `pub fn state(mut self, state: Arc<NetworkProxyState>) -> Self {` |
| `pub_fn` | `codex-rs/network-proxy/src/proxy.rs:34` | `pub fn http_addr(mut self, addr: SocketAddr) -> Self {` |
| `pub_fn` | `codex-rs/network-proxy/src/proxy.rs:39` | `pub fn admin_addr(mut self, addr: SocketAddr) -> Self {` |
| `pub_fn` | `codex-rs/network-proxy/src/proxy.rs:52` | `pub fn policy_decider_arc(mut self, decider: Arc<dyn NetworkPolicyDecider>) -> Self {` |
| `pub_fn` | `codex-rs/network-proxy/src/proxy.rs:57` | `pub async fn build(self) -> Result<NetworkProxy> {` |
| `pub_struct` | `codex-rs/network-proxy/src/proxy.rs:83` | `pub struct NetworkProxy {` |
| `pub_fn` | `codex-rs/network-proxy/src/proxy.rs:92` | `pub fn builder() -> NetworkProxyBuilder {` |
| `pub_fn` | `codex-rs/network-proxy/src/proxy.rs:96` | `pub async fn run(&self) -> Result<NetworkProxyHandle> {` |
| `pub_struct` | `codex-rs/network-proxy/src/proxy.rs:133` | `pub struct NetworkProxyHandle {` |
| `pub_fn` | `codex-rs/network-proxy/src/proxy.rs:150` | `pub async fn wait(mut self) -> Result<()> {` |
| `pub_fn` | `codex-rs/network-proxy/src/proxy.rs:169` | `pub async fn shutdown(mut self) -> Result<()> {` |
| `pub_fn` | `codex-rs/network-proxy/src/responses.rs:11` | `pub fn text_response(status: StatusCode, body: &str) -> Response {` |
| `pub_fn` | `codex-rs/network-proxy/src/responses.rs:37` | `pub fn blocked_header_value(reason: &str) -> &'static str {` |
| `pub_fn` | `codex-rs/network-proxy/src/responses.rs:46` | `pub fn blocked_message(reason: &str) -> &'static str {` |
| `pub_fn` | `codex-rs/network-proxy/src/responses.rs:60` | `pub fn blocked_text_response(reason: &str) -> Response {` |
| `pub_enum` | `codex-rs/network-proxy/src/runtime.rs:37` | `pub enum HostBlockReason {` |
| `pub_const` | `codex-rs/network-proxy/src/runtime.rs:44` | `pub const fn as_str(self) -> &'static str {` |
| `pub_enum` | `codex-rs/network-proxy/src/runtime.rs:60` | `pub enum HostBlockDecision {` |
| `pub_struct` | `codex-rs/network-proxy/src/runtime.rs:66` | `pub struct BlockedRequest {` |
| `pub_struct` | `codex-rs/network-proxy/src/runtime.rs:76` | `pub struct BlockedRequestArgs {` |
| `pub_fn` | `codex-rs/network-proxy/src/runtime.rs:86` | `pub fn new(args: BlockedRequestArgs) -> Self {` |
| `pub_struct` | `codex-rs/network-proxy/src/runtime.rs:132` | `pub struct NetworkProxyState {` |
| `pub_fn` | `codex-rs/network-proxy/src/runtime.rs:145` | `pub async fn new() -> Result<Self> {` |
| `pub_fn` | `codex-rs/network-proxy/src/runtime.rs:152` | `pub async fn current_cfg(&self) -> Result<NetworkProxyConfig> {` |
| `pub_fn` | `codex-rs/network-proxy/src/runtime.rs:160` | `pub async fn current_patterns(&self) -> Result<(Vec<String>, Vec<String>)> {` |
| `pub_fn` | `codex-rs/network-proxy/src/runtime.rs:169` | `pub async fn enabled(&self) -> Result<bool> {` |
| `pub_fn` | `codex-rs/network-proxy/src/runtime.rs:175` | `pub async fn force_reload(&self) -> Result<()> {` |
| `pub_fn` | `codex-rs/network-proxy/src/runtime.rs:201` | `pub async fn host_blocked(&self, host: &str, port: u16) -> Result<HostBlockDecision> {` |
| `pub_fn` | `codex-rs/network-proxy/src/runtime.rs:268` | `pub async fn record_blocked(&self, entry: BlockedRequest) -> Result<()> {` |
| `pub_fn` | `codex-rs/network-proxy/src/runtime.rs:279` | `pub async fn drain_blocked(&self) -> Result<Vec<BlockedRequest>> {` |
| `pub_fn` | `codex-rs/network-proxy/src/runtime.rs:288` | `pub async fn is_unix_socket_allowed(&self, path: &str) -> Result<bool> {` |
| `pub_fn` | `codex-rs/network-proxy/src/runtime.rs:327` | `pub async fn method_allowed(&self, method: &str) -> Result<bool> {` |
| `pub_fn` | `codex-rs/network-proxy/src/runtime.rs:333` | `pub async fn allow_upstream_proxy(&self) -> Result<bool> {` |
| `pub_fn` | `codex-rs/network-proxy/src/runtime.rs:339` | `pub async fn network_mode(&self) -> Result<NetworkMode> {` |
| `pub_fn` | `codex-rs/network-proxy/src/runtime.rs:345` | `pub async fn set_network_mode(&self, mode: NetworkMode) -> Result<()> {` |
| `pub_fn` | `codex-rs/network-proxy/src/socks5.rs:40` | `pub async fn run_socks5(` |
| `pub_struct` | `codex-rs/ollama/src/client.rs:22` | `pub struct OllamaClient {` |
| `pub_fn` | `codex-rs/ollama/src/client.rs:32` | `pub async fn try_from_oss_provider(config: &Config) -> io::Result<Self> {` |
| `pub_fn` | `codex-rs/ollama/src/client.rs:104` | `pub async fn fetch_models(&self) -> io::Result<Vec<String>> {` |
| `pub_fn` | `codex-rs/ollama/src/client.rs:130` | `pub async fn fetch_version(&self) -> io::Result<Option<Version>> {` |
| `pub_fn` | `codex-rs/ollama/src/client.rs:157` | `pub async fn pull_model_stream(` |
| `pub_fn` | `codex-rs/ollama/src/client.rs:215` | `pub async fn pull_with_reporter(` |
| `pub_const` | `codex-rs/ollama/src/lib.rs:17` | `pub const DEFAULT_OSS_MODEL: &str = "gpt-oss:20b";` |
| `pub_struct` | `codex-rs/ollama/src/lib.rs:19` | `pub struct WireApiDetection {` |
| `pub_fn` | `codex-rs/ollama/src/lib.rs:28` | `pub async fn ensure_oss_ready(config: &Config) -> std::io::Result<()> {` |
| `pub_fn` | `codex-rs/ollama/src/lib.rs:72` | `pub async fn detect_wire_api(` |
| `pub_enum` | `codex-rs/ollama/src/pull.rs:7` | `pub enum PullEvent {` |
| `pub_trait` | `codex-rs/ollama/src/pull.rs:25` | `pub trait PullProgressReporter {` |
| `pub_struct` | `codex-rs/ollama/src/pull.rs:30` | `pub struct CliProgressReporter {` |
| `pub_fn` | `codex-rs/ollama/src/pull.rs:45` | `pub fn new() -> Self {` |
| `pub_struct` | `codex-rs/ollama/src/pull.rs:141` | `pub struct TuiProgressReporter(CliProgressReporter);` |
| `pub_fn` | `codex-rs/ollama/src/url.rs:8` | `pub fn base_url_to_host_root(base_url: &str) -> String {` |
| `pub_struct` | `codex-rs/otel/src/config.rs:32` | `pub struct OtelSettings {` |
| `pub_enum` | `codex-rs/otel/src/config.rs:44` | `pub enum OtelHttpProtocol {` |
| `pub_struct` | `codex-rs/otel/src/config.rs:52` | `pub struct OtelTlsConfig {` |
| `pub_enum` | `codex-rs/otel/src/config.rs:59` | `pub enum OtelExporter {` |
| `pub_mod` | `codex-rs/otel/src/lib.rs:1` | `pub mod config;` |
| `pub_mod` | `codex-rs/otel/src/lib.rs:2` | `pub mod metrics;` |
| `pub_mod` | `codex-rs/otel/src/lib.rs:3` | `pub mod otel_provider;` |
| `pub_mod` | `codex-rs/otel/src/lib.rs:4` | `pub mod traces;` |
| `pub_enum` | `codex-rs/otel/src/lib.rs:28` | `pub enum ToolDecisionSource {` |
| `pub_struct` | `codex-rs/otel/src/lib.rs:34` | `pub struct OtelEventMetadata {` |
| `pub_struct` | `codex-rs/otel/src/lib.rs:48` | `pub struct OtelManager {` |
| `pub_fn` | `codex-rs/otel/src/lib.rs:55` | `pub fn with_model(mut self, model: &str, slug: &str) -> Self {` |
| `pub_fn` | `codex-rs/otel/src/lib.rs:61` | `pub fn with_metrics(mut self, metrics: MetricsClient) -> Self {` |
| `pub_fn` | `codex-rs/otel/src/lib.rs:67` | `pub fn with_metrics_without_metadata_tags(mut self, metrics: MetricsClient) -> Self {` |
| `pub_fn` | `codex-rs/otel/src/lib.rs:73` | `pub fn with_metrics_config(self, config: MetricsConfig) -> MetricsResult<Self> {` |
| `pub_fn` | `codex-rs/otel/src/lib.rs:78` | `pub fn with_provider_metrics(self, provider: &OtelProvider) -> Self {` |
| `pub_fn` | `codex-rs/otel/src/lib.rs:85` | `pub fn counter(&self, name: &str, inc: i64, tags: &[(&str, &str)]) {` |
| `pub_fn` | `codex-rs/otel/src/lib.rs:100` | `pub fn histogram(&self, name: &str, value: i64, tags: &[(&str, &str)]) {` |
| `pub_fn` | `codex-rs/otel/src/lib.rs:115` | `pub fn record_duration(&self, name: &str, duration: Duration, tags: &[(&str, &str)]) {` |
| `pub_fn` | `codex-rs/otel/src/lib.rs:130` | `pub fn start_timer(&self, name: &str, tags: &[(&str, &str)]) -> Result<Timer, MetricsError> {` |
| `pub_fn` | `codex-rs/otel/src/lib.rs:138` | `pub fn shutdown_metrics(&self) -> MetricsResult<()> {` |
| `pub_fn` | `codex-rs/otel/src/lib.rs:145` | `pub fn snapshot_metrics(&self) -> MetricsResult<ResourceMetrics> {` |
| `pub_fn` | `codex-rs/otel/src/lib.rs:153` | `pub fn reset_runtime_metrics(&self) {` |
| `pub_fn` | `codex-rs/otel/src/lib.rs:163` | `pub fn runtime_metrics_summary(&self) -> Option<RuntimeMetricsSummary> {` |
| `pub_fn` | `codex-rs/otel/src/lib.rs:219` | `pub fn start_global_timer(name: &str, tags: &[(&str, &str)]) -> MetricsResult<Timer> {` |
| `pub_struct` | `codex-rs/otel/src/metrics/client.rs:183` | `pub struct MetricsClient(std::sync::Arc<MetricsClientInner>);` |
| `pub_fn` | `codex-rs/otel/src/metrics/client.rs:187` | `pub fn new(config: MetricsConfig) -> Result<Self> {` |
| `pub_fn` | `codex-rs/otel/src/metrics/client.rs:238` | `pub fn counter(&self, name: &str, inc: i64, tags: &[(&str, &str)]) -> Result<()> {` |
| `pub_fn` | `codex-rs/otel/src/metrics/client.rs:243` | `pub fn histogram(&self, name: &str, value: i64, tags: &[(&str, &str)]) -> Result<()> {` |
| `pub_fn` | `codex-rs/otel/src/metrics/client.rs:248` | `pub fn record_duration(` |
| `pub_fn` | `codex-rs/otel/src/metrics/client.rs:261` | `pub fn start_timer(` |
| `pub_fn` | `codex-rs/otel/src/metrics/client.rs:270` | `pub fn snapshot(&self) -> Result<ResourceMetrics> {` |
| `pub_fn` | `codex-rs/otel/src/metrics/client.rs:282` | `pub fn shutdown(&self) -> Result<()> {` |
| `pub_enum` | `codex-rs/otel/src/metrics/config.rs:10` | `pub enum MetricsExporter {` |
| `pub_struct` | `codex-rs/otel/src/metrics/config.rs:16` | `pub struct MetricsConfig {` |
| `pub_fn` | `codex-rs/otel/src/metrics/config.rs:27` | `pub fn otlp(` |
| `pub_fn` | `codex-rs/otel/src/metrics/config.rs:45` | `pub fn in_memory(` |
| `pub_fn` | `codex-rs/otel/src/metrics/config.rs:63` | `pub fn with_export_interval(mut self, interval: Duration) -> Self {` |
| `pub_fn` | `codex-rs/otel/src/metrics/config.rs:69` | `pub fn with_runtime_reader(mut self) -> Self {` |
| `pub_fn` | `codex-rs/otel/src/metrics/config.rs:75` | `pub fn with_tag(mut self, key: impl Into<String>, value: impl Into<String>) -> Result<Self> {` |
| `pub_type` | `codex-rs/otel/src/metrics/error.rs:3` | `pub type Result<T> = std::result::Result<T, MetricsError>;` |
| `pub_enum` | `codex-rs/otel/src/metrics/error.rs:6` | `pub enum MetricsError {` |
| `pub_fn` | `codex-rs/otel/src/metrics/mod.rs:22` | `pub fn global() -> Option<MetricsClient> {` |
| `pub_struct` | `codex-rs/otel/src/metrics/runtime_metrics.rs:17` | `pub struct RuntimeMetricTotals {` |
| `pub_fn` | `codex-rs/otel/src/metrics/runtime_metrics.rs:23` | `pub fn is_empty(self) -> bool {` |
| `pub_struct` | `codex-rs/otel/src/metrics/runtime_metrics.rs:29` | `pub struct RuntimeMetricsSummary {` |
| `pub_fn` | `codex-rs/otel/src/metrics/runtime_metrics.rs:38` | `pub fn is_empty(self) -> bool {` |
| `pub_struct` | `codex-rs/otel/src/metrics/timer.rs:6` | `pub struct Timer {` |
| `pub_fn` | `codex-rs/otel/src/metrics/timer.rs:34` | `pub fn record(&self, additional_tags: &[(&str, &str)]) -> Result<()> {` |
| `pub_struct` | `codex-rs/otel/src/otel_provider.rs:50` | `pub struct OtelProvider {` |
| `pub_fn` | `codex-rs/otel/src/otel_provider.rs:58` | `pub fn shutdown(&self) {` |
| `pub_fn` | `codex-rs/otel/src/otel_provider.rs:70` | `pub fn from(settings: &OtelSettings) -> Result<Option<Self>, Box<dyn Error>> {` |
| `pub_fn` | `codex-rs/otel/src/otel_provider.rs:150` | `pub fn codex_export_filter(meta: &tracing::Metadata<'_>) -> bool {` |
| `pub_fn` | `codex-rs/otel/src/otel_provider.rs:154` | `pub fn metrics(&self) -> Option<&MetricsClient> {` |
| `pub_mod` | `codex-rs/otel/src/traces/mod.rs:1` | `pub mod otel_manager;` |
| `pub_fn` | `codex-rs/otel/src/traces/otel_manager.rs:48` | `pub fn new(` |
| `pub_fn` | `codex-rs/otel/src/traces/otel_manager.rs:77` | `pub fn apply_traceparent_parent(&self, span: &Span) {` |
| `pub_fn` | `codex-rs/otel/src/traces/otel_manager.rs:83` | `pub fn record_responses(&self, handle_responses_span: &Span, event: &ResponseEvent) {` |
| `pub_fn` | `codex-rs/otel/src/traces/otel_manager.rs:104` | `pub fn conversation_starts(` |
| `pub_fn` | `codex-rs/otel/src/traces/otel_manager.rs:158` | `pub fn record_api_request(` |
| `pub_fn` | `codex-rs/otel/src/traces/otel_manager.rs:199` | `pub fn record_websocket_request(&self, duration: Duration, error: Option<&str>) {` |
| `pub_fn` | `codex-rs/otel/src/traces/otel_manager.rs:229` | `pub fn record_websocket_event(` |
| `pub_fn` | `codex-rs/otel/src/traces/otel_manager.rs:473` | `pub fn sse_event_completed(` |
| `pub_fn` | `codex-rs/otel/src/traces/otel_manager.rs:502` | `pub fn user_prompt(&self, items: &[UserInput]) {` |
| `pub_fn` | `codex-rs/otel/src/traces/otel_manager.rs:534` | `pub fn tool_decision(` |
| `pub_fn` | `codex-rs/otel/src/traces/otel_manager.rs:593` | `pub fn log_tool_failed(&self, tool_name: &str, error: &str) {` |
| `pub_fn` | `codex-rs/otel/src/traces/otel_manager.rs:613` | `pub fn tool_result(` |
| `pub_fn` | `codex-rs/process-hardening/src/lib.rs:12` | `pub fn pre_main_hardening() {` |
| `pub_enum` | `codex-rs/protocol/src/account.rs:9` | `pub enum PlanType {` |
| `pub_struct` | `codex-rs/protocol/src/approvals.rs:20` | `pub struct ExecPolicyAmendment {` |
| `pub_fn` | `codex-rs/protocol/src/approvals.rs:25` | `pub fn new(command: Vec<String>) -> Self {` |
| `pub_fn` | `codex-rs/protocol/src/approvals.rs:29` | `pub fn command(&self) -> &[String] {` |
| `pub_struct` | `codex-rs/protocol/src/approvals.rs:41` | `pub struct ExecApprovalRequestEvent {` |
| `pub_struct` | `codex-rs/protocol/src/approvals.rs:63` | `pub struct ElicitationRequestEvent {` |
| `pub_enum` | `codex-rs/protocol/src/approvals.rs:75` | `pub enum ElicitationAction {` |
| `pub_struct` | `codex-rs/protocol/src/approvals.rs:82` | `pub struct ApplyPatchApprovalRequestEvent {` |
| `pub_enum` | `codex-rs/protocol/src/config_types.rs:18` | `pub enum ReasoningSummary {` |
| `pub_enum` | `codex-rs/protocol/src/config_types.rs:45` | `pub enum Verbosity {` |
| `pub_enum` | `codex-rs/protocol/src/config_types.rs:57` | `pub enum SandboxMode {` |
| `pub_enum` | `codex-rs/protocol/src/config_types.rs:74` | `pub enum WindowsSandboxLevel {` |
| `pub_enum` | `codex-rs/protocol/src/config_types.rs:98` | `pub enum Personality {` |
| `pub_enum` | `codex-rs/protocol/src/config_types.rs:108` | `pub enum WebSearchMode {` |
| `pub_enum` | `codex-rs/protocol/src/config_types.rs:118` | `pub enum ForcedLoginMethod {` |
| `pub_enum` | `codex-rs/protocol/src/config_types.rs:128` | `pub enum TrustLevel {` |
| `pub_enum` | `codex-rs/protocol/src/config_types.rs:158` | `pub enum AltScreenMode {` |
| `pub_enum` | `codex-rs/protocol/src/config_types.rs:173` | `pub enum ModeKind {` |
| `pub_struct` | `codex-rs/protocol/src/config_types.rs:185` | `pub struct CollaborationMode {` |
| `pub_fn` | `codex-rs/protocol/src/config_types.rs:196` | `pub fn model(&self) -> &str {` |
| `pub_fn` | `codex-rs/protocol/src/config_types.rs:200` | `pub fn reasoning_effort(&self) -> Option<ReasoningEffort> {` |
| `pub_fn` | `codex-rs/protocol/src/config_types.rs:211` | `pub fn with_updates(` |
| `pub_fn` | `codex-rs/protocol/src/config_types.rs:236` | `pub fn apply_mask(&self, mask: &CollaborationModeMask) -> Self {` |
| `pub_struct` | `codex-rs/protocol/src/config_types.rs:254` | `pub struct Settings {` |
| `pub_struct` | `codex-rs/protocol/src/config_types.rs:263` | `pub struct CollaborationModeMask {` |
| `pub_const` | `codex-rs/protocol/src/custom_prompts.rs:11` | `pub const PROMPTS_CMD_PREFIX: &str = "prompts";` |
| `pub_struct` | `codex-rs/protocol/src/custom_prompts.rs:14` | `pub struct CustomPrompt {` |
| `pub_struct` | `codex-rs/protocol/src/dynamic_tools.rs:9` | `pub struct DynamicToolSpec {` |
| `pub_struct` | `codex-rs/protocol/src/dynamic_tools.rs:17` | `pub struct DynamicToolCallRequest {` |
| `pub_struct` | `codex-rs/protocol/src/dynamic_tools.rs:26` | `pub struct DynamicToolResponse {` |
| `pub_enum` | `codex-rs/protocol/src/items.rs:20` | `pub enum TurnItem {` |
| `pub_struct` | `codex-rs/protocol/src/items.rs:30` | `pub struct UserMessageItem {` |
| `pub_enum` | `codex-rs/protocol/src/items.rs:38` | `pub enum AgentMessageContent {` |
| `pub_struct` | `codex-rs/protocol/src/items.rs:43` | `pub struct AgentMessageItem {` |
| `pub_struct` | `codex-rs/protocol/src/items.rs:49` | `pub struct PlanItem {` |
| `pub_struct` | `codex-rs/protocol/src/items.rs:55` | `pub struct ReasoningItem {` |
| `pub_struct` | `codex-rs/protocol/src/items.rs:63` | `pub struct WebSearchItem {` |
| `pub_struct` | `codex-rs/protocol/src/items.rs:70` | `pub struct ContextCompactionItem {` |
| `pub_fn` | `codex-rs/protocol/src/items.rs:75` | `pub fn new() -> Self {` |
| `pub_fn` | `codex-rs/protocol/src/items.rs:81` | `pub fn as_legacy_event(&self) -> EventMsg {` |
| `pub_fn` | `codex-rs/protocol/src/items.rs:93` | `pub fn new(content: &[UserInput]) -> Self {` |
| `pub_fn` | `codex-rs/protocol/src/items.rs:100` | `pub fn as_legacy_event(&self) -> EventMsg {` |
| `pub_fn` | `codex-rs/protocol/src/items.rs:111` | `pub fn message(&self) -> String {` |
| `pub_fn` | `codex-rs/protocol/src/items.rs:122` | `pub fn text_elements(&self) -> Vec<TextElement> {` |
| `pub_fn` | `codex-rs/protocol/src/items.rs:149` | `pub fn image_urls(&self) -> Vec<String> {` |
| `pub_fn` | `codex-rs/protocol/src/items.rs:159` | `pub fn local_image_paths(&self) -> Vec<std::path::PathBuf> {` |
| `pub_fn` | `codex-rs/protocol/src/items.rs:171` | `pub fn new(content: &[AgentMessageContent]) -> Self {` |
| `pub_fn` | `codex-rs/protocol/src/items.rs:178` | `pub fn as_legacy_events(&self) -> Vec<EventMsg> {` |
| `pub_fn` | `codex-rs/protocol/src/items.rs:191` | `pub fn as_legacy_events(&self, show_raw_agent_reasoning: bool) -> Vec<EventMsg> {` |
| `pub_fn` | `codex-rs/protocol/src/items.rs:214` | `pub fn as_legacy_event(&self) -> EventMsg {` |
| `pub_fn` | `codex-rs/protocol/src/items.rs:224` | `pub fn id(&self) -> String {` |
| `pub_fn` | `codex-rs/protocol/src/items.rs:235` | `pub fn as_legacy_events(&self, show_raw_agent_reasoning: bool) -> Vec<EventMsg> {` |
| `pub_mod` | `codex-rs/protocol/src/lib.rs:1` | `pub mod account;` |
| `pub_mod` | `codex-rs/protocol/src/lib.rs:4` | `pub mod approvals;` |
| `pub_mod` | `codex-rs/protocol/src/lib.rs:5` | `pub mod config_types;` |
| `pub_mod` | `codex-rs/protocol/src/lib.rs:6` | `pub mod custom_prompts;` |
| `pub_mod` | `codex-rs/protocol/src/lib.rs:7` | `pub mod dynamic_tools;` |
| `pub_mod` | `codex-rs/protocol/src/lib.rs:8` | `pub mod items;` |
| `pub_mod` | `codex-rs/protocol/src/lib.rs:9` | `pub mod mcp;` |
| `pub_mod` | `codex-rs/protocol/src/lib.rs:10` | `pub mod message_history;` |
| `pub_mod` | `codex-rs/protocol/src/lib.rs:11` | `pub mod models;` |
| `pub_mod` | `codex-rs/protocol/src/lib.rs:12` | `pub mod num_format;` |
| `pub_mod` | `codex-rs/protocol/src/lib.rs:13` | `pub mod openai_models;` |
| `pub_mod` | `codex-rs/protocol/src/lib.rs:14` | `pub mod parse_command;` |
| `pub_mod` | `codex-rs/protocol/src/lib.rs:15` | `pub mod plan_tool;` |
| `pub_mod` | `codex-rs/protocol/src/lib.rs:16` | `pub mod protocol;` |
| `pub_mod` | `codex-rs/protocol/src/lib.rs:17` | `pub mod request_user_input;` |
| `pub_mod` | `codex-rs/protocol/src/lib.rs:18` | `pub mod user_input;` |
| `pub_enum` | `codex-rs/protocol/src/mcp.rs:14` | `pub enum RequestId {` |
| `pub_struct` | `codex-rs/protocol/src/mcp.rs:32` | `pub struct Tool {` |
| `pub_struct` | `codex-rs/protocol/src/mcp.rs:58` | `pub struct Resource {` |
| `pub_struct` | `codex-rs/protocol/src/mcp.rs:88` | `pub struct ResourceTemplate {` |
| `pub_struct` | `codex-rs/protocol/src/mcp.rs:108` | `pub struct CallToolResult {` |
| `pub_fn` | `codex-rs/protocol/src/mcp.rs:276` | `pub fn from_mcp_value(value: serde_json::Value) -> Result<Self, serde_json::Error> {` |
| `pub_fn` | `codex-rs/protocol/src/mcp.rs:282` | `pub fn from_mcp_value(value: serde_json::Value) -> Result<Self, serde_json::Error> {` |
| `pub_fn` | `codex-rs/protocol/src/mcp.rs:288` | `pub fn from_mcp_value(value: serde_json::Value) -> Result<Self, serde_json::Error> {` |
| `pub_struct` | `codex-rs/protocol/src/message_history.rs:7` | `pub struct HistoryEntry {` |
| `pub_enum` | `codex-rs/protocol/src/models.rs:32` | `pub enum SandboxPermissions {` |
| `pub_fn` | `codex-rs/protocol/src/models.rs:41` | `pub fn requires_escalated_permissions(self) -> bool {` |
| `pub_enum` | `codex-rs/protocol/src/models.rs:48` | `pub enum ResponseInputItem {` |
| `pub_enum` | `codex-rs/protocol/src/models.rs:69` | `pub enum ContentItem {` |
| `pub_enum` | `codex-rs/protocol/src/models.rs:77` | `pub enum MessagePhase {` |
| `pub_enum` | `codex-rs/protocol/src/models.rs:84` | `pub enum ResponseItem {` |
| `pub_const` | `codex-rs/protocol/src/models.rs:189` | `pub const BASE_INSTRUCTIONS_DEFAULT: &str = include_str!("prompts/base_instructions/default.md");` |
| `pub_struct` | `codex-rs/protocol/src/models.rs:194` | `pub struct BaseInstructions {` |
| `pub_struct` | `codex-rs/protocol/src/models.rs:210` | `pub struct DeveloperInstructions {` |
| `pub_fn` | `codex-rs/protocol/src/models.rs:235` | `pub fn from(` |
| `pub_fn` | `codex-rs/protocol/src/models.rs:265` | `pub fn into_text(self) -> String {` |
| `pub_fn` | `codex-rs/protocol/src/models.rs:269` | `pub fn concat(self, other: impl Into<DeveloperInstructions>) -> Self {` |
| `pub_fn` | `codex-rs/protocol/src/models.rs:278` | `pub fn personality_spec_message(spec: String) -> Self {` |
| `pub_fn` | `codex-rs/protocol/src/models.rs:285` | `pub fn from_policy(` |
| `pub_fn` | `codex-rs/protocol/src/models.rs:319` | `pub fn from_collaboration_mode(collaboration_mode: &CollaborationMode) -> Option<Self> {` |
| `pub_fn` | `codex-rs/protocol/src/models.rs:393` | `pub fn format_allow_prefixes(prefixes: Vec<Vec<String>>) -> Option<String> {` |
| `pub_const` | `codex-rs/protocol/src/models.rs:492` | `pub const VIEW_IMAGE_TOOL_NAME: &str = "view_image";` |
| `pub_fn` | `codex-rs/protocol/src/models.rs:500` | `pub fn image_open_tag_text() -> String {` |
| `pub_fn` | `codex-rs/protocol/src/models.rs:504` | `pub fn image_close_tag_text() -> String {` |
| `pub_fn` | `codex-rs/protocol/src/models.rs:508` | `pub fn local_image_label_text(label_number: usize) -> String {` |
| `pub_fn` | `codex-rs/protocol/src/models.rs:512` | `pub fn local_image_open_tag_text(label_number: usize) -> String {` |
| `pub_fn` | `codex-rs/protocol/src/models.rs:517` | `pub fn is_local_image_open_tag_text(text: &str) -> bool {` |
| `pub_fn` | `codex-rs/protocol/src/models.rs:522` | `pub fn is_local_image_close_tag_text(text: &str) -> bool {` |
| `pub_fn` | `codex-rs/protocol/src/models.rs:526` | `pub fn is_image_open_tag_text(text: &str) -> bool {` |
| `pub_fn` | `codex-rs/protocol/src/models.rs:530` | `pub fn is_image_close_tag_text(text: &str) -> bool {` |
| `pub_fn` | `codex-rs/protocol/src/models.rs:557` | `pub fn local_image_content_items_with_label_number(` |
| `pub_enum` | `codex-rs/protocol/src/models.rs:637` | `pub enum LocalShellStatus {` |
| `pub_enum` | `codex-rs/protocol/src/models.rs:645` | `pub enum LocalShellAction {` |
| `pub_struct` | `codex-rs/protocol/src/models.rs:650` | `pub struct LocalShellExecAction {` |
| `pub_enum` | `codex-rs/protocol/src/models.rs:660` | `pub enum WebSearchAction {` |
| `pub_enum` | `codex-rs/protocol/src/models.rs:689` | `pub enum ReasoningItemReasoningSummary {` |
| `pub_enum` | `codex-rs/protocol/src/models.rs:695` | `pub enum ReasoningItemContent {` |
| `pub_struct` | `codex-rs/protocol/src/models.rs:732` | `pub struct ShellToolCallParams {` |
| `pub_struct` | `codex-rs/protocol/src/models.rs:753` | `pub struct ShellCommandToolCallParams {` |
| `pub_enum` | `codex-rs/protocol/src/models.rs:777` | `pub enum FunctionCallOutputContentItem {` |
| `pub_struct` | `codex-rs/protocol/src/models.rs:792` | `pub struct FunctionCallOutputPayload {` |
| `pub_fn` | `codex-rs/protocol/src/num_format.rs:27` | `pub fn format_with_separators(n: i64) -> String {` |
| `pub_fn` | `codex-rs/protocol/src/num_format.rs:75` | `pub fn format_si_suffix(n: i64) -> String {` |
| `pub_enum` | `codex-rs/protocol/src/openai_models.rs:41` | `pub enum ReasoningEffort {` |
| `pub_enum` | `codex-rs/protocol/src/openai_models.rs:68` | `pub enum InputModality {` |
| `pub_fn` | `codex-rs/protocol/src/openai_models.rs:79` | `pub fn default_input_modalities() -> Vec<InputModality> {` |
| `pub_struct` | `codex-rs/protocol/src/openai_models.rs:85` | `pub struct ReasoningEffortPreset {` |
| `pub_struct` | `codex-rs/protocol/src/openai_models.rs:93` | `pub struct ModelUpgrade {` |
| `pub_struct` | `codex-rs/protocol/src/openai_models.rs:104` | `pub struct ModelPreset {` |
| `pub_enum` | `codex-rs/protocol/src/openai_models.rs:139` | `pub enum ModelVisibility {` |
| `pub_enum` | `codex-rs/protocol/src/openai_models.rs:162` | `pub enum ConfigShellToolType {` |
| `pub_enum` | `codex-rs/protocol/src/openai_models.rs:172` | `pub enum ApplyPatchToolType {` |
| `pub_enum` | `codex-rs/protocol/src/openai_models.rs:180` | `pub enum TruncationMode {` |
| `pub_struct` | `codex-rs/protocol/src/openai_models.rs:186` | `pub struct TruncationPolicyConfig {` |
| `pub_const` | `codex-rs/protocol/src/openai_models.rs:192` | `pub const fn bytes(limit: i64) -> Self {` |
| `pub_const` | `codex-rs/protocol/src/openai_models.rs:199` | `pub const fn tokens(limit: i64) -> Self {` |
| `pub_struct` | `codex-rs/protocol/src/openai_models.rs:209` | `pub struct ClientVersion(pub i32, pub i32, pub i32);` |
| `pub_struct` | `codex-rs/protocol/src/openai_models.rs:217` | `pub struct ModelInfo {` |
| `pub_fn` | `codex-rs/protocol/src/openai_models.rs:255` | `pub fn auto_compact_token_limit(&self) -> Option<i64> {` |
| `pub_fn` | `codex-rs/protocol/src/openai_models.rs:262` | `pub fn supports_personality(&self) -> bool {` |
| `pub_fn` | `codex-rs/protocol/src/openai_models.rs:268` | `pub fn get_model_instructions(&self, personality: Option<Personality>) -> String {` |
| `pub_struct` | `codex-rs/protocol/src/openai_models.rs:293` | `pub struct ModelMessages {` |
| `pub_fn` | `codex-rs/protocol/src/openai_models.rs:314` | `pub fn get_personality_message(&self, personality: Option<Personality>) -> Option<String> {` |
| `pub_struct` | `codex-rs/protocol/src/openai_models.rs:322` | `pub struct ModelInstructionsVariables {` |
| `pub_fn` | `codex-rs/protocol/src/openai_models.rs:329` | `pub fn is_complete(&self) -> bool {` |
| `pub_fn` | `codex-rs/protocol/src/openai_models.rs:335` | `pub fn get_personality_message(&self, personality: Option<Personality>) -> Option<String> {` |
| `pub_struct` | `codex-rs/protocol/src/openai_models.rs:348` | `pub struct ModelInfoUpgrade {` |
| `pub_struct` | `codex-rs/protocol/src/openai_models.rs:364` | `pub struct ModelsResponse {` |
| `pub_fn` | `codex-rs/protocol/src/openai_models.rs:405` | `pub fn filter_by_auth(models: Vec<ModelPreset>, chatgpt_mode: bool) -> Vec<ModelPreset> {` |
| `pub_fn` | `codex-rs/protocol/src/openai_models.rs:415` | `pub fn merge(` |
| `pub_enum` | `codex-rs/protocol/src/parse_command.rs:9` | `pub enum ParsedCommand {` |
| `pub_enum` | `codex-rs/protocol/src/plan_tool.rs:9` | `pub enum StepStatus {` |
| `pub_struct` | `codex-rs/protocol/src/plan_tool.rs:17` | `pub struct PlanItemArg {` |
| `pub_struct` | `codex-rs/protocol/src/plan_tool.rs:24` | `pub struct UpdatePlanArgs {` |
| `pub_const` | `codex-rs/protocol/src/protocol.rs:60` | `pub const USER_INSTRUCTIONS_OPEN_TAG: &str = "<user_instructions>";` |
| `pub_const` | `codex-rs/protocol/src/protocol.rs:61` | `pub const USER_INSTRUCTIONS_CLOSE_TAG: &str = "</user_instructions>";` |
| `pub_const` | `codex-rs/protocol/src/protocol.rs:62` | `pub const ENVIRONMENT_CONTEXT_OPEN_TAG: &str = "<environment_context>";` |
| `pub_const` | `codex-rs/protocol/src/protocol.rs:63` | `pub const ENVIRONMENT_CONTEXT_CLOSE_TAG: &str = "</environment_context>";` |
| `pub_const` | `codex-rs/protocol/src/protocol.rs:64` | `pub const COLLABORATION_MODE_OPEN_TAG: &str = "<collaboration_mode>";` |
| `pub_const` | `codex-rs/protocol/src/protocol.rs:65` | `pub const COLLABORATION_MODE_CLOSE_TAG: &str = "</collaboration_mode>";` |
| `pub_const` | `codex-rs/protocol/src/protocol.rs:66` | `pub const USER_MESSAGE_BEGIN: &str = "## My request for Codex:";` |
| `pub_struct` | `codex-rs/protocol/src/protocol.rs:70` | `pub struct Submission {` |
| `pub_struct` | `codex-rs/protocol/src/protocol.rs:79` | `pub struct McpServerRefreshConfig {` |
| `pub_enum` | `codex-rs/protocol/src/protocol.rs:89` | `pub enum Op {` |
| `pub_enum` | `codex-rs/protocol/src/protocol.rs:329` | `pub enum AskForApproval {` |
| `pub_enum` | `codex-rs/protocol/src/protocol.rs:358` | `pub enum NetworkAccess {` |
| `pub_fn` | `codex-rs/protocol/src/protocol.rs:365` | `pub fn is_enabled(self) -> bool {` |
| `pub_enum` | `codex-rs/protocol/src/protocol.rs:374` | `pub enum SandboxPolicy {` |
| `pub_struct` | `codex-rs/protocol/src/protocol.rs:425` | `pub struct WritableRoot {` |
| `pub_fn` | `codex-rs/protocol/src/protocol.rs:433` | `pub fn is_path_writable(&self, path: &Path) -> bool {` |
| `pub_fn` | `codex-rs/protocol/src/protocol.rs:460` | `pub fn new_read_only_policy() -> Self {` |
| `pub_fn` | `codex-rs/protocol/src/protocol.rs:467` | `pub fn new_workspace_write_policy() -> Self {` |
| `pub_fn` | `codex-rs/protocol/src/protocol.rs:477` | `pub fn has_full_disk_read_access(&self) -> bool {` |
| `pub_fn` | `codex-rs/protocol/src/protocol.rs:481` | `pub fn has_full_disk_write_access(&self) -> bool {` |
| `pub_fn` | `codex-rs/protocol/src/protocol.rs:490` | `pub fn has_full_network_access(&self) -> bool {` |
| `pub_fn` | `codex-rs/protocol/src/protocol.rs:502` | `pub fn get_writable_roots_with_cwd(&self, cwd: &Path) -> Vec<WritableRoot> {` |
| `pub_struct` | `codex-rs/protocol/src/protocol.rs:677` | `pub struct Event {` |
| `pub_enum` | `codex-rs/protocol/src/protocol.rs:690` | `pub enum EventMsg {` |
| `pub_enum` | `codex-rs/protocol/src/protocol.rs:916` | `pub enum AgentStatus {` |
| `pub_enum` | `codex-rs/protocol/src/protocol.rs:936` | `pub enum CodexErrorInfo {` |
| `pub_struct` | `codex-rs/protocol/src/protocol.rs:967` | `pub struct RawResponseItemEvent {` |
| `pub_struct` | `codex-rs/protocol/src/protocol.rs:972` | `pub struct ItemStartedEvent {` |
| `pub_struct` | `codex-rs/protocol/src/protocol.rs:990` | `pub struct ItemCompletedEvent {` |
| `pub_trait` | `codex-rs/protocol/src/protocol.rs:996` | `pub trait HasLegacyEvent {` |
| `pub_struct` | `codex-rs/protocol/src/protocol.rs:1007` | `pub struct AgentMessageContentDeltaEvent {` |
| `pub_struct` | `codex-rs/protocol/src/protocol.rs:1023` | `pub struct PlanDeltaEvent {` |
| `pub_struct` | `codex-rs/protocol/src/protocol.rs:1031` | `pub struct ReasoningContentDeltaEvent {` |
| `pub_struct` | `codex-rs/protocol/src/protocol.rs:1050` | `pub struct ReasoningRawContentDeltaEvent {` |
| `pub_struct` | `codex-rs/protocol/src/protocol.rs:1090` | `pub struct ExitedReviewModeEvent {` |
| `pub_struct` | `codex-rs/protocol/src/protocol.rs:1097` | `pub struct ErrorEvent {` |
| `pub_struct` | `codex-rs/protocol/src/protocol.rs:1104` | `pub struct WarningEvent {` |
| `pub_struct` | `codex-rs/protocol/src/protocol.rs:1109` | `pub struct ContextCompactedEvent;` |
| `pub_struct` | `codex-rs/protocol/src/protocol.rs:1112` | `pub struct TurnCompleteEvent {` |
| `pub_struct` | `codex-rs/protocol/src/protocol.rs:1117` | `pub struct TurnStartedEvent {` |
| `pub_struct` | `codex-rs/protocol/src/protocol.rs:1125` | `pub struct TokenUsage {` |
| `pub_struct` | `codex-rs/protocol/src/protocol.rs:1139` | `pub struct TokenUsageInfo {` |
| `pub_fn` | `codex-rs/protocol/src/protocol.rs:1148` | `pub fn new_or_append(` |
| `pub_fn` | `codex-rs/protocol/src/protocol.rs:1171` | `pub fn append_last_usage(&mut self, last: &TokenUsage) {` |
| `pub_fn` | `codex-rs/protocol/src/protocol.rs:1176` | `pub fn fill_to_context_window(&mut self, context_window: i64) {` |
| `pub_fn` | `codex-rs/protocol/src/protocol.rs:1191` | `pub fn full_context_window(context_window: i64) -> Self {` |
| `pub_struct` | `codex-rs/protocol/src/protocol.rs:1203` | `pub struct TokenCountEvent {` |
| `pub_struct` | `codex-rs/protocol/src/protocol.rs:1209` | `pub struct RateLimitSnapshot {` |
| `pub_struct` | `codex-rs/protocol/src/protocol.rs:1217` | `pub struct RateLimitWindow {` |
| `pub_struct` | `codex-rs/protocol/src/protocol.rs:1229` | `pub struct CreditsSnapshot {` |
| `pub_fn` | `codex-rs/protocol/src/protocol.rs:1239` | `pub fn is_zero(&self) -> bool {` |
| `pub_fn` | `codex-rs/protocol/src/protocol.rs:1243` | `pub fn cached_input(&self) -> i64 {` |
| `pub_fn` | `codex-rs/protocol/src/protocol.rs:1247` | `pub fn non_cached_input(&self) -> i64 {` |
| `pub_fn` | `codex-rs/protocol/src/protocol.rs:1252` | `pub fn blended_total(&self) -> i64 {` |
| `pub_fn` | `codex-rs/protocol/src/protocol.rs:1256` | `pub fn tokens_in_context_window(&self) -> i64 {` |
| `pub_fn` | `codex-rs/protocol/src/protocol.rs:1270` | `pub fn percent_of_context_window_remaining(&self, context_window: i64) -> i64 {` |
| `pub_fn` | `codex-rs/protocol/src/protocol.rs:1284` | `pub fn add_assign(&mut self, other: &TokenUsage) {` |
| `pub_struct` | `codex-rs/protocol/src/protocol.rs:1294` | `pub struct FinalOutput {` |
| `pub_struct` | `codex-rs/protocol/src/protocol.rs:1335` | `pub struct AgentMessageEvent {` |
| `pub_struct` | `codex-rs/protocol/src/protocol.rs:1340` | `pub struct UserMessageEvent {` |
| `pub_struct` | `codex-rs/protocol/src/protocol.rs:1358` | `pub struct AgentMessageDeltaEvent {` |
| `pub_struct` | `codex-rs/protocol/src/protocol.rs:1363` | `pub struct AgentReasoningEvent {` |
| `pub_struct` | `codex-rs/protocol/src/protocol.rs:1368` | `pub struct AgentReasoningRawContentEvent {` |
| `pub_struct` | `codex-rs/protocol/src/protocol.rs:1373` | `pub struct AgentReasoningRawContentDeltaEvent {` |
| `pub_struct` | `codex-rs/protocol/src/protocol.rs:1378` | `pub struct AgentReasoningSectionBreakEvent {` |
| `pub_struct` | `codex-rs/protocol/src/protocol.rs:1387` | `pub struct AgentReasoningDeltaEvent {` |
| `pub_struct` | `codex-rs/protocol/src/protocol.rs:1392` | `pub struct McpInvocation {` |
| `pub_struct` | `codex-rs/protocol/src/protocol.rs:1402` | `pub struct McpToolCallBeginEvent {` |
| `pub_struct` | `codex-rs/protocol/src/protocol.rs:1409` | `pub struct McpToolCallEndEvent {` |
| `pub_fn` | `codex-rs/protocol/src/protocol.rs:1420` | `pub fn is_success(&self) -> bool {` |
| `pub_struct` | `codex-rs/protocol/src/protocol.rs:1429` | `pub struct WebSearchBeginEvent {` |
| `pub_struct` | `codex-rs/protocol/src/protocol.rs:1434` | `pub struct WebSearchEndEvent {` |
| `pub_struct` | `codex-rs/protocol/src/protocol.rs:1444` | `pub struct ConversationPathResponseEvent {` |
| `pub_struct` | `codex-rs/protocol/src/protocol.rs:1450` | `pub struct ResumedHistory {` |
| `pub_enum` | `codex-rs/protocol/src/protocol.rs:1457` | `pub enum InitialHistory {` |
| `pub_fn` | `codex-rs/protocol/src/protocol.rs:1464` | `pub fn forked_from_id(&self) -> Option<ThreadId> {` |
| `pub_fn` | `codex-rs/protocol/src/protocol.rs:1480` | `pub fn session_cwd(&self) -> Option<PathBuf> {` |
| `pub_fn` | `codex-rs/protocol/src/protocol.rs:1488` | `pub fn get_rollout_items(&self) -> Vec<RolloutItem> {` |
| `pub_fn` | `codex-rs/protocol/src/protocol.rs:1496` | `pub fn get_event_msgs(&self) -> Option<Vec<EventMsg>> {` |
| `pub_fn` | `codex-rs/protocol/src/protocol.rs:1521` | `pub fn get_base_instructions(&self) -> Option<BaseInstructions> {` |
| `pub_fn` | `codex-rs/protocol/src/protocol.rs:1538` | `pub fn get_dynamic_tools(&self) -> Option<Vec<DynamicToolSpec>> {` |
| `pub_enum` | `codex-rs/protocol/src/protocol.rs:1565` | `pub enum SessionSource {` |
| `pub_enum` | `codex-rs/protocol/src/protocol.rs:1579` | `pub enum SubAgentSource {` |
| `pub_struct` | `codex-rs/protocol/src/protocol.rs:1624` | `pub struct SessionMeta {` |
| `pub_struct` | `codex-rs/protocol/src/protocol.rs:1661` | `pub struct SessionMetaLine {` |
| `pub_enum` | `codex-rs/protocol/src/protocol.rs:1670` | `pub enum RolloutItem {` |
| `pub_struct` | `codex-rs/protocol/src/protocol.rs:1679` | `pub struct CompactedItem {` |
| `pub_struct` | `codex-rs/protocol/src/protocol.rs:1700` | `pub struct TurnContextItem {` |
| `pub_enum` | `codex-rs/protocol/src/protocol.rs:1724` | `pub enum TruncationPolicy {` |
| `pub_struct` | `codex-rs/protocol/src/protocol.rs:1730` | `pub struct RolloutLine {` |
| `pub_struct` | `codex-rs/protocol/src/protocol.rs:1737` | `pub struct GitInfo {` |
| `pub_enum` | `codex-rs/protocol/src/protocol.rs:1751` | `pub enum ReviewDelivery {` |
| `pub_enum` | `codex-rs/protocol/src/protocol.rs:1759` | `pub enum ReviewTarget {` |
| `pub_struct` | `codex-rs/protocol/src/protocol.rs:1785` | `pub struct ReviewRequest {` |
| `pub_struct` | `codex-rs/protocol/src/protocol.rs:1794` | `pub struct ReviewOutputEvent {` |
| `pub_struct` | `codex-rs/protocol/src/protocol.rs:1814` | `pub struct ReviewFinding {` |
| `pub_struct` | `codex-rs/protocol/src/protocol.rs:1824` | `pub struct ReviewCodeLocation {` |
| `pub_struct` | `codex-rs/protocol/src/protocol.rs:1831` | `pub struct ReviewLineRange {` |
| `pub_enum` | `codex-rs/protocol/src/protocol.rs:1840` | `pub enum ExecCommandSource {` |
| `pub_struct` | `codex-rs/protocol/src/protocol.rs:1849` | `pub struct ExecCommandBeginEvent {` |
| `pub_struct` | `codex-rs/protocol/src/protocol.rs:1873` | `pub struct ExecCommandEndEvent {` |
| `pub_struct` | `codex-rs/protocol/src/protocol.rs:1912` | `pub struct ViewImageToolCallEvent {` |
| `pub_enum` | `codex-rs/protocol/src/protocol.rs:1921` | `pub enum ExecOutputStream {` |
| `pub_struct` | `codex-rs/protocol/src/protocol.rs:1928` | `pub struct ExecCommandOutputDeltaEvent {` |
| `pub_struct` | `codex-rs/protocol/src/protocol.rs:1942` | `pub struct TerminalInteractionEvent {` |
| `pub_struct` | `codex-rs/protocol/src/protocol.rs:1952` | `pub struct BackgroundEventEvent {` |
| `pub_struct` | `codex-rs/protocol/src/protocol.rs:1957` | `pub struct DeprecationNoticeEvent {` |
| `pub_struct` | `codex-rs/protocol/src/protocol.rs:1966` | `pub struct UndoStartedEvent {` |
| `pub_struct` | `codex-rs/protocol/src/protocol.rs:1972` | `pub struct UndoCompletedEvent {` |
| `pub_struct` | `codex-rs/protocol/src/protocol.rs:1979` | `pub struct ThreadRolledBackEvent {` |
| `pub_struct` | `codex-rs/protocol/src/protocol.rs:1985` | `pub struct StreamErrorEvent {` |
| `pub_struct` | `codex-rs/protocol/src/protocol.rs:1997` | `pub struct StreamInfoEvent {` |
| `pub_struct` | `codex-rs/protocol/src/protocol.rs:2002` | `pub struct PatchApplyBeginEvent {` |
| `pub_struct` | `codex-rs/protocol/src/protocol.rs:2016` | `pub struct PatchApplyEndEvent {` |
| `pub_struct` | `codex-rs/protocol/src/protocol.rs:2035` | `pub struct TurnDiffEvent {` |
| `pub_struct` | `codex-rs/protocol/src/protocol.rs:2040` | `pub struct GetHistoryEntryResponseEvent {` |
| `pub_struct` | `codex-rs/protocol/src/protocol.rs:2049` | `pub struct McpListToolsResponseEvent {` |
| `pub_struct` | `codex-rs/protocol/src/protocol.rs:2061` | `pub struct McpStartupUpdateEvent {` |
| `pub_enum` | `codex-rs/protocol/src/protocol.rs:2071` | `pub enum McpStartupStatus {` |
| `pub_struct` | `codex-rs/protocol/src/protocol.rs:2079` | `pub struct McpStartupCompleteEvent {` |
| `pub_struct` | `codex-rs/protocol/src/protocol.rs:2086` | `pub struct McpStartupFailure {` |
| `pub_enum` | `codex-rs/protocol/src/protocol.rs:2094` | `pub enum McpAuthStatus {` |
| `pub_struct` | `codex-rs/protocol/src/protocol.rs:2115` | `pub struct ListCustomPromptsResponseEvent {` |
| `pub_struct` | `codex-rs/protocol/src/protocol.rs:2121` | `pub struct ListSkillsResponseEvent {` |
| `pub_enum` | `codex-rs/protocol/src/protocol.rs:2128` | `pub enum SkillScope {` |
| `pub_struct` | `codex-rs/protocol/src/protocol.rs:2136` | `pub struct SkillMetadata {` |
| `pub_struct` | `codex-rs/protocol/src/protocol.rs:2155` | `pub struct SkillInterface {` |
| `pub_struct` | `codex-rs/protocol/src/protocol.rs:2171` | `pub struct SkillDependencies {` |
| `pub_struct` | `codex-rs/protocol/src/protocol.rs:2176` | `pub struct SkillToolDependency {` |
| `pub_struct` | `codex-rs/protocol/src/protocol.rs:2196` | `pub struct SkillErrorInfo {` |
| `pub_struct` | `codex-rs/protocol/src/protocol.rs:2202` | `pub struct SkillsListEntry {` |
| `pub_struct` | `codex-rs/protocol/src/protocol.rs:2209` | `pub struct SessionConfiguredEvent {` |
| `pub_struct` | `codex-rs/protocol/src/protocol.rs:2255` | `pub struct ThreadNameUpdatedEvent {` |
| `pub_enum` | `codex-rs/protocol/src/protocol.rs:2265` | `pub enum ReviewDecision {` |
| `pub_fn` | `codex-rs/protocol/src/protocol.rs:2293` | `pub fn to_opaque_string(&self) -> &'static str {` |
| `pub_enum` | `codex-rs/protocol/src/protocol.rs:2307` | `pub enum FileChange {` |
| `pub_struct` | `codex-rs/protocol/src/protocol.rs:2321` | `pub struct Chunk {` |
| `pub_struct` | `codex-rs/protocol/src/protocol.rs:2329` | `pub struct TurnAbortedEvent {` |
| `pub_enum` | `codex-rs/protocol/src/protocol.rs:2335` | `pub enum TurnAbortReason {` |
| `pub_struct` | `codex-rs/protocol/src/protocol.rs:2342` | `pub struct CollabAgentSpawnBeginEvent {` |
| `pub_struct` | `codex-rs/protocol/src/protocol.rs:2353` | `pub struct CollabAgentSpawnEndEvent {` |
| `pub_struct` | `codex-rs/protocol/src/protocol.rs:2368` | `pub struct CollabAgentInteractionBeginEvent {` |
| `pub_struct` | `codex-rs/protocol/src/protocol.rs:2381` | `pub struct CollabAgentInteractionEndEvent {` |
| `pub_struct` | `codex-rs/protocol/src/protocol.rs:2396` | `pub struct CollabWaitingBeginEvent {` |
| `pub_struct` | `codex-rs/protocol/src/protocol.rs:2406` | `pub struct CollabWaitingEndEvent {` |
| `pub_struct` | `codex-rs/protocol/src/protocol.rs:2416` | `pub struct CollabCloseBeginEvent {` |
| `pub_struct` | `codex-rs/protocol/src/protocol.rs:2426` | `pub struct CollabCloseEndEvent {` |
| `pub_struct` | `codex-rs/protocol/src/request_user_input.rs:9` | `pub struct RequestUserInputQuestionOption {` |
| `pub_struct` | `codex-rs/protocol/src/request_user_input.rs:15` | `pub struct RequestUserInputQuestion {` |
| `pub_struct` | `codex-rs/protocol/src/request_user_input.rs:32` | `pub struct RequestUserInputArgs {` |
| `pub_struct` | `codex-rs/protocol/src/request_user_input.rs:37` | `pub struct RequestUserInputAnswer {` |
| `pub_struct` | `codex-rs/protocol/src/request_user_input.rs:42` | `pub struct RequestUserInputResponse {` |
| `pub_struct` | `codex-rs/protocol/src/request_user_input.rs:47` | `pub struct RequestUserInputEvent {` |
| `pub_struct` | `codex-rs/protocol/src/thread_id.rs:13` | `pub struct ThreadId {` |
| `pub_fn` | `codex-rs/protocol/src/thread_id.rs:18` | `pub fn new() -> Self {` |
| `pub_fn` | `codex-rs/protocol/src/thread_id.rs:24` | `pub fn from_string(s: &str) -> Result<Self, uuid::Error> {` |
| `pub_enum` | `codex-rs/protocol/src/user_input.rs:10` | `pub enum UserInput {` |
| `pub_struct` | `codex-rs/protocol/src/user_input.rs:37` | `pub struct TextElement {` |
| `pub_fn` | `codex-rs/protocol/src/user_input.rs:45` | `pub fn new(byte_range: ByteRange, placeholder: Option<String>) -> Self {` |
| `pub_fn` | `codex-rs/protocol/src/user_input.rs:67` | `pub fn set_placeholder(&mut self, placeholder: Option<String>) {` |
| `pub_fn` | `codex-rs/protocol/src/user_input.rs:77` | `pub fn _placeholder_for_conversion_only(&self) -> Option<&str> {` |
| `pub_struct` | `codex-rs/protocol/src/user_input.rs:89` | `pub struct ByteRange {` |
| `pub_struct` | `codex-rs/responses-api-proxy/src/lib.rs:36` | `pub struct Args {` |
| `pub_fn` | `codex-rs/responses-api-proxy/src/lib.rs:66` | `pub fn run_main(args: Args) -> Result<()> {` |
| `pub_fn` | `codex-rs/responses-api-proxy/src/main.rs:9` | `pub fn main() -> anyhow::Result<()> {` |
| `pub_fn` | `codex-rs/rmcp-client/src/auth_status.rs:24` | `pub async fn determine_streamable_http_auth_status(` |
| `pub_fn` | `codex-rs/rmcp-client/src/auth_status.rs:55` | `pub async fn supports_oauth_login(url: &str) -> Result<bool> {` |
| `pub_fn` | `codex-rs/rmcp-client/src/bin/rmcp_test_server.rs:24` | `pub fn stdio() -> (tokio::io::Stdin, tokio::io::Stdout) {` |
| `pub_fn` | `codex-rs/rmcp-client/src/bin/test_stdio_server.rs:40` | `pub fn stdio() -> (tokio::io::Stdin, tokio::io::Stdout) {` |
| `pub_struct` | `codex-rs/rmcp-client/src/oauth.rs:57` | `pub struct StoredOAuthTokens {` |
| `pub_enum` | `codex-rs/rmcp-client/src/oauth.rs:69` | `pub enum OAuthCredentialsStoreMode {` |
| `pub_struct` | `codex-rs/rmcp-client/src/oauth.rs:83` | `pub struct WrappedOAuthTokenResponse(pub OAuthTokenResponse);` |
| `pub_fn` | `codex-rs/rmcp-client/src/oauth.rs:170` | `pub fn save_oauth_tokens(` |
| `pub_fn` | `codex-rs/rmcp-client/src/oauth.rs:231` | `pub fn delete_oauth_tokens(` |
| `pub_fn` | `codex-rs/rmcp-client/src/perform_oauth_login.rs:41` | `pub async fn perform_oauth_login(` |
| `pub_fn` | `codex-rs/rmcp-client/src/perform_oauth_login.rs:70` | `pub async fn perform_oauth_login_return_url(` |
| `pub_struct` | `codex-rs/rmcp-client/src/perform_oauth_login.rs:188` | `pub struct OauthLoginHandle {` |
| `pub_fn` | `codex-rs/rmcp-client/src/perform_oauth_login.rs:201` | `pub fn authorization_url(&self) -> &str {` |
| `pub_fn` | `codex-rs/rmcp-client/src/perform_oauth_login.rs:205` | `pub fn into_parts(self) -> (String, oneshot::Receiver<Result<()>>) {` |
| `pub_fn` | `codex-rs/rmcp-client/src/perform_oauth_login.rs:209` | `pub async fn wait(self) -> Result<()> {` |
| `pub_fn` | `codex-rs/rmcp-client/src/program_resolver.rs:27` | `pub fn resolve(program: OsString, _env: &HashMap<String, String>) -> std::io::Result<OsString> {` |
| `pub_fn` | `codex-rs/rmcp-client/src/program_resolver.rs:41` | `pub fn resolve(program: OsString, env: &HashMap<String, String>) -> std::io::Result<OsString> {` |
| `pub_type` | `codex-rs/rmcp-client/src/rmcp_client.rs:83` | `pub type Elicitation = CreateElicitationRequestParam;` |
| `pub_type` | `codex-rs/rmcp-client/src/rmcp_client.rs:84` | `pub type ElicitationResponse = CreateElicitationResult;` |
| `pub_type` | `codex-rs/rmcp-client/src/rmcp_client.rs:87` | `pub type SendElicitation = Box<` |
| `pub_struct` | `codex-rs/rmcp-client/src/rmcp_client.rs:91` | `pub struct ToolWithConnectorId {` |
| `pub_struct` | `codex-rs/rmcp-client/src/rmcp_client.rs:97` | `pub struct ListToolsWithConnectorIdResult {` |
| `pub_struct` | `codex-rs/rmcp-client/src/rmcp_client.rs:104` | `pub struct RmcpClient {` |
| `pub_fn` | `codex-rs/rmcp-client/src/rmcp_client.rs:109` | `pub async fn new_stdio_client(` |
| `pub_fn` | `codex-rs/rmcp-client/src/rmcp_client.rs:166` | `pub async fn new_streamable_http_client(` |
| `pub_fn` | `codex-rs/rmcp-client/src/rmcp_client.rs:221` | `pub async fn initialize(` |
| `pub_fn` | `codex-rs/rmcp-client/src/rmcp_client.rs:287` | `pub async fn list_tools(` |
| `pub_fn` | `codex-rs/rmcp-client/src/rmcp_client.rs:300` | `pub async fn list_tools_with_connector_ids(` |
| `pub_fn` | `codex-rs/rmcp-client/src/rmcp_client.rs:340` | `pub async fn list_resources(` |
| `pub_fn` | `codex-rs/rmcp-client/src/rmcp_client.rs:354` | `pub async fn list_resource_templates(` |
| `pub_fn` | `codex-rs/rmcp-client/src/rmcp_client.rs:368` | `pub async fn read_resource(` |
| `pub_fn` | `codex-rs/rmcp-client/src/rmcp_client.rs:381` | `pub async fn call_tool(` |
| `pub_fn` | `codex-rs/rmcp-client/src/rmcp_client.rs:408` | `pub async fn send_custom_notification(` |
| `pub_fn` | `codex-rs/rmcp-client/src/rmcp_client.rs:424` | `pub async fn send_custom_request(` |
| `pub_fn` | `codex-rs/state/src/extract.rs:15` | `pub fn apply_rollout_item(` |
| `pub_mod` | `codex-rs/state/src/lib.rs:8` | `pub mod log_db;` |
| `pub_const` | `codex-rs/state/src/lib.rs:34` | `pub const DB_ERROR_METRIC: &str = "codex.db.error";` |
| `pub_const` | `codex-rs/state/src/lib.rs:36` | `pub const DB_METRIC_BACKFILL: &str = "codex.db.backfill";` |
| `pub_const` | `codex-rs/state/src/lib.rs:38` | `pub const DB_METRIC_BACKFILL_DURATION_MS: &str = "codex.db.backfill.duration_ms";` |
| `pub_const` | `codex-rs/state/src/lib.rs:40` | `pub const DB_METRIC_COMPARE_ERROR: &str = "codex.db.compare_error";` |
| `pub_struct` | `codex-rs/state/src/log_db.rs:45` | `pub struct LogDbLayer {` |
| `pub_fn` | `codex-rs/state/src/log_db.rs:49` | `pub fn start(state_db: std::sync::Arc<StateRuntime>) -> LogDbLayer {` |
| `pub_struct` | `codex-rs/state/src/model/log.rs:5` | `pub struct LogEntry {` |
| `pub_struct` | `codex-rs/state/src/model/log.rs:18` | `pub struct LogRow {` |
| `pub_struct` | `codex-rs/state/src/model/log.rs:31` | `pub struct LogQuery {` |
| `pub_enum` | `codex-rs/state/src/model/thread_metadata.rs:16` | `pub enum SortKey {` |
| `pub_struct` | `codex-rs/state/src/model/thread_metadata.rs:25` | `pub struct Anchor {` |
| `pub_struct` | `codex-rs/state/src/model/thread_metadata.rs:34` | `pub struct ThreadsPage {` |
| `pub_struct` | `codex-rs/state/src/model/thread_metadata.rs:45` | `pub struct ExtractionOutcome {` |
| `pub_struct` | `codex-rs/state/src/model/thread_metadata.rs:54` | `pub struct ThreadMetadata {` |
| `pub_struct` | `codex-rs/state/src/model/thread_metadata.rs:91` | `pub struct ThreadMetadataBuilder {` |
| `pub_fn` | `codex-rs/state/src/model/thread_metadata.rs:122` | `pub fn new(` |
| `pub_fn` | `codex-rs/state/src/model/thread_metadata.rs:146` | `pub fn build(&self, default_provider: &str) -> ThreadMetadata {` |
| `pub_fn` | `codex-rs/state/src/model/thread_metadata.rs:181` | `pub fn diff_fields(&self, other: &Self) -> Vec<&'static str> {` |
| `pub_struct` | `codex-rs/state/src/model/thread_metadata.rs:345` | `pub struct BackfillStats {` |
| `pub_const` | `codex-rs/state/src/runtime.rs:38` | `pub const STATE_DB_FILENAME: &str = "state.sqlite";` |
| `pub_struct` | `codex-rs/state/src/runtime.rs:43` | `pub struct StateRuntime {` |
| `pub_fn` | `codex-rs/state/src/runtime.rs:53` | `pub async fn init(` |
| `pub_fn` | `codex-rs/state/src/runtime.rs:86` | `pub fn codex_home(&self) -> &Path {` |
| `pub_fn` | `codex-rs/state/src/runtime.rs:91` | `pub async fn get_thread(&self, id: ThreadId) -> anyhow::Result<Option<crate::ThreadMetadata>> {` |
| `pub_fn` | `codex-rs/state/src/runtime.rs:123` | `pub async fn get_dynamic_tools(` |
| `pub_fn` | `codex-rs/state/src/runtime.rs:155` | `pub async fn find_rollout_path_by_id(` |
| `pub_fn` | `codex-rs/state/src/runtime.rs:179` | `pub async fn list_threads(` |
| `pub_fn` | `codex-rs/state/src/runtime.rs:244` | `pub async fn insert_log(&self, entry: &LogEntry) -> anyhow::Result<()> {` |
| `pub_fn` | `codex-rs/state/src/runtime.rs:249` | `pub async fn insert_logs(&self, entries: &[LogEntry]) -> anyhow::Result<()> {` |
| `pub_fn` | `codex-rs/state/src/runtime.rs:281` | `pub async fn query_logs(&self, query: &LogQuery) -> anyhow::Result<Vec<LogRow>> {` |
| `pub_fn` | `codex-rs/state/src/runtime.rs:303` | `pub async fn max_log_id(&self, query: &LogQuery) -> anyhow::Result<i64> {` |
| `pub_fn` | `codex-rs/state/src/runtime.rs:313` | `pub async fn list_thread_ids(` |
| `pub_fn` | `codex-rs/state/src/runtime.rs:343` | `pub async fn upsert_thread(&self, metadata: &crate::ThreadMetadata) -> anyhow::Result<()> {` |
| `pub_fn` | `codex-rs/state/src/runtime.rs:410` | `pub async fn persist_dynamic_tools(` |
| `pub_fn` | `codex-rs/state/src/runtime.rs:459` | `pub async fn apply_rollout_items(` |
| `pub_fn` | `codex-rs/state/src/runtime.rs:502` | `pub async fn mark_archived(` |
| `pub_fn` | `codex-rs/state/src/runtime.rs:526` | `pub async fn mark_unarchived(` |
| `pub_fn` | `codex-rs/stdio-to-uds/src/lib.rs:20` | `pub fn run(socket_path: &Path) -> anyhow::Result<()> {` |
| `fn_main` | `codex-rs/stdio-to-uds/src/main.rs:5` | `fn main() -> anyhow::Result<()> {` |
| `pub_fn` | `codex-rs/tui/src/additional_dirs.rs:7` | `pub fn add_dir_warning_message(` |
| `pub_struct` | `codex-rs/tui/src/app.rs:108` | `pub struct AppExitInfo {` |
| `pub_fn` | `codex-rs/tui/src/app.rs:117` | `pub fn fatal(message: impl Into<String>) -> Self {` |
| `pub_enum` | `codex-rs/tui/src/app.rs:135` | `pub enum ExitReason {` |
| `pub_fn` | `codex-rs/tui/src/app.rs:595` | `pub fn chatwidget_init_for_forked_or_resumed_thread(` |
| `pub_fn` | `codex-rs/tui/src/app.rs:917` | `pub async fn run(` |
| `fn_main` | `codex-rs/tui/src/bin/md-events.rs:4` | `fn main() {` |
| `pub_fn` | `codex-rs/tui/src/bottom_pane/approval_overlay.rs:75` | `pub fn new(request: ApprovalRequest, app_event_tx: AppEventSender, features: Features) -> Self {` |
| `pub_fn` | `codex-rs/tui/src/bottom_pane/approval_overlay.rs:91` | `pub fn enqueue_request(&mut self, req: ApprovalRequest) {` |
| `pub_enum` | `codex-rs/tui/src/bottom_pane/chat_composer.rs:181` | `pub enum InputResult {` |
| `pub_fn` | `codex-rs/tui/src/bottom_pane/chat_composer.rs:317` | `pub fn new(` |
| `pub_fn` | `codex-rs/tui/src/bottom_pane/chat_composer.rs:393` | `pub fn set_skill_mentions(&mut self, skills: Option<Vec<SkillMetadata>>) {` |
| `pub_fn` | `codex-rs/tui/src/bottom_pane/chat_composer.rs:401` | `pub fn set_image_paste_enabled(&mut self, enabled: bool) {` |
| `pub_fn` | `codex-rs/tui/src/bottom_pane/chat_composer.rs:405` | `pub fn set_connector_mentions(&mut self, connectors_snapshot: Option<ConnectorsSnapshot>) {` |
| `pub_fn` | `codex-rs/tui/src/bottom_pane/chat_composer.rs:419` | `pub fn set_steer_enabled(&mut self, enabled: bool) {` |
| `pub_fn` | `codex-rs/tui/src/bottom_pane/chat_composer.rs:423` | `pub fn set_collaboration_modes_enabled(&mut self, enabled: bool) {` |
| `pub_fn` | `codex-rs/tui/src/bottom_pane/chat_composer.rs:427` | `pub fn set_connectors_enabled(&mut self, enabled: bool) {` |
| `pub_fn` | `codex-rs/tui/src/bottom_pane/chat_composer.rs:431` | `pub fn set_collaboration_mode_indicator(` |
| `pub_fn` | `codex-rs/tui/src/bottom_pane/chat_composer.rs:438` | `pub fn set_personality_command_enabled(&mut self, enabled: bool) {` |
| `pub_fn` | `codex-rs/tui/src/bottom_pane/chat_composer.rs:454` | `pub fn set_windows_degraded_sandbox_active(&mut self, enabled: bool) {` |
| `pub_fn` | `codex-rs/tui/src/bottom_pane/chat_composer.rs:535` | `pub fn handle_paste(&mut self, pasted: String) -> bool {` |
| `pub_fn` | `codex-rs/tui/src/bottom_pane/chat_composer.rs:556` | `pub fn handle_paste_image_path(&mut self, pasted: String) -> bool {` |
| `pub_fn` | `codex-rs/tui/src/bottom_pane/chat_composer.rs:853` | `pub fn attach_image(&mut self, path: PathBuf) {` |
| `pub_fn` | `codex-rs/tui/src/bottom_pane/chat_composer.rs:864` | `pub fn take_recent_submission_images(&mut self) -> Vec<PathBuf> {` |
| `pub_fn` | `codex-rs/tui/src/bottom_pane/chat_composer.rs:869` | `pub fn take_recent_submission_images_with_placeholders(&mut self) -> Vec<LocalImageAttachment> {` |
| `pub_fn` | `codex-rs/tui/src/bottom_pane/chat_composer.rs:931` | `pub fn show_quit_shortcut_hint(&mut self, key: KeyBinding, has_focus: bool) {` |
| `pub_fn` | `codex-rs/tui/src/bottom_pane/chat_composer.rs:941` | `pub fn clear_quit_shortcut_hint(&mut self, has_focus: bool) {` |
| `pub_fn` | `codex-rs/tui/src/bottom_pane/chat_composer.rs:974` | `pub fn handle_key_event(&mut self, key_event: KeyEvent) -> (InputResult, bool) {` |
| `pub_fn` | `codex-rs/tui/src/bottom_pane/chat_composer.rs:1592` | `pub fn skills(&self) -> Option<&Vec<SkillMetadata>> {` |
| `pub_fn` | `codex-rs/tui/src/bottom_pane/chat_composer.rs:2988` | `pub fn set_task_running(&mut self, running: bool) {` |
| `pub_fn` | `codex-rs/tui/src/bottom_pane/chat_composer_history.rs:61` | `pub fn new() -> Self {` |
| `pub_fn` | `codex-rs/tui/src/bottom_pane/chat_composer_history.rs:73` | `pub fn set_metadata(&mut self, log_id: u64, entry_count: usize) {` |
| `pub_fn` | `codex-rs/tui/src/bottom_pane/chat_composer_history.rs:84` | `pub fn record_local_submission(&mut self, entry: HistoryEntry) {` |
| `pub_fn` | `codex-rs/tui/src/bottom_pane/chat_composer_history.rs:101` | `pub fn reset_navigation(&mut self) {` |
| `pub_fn` | `codex-rs/tui/src/bottom_pane/chat_composer_history.rs:108` | `pub fn should_handle_navigation(&self, text: &str, cursor: usize) -> bool {` |
| `pub_fn` | `codex-rs/tui/src/bottom_pane/chat_composer_history.rs:129` | `pub fn navigate_up(&mut self, app_event_tx: &AppEventSender) -> Option<HistoryEntry> {` |
| `pub_fn` | `codex-rs/tui/src/bottom_pane/chat_composer_history.rs:146` | `pub fn navigate_down(&mut self, app_event_tx: &AppEventSender) -> Option<HistoryEntry> {` |
| `pub_fn` | `codex-rs/tui/src/bottom_pane/chat_composer_history.rs:173` | `pub fn on_entry_response(` |
| `pub_fn` | `codex-rs/tui/src/bottom_pane/list_selection_view.rs:94` | `pub fn new(params: SelectionViewParams, app_event_tx: AppEventSender) -> Self {` |
| `pub_mod` | `codex-rs/tui/src/bottom_pane/mod.rs:58` | `pub mod custom_prompt_view;` |
| `pub_mod` | `codex-rs/tui/src/bottom_pane/mod.rs:77` | `pub mod popup_consts;` |
| `pub_fn` | `codex-rs/tui/src/bottom_pane/mod.rs:168` | `pub fn new(params: BottomPaneParams) -> Self {` |
| `pub_fn` | `codex-rs/tui/src/bottom_pane/mod.rs:207` | `pub fn set_skills(&mut self, skills: Option<Vec<SkillMetadata>>) {` |
| `pub_fn` | `codex-rs/tui/src/bottom_pane/mod.rs:215` | `pub fn set_image_paste_enabled(&mut self, enabled: bool) {` |
| `pub_fn` | `codex-rs/tui/src/bottom_pane/mod.rs:220` | `pub fn set_connectors_snapshot(&mut self, snapshot: Option<ConnectorsSnapshot>) {` |
| `pub_fn` | `codex-rs/tui/src/bottom_pane/mod.rs:225` | `pub fn take_mention_paths(&mut self) -> HashMap<String, String> {` |
| `pub_fn` | `codex-rs/tui/src/bottom_pane/mod.rs:235` | `pub fn set_steer_enabled(&mut self, enabled: bool) {` |
| `pub_fn` | `codex-rs/tui/src/bottom_pane/mod.rs:239` | `pub fn set_collaboration_modes_enabled(&mut self, enabled: bool) {` |
| `pub_fn` | `codex-rs/tui/src/bottom_pane/mod.rs:244` | `pub fn set_connectors_enabled(&mut self, enabled: bool) {` |
| `pub_fn` | `codex-rs/tui/src/bottom_pane/mod.rs:249` | `pub fn set_windows_degraded_sandbox_active(&mut self, enabled: bool) {` |
| `pub_fn` | `codex-rs/tui/src/bottom_pane/mod.rs:254` | `pub fn set_collaboration_mode_indicator(` |
| `pub_fn` | `codex-rs/tui/src/bottom_pane/mod.rs:262` | `pub fn set_personality_command_enabled(&mut self, enabled: bool) {` |
| `pub_fn` | `codex-rs/tui/src/bottom_pane/mod.rs:267` | `pub fn status_widget(&self) -> Option<&StatusIndicatorWidget> {` |
| `pub_fn` | `codex-rs/tui/src/bottom_pane/mod.rs:271` | `pub fn skills(&self) -> Option<&Vec<SkillMetadata>> {` |
| `pub_fn` | `codex-rs/tui/src/bottom_pane/mod.rs:295` | `pub fn handle_key_event(&mut self, key_event: KeyEvent) -> InputResult {` |
| `pub_fn` | `codex-rs/tui/src/bottom_pane/mod.rs:390` | `pub fn handle_paste(&mut self, pasted: String) {` |
| `pub_fn` | `codex-rs/tui/src/bottom_pane/mod.rs:570` | `pub fn set_task_running(&mut self, running: bool) {` |
| `pub_fn` | `codex-rs/tui/src/bottom_pane/mod.rs:691` | `pub fn push_approval_request(&mut self, request: ApprovalRequest, features: &Features) {` |
| `pub_fn` | `codex-rs/tui/src/bottom_pane/mod.rs:711` | `pub fn push_user_input_request(&mut self, request: RequestUserInputEvent) {` |
| `pub_fn` | `codex-rs/tui/src/bottom_pane/paste_burst.rs:204` | `pub fn recommended_flush_delay() -> Duration {` |
| `pub_fn` | `codex-rs/tui/src/bottom_pane/paste_burst.rs:214` | `pub fn on_plain_char(&mut self, ch: char, now: Instant) -> CharDecision {` |
| `pub_fn` | `codex-rs/tui/src/bottom_pane/paste_burst.rs:252` | `pub fn on_plain_char_no_hold(&mut self, now: Instant) -> Option<CharDecision> {` |
| `pub_fn` | `codex-rs/tui/src/bottom_pane/paste_burst.rs:289` | `pub fn flush_if_due(&mut self, now: Instant) -> FlushResult {` |
| `pub_fn` | `codex-rs/tui/src/bottom_pane/paste_burst.rs:320` | `pub fn append_newline_if_active(&mut self, now: Instant) -> bool {` |
| `pub_fn` | `codex-rs/tui/src/bottom_pane/paste_burst.rs:331` | `pub fn newline_should_insert_instead_of_submit(&self, now: Instant) -> bool {` |
| `pub_fn` | `codex-rs/tui/src/bottom_pane/paste_burst.rs:337` | `pub fn extend_window(&mut self, now: Instant) {` |
| `pub_fn` | `codex-rs/tui/src/bottom_pane/paste_burst.rs:342` | `pub fn begin_with_retro_grabbed(&mut self, grabbed: String, now: Instant) {` |
| `pub_fn` | `codex-rs/tui/src/bottom_pane/paste_burst.rs:351` | `pub fn append_char_to_buffer(&mut self, ch: char, now: Instant) {` |
| `pub_fn` | `codex-rs/tui/src/bottom_pane/paste_burst.rs:359` | `pub fn try_append_char_if_active(&mut self, ch: char, now: Instant) -> bool {` |
| `pub_fn` | `codex-rs/tui/src/bottom_pane/paste_burst.rs:379` | `pub fn decide_begin_buffer(` |
| `pub_fn` | `codex-rs/tui/src/bottom_pane/paste_burst.rs:402` | `pub fn flush_before_modified_input(&mut self) -> Option<String> {` |
| `pub_fn` | `codex-rs/tui/src/bottom_pane/paste_burst.rs:418` | `pub fn clear_window_after_non_char(&mut self) {` |
| `pub_fn` | `codex-rs/tui/src/bottom_pane/paste_burst.rs:429` | `pub fn is_active(&self) -> bool {` |
| `pub_fn` | `codex-rs/tui/src/bottom_pane/paste_burst.rs:437` | `pub fn clear_after_explicit_paste(&mut self) {` |
| `pub_enum` | `codex-rs/tui/src/bottom_pane/prompt_args.rs:17` | `pub enum PromptArgsError {` |
| `pub_enum` | `codex-rs/tui/src/bottom_pane/prompt_args.rs:36` | `pub enum PromptExpansionError {` |
| `pub_fn` | `codex-rs/tui/src/bottom_pane/prompt_args.rs:48` | `pub fn user_message(&self) -> String {` |
| `pub_fn` | `codex-rs/tui/src/bottom_pane/prompt_args.rs:67` | `pub fn parse_slash_name(line: &str) -> Option<(&str, &str, usize)> {` |
| `pub_struct` | `codex-rs/tui/src/bottom_pane/prompt_args.rs:89` | `pub struct PromptArg {` |
| `pub_struct` | `codex-rs/tui/src/bottom_pane/prompt_args.rs:95` | `pub struct PromptExpansion {` |
| `pub_fn` | `codex-rs/tui/src/bottom_pane/prompt_args.rs:103` | `pub fn parse_positional_args(rest: &str, text_elements: &[TextElement]) -> Vec<PromptArg> {` |
| `pub_fn` | `codex-rs/tui/src/bottom_pane/prompt_args.rs:112` | `pub fn prompt_argument_names(content: &str) -> Vec<String> {` |
| `pub_fn` | `codex-rs/tui/src/bottom_pane/prompt_args.rs:149` | `pub fn parse_prompt_inputs(` |
| `pub_fn` | `codex-rs/tui/src/bottom_pane/prompt_args.rs:191` | `pub fn expand_custom_prompt(` |
| `pub_fn` | `codex-rs/tui/src/bottom_pane/prompt_args.rs:256` | `pub fn prompt_has_numeric_placeholders(content: &str) -> bool {` |
| `pub_fn` | `codex-rs/tui/src/bottom_pane/prompt_args.rs:276` | `pub fn extract_positional_args_for_prompt_line(` |
| `pub_fn` | `codex-rs/tui/src/bottom_pane/prompt_args.rs:316` | `pub fn expand_if_numeric_with_positional_args(` |
| `pub_fn` | `codex-rs/tui/src/bottom_pane/prompt_args.rs:335` | `pub fn expand_numeric_placeholders(content: &str, args: &[PromptArg]) -> PromptExpansion {` |
| `pub_fn` | `codex-rs/tui/src/bottom_pane/prompt_args.rs:550` | `pub fn prompt_command_with_arg_placeholders(name: &str, args: &[String]) -> (String, usize) {` |
| `pub_fn` | `codex-rs/tui/src/bottom_pane/scroll_state.rs:14` | `pub fn new() -> Self {` |
| `pub_fn` | `codex-rs/tui/src/bottom_pane/scroll_state.rs:22` | `pub fn reset(&mut self) {` |
| `pub_fn` | `codex-rs/tui/src/bottom_pane/scroll_state.rs:28` | `pub fn clamp_selection(&mut self, len: usize) {` |
| `pub_fn` | `codex-rs/tui/src/bottom_pane/scroll_state.rs:39` | `pub fn move_up_wrap(&mut self, len: usize) {` |
| `pub_fn` | `codex-rs/tui/src/bottom_pane/scroll_state.rs:53` | `pub fn move_down_wrap(&mut self, len: usize) {` |
| `pub_fn` | `codex-rs/tui/src/bottom_pane/scroll_state.rs:67` | `pub fn ensure_visible(&mut self, len: usize, visible_rows: usize) {` |
| `pub_fn` | `codex-rs/tui/src/bottom_pane/textarea.rs:54` | `pub fn new() -> Self {` |
| `pub_fn` | `codex-rs/tui/src/bottom_pane/textarea.rs:66` | `pub fn set_text_clearing_elements(&mut self, text: &str) {` |
| `pub_fn` | `codex-rs/tui/src/bottom_pane/textarea.rs:71` | `pub fn set_text_with_elements(&mut self, text: &str, elements: &[UserTextElement]) {` |
| `pub_fn` | `codex-rs/tui/src/bottom_pane/textarea.rs:101` | `pub fn text(&self) -> &str {` |
| `pub_fn` | `codex-rs/tui/src/bottom_pane/textarea.rs:105` | `pub fn insert_str(&mut self, text: &str) {` |
| `pub_fn` | `codex-rs/tui/src/bottom_pane/textarea.rs:109` | `pub fn insert_str_at(&mut self, pos: usize, text: &str) {` |
| `pub_fn` | `codex-rs/tui/src/bottom_pane/textarea.rs:120` | `pub fn replace_range(&mut self, range: std::ops::Range<usize>, text: &str) {` |
| `pub_fn` | `codex-rs/tui/src/bottom_pane/textarea.rs:158` | `pub fn cursor(&self) -> usize {` |
| `pub_fn` | `codex-rs/tui/src/bottom_pane/textarea.rs:162` | `pub fn set_cursor(&mut self, pos: usize) {` |
| `pub_fn` | `codex-rs/tui/src/bottom_pane/textarea.rs:168` | `pub fn desired_height(&self, width: u16) -> u16 {` |
| `pub_fn` | `codex-rs/tui/src/bottom_pane/textarea.rs:173` | `pub fn cursor_pos(&self, area: Rect) -> Option<(u16, u16)> {` |
| `pub_fn` | `codex-rs/tui/src/bottom_pane/textarea.rs:178` | `pub fn cursor_pos_with_state(&self, area: Rect, state: TextAreaState) -> Option<(u16, u16)> {` |
| `pub_fn` | `codex-rs/tui/src/bottom_pane/textarea.rs:191` | `pub fn is_empty(&self) -> bool {` |
| `pub_fn` | `codex-rs/tui/src/bottom_pane/textarea.rs:244` | `pub fn input(&mut self, event: KeyEvent) {` |
| `pub_fn` | `codex-rs/tui/src/bottom_pane/textarea.rs:483` | `pub fn delete_backward(&mut self, n: usize) {` |
| `pub_fn` | `codex-rs/tui/src/bottom_pane/textarea.rs:497` | `pub fn delete_forward(&mut self, n: usize) {` |
| `pub_fn` | `codex-rs/tui/src/bottom_pane/textarea.rs:511` | `pub fn delete_backward_word(&mut self) {` |
| `pub_fn` | `codex-rs/tui/src/bottom_pane/textarea.rs:521` | `pub fn delete_forward_word(&mut self) {` |
| `pub_fn` | `codex-rs/tui/src/bottom_pane/textarea.rs:528` | `pub fn kill_to_end_of_line(&mut self) {` |
| `pub_fn` | `codex-rs/tui/src/bottom_pane/textarea.rs:545` | `pub fn kill_to_beginning_of_line(&mut self) {` |
| `pub_fn` | `codex-rs/tui/src/bottom_pane/textarea.rs:558` | `pub fn yank(&mut self) {` |
| `pub_fn` | `codex-rs/tui/src/bottom_pane/textarea.rs:582` | `pub fn move_cursor_left(&mut self) {` |
| `pub_fn` | `codex-rs/tui/src/bottom_pane/textarea.rs:588` | `pub fn move_cursor_right(&mut self) {` |
| `pub_fn` | `codex-rs/tui/src/bottom_pane/textarea.rs:593` | `pub fn move_cursor_up(&mut self) {` |
| `pub_fn` | `codex-rs/tui/src/bottom_pane/textarea.rs:656` | `pub fn move_cursor_down(&mut self) {` |
| `pub_fn` | `codex-rs/tui/src/bottom_pane/textarea.rs:724` | `pub fn move_cursor_to_beginning_of_line(&mut self, move_up_at_bol: bool) {` |
| `pub_fn` | `codex-rs/tui/src/bottom_pane/textarea.rs:734` | `pub fn move_cursor_to_end_of_line(&mut self, move_down_at_eol: bool) {` |
| `pub_fn` | `codex-rs/tui/src/bottom_pane/textarea.rs:746` | `pub fn element_payloads(&self) -> Vec<String> {` |
| `pub_fn` | `codex-rs/tui/src/bottom_pane/textarea.rs:753` | `pub fn text_elements(&self) -> Vec<UserTextElement> {` |
| `pub_fn` | `codex-rs/tui/src/bottom_pane/textarea.rs:773` | `pub fn replace_element_payload(&mut self, old: &str, new: &str) -> bool {` |
| `pub_fn` | `codex-rs/tui/src/bottom_pane/textarea.rs:838` | `pub fn insert_element(&mut self, text: &str) {` |
| `pub_fn` | `codex-rs/tui/src/bottom_pane/textarea.rs:851` | `pub fn add_element_range(&mut self, range: Range<usize>) {` |
| `pub_fn` | `codex-rs/tui/src/bottom_pane/textarea.rs:875` | `pub fn remove_element_range(&mut self, range: Range<usize>) -> bool {` |
| `pub_struct` | `codex-rs/tui/src/cli.rs:9` | `pub struct Cli {` |
| `pub_enum` | `codex-rs/tui/src/clipboard_paste.rs:6` | `pub enum PasteImageError {` |
| `pub_enum` | `codex-rs/tui/src/clipboard_paste.rs:26` | `pub enum EncodedImageFormat {` |
| `pub_fn` | `codex-rs/tui/src/clipboard_paste.rs:33` | `pub fn label(self) -> &'static str {` |
| `pub_struct` | `codex-rs/tui/src/clipboard_paste.rs:43` | `pub struct PastedImageInfo {` |
| `pub_fn` | `codex-rs/tui/src/clipboard_paste.rs:51` | `pub fn paste_image_as_png() -> Result<(Vec<u8>, PastedImageInfo), PasteImageError> {` |
| `pub_fn` | `codex-rs/tui/src/clipboard_paste.rs:113` | `pub fn paste_image_as_png() -> Result<(Vec<u8>, PastedImageInfo), PasteImageError> {` |
| `pub_fn` | `codex-rs/tui/src/clipboard_paste.rs:121` | `pub fn paste_image_to_temp_png() -> Result<(PathBuf, PastedImageInfo), PasteImageError> {` |
| `pub_fn` | `codex-rs/tui/src/clipboard_paste.rs:232` | `pub fn paste_image_to_temp_png() -> Result<(PathBuf, PastedImageInfo), PasteImageError> {` |
| `pub_fn` | `codex-rs/tui/src/clipboard_paste.rs:245` | `pub fn normalize_pasted_path(pasted: &str) -> Option<PathBuf> {` |
| `pub_fn` | `codex-rs/tui/src/clipboard_paste.rs:358` | `pub fn pasted_image_format(path: &Path) -> EncodedImageFormat {` |
| `pub_struct` | `codex-rs/tui/src/custom_terminal.rs:48` | `pub struct Frame<'a> {` |
| `pub_const` | `codex-rs/tui/src/custom_terminal.rs:70` | `pub const fn area(&self) -> Rect {` |
| `pub_fn` | `codex-rs/tui/src/custom_terminal.rs:98` | `pub fn buffer_mut(&mut self) -> &mut Buffer {` |
| `pub_struct` | `codex-rs/tui/src/custom_terminal.rs:104` | `pub struct Terminal<B>` |
| `pub_fn` | `codex-rs/tui/src/custom_terminal.rs:148` | `pub fn with_options(mut backend: B) -> io::Result<Self> {` |
| `pub_fn` | `codex-rs/tui/src/custom_terminal.rs:163` | `pub fn get_frame(&mut self) -> Frame<'_> {` |
| `pub_const` | `codex-rs/tui/src/custom_terminal.rs:192` | `pub const fn backend(&self) -> &B {` |
| `pub_fn` | `codex-rs/tui/src/custom_terminal.rs:197` | `pub fn backend_mut(&mut self) -> &mut B {` |
| `pub_fn` | `codex-rs/tui/src/custom_terminal.rs:203` | `pub fn flush(&mut self) -> io::Result<()> {` |
| `pub_fn` | `codex-rs/tui/src/custom_terminal.rs:216` | `pub fn resize(&mut self, screen_size: Size) -> io::Result<()> {` |
| `pub_fn` | `codex-rs/tui/src/custom_terminal.rs:222` | `pub fn set_viewport_area(&mut self, area: Rect) {` |
| `pub_fn` | `codex-rs/tui/src/custom_terminal.rs:229` | `pub fn autoresize(&mut self) -> io::Result<()> {` |
| `pub_fn` | `codex-rs/tui/src/custom_terminal.rs:342` | `pub fn hide_cursor(&mut self) -> io::Result<()> {` |
| `pub_fn` | `codex-rs/tui/src/custom_terminal.rs:349` | `pub fn show_cursor(&mut self) -> io::Result<()> {` |
| `pub_fn` | `codex-rs/tui/src/custom_terminal.rs:359` | `pub fn get_cursor_position(&mut self) -> io::Result<Position> {` |
| `pub_fn` | `codex-rs/tui/src/custom_terminal.rs:372` | `pub fn clear(&mut self) -> io::Result<()> {` |
| `pub_fn` | `codex-rs/tui/src/custom_terminal.rs:385` | `pub fn clear_scrollback(&mut self) -> io::Result<()> {` |
| `pub_fn` | `codex-rs/tui/src/custom_terminal.rs:398` | `pub fn swap_buffers(&mut self) {` |
| `pub_fn` | `codex-rs/tui/src/custom_terminal.rs:404` | `pub fn size(&self) -> io::Result<Size> {` |
| `pub_struct` | `codex-rs/tui/src/diff_render.rs:31` | `pub struct DiffSummary {` |
| `pub_fn` | `codex-rs/tui/src/diff_render.rs:37` | `pub fn new(changes: HashMap<PathBuf, FileChange>, cwd: PathBuf) -> Self {` |
| `pub_fn` | `codex-rs/tui/src/file_search.rs:29` | `pub fn new(search_dir: PathBuf, tx: AppEventSender) -> Self {` |
| `pub_fn` | `codex-rs/tui/src/file_search.rs:44` | `pub fn update_search_dir(&mut self, new_dir: PathBuf) {` |
| `pub_fn` | `codex-rs/tui/src/file_search.rs:53` | `pub fn on_user_query(&self, query: String) {` |
| `pub_fn` | `codex-rs/tui/src/history_cell.rs:711` | `pub fn new_approval_decision_cell(` |
| `pub_struct` | `codex-rs/tui/src/history_cell.rs:926` | `pub struct SessionInfoCell(CompositeHistoryCell);` |
| `pub_struct` | `codex-rs/tui/src/history_cell.rs:2129` | `pub struct FinalMessageSeparator {` |
| `pub_struct` | `codex-rs/tui/src/insert_history.rs:138` | `pub struct SetScrollRegion(pub std::ops::Range<u16>);` |
| `pub_struct` | `codex-rs/tui/src/insert_history.rs:158` | `pub struct ResetScrollRegion;` |
| `pub_fn` | `codex-rs/tui/src/key_hint.rs:29` | `pub fn is_press(&self, event: KeyEvent) -> bool {` |
| `pub_mod` | `codex-rs/tui/src/lib.rs:69` | `pub mod custom_terminal;` |
| `pub_mod` | `codex-rs/tui/src/lib.rs:79` | `pub mod insert_history;` |
| `pub_mod` | `codex-rs/tui/src/lib.rs:81` | `pub mod live_wrap;` |
| `pub_mod` | `codex-rs/tui/src/lib.rs:87` | `pub mod onboarding;` |
| `pub_mod` | `codex-rs/tui/src/lib.rs:90` | `pub mod public_widgets;` |
| `pub_mod` | `codex-rs/tui/src/lib.rs:107` | `pub mod update_action;` |
| `pub_mod` | `codex-rs/tui/src/lib.rs:115` | `pub mod test_backend;` |
| `pub_fn` | `codex-rs/tui/src/lib.rs:126` | `pub async fn run_main(` |
| `pub_enum` | `codex-rs/tui/src/lib.rs:830` | `pub enum LoginStatus {` |
| `pub_struct` | `codex-rs/tui/src/live_wrap.rs:6` | `pub struct Row {` |
| `pub_fn` | `codex-rs/tui/src/live_wrap.rs:13` | `pub fn width(&self) -> usize {` |
| `pub_struct` | `codex-rs/tui/src/live_wrap.rs:21` | `pub struct RowBuilder {` |
| `pub_fn` | `codex-rs/tui/src/live_wrap.rs:30` | `pub fn new(target_width: usize) -> Self {` |
| `pub_fn` | `codex-rs/tui/src/live_wrap.rs:38` | `pub fn width(&self) -> usize {` |
| `pub_fn` | `codex-rs/tui/src/live_wrap.rs:42` | `pub fn set_width(&mut self, width: usize) {` |
| `pub_fn` | `codex-rs/tui/src/live_wrap.rs:58` | `pub fn push_fragment(&mut self, fragment: &str) {` |
| `pub_fn` | `codex-rs/tui/src/live_wrap.rs:80` | `pub fn end_line(&mut self) {` |
| `pub_fn` | `codex-rs/tui/src/live_wrap.rs:85` | `pub fn drain_rows(&mut self) -> Vec<Row> {` |
| `pub_fn` | `codex-rs/tui/src/live_wrap.rs:90` | `pub fn rows(&self) -> &[Row] {` |
| `pub_fn` | `codex-rs/tui/src/live_wrap.rs:95` | `pub fn display_rows(&self) -> Vec<Row> {` |
| `pub_fn` | `codex-rs/tui/src/live_wrap.rs:108` | `pub fn drain_commit_ready(&mut self, max_keep: usize) -> Vec<Row> {` |
| `pub_fn` | `codex-rs/tui/src/live_wrap.rs:187` | `pub fn take_prefix_by_width(text: &str, max_cols: usize) -> (String, &str, usize) {` |
| `fn_main` | `codex-rs/tui/src/main.rs:16` | `fn main() -> anyhow::Result<()> {` |
| `pub_fn` | `codex-rs/tui/src/markdown_render.rs:74` | `pub fn render_markdown_text(input: &str) -> Text<'static> {` |
| `pub_fn` | `codex-rs/tui/src/markdown_stream.rs:14` | `pub fn new(width: Option<usize>) -> Self {` |
| `pub_fn` | `codex-rs/tui/src/markdown_stream.rs:22` | `pub fn clear(&mut self) {` |
| `pub_fn` | `codex-rs/tui/src/markdown_stream.rs:27` | `pub fn push_delta(&mut self, delta: &str) {` |
| `pub_fn` | `codex-rs/tui/src/markdown_stream.rs:35` | `pub fn commit_complete_lines(&mut self) -> Vec<Line<'static>> {` |
| `pub_fn` | `codex-rs/tui/src/markdown_stream.rs:69` | `pub fn finalize_and_drain(&mut self) -> Vec<Line<'static>> {` |
| `pub_struct` | `codex-rs/tui/src/notifications/bel.rs:9` | `pub struct BelBackend;` |
| `pub_fn` | `codex-rs/tui/src/notifications/bel.rs:12` | `pub fn notify(&mut self, _message: &str) -> io::Result<()> {` |
| `pub_struct` | `codex-rs/tui/src/notifications/bel.rs:19` | `pub struct PostNotification;` |
| `pub_enum` | `codex-rs/tui/src/notifications/mod.rs:12` | `pub enum DesktopNotificationBackend {` |
| `pub_fn` | `codex-rs/tui/src/notifications/mod.rs:18` | `pub fn for_method(method: NotificationMethod) -> Self {` |
| `pub_fn` | `codex-rs/tui/src/notifications/mod.rs:32` | `pub fn method(&self) -> NotificationMethod {` |
| `pub_fn` | `codex-rs/tui/src/notifications/mod.rs:39` | `pub fn notify(&mut self, message: &str) -> io::Result<()> {` |
| `pub_fn` | `codex-rs/tui/src/notifications/mod.rs:47` | `pub fn detect_backend(method: NotificationMethod) -> DesktopNotificationBackend {` |
| `pub_struct` | `codex-rs/tui/src/notifications/osc9.rs:9` | `pub struct Osc9Backend;` |
| `pub_fn` | `codex-rs/tui/src/notifications/osc9.rs:12` | `pub fn notify(&mut self, message: &str) -> io::Result<()> {` |
| `pub_struct` | `codex-rs/tui/src/notifications/osc9.rs:19` | `pub struct PostNotification(pub String);` |
| `pub_mod` | `codex-rs/tui/src/onboarding/mod.rs:2` | `pub mod onboarding_screen;` |
| `pub_fn` | `codex-rs/tui/src/onboarding/onboarding_screen.rs:182` | `pub fn directory_trust_decision(&self) -> Option<TrustDirectorySelection> {` |
| `pub_fn` | `codex-rs/tui/src/onboarding/onboarding_screen.rs:195` | `pub fn should_exit(&self) -> bool {` |
| `pub_enum` | `codex-rs/tui/src/onboarding/trust_directory.rs:37` | `pub enum TrustDirectorySelection {` |
| `pub_struct` | `codex-rs/tui/src/oss_selection.rs:87` | `pub struct OssSelectionWidget<'a> {` |
| `pub_fn` | `codex-rs/tui/src/oss_selection.rs:166` | `pub fn handle_key_event(&mut self, key: KeyEvent) -> Option<String> {` |
| `pub_fn` | `codex-rs/tui/src/oss_selection.rs:230` | `pub fn is_complete(&self) -> bool {` |
| `pub_fn` | `codex-rs/tui/src/oss_selection.rs:234` | `pub fn desired_height(&self, width: u16) -> u16 {` |
| `pub_fn` | `codex-rs/tui/src/oss_selection.rs:297` | `pub async fn select_oss_provider(codex_home: &std::path::Path) -> io::Result<String> {` |
| `pub_enum` | `codex-rs/tui/src/public_widgets/composer_input.rs:19` | `pub enum ComposerAction {` |
| `pub_struct` | `codex-rs/tui/src/public_widgets/composer_input.rs:28` | `pub struct ComposerInput {` |
| `pub_fn` | `codex-rs/tui/src/public_widgets/composer_input.rs:36` | `pub fn new() -> Self {` |
| `pub_fn` | `codex-rs/tui/src/public_widgets/composer_input.rs:45` | `pub fn is_empty(&self) -> bool {` |
| `pub_fn` | `codex-rs/tui/src/public_widgets/composer_input.rs:50` | `pub fn clear(&mut self) {` |
| `pub_fn` | `codex-rs/tui/src/public_widgets/composer_input.rs:56` | `pub fn input(&mut self, key: KeyEvent) -> ComposerAction {` |
| `pub_fn` | `codex-rs/tui/src/public_widgets/composer_input.rs:65` | `pub fn handle_paste(&mut self, pasted: String) -> bool {` |
| `pub_fn` | `codex-rs/tui/src/public_widgets/composer_input.rs:73` | `pub fn set_hint_items(&mut self, items: Vec<(impl Into<String>, impl Into<String>)>) {` |
| `pub_fn` | `codex-rs/tui/src/public_widgets/composer_input.rs:82` | `pub fn clear_hint_items(&mut self) {` |
| `pub_fn` | `codex-rs/tui/src/public_widgets/composer_input.rs:87` | `pub fn desired_height(&self, width: u16) -> u16 {` |
| `pub_fn` | `codex-rs/tui/src/public_widgets/composer_input.rs:92` | `pub fn cursor_pos(&self, area: Rect) -> Option<(u16, u16)> {` |
| `pub_fn` | `codex-rs/tui/src/public_widgets/composer_input.rs:97` | `pub fn render_ref(&self, area: Rect, buf: &mut Buffer) {` |
| `pub_fn` | `codex-rs/tui/src/public_widgets/composer_input.rs:102` | `pub fn is_in_paste_burst(&self) -> bool {` |
| `pub_fn` | `codex-rs/tui/src/public_widgets/composer_input.rs:108` | `pub fn flush_paste_burst_if_due(&mut self) -> bool {` |
| `pub_fn` | `codex-rs/tui/src/public_widgets/composer_input.rs:116` | `pub fn recommended_flush_delay() -> Duration {` |
| `pub_mod` | `codex-rs/tui/src/public_widgets/mod.rs:1` | `pub mod composer_input;` |
| `pub_fn` | `codex-rs/tui/src/render/line_utils.rs:5` | `pub fn line_to_static(line: &Line<'_>) -> Line<'static> {` |
| `pub_fn` | `codex-rs/tui/src/render/line_utils.rs:29` | `pub fn is_blank_line_spaces_only(line: &Line<'_>) -> bool {` |
| `pub_fn` | `codex-rs/tui/src/render/line_utils.rs:40` | `pub fn prefix_lines(` |
| `pub_mod` | `codex-rs/tui/src/render/mod.rs:3` | `pub mod highlight;` |
| `pub_mod` | `codex-rs/tui/src/render/mod.rs:4` | `pub mod line_utils;` |
| `pub_mod` | `codex-rs/tui/src/render/mod.rs:5` | `pub mod renderable;` |
| `pub_struct` | `codex-rs/tui/src/render/mod.rs:8` | `pub struct Insets {` |
| `pub_fn` | `codex-rs/tui/src/render/mod.rs:16` | `pub fn tlbr(top: u16, left: u16, bottom: u16, right: u16) -> Self {` |
| `pub_fn` | `codex-rs/tui/src/render/mod.rs:25` | `pub fn vh(v: u16, h: u16) -> Self {` |
| `pub_trait` | `codex-rs/tui/src/render/mod.rs:35` | `pub trait RectExt {` |
| `pub_trait` | `codex-rs/tui/src/render/renderable.rs:13` | `pub trait Renderable {` |
| `pub_enum` | `codex-rs/tui/src/render/renderable.rs:21` | `pub enum RenderableItem<'a> {` |
| `pub_struct` | `codex-rs/tui/src/render/renderable.rs:141` | `pub struct ColumnRenderable<'a> {` |
| `pub_fn` | `codex-rs/tui/src/render/renderable.rs:186` | `pub fn new() -> Self {` |
| `pub_fn` | `codex-rs/tui/src/render/renderable.rs:200` | `pub fn push(&mut self, child: impl Into<Box<dyn Renderable + 'a>>) {` |
| `pub_struct` | `codex-rs/tui/src/render/renderable.rs:214` | `pub struct FlexChild<'a> {` |
| `pub_struct` | `codex-rs/tui/src/render/renderable.rs:219` | `pub struct FlexRenderable<'a> {` |
| `pub_fn` | `codex-rs/tui/src/render/renderable.rs:228` | `pub fn new() -> Self {` |
| `pub_fn` | `codex-rs/tui/src/render/renderable.rs:232` | `pub fn push(&mut self, flex: i32, child: impl Into<RenderableItem<'a>>) {` |
| `pub_struct` | `codex-rs/tui/src/render/renderable.rs:318` | `pub struct RowRenderable<'a> {` |
| `pub_fn` | `codex-rs/tui/src/render/renderable.rs:369` | `pub fn new() -> Self {` |
| `pub_fn` | `codex-rs/tui/src/render/renderable.rs:373` | `pub fn push(&mut self, width: u16, child: impl Into<Box<dyn Renderable>>) {` |
| `pub_struct` | `codex-rs/tui/src/render/renderable.rs:388` | `pub struct InsetRenderable<'a> {` |
| `pub_fn` | `codex-rs/tui/src/render/renderable.rs:409` | `pub fn new(child: impl Into<RenderableItem<'a>>, insets: Insets) -> Self {` |
| `pub_trait` | `codex-rs/tui/src/render/renderable.rs:417` | `pub trait RenderableExt<'a> {` |
| `pub_enum` | `codex-rs/tui/src/resume_picker.rs:46` | `pub enum SessionSelection {` |
| `pub_enum` | `codex-rs/tui/src/resume_picker.rs:54` | `pub enum SessionPickerAction {` |
| `pub_fn` | `codex-rs/tui/src/resume_picker.rs:105` | `pub async fn run_resume_picker(` |
| `pub_fn` | `codex-rs/tui/src/resume_picker.rs:121` | `pub async fn run_fork_picker(` |
| `pub_enum` | `codex-rs/tui/src/slash_command.rs:12` | `pub enum SlashCommand {` |
| `pub_fn` | `codex-rs/tui/src/slash_command.rs:50` | `pub fn description(self) -> &'static str {` |
| `pub_fn` | `codex-rs/tui/src/slash_command.rs:86` | `pub fn command(self) -> &'static str {` |
| `pub_fn` | `codex-rs/tui/src/slash_command.rs:91` | `pub fn supports_inline_args(self) -> bool {` |
| `pub_fn` | `codex-rs/tui/src/slash_command.rs:99` | `pub fn available_during_task(self) -> bool {` |
| `pub_fn` | `codex-rs/tui/src/slash_command.rs:143` | `pub fn built_in_slash_commands() -> Vec<(&'static str, SlashCommand)> {` |
| `pub_fn` | `codex-rs/tui/src/status_indicator_widget.rs:49` | `pub fn fmt_elapsed_compact(elapsed_secs: u64) -> String {` |
| `pub_fn` | `codex-rs/tui/src/status_indicator_widget.rs:156` | `pub fn elapsed_seconds(&self) -> u64 {` |
| `pub_fn` | `codex-rs/tui/src/style.rs:8` | `pub fn user_message_style() -> Style {` |
| `pub_fn` | `codex-rs/tui/src/style.rs:12` | `pub fn proposed_plan_style() -> Style {` |
| `pub_fn` | `codex-rs/tui/src/style.rs:17` | `pub fn user_message_style_for(terminal_bg: Option<(u8, u8, u8)>) -> Style {` |
| `pub_fn` | `codex-rs/tui/src/style.rs:24` | `pub fn proposed_plan_style_for(terminal_bg: Option<(u8, u8, u8)>) -> Style {` |
| `pub_fn` | `codex-rs/tui/src/style.rs:32` | `pub fn user_message_bg(terminal_bg: (u8, u8, u8)) -> Color {` |
| `pub_fn` | `codex-rs/tui/src/style.rs:42` | `pub fn proposed_plan_bg(terminal_bg: (u8, u8, u8)) -> Color {` |
| `pub_fn` | `codex-rs/tui/src/terminal_palette.rs:13` | `pub fn best_color(target: (u8, u8, u8)) -> Color {` |
| `pub_fn` | `codex-rs/tui/src/terminal_palette.rs:36` | `pub fn requery_default_colors() {` |
| `pub_struct` | `codex-rs/tui/src/terminal_palette.rs:42` | `pub struct DefaultColors {` |
| `pub_fn` | `codex-rs/tui/src/terminal_palette.rs:47` | `pub fn default_colors() -> Option<DefaultColors> {` |
| `pub_fn` | `codex-rs/tui/src/terminal_palette.rs:51` | `pub fn default_fg() -> Option<(u8, u8, u8)> {` |
| `pub_fn` | `codex-rs/tui/src/terminal_palette.rs:55` | `pub fn default_bg() -> Option<(u8, u8, u8)> {` |
| `pub_fn` | `codex-rs/tui/src/terminal_palette.rs:63` | `pub fn palette_version() -> u64 {` |
| `pub_const` | `codex-rs/tui/src/terminal_palette.rs:158` | `pub const XTERM_COLORS: [(u8, u8, u8); 256] = [` |
| `pub_struct` | `codex-rs/tui/src/test_backend.rs:21` | `pub struct VT100Backend {` |
| `pub_fn` | `codex-rs/tui/src/test_backend.rs:27` | `pub fn new(width: u16, height: u16) -> Self {` |
| `pub_fn` | `codex-rs/tui/src/test_backend.rs:34` | `pub fn vt100(&self) -> &vt100::Parser {` |
| `pub_type` | `codex-rs/tui/src/tui.rs:56` | `pub type Terminal = CustomTerminal<CrosstermBackend<Stdout>>;` |
| `pub_fn` | `codex-rs/tui/src/tui.rs:58` | `pub fn set_modes() -> Result<()> {` |
| `pub_fn` | `codex-rs/tui/src/tui.rs:137` | `pub fn restore() -> Result<()> {` |
| `pub_fn` | `codex-rs/tui/src/tui.rs:143` | `pub fn restore_keep_raw() -> Result<()> {` |
| `pub_enum` | `codex-rs/tui/src/tui.rs:149` | `pub enum RestoreMode {` |
| `pub_fn` | `codex-rs/tui/src/tui.rs:204` | `pub fn init() -> Result<Terminal> {` |
| `pub_enum` | `codex-rs/tui/src/tui.rs:229` | `pub enum TuiEvent {` |
| `pub_struct` | `codex-rs/tui/src/tui.rs:235` | `pub struct Tui {` |
| `pub_fn` | `codex-rs/tui/src/tui.rs:255` | `pub fn new(terminal: Terminal) -> Self {` |
| `pub_fn` | `codex-rs/tui/src/tui.rs:284` | `pub fn set_alt_screen_enabled(&mut self, enabled: bool) {` |
| `pub_fn` | `codex-rs/tui/src/tui.rs:288` | `pub fn set_notification_method(&mut self, method: NotificationMethod) {` |
| `pub_fn` | `codex-rs/tui/src/tui.rs:292` | `pub fn frame_requester(&self) -> FrameRequester {` |
| `pub_fn` | `codex-rs/tui/src/tui.rs:296` | `pub fn enhanced_keys_supported(&self) -> bool {` |
| `pub_fn` | `codex-rs/tui/src/tui.rs:300` | `pub fn is_alt_screen_active(&self) -> bool {` |
| `pub_fn` | `codex-rs/tui/src/tui.rs:305` | `pub fn pause_events(&mut self) {` |
| `pub_fn` | `codex-rs/tui/src/tui.rs:311` | `pub fn resume_events(&mut self) {` |
| `pub_fn` | `codex-rs/tui/src/tui.rs:356` | `pub fn notify(&mut self, message: impl AsRef<str>) -> bool {` |
| `pub_fn` | `codex-rs/tui/src/tui.rs:381` | `pub fn event_stream(&self) -> Pin<Box<dyn Stream<Item = TuiEvent> + Send + 'static>> {` |
| `pub_fn` | `codex-rs/tui/src/tui.rs:401` | `pub fn enter_alt_screen(&mut self) -> Result<()> {` |
| `pub_fn` | `codex-rs/tui/src/tui.rs:423` | `pub fn leave_alt_screen(&mut self) -> Result<()> {` |
| `pub_fn` | `codex-rs/tui/src/tui.rs:437` | `pub fn insert_history_lines(&mut self, lines: Vec<Line<'static>>) {` |
| `pub_fn` | `codex-rs/tui/src/tui.rs:442` | `pub fn draw(` |
| `pub_type` | `codex-rs/tui/src/tui/event_stream.rs:39` | `pub type EventResult = std::io::Result<Event>;` |
| `pub_trait` | `codex-rs/tui/src/tui/event_stream.rs:43` | `pub trait EventSource: Send + 'static {` |
| `pub_struct` | `codex-rs/tui/src/tui/event_stream.rs:51` | `pub struct EventBroker<S: EventSource = CrosstermEventSource> {` |
| `pub_fn` | `codex-rs/tui/src/tui/event_stream.rs:81` | `pub fn new() -> Self {` |
| `pub_fn` | `codex-rs/tui/src/tui/event_stream.rs:90` | `pub fn pause_events(&self) {` |
| `pub_fn` | `codex-rs/tui/src/tui/event_stream.rs:99` | `pub fn resume_events(&self) {` |
| `pub_fn` | `codex-rs/tui/src/tui/event_stream.rs:112` | `pub fn resume_events_rx(&self) -> watch::Receiver<()> {` |
| `pub_struct` | `codex-rs/tui/src/tui/event_stream.rs:118` | `pub struct CrosstermEventSource(pub crossterm::event::EventStream);` |
| `pub_struct` | `codex-rs/tui/src/tui/event_stream.rs:139` | `pub struct TuiEventStream<S: EventSource + Default + Unpin = CrosstermEventSource> {` |
| `pub_fn` | `codex-rs/tui/src/tui/event_stream.rs:152` | `pub fn new(` |
| `pub_fn` | `codex-rs/tui/src/tui/event_stream.rs:178` | `pub fn poll_crossterm_event(&mut self, cx: &mut Context<'_>) -> Poll<Option<TuiEvent>> {` |
| `pub_fn` | `codex-rs/tui/src/tui/event_stream.rs:225` | `pub fn poll_draw_event(&mut self, cx: &mut Context<'_>) -> Poll<Option<TuiEvent>> {` |
| `pub_struct` | `codex-rs/tui/src/tui/frame_requester.rs:31` | `pub struct FrameRequester {` |
| `pub_fn` | `codex-rs/tui/src/tui/frame_requester.rs:39` | `pub fn new(draw_tx: broadcast::Sender<()>) -> Self {` |
| `pub_fn` | `codex-rs/tui/src/tui/frame_requester.rs:49` | `pub fn schedule_frame(&self) {` |
| `pub_fn` | `codex-rs/tui/src/tui/frame_requester.rs:54` | `pub fn schedule_frame_in(&self, dur: Duration) {` |
| `pub_const` | `codex-rs/tui/src/tui/job_control.rs:25` | `pub const SUSPEND_KEY: key_hint::KeyBinding = key_hint::ctrl(KeyCode::Char('z'));` |
| `pub_struct` | `codex-rs/tui/src/tui/job_control.rs:43` | `pub struct SuspendContext {` |
| `pub_enum` | `codex-rs/tui/src/update_action.rs:3` | `pub enum UpdateAction {` |
| `pub_fn` | `codex-rs/tui/src/update_action.rs:14` | `pub fn command_args(self) -> (&'static str, &'static [&'static str]) {` |
| `pub_fn` | `codex-rs/tui/src/update_action.rs:23` | `pub fn command_str(self) -> String {` |
| `pub_fn` | `codex-rs/tui/src/updates.rs:17` | `pub fn get_upgrade_version(config: &Config) -> Option<String> {` |
| `pub_fn` | `codex-rs/tui/src/updates.rs:147` | `pub fn get_upgrade_version_for_popup(config: &Config) -> Option<String> {` |
| `pub_fn` | `codex-rs/tui/src/updates.rs:165` | `pub async fn dismiss_version(config: &Config, version: &str) -> anyhow::Result<()> {` |
| `pub_const` | `codex-rs/tui/src/version.rs:2` | `pub const CODEX_CLI_VERSION: &str = env!("CARGO_PKG_VERSION");` |
| `pub_struct` | `codex-rs/tui/src/wrapping.rs:52` | `pub struct RtOptions<'a> {` |
| `pub_fn` | `codex-rs/tui/src/wrapping.rs:86` | `pub fn new(width: usize) -> Self {` |
| `pub_fn` | `codex-rs/tui/src/wrapping.rs:99` | `pub fn line_ending(self, line_ending: textwrap::LineEnding) -> Self {` |
| `pub_fn` | `codex-rs/tui/src/wrapping.rs:106` | `pub fn width(self, width: usize) -> Self {` |
| `pub_fn` | `codex-rs/tui/src/wrapping.rs:110` | `pub fn initial_indent(self, initial_indent: Line<'a>) -> Self {` |
| `pub_fn` | `codex-rs/tui/src/wrapping.rs:117` | `pub fn subsequent_indent(self, subsequent_indent: Line<'a>) -> Self {` |
| `pub_fn` | `codex-rs/tui/src/wrapping.rs:124` | `pub fn break_words(self, break_words: bool) -> Self {` |
| `pub_fn` | `codex-rs/tui/src/wrapping.rs:131` | `pub fn word_separator(self, word_separator: textwrap::WordSeparator) -> RtOptions<'a> {` |
| `pub_fn` | `codex-rs/tui/src/wrapping.rs:138` | `pub fn wrap_algorithm(self, wrap_algorithm: textwrap::WrapAlgorithm) -> RtOptions<'a> {` |
| `pub_fn` | `codex-rs/tui/src/wrapping.rs:145` | `pub fn word_splitter(self, word_splitter: textwrap::WordSplitter) -> RtOptions<'a> {` |
| `pub_struct` | `codex-rs/utils/absolute-path/src/lib.rs:22` | `pub struct AbsolutePathBuf(PathBuf);` |
| `pub_fn` | `codex-rs/utils/absolute-path/src/lib.rs:61` | `pub fn current_dir() -> std::io::Result<Self> {` |
| `pub_fn` | `codex-rs/utils/absolute-path/src/lib.rs:70` | `pub fn parent(&self) -> Option<Self> {` |
| `pub_fn` | `codex-rs/utils/absolute-path/src/lib.rs:77` | `pub fn as_path(&self) -> &Path {` |
| `pub_fn` | `codex-rs/utils/absolute-path/src/lib.rs:81` | `pub fn into_path_buf(self) -> PathBuf {` |
| `pub_fn` | `codex-rs/utils/absolute-path/src/lib.rs:85` | `pub fn to_path_buf(&self) -> PathBuf {` |
| `pub_fn` | `codex-rs/utils/absolute-path/src/lib.rs:89` | `pub fn to_string_lossy(&self) -> std::borrow::Cow<'_, str> {` |
| `pub_fn` | `codex-rs/utils/absolute-path/src/lib.rs:93` | `pub fn display(&self) -> Display<'_> {` |
| `pub_struct` | `codex-rs/utils/absolute-path/src/lib.rs:150` | `pub struct AbsolutePathBufGuard;` |
| `pub_fn` | `codex-rs/utils/absolute-path/src/lib.rs:153` | `pub fn new(base_path: &Path) -> Self {` |
| `pub_struct` | `codex-rs/utils/cache/src/lib.rs:13` | `pub struct BlockingLruCache<K, V> {` |
| `pub_fn` | `codex-rs/utils/cache/src/lib.rs:23` | `pub fn new(capacity: NonZeroUsize) -> Self {` |
| `pub_fn` | `codex-rs/utils/cache/src/lib.rs:30` | `pub fn get_or_insert_with(&self, key: K, value: impl FnOnce() -> V) -> V` |
| `pub_fn` | `codex-rs/utils/cache/src/lib.rs:68` | `pub fn try_with_capacity(capacity: usize) -> Option<Self> {` |
| `pub_fn` | `codex-rs/utils/cache/src/lib.rs:84` | `pub fn insert(&self, key: K, value: V) -> Option<V> {` |
| `pub_fn` | `codex-rs/utils/cache/src/lib.rs:100` | `pub fn clear(&self) {` |
| `pub_fn` | `codex-rs/utils/cache/src/lib.rs:117` | `pub fn blocking_lock(&self) -> Option<MutexGuard<'_, LruCache<K, V>>> {` |
| `pub_fn` | `codex-rs/utils/cache/src/lib.rs:135` | `pub fn sha1_digest(bytes: &[u8]) -> [u8; 20] {` |
| `pub_enum` | `codex-rs/utils/cargo-bin/src/lib.rs:12` | `pub enum CargoBinError {` |
| `pub_fn` | `codex-rs/utils/cargo-bin/src/lib.rs:39` | `pub fn cargo_bin(name: &str) -> Result<PathBuf, CargoBinError> {` |
| `pub_fn` | `codex-rs/utils/cargo-bin/src/lib.rs:84` | `pub fn runfiles_available() -> bool {` |
| `pub_fn` | `codex-rs/utils/cargo-bin/src/lib.rs:135` | `pub fn resolve_bazel_runfile(` |
| `pub_fn` | `codex-rs/utils/cargo-bin/src/lib.rs:163` | `pub fn resolve_cargo_runfile(resource: &Path) -> std::io::Result<PathBuf> {` |
| `pub_fn` | `codex-rs/utils/cargo-bin/src/lib.rs:168` | `pub fn repo_root() -> io::Result<PathBuf> {` |
| `pub_struct` | `codex-rs/utils/git/src/apply.rs:18` | `pub struct ApplyGitRequest {` |
| `pub_struct` | `codex-rs/utils/git/src/apply.rs:27` | `pub struct ApplyGitResult {` |
| `pub_fn` | `codex-rs/utils/git/src/apply.rs:41` | `pub fn apply_git_patch(req: &ApplyGitRequest) -> io::Result<ApplyGitResult> {` |
| `pub_fn` | `codex-rs/utils/git/src/apply.rs:194` | `pub fn extract_paths_from_patch(diff_text: &str) -> Vec<String> {` |
| `pub_fn` | `codex-rs/utils/git/src/apply.rs:320` | `pub fn stage_paths(git_root: &Path, diff: &str) -> io::Result<()> {` |
| `pub_fn` | `codex-rs/utils/git/src/apply.rs:347` | `pub fn parse_git_apply_output(` |
| `pub_fn` | `codex-rs/utils/git/src/branch.rs:15` | `pub fn merge_base_with_head(` |
| `pub_enum` | `codex-rs/utils/git/src/errors.rs:10` | `pub enum GitToolingError {` |
| `pub_struct` | `codex-rs/utils/git/src/ghost_commits.rs:51` | `pub struct CreateGhostCommitOptions<'a> {` |
| `pub_struct` | `codex-rs/utils/git/src/ghost_commits.rs:59` | `pub struct RestoreGhostCommitOptions<'a> {` |
| `pub_struct` | `codex-rs/utils/git/src/ghost_commits.rs:65` | `pub struct GhostSnapshotConfig {` |
| `pub_struct` | `codex-rs/utils/git/src/ghost_commits.rs:83` | `pub struct GhostSnapshotReport {` |
| `pub_struct` | `codex-rs/utils/git/src/ghost_commits.rs:90` | `pub struct LargeUntrackedDir {` |
| `pub_struct` | `codex-rs/utils/git/src/ghost_commits.rs:97` | `pub struct IgnoredUntrackedFile {` |
| `pub_fn` | `codex-rs/utils/git/src/ghost_commits.rs:104` | `pub fn new(repo_path: &'a Path) -> Self {` |
| `pub_fn` | `codex-rs/utils/git/src/ghost_commits.rs:114` | `pub fn message(mut self, message: &'a str) -> Self {` |
| `pub_fn` | `codex-rs/utils/git/src/ghost_commits.rs:119` | `pub fn ghost_snapshot(mut self, ghost_snapshot: GhostSnapshotConfig) -> Self {` |
| `pub_fn` | `codex-rs/utils/git/src/ghost_commits.rs:128` | `pub fn ignore_large_untracked_files(mut self, bytes: i64) -> Self {` |
| `pub_fn` | `codex-rs/utils/git/src/ghost_commits.rs:158` | `pub fn new(repo_path: &'a Path) -> Self {` |
| `pub_fn` | `codex-rs/utils/git/src/ghost_commits.rs:165` | `pub fn ghost_snapshot(mut self, ghost_snapshot: GhostSnapshotConfig) -> Self {` |
| `pub_fn` | `codex-rs/utils/git/src/ghost_commits.rs:173` | `pub fn ignore_large_untracked_files(mut self, bytes: i64) -> Self {` |
| `pub_fn` | `codex-rs/utils/git/src/ghost_commits.rs:183` | `pub fn ignore_large_untracked_dirs(mut self, file_count: i64) -> Self {` |
| `pub_fn` | `codex-rs/utils/git/src/ghost_commits.rs:255` | `pub fn create_ghost_commit(` |
| `pub_fn` | `codex-rs/utils/git/src/ghost_commits.rs:262` | `pub fn capture_ghost_snapshot_report(` |
| `pub_fn` | `codex-rs/utils/git/src/ghost_commits.rs:302` | `pub fn create_ghost_commit_with_report(` |
| `pub_fn` | `codex-rs/utils/git/src/ghost_commits.rs:427` | `pub fn restore_ghost_commit(repo_path: &Path, commit: &GhostCommit) -> Result<(), GitToolingError> {` |
| `pub_fn` | `codex-rs/utils/git/src/ghost_commits.rs:432` | `pub fn restore_ghost_commit_with_options(` |
| `pub_fn` | `codex-rs/utils/git/src/ghost_commits.rs:457` | `pub fn restore_to_commit(repo_path: &Path, commit_id: &str) -> Result<(), GitToolingError> {` |
| `pub_struct` | `codex-rs/utils/git/src/lib.rs:41` | `pub struct GhostCommit {` |
| `pub_fn` | `codex-rs/utils/git/src/lib.rs:50` | `pub fn new(` |
| `pub_fn` | `codex-rs/utils/git/src/lib.rs:65` | `pub fn id(&self) -> &str {` |
| `pub_fn` | `codex-rs/utils/git/src/lib.rs:70` | `pub fn parent(&self) -> Option<&str> {` |
| `pub_fn` | `codex-rs/utils/git/src/lib.rs:75` | `pub fn preexisting_untracked_files(&self) -> &[PathBuf] {` |
| `pub_fn` | `codex-rs/utils/git/src/lib.rs:80` | `pub fn preexisting_untracked_dirs(&self) -> &[PathBuf] {` |
| `pub_fn` | `codex-rs/utils/git/src/platform.rs:6` | `pub fn create_symlink(` |
| `pub_fn` | `codex-rs/utils/git/src/platform.rs:18` | `pub fn create_symlink(` |
| `pub_fn` | `codex-rs/utils/home-dir/src/lib.rs:12` | `pub fn find_codex_home() -> std::io::Result<PathBuf> {` |
| `pub_enum` | `codex-rs/utils/image/src/error.rs:7` | `pub enum ImageProcessingError {` |
| `pub_fn` | `codex-rs/utils/image/src/error.rs:29` | `pub fn is_invalid_image(&self) -> bool {` |
| `pub_const` | `codex-rs/utils/image/src/lib.rs:19` | `pub const MAX_WIDTH: u32 = 2048;` |
| `pub_const` | `codex-rs/utils/image/src/lib.rs:21` | `pub const MAX_HEIGHT: u32 = 768;` |
| `pub_mod` | `codex-rs/utils/image/src/lib.rs:23` | `pub mod error;` |
| `pub_struct` | `codex-rs/utils/image/src/lib.rs:26` | `pub struct EncodedImage {` |
| `pub_fn` | `codex-rs/utils/image/src/lib.rs:34` | `pub fn into_data_url(self) -> String {` |
| `pub_fn` | `codex-rs/utils/image/src/lib.rs:43` | `pub fn load_and_resize_to_fit(path: &Path) -> Result<EncodedImage, ImageProcessingError> {` |
| `pub_fn` | `codex-rs/utils/json-to-toml/src/lib.rs:5` | `pub fn json_to_toml(v: JsonValue) -> TomlValue {` |
| `pub_mod` | `codex-rs/utils/pty/src/lib.rs:1` | `pub mod pipe;` |
| `pub_mod` | `codex-rs/utils/pty/src/lib.rs:3` | `pub mod process_group;` |
| `pub_mod` | `codex-rs/utils/pty/src/lib.rs:4` | `pub mod pty;` |
| `pub_type` | `codex-rs/utils/pty/src/lib.rs:19` | `pub type ExecCommandSession = ProcessHandle;` |
| `pub_type` | `codex-rs/utils/pty/src/lib.rs:21` | `pub type SpawnedPty = SpawnedProcess;` |
| `pub_fn` | `codex-rs/utils/pty/src/pipe.rs:249` | `pub async fn spawn_process(` |
| `pub_fn` | `codex-rs/utils/pty/src/pipe.rs:260` | `pub async fn spawn_process_no_stdin(` |
| `pub_struct` | `codex-rs/utils/pty/src/process.rs:19` | `pub struct PtyHandles {` |
| `pub_struct` | `codex-rs/utils/pty/src/process.rs:31` | `pub struct ProcessHandle {` |
| `pub_fn` | `codex-rs/utils/pty/src/process.rs:85` | `pub fn writer_sender(&self) -> mpsc::Sender<Vec<u8>> {` |
| `pub_fn` | `codex-rs/utils/pty/src/process.rs:90` | `pub fn output_receiver(&self) -> broadcast::Receiver<Vec<u8>> {` |
| `pub_fn` | `codex-rs/utils/pty/src/process.rs:95` | `pub fn has_exited(&self) -> bool {` |
| `pub_fn` | `codex-rs/utils/pty/src/process.rs:100` | `pub fn exit_code(&self) -> Option<i32> {` |
| `pub_fn` | `codex-rs/utils/pty/src/process.rs:105` | `pub fn terminate(&self) {` |
| `pub_struct` | `codex-rs/utils/pty/src/process.rs:143` | `pub struct SpawnedProcess {` |
| `pub_fn` | `codex-rs/utils/pty/src/process_group.rs:27` | `pub fn set_parent_death_signal(parent_pid: libc::pid_t) -> io::Result<()> {` |
| `pub_fn` | `codex-rs/utils/pty/src/process_group.rs:43` | `pub fn set_parent_death_signal(_parent_pid: i32) -> io::Result<()> {` |
| `pub_fn` | `codex-rs/utils/pty/src/process_group.rs:49` | `pub fn detach_from_tty() -> io::Result<()> {` |
| `pub_fn` | `codex-rs/utils/pty/src/process_group.rs:63` | `pub fn detach_from_tty() -> io::Result<()> {` |
| `pub_fn` | `codex-rs/utils/pty/src/process_group.rs:71` | `pub fn set_process_group() -> io::Result<()> {` |
| `pub_fn` | `codex-rs/utils/pty/src/process_group.rs:82` | `pub fn set_process_group() -> io::Result<()> {` |
| `pub_fn` | `codex-rs/utils/pty/src/process_group.rs:90` | `pub fn kill_process_group_by_pid(pid: u32) -> io::Result<()> {` |
| `pub_fn` | `codex-rs/utils/pty/src/process_group.rs:116` | `pub fn kill_process_group_by_pid(_pid: u32) -> io::Result<()> {` |
| `pub_fn` | `codex-rs/utils/pty/src/process_group.rs:122` | `pub fn kill_process_group(process_group_id: u32) -> io::Result<()> {` |
| `pub_fn` | `codex-rs/utils/pty/src/process_group.rs:139` | `pub fn kill_process_group(_process_group_id: u32) -> io::Result<()> {` |
| `pub_fn` | `codex-rs/utils/pty/src/process_group.rs:145` | `pub fn kill_child_process_group(child: &mut Child) -> io::Result<()> {` |
| `pub_fn` | `codex-rs/utils/pty/src/process_group.rs:155` | `pub fn kill_child_process_group(_child: &mut Child) -> io::Result<()> {` |
| `pub_fn` | `codex-rs/utils/pty/src/pty.rs:26` | `pub fn conpty_supported() -> bool {` |
| `pub_fn` | `codex-rs/utils/pty/src/pty.rs:32` | `pub fn conpty_supported() -> bool {` |
| `pub_fn` | `codex-rs/utils/pty/src/pty.rs:59` | `pub async fn spawn_process(` |
| `pub_struct` | `codex-rs/utils/pty/src/win/conpty.rs:37` | `pub struct ConPtySystem {}` |
| `pub_fn` | `codex-rs/utils/pty/src/win/conpty.rs:81` | `pub fn resize(` |
| `pub_struct` | `codex-rs/utils/pty/src/win/conpty.rs:103` | `pub struct ConPtyMasterPty {` |
| `pub_struct` | `codex-rs/utils/pty/src/win/conpty.rs:107` | `pub struct ConPtySlavePty {` |
| `pub_mod` | `codex-rs/utils/pty/src/win/mod.rs:39` | `pub mod conpty;` |
| `pub_struct` | `codex-rs/utils/pty/src/win/mod.rs:47` | `pub struct WinChild {` |
| `pub_struct` | `codex-rs/utils/pty/src/win/mod.rs:92` | `pub struct WinChildKiller {` |
| `pub_struct` | `codex-rs/utils/pty/src/win/procthreadattr.rs:32` | `pub struct ProcThreadAttributeList {` |
| `pub_fn` | `codex-rs/utils/pty/src/win/procthreadattr.rs:37` | `pub fn with_capacity(num_attributes: DWORD) -> Result<Self, Error> {` |
| `pub_fn` | `codex-rs/utils/pty/src/win/procthreadattr.rs:62` | `pub fn as_mut_ptr(&mut self) -> LPPROC_THREAD_ATTRIBUTE_LIST {` |
| `pub_fn` | `codex-rs/utils/pty/src/win/procthreadattr.rs:66` | `pub fn set_pty(&mut self, con: HPCON) -> Result<(), Error> {` |
| `pub_type` | `codex-rs/utils/pty/src/win/psuedocon.rs:59` | `pub type HPCON = HANDLE;` |
| `pub_const` | `codex-rs/utils/pty/src/win/psuedocon.rs:61` | `pub const PSEUDOCONSOLE_RESIZE_QUIRK: DWORD = 0x2;` |
| `pub_const` | `codex-rs/utils/pty/src/win/psuedocon.rs:63` | `pub const PSEUDOCONSOLE_PASSTHROUGH_MODE: DWORD = 0x8;` |
| `pub_fn` | `codex-rs/utils/pty/src/win/psuedocon.rs:70` | `pub fn CreatePseudoConsole(` |
| `pub_fn` | `codex-rs/utils/pty/src/win/psuedocon.rs:77` | `pub fn ResizePseudoConsole(hpc: HPCON, size: COORD) -> HRESULT,` |
| `pub_fn` | `codex-rs/utils/pty/src/win/psuedocon.rs:78` | `pub fn ClosePseudoConsole(hpc: HPCON),` |
| `pub_fn` | `codex-rs/utils/pty/src/win/psuedocon.rs:82` | `pub fn RtlGetVersion(` |
| `pub_fn` | `codex-rs/utils/pty/src/win/psuedocon.rs:103` | `pub fn conpty_supported() -> bool {` |
| `pub_struct` | `codex-rs/utils/pty/src/win/psuedocon.rs:119` | `pub struct PsuedoCon {` |
| `pub_fn` | `codex-rs/utils/pty/src/win/psuedocon.rs:133` | `pub fn new(size: COORD, input: FileDescriptor, output: FileDescriptor) -> Result<Self, Error> {` |
| `pub_fn` | `codex-rs/utils/pty/src/win/psuedocon.rs:151` | `pub fn resize(&self, size: COORD) -> Result<(), Error> {` |
| `pub_fn` | `codex-rs/utils/pty/src/win/psuedocon.rs:163` | `pub fn spawn_command(&self, cmd: CommandBuilder) -> anyhow::Result<WinChild> {` |
| `pub_struct` | `codex-rs/utils/readiness/src/lib.rs:16` | `pub struct Token(i32);` |
| `pub_trait` | `codex-rs/utils/readiness/src/lib.rs:21` | `pub trait Readiness: Send + Sync + 'static {` |
| `pub_struct` | `codex-rs/utils/readiness/src/lib.rs:43` | `pub struct ReadinessFlag {` |
| `pub_fn` | `codex-rs/utils/readiness/src/lib.rs:56` | `pub fn new() -> Self {` |
| `pub_enum` | `codex-rs/utils/readiness/src/lib.rs:190` | `pub enum ReadinessError {` |
| `pub_fn` | `codex-rs/utils/string/src/lib.rs:3` | `pub fn take_bytes_at_char_boundary(s: &str, maxb: usize) -> &str {` |
| `pub_fn` | `codex-rs/utils/string/src/lib.rs:20` | `pub fn take_last_bytes_at_char_boundary(s: &str, maxb: usize) -> &str {` |
| `fn_main` | `codex-rs/windows-sandbox-rs/build.rs:1` | `fn main() {` |
| `pub_fn` | `codex-rs/windows-sandbox-rs/src/acl.rs:160` | `pub fn path_mask_allows(` |
| `pub_struct` | `codex-rs/windows-sandbox-rs/src/allow.rs:9` | `pub struct AllowDenyPaths {` |
| `pub_fn` | `codex-rs/windows-sandbox-rs/src/allow.rs:14` | `pub fn compute_allow_paths(` |
| `pub_fn` | `codex-rs/windows-sandbox-rs/src/audit.rs:91` | `pub fn audit_everyone_writable(` |
| `pub_fn` | `codex-rs/windows-sandbox-rs/src/audit.rs:217` | `pub fn apply_world_writable_scan_and_denies(` |
| `pub_fn` | `codex-rs/windows-sandbox-rs/src/audit.rs:243` | `pub fn apply_capability_denies_for_world_writable(` |
| `fn_main` | `codex-rs/windows-sandbox-rs/src/bin/command_runner.rs:5` | `fn main() -> anyhow::Result<()> {` |
| `fn_main` | `codex-rs/windows-sandbox-rs/src/bin/command_runner.rs:10` | `fn main() {` |
| `fn_main` | `codex-rs/windows-sandbox-rs/src/bin/setup_main.rs:5` | `fn main() -> anyhow::Result<()> {` |
| `fn_main` | `codex-rs/windows-sandbox-rs/src/bin/setup_main.rs:10` | `fn main() {` |
| `pub_struct` | `codex-rs/windows-sandbox-rs/src/cap.rs:13` | `pub struct CapSids {` |
| `pub_fn` | `codex-rs/windows-sandbox-rs/src/cap.rs:18` | `pub fn cap_sid_file(codex_home: &Path) -> PathBuf {` |
| `pub_fn` | `codex-rs/windows-sandbox-rs/src/cap.rs:41` | `pub fn load_or_create_cap_sids(codex_home: &Path) -> Result<CapSids> {` |
| `pub_fn` | `codex-rs/windows-sandbox-rs/src/command_runner_win.rs:89` | `pub fn main() -> Result<()> {` |
| `pub_fn` | `codex-rs/windows-sandbox-rs/src/cwd_junction.rs:26` | `pub fn create_cwd_junction(requested_cwd: &Path, log_dir: Option<&Path>) -> Option<PathBuf> {` |
| `pub_fn` | `codex-rs/windows-sandbox-rs/src/dpapi.rs:20` | `pub fn protect(data: &[u8]) -> Result<Vec<u8>> {` |
| `pub_fn` | `codex-rs/windows-sandbox-rs/src/dpapi.rs:54` | `pub fn unprotect(blob: &[u8]) -> Result<Vec<u8>> {` |
| `pub_fn` | `codex-rs/windows-sandbox-rs/src/elevated_impl.rs:211` | `pub fn run_windows_sandbox_capture(` |
| `pub_struct` | `codex-rs/windows-sandbox-rs/src/elevated_impl.rs:504` | `pub struct CaptureResult {` |
| `pub_fn` | `codex-rs/windows-sandbox-rs/src/elevated_impl.rs:512` | `pub fn run_windows_sandbox_capture(` |
| `pub_fn` | `codex-rs/windows-sandbox-rs/src/env.rs:9` | `pub fn normalize_null_device_env(env_map: &mut HashMap<String, String>) {` |
| `pub_fn` | `codex-rs/windows-sandbox-rs/src/env.rs:21` | `pub fn ensure_non_interactive_pager(env_map: &mut HashMap<String, String>) {` |
| `pub_fn` | `codex-rs/windows-sandbox-rs/src/env.rs:32` | `pub fn inherit_path_env(env_map: &mut HashMap<String, String>) {` |
| `pub_fn` | `codex-rs/windows-sandbox-rs/src/env.rs:123` | `pub fn apply_no_network_to_env(env_map: &mut HashMap<String, String>) -> Result<()> {` |
| `pub_fn` | `codex-rs/windows-sandbox-rs/src/firewall.rs:34` | `pub fn ensure_offline_outbound_block(offline_sid: &str, log: &mut File) -> Result<()> {` |
| `pub_fn` | `codex-rs/windows-sandbox-rs/src/hide_users.rs:28` | `pub fn hide_newly_created_users(usernames: &[String], log_base: &Path) {` |
| `pub_fn` | `codex-rs/windows-sandbox-rs/src/hide_users.rs:45` | `pub fn hide_current_user_profile_dir(log_base: &Path) {` |
| `pub_struct` | `codex-rs/windows-sandbox-rs/src/identity.rs:28` | `pub struct SandboxCreds {` |
| `pub_fn` | `codex-rs/windows-sandbox-rs/src/identity.rs:37` | `pub fn sandbox_setup_is_complete(codex_home: &Path) -> bool {` |
| `pub_fn` | `codex-rs/windows-sandbox-rs/src/identity.rs:125` | `pub fn require_logon_sandbox_creds(` |
| `pub_struct` | `codex-rs/windows-sandbox-rs/src/lib.rs:194` | `pub struct CaptureResult {` |
| `pub_fn` | `codex-rs/windows-sandbox-rs/src/lib.rs:201` | `pub fn run_windows_sandbox_capture(` |
| `pub_struct` | `codex-rs/windows-sandbox-rs/src/lib.rs:495` | `pub struct CaptureResult {` |
| `pub_fn` | `codex-rs/windows-sandbox-rs/src/lib.rs:502` | `pub fn run_windows_sandbox_capture(` |
| `pub_fn` | `codex-rs/windows-sandbox-rs/src/lib.rs:514` | `pub fn apply_world_writable_scan_and_denies(` |
| `pub_const` | `codex-rs/windows-sandbox-rs/src/logging.rs:10` | `pub const LOG_FILE_NAME: &str = "sandbox.log";` |
| `pub_fn` | `codex-rs/windows-sandbox-rs/src/logging.rs:49` | `pub fn log_start(command: &[String], base_dir: Option<&Path>) {` |
| `pub_fn` | `codex-rs/windows-sandbox-rs/src/logging.rs:54` | `pub fn log_success(command: &[String], base_dir: Option<&Path>) {` |
| `pub_fn` | `codex-rs/windows-sandbox-rs/src/logging.rs:59` | `pub fn log_failure(command: &[String], detail: &str, base_dir: Option<&Path>) {` |
| `pub_fn` | `codex-rs/windows-sandbox-rs/src/logging.rs:65` | `pub fn debug_log(msg: &str, base_dir: Option<&Path>) {` |
| `pub_fn` | `codex-rs/windows-sandbox-rs/src/logging.rs:73` | `pub fn log_note(msg: &str, base_dir: Option<&Path>) {` |
| `pub_fn` | `codex-rs/windows-sandbox-rs/src/policy.rs:4` | `pub fn parse_policy(value: &str) -> Result<SandboxPolicy> {` |
| `pub_fn` | `codex-rs/windows-sandbox-rs/src/process.rs:25` | `pub fn make_env_block(env: &HashMap<String, String>) -> Vec<u16> {` |
| `pub_struct` | `codex-rs/windows-sandbox-rs/src/read_acl_mutex.rs:17` | `pub struct ReadAclMutexGuard {` |
| `pub_fn` | `codex-rs/windows-sandbox-rs/src/read_acl_mutex.rs:30` | `pub fn read_acl_mutex_exists() -> Result<bool> {` |
| `pub_fn` | `codex-rs/windows-sandbox-rs/src/read_acl_mutex.rs:46` | `pub fn acquire_read_acl_mutex() -> Result<Option<ReadAclMutexGuard>> {` |
| `pub_const` | `codex-rs/windows-sandbox-rs/src/sandbox_users.rs:46` | `pub const SANDBOX_USERS_GROUP: &str = "CodexSandboxUsers";` |
| `pub_fn` | `codex-rs/windows-sandbox-rs/src/sandbox_users.rs:54` | `pub fn ensure_sandbox_users_group(log: &mut File) -> Result<()> {` |
| `pub_fn` | `codex-rs/windows-sandbox-rs/src/sandbox_users.rs:58` | `pub fn resolve_sandbox_users_group_sid() -> Result<Vec<u8>> {` |
| `pub_fn` | `codex-rs/windows-sandbox-rs/src/sandbox_users.rs:62` | `pub fn provision_sandbox_users(` |
| `pub_fn` | `codex-rs/windows-sandbox-rs/src/sandbox_users.rs:87` | `pub fn ensure_sandbox_user(username: &str, password: &str, log: &mut File) -> Result<()> {` |
| `pub_fn` | `codex-rs/windows-sandbox-rs/src/sandbox_users.rs:93` | `pub fn ensure_local_user(name: &str, password: &str, log: &mut File) -> Result<()> {` |
| `pub_fn` | `codex-rs/windows-sandbox-rs/src/sandbox_users.rs:157` | `pub fn ensure_local_group(name: &str, comment: &str, log: &mut File) -> Result<()> {` |
| `pub_fn` | `codex-rs/windows-sandbox-rs/src/sandbox_users.rs:189` | `pub fn ensure_local_group_member(group_name: &str, member_name: &str) -> Result<()> {` |
| `pub_fn` | `codex-rs/windows-sandbox-rs/src/sandbox_users.rs:209` | `pub fn resolve_sid(name: &str) -> Result<Vec<u8>> {` |
| `pub_fn` | `codex-rs/windows-sandbox-rs/src/sandbox_users.rs:345` | `pub fn sid_bytes_to_psid(sid: &[u8]) -> Result<*mut c_void> {` |
| `pub_enum` | `codex-rs/windows-sandbox-rs/src/setup_error.rs:15` | `pub enum SetupErrorCode {` |
| `pub_fn` | `codex-rs/windows-sandbox-rs/src/setup_error.rs:71` | `pub fn as_str(self) -> &'static str {` |
| `pub_struct` | `codex-rs/windows-sandbox-rs/src/setup_error.rs:105` | `pub struct SetupErrorReport {` |
| `pub_struct` | `codex-rs/windows-sandbox-rs/src/setup_error.rs:111` | `pub struct SetupFailure {` |
| `pub_fn` | `codex-rs/windows-sandbox-rs/src/setup_error.rs:117` | `pub fn new(code: SetupErrorCode, message: impl Into<String>) -> Self {` |
| `pub_fn` | `codex-rs/windows-sandbox-rs/src/setup_error.rs:124` | `pub fn from_report(report: SetupErrorReport) -> Self {` |
| `pub_fn` | `codex-rs/windows-sandbox-rs/src/setup_error.rs:128` | `pub fn metric_message(&self) -> String {` |
| `pub_fn` | `codex-rs/windows-sandbox-rs/src/setup_error.rs:141` | `pub fn failure(code: SetupErrorCode, message: impl Into<String>) -> anyhow::Error {` |
| `pub_fn` | `codex-rs/windows-sandbox-rs/src/setup_error.rs:145` | `pub fn extract_failure(err: &anyhow::Error) -> Option<&SetupFailure> {` |
| `pub_fn` | `codex-rs/windows-sandbox-rs/src/setup_error.rs:149` | `pub fn setup_error_path(codex_home: &Path) -> PathBuf {` |
| `pub_fn` | `codex-rs/windows-sandbox-rs/src/setup_error.rs:153` | `pub fn clear_setup_error_report(codex_home: &Path) -> Result<()> {` |
| `pub_fn` | `codex-rs/windows-sandbox-rs/src/setup_error.rs:162` | `pub fn write_setup_error_report(codex_home: &Path, report: &SetupErrorReport) -> Result<()> {` |
| `pub_fn` | `codex-rs/windows-sandbox-rs/src/setup_error.rs:172` | `pub fn read_setup_error_report(codex_home: &Path) -> Result<Option<SetupErrorReport>> {` |
| `pub_fn` | `codex-rs/windows-sandbox-rs/src/setup_error.rs:186` | `pub fn sanitize_tag_value(value: &str) -> String {` |
| `pub_fn` | `codex-rs/windows-sandbox-rs/src/setup_main_win.rs:338` | `pub fn main() -> Result<()> {` |
| `pub_const` | `codex-rs/windows-sandbox-rs/src/setup_orchestrator.rs:34` | `pub const SETUP_VERSION: u32 = 5;` |
| `pub_const` | `codex-rs/windows-sandbox-rs/src/setup_orchestrator.rs:35` | `pub const OFFLINE_USERNAME: &str = "CodexSandboxOffline";` |
| `pub_const` | `codex-rs/windows-sandbox-rs/src/setup_orchestrator.rs:36` | `pub const ONLINE_USERNAME: &str = "CodexSandboxOnline";` |
| `pub_fn` | `codex-rs/windows-sandbox-rs/src/setup_orchestrator.rs:41` | `pub fn sandbox_dir(codex_home: &Path) -> PathBuf {` |
| `pub_fn` | `codex-rs/windows-sandbox-rs/src/setup_orchestrator.rs:45` | `pub fn sandbox_secrets_dir(codex_home: &Path) -> PathBuf {` |
| `pub_fn` | `codex-rs/windows-sandbox-rs/src/setup_orchestrator.rs:49` | `pub fn setup_marker_path(codex_home: &Path) -> PathBuf {` |
| `pub_fn` | `codex-rs/windows-sandbox-rs/src/setup_orchestrator.rs:53` | `pub fn sandbox_users_path(codex_home: &Path) -> PathBuf {` |
| `pub_fn` | `codex-rs/windows-sandbox-rs/src/setup_orchestrator.rs:57` | `pub fn run_setup_refresh(` |
| `pub_struct` | `codex-rs/windows-sandbox-rs/src/setup_orchestrator.rs:127` | `pub struct SetupMarker {` |
| `pub_fn` | `codex-rs/windows-sandbox-rs/src/setup_orchestrator.rs:136` | `pub fn version_matches(&self) -> bool {` |
| `pub_struct` | `codex-rs/windows-sandbox-rs/src/setup_orchestrator.rs:142` | `pub struct SandboxUserRecord {` |
| `pub_struct` | `codex-rs/windows-sandbox-rs/src/setup_orchestrator.rs:149` | `pub struct SandboxUsersFile {` |
| `pub_fn` | `codex-rs/windows-sandbox-rs/src/setup_orchestrator.rs:156` | `pub fn version_matches(&self) -> bool {` |
| `pub_fn` | `codex-rs/windows-sandbox-rs/src/setup_orchestrator.rs:447` | `pub fn run_elevated_setup(` |
| `pub_fn` | `codex-rs/windows-sandbox-rs/src/winutil.rs:21` | `pub fn quote_windows_arg(arg: &str) -> String {` |
| `pub_fn` | `codex-rs/windows-sandbox-rs/src/winutil.rs:60` | `pub fn format_last_error(err: i32) -> String {` |
| `pub_fn` | `codex-rs/windows-sandbox-rs/src/winutil.rs:88` | `pub fn string_from_sid_bytes(sid: &[u8]) -> Result<String, String> {` |
