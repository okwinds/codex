# `codex-rmcp-client`

- path: `codex-rs/rmcp-client`
- generated_utc: `2026-02-03T09:48:37Z`
- role: MCP client/server or related support

## Build Targets
- has_lib_rs: `true`
- has_main_rs: `false`
- explicit_bins: (none)

## Key Dependencies (direct, from Cargo.toml)
- `anyhow`
- `axum`
- `codex-keyring-store`
- `codex-protocol`
- `codex-utils-home-dir`
- `futures`
- `keyring`
- `oauth2`
- `reqwest`
- `rmcp`
- `schemars`
- `serde`
- `serde_json`
- `sha2`
- `tiny_http`
- `tokio`
- `tracing`
- `urlencoding`
- `webbrowser`
- `which`

## Features
- (none)

## Public Surface (auto, from src/lib.rs or src/main.rs)
- `pub use auth_status::determine_streamable_http_auth_status;`
- `pub use auth_status::supports_oauth_login;`
- `pub use codex_protocol::protocol::McpAuthStatus;`
- `pub use oauth::OAuthCredentialsStoreMode;`
- `pub use oauth::StoredOAuthTokens;`
- `pub use oauth::WrappedOAuthTokenResponse;`
- `pub use oauth::delete_oauth_tokens;`
- `pub use oauth::save_oauth_tokens;`
- `pub use perform_oauth_login::OauthLoginHandle;`
- `pub use perform_oauth_login::perform_oauth_login;`
- `pub use perform_oauth_login::perform_oauth_login_return_url;`
- `pub use rmcp::model::ElicitationAction;`
- `pub use rmcp_client::Elicitation;`
- `pub use rmcp_client::ElicitationResponse;`
- `pub use rmcp_client::ListToolsWithConnectorIdResult;`
- `pub use rmcp_client::RmcpClient;`
- `pub use rmcp_client::SendElicitation;`
- `pub use rmcp_client::ToolWithConnectorId;`

## Spec Links
- `workdocjcl/spec/00_Overview/MODULE_MAP.md`
- `workdocjcl/spec/09_Verification/CODE_TO_SPEC_MAP.md`
