# `codex-login`

- path: `codex-rs/login`
- generated_utc: `2026-02-03T09:48:37Z`
- role: login/auth flows and credential handling

## Build Targets
- has_lib_rs: `true`
- has_main_rs: `false`
- explicit_bins: (none)

## Key Dependencies (direct, from Cargo.toml)
- `base64`
- `chrono`
- `codex-app-server-protocol`
- `codex-core`
- `rand`
- `reqwest`
- `serde`
- `serde_json`
- `sha2`
- `tempfile`
- `tiny_http`
- `tokio`
- `url`
- `urlencoding`
- `webbrowser`

## Features
- (none)

## Public Surface (auto, from src/lib.rs or src/main.rs)
- `pub use device_code_auth::DeviceCode;`
- `pub use device_code_auth::complete_device_code_login;`
- `pub use device_code_auth::request_device_code;`
- `pub use device_code_auth::run_device_code_login;`
- `pub use server::LoginServer;`
- `pub use server::ServerOptions;`
- `pub use server::ShutdownHandle;`
- `pub use server::run_login_server;`
- `pub use codex_app_server_protocol::AuthMode;`
- `pub use codex_core::AuthManager;`
- `pub use codex_core::CodexAuth;`
- `pub use codex_core::auth::AuthDotJson;`
- `pub use codex_core::auth::CLIENT_ID;`
- `pub use codex_core::auth::CODEX_API_KEY_ENV_VAR;`
- `pub use codex_core::auth::OPENAI_API_KEY_ENV_VAR;`
- `pub use codex_core::auth::login_with_api_key;`
- `pub use codex_core::auth::logout;`
- `pub use codex_core::auth::save_auth;`
- `pub use codex_core::token_data::TokenData;`

## Spec Links
- `workdocjcl/spec/00_Overview/MODULE_MAP.md`
- `workdocjcl/spec/09_Verification/CODE_TO_SPEC_MAP.md`
