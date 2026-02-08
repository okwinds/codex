# `codex-rs/login/src/server.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `24863`
- sha256: `db94920c99e775aa70038fc2b19b99d80d506af5a84bb9978d9c58170bc4c178`
- generated_utc: `2026-02-08T10:45:38Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/login/src/server.rs` (read)

### Outputs / Side Effects
- performs network I/O
- spawns subprocesses
- writes to stdout/stderr

## Public Surface (auto)
- `pub struct ServerOptions {`
- `pub fn new(`
- `pub struct LoginServer {`
- `pub fn cancel(&self) {`
- `pub fn cancel_handle(&self) -> ShutdownHandle {`
- `pub struct ShutdownHandle {`
- `pub fn shutdown(&self) {`
- `pub fn run_login_server(opts: ServerOptions) -> io::Result<LoginServer> {`

## Definitions (auto, per-file)
- `use` `codex-rs/login/src/server.rs:1` `use std::io::Cursor;`
- `use` `codex-rs/login/src/server.rs:2` `use std::io::Read;`
- `use` `codex-rs/login/src/server.rs:3` `use std::io::Write;`
- `use` `codex-rs/login/src/server.rs:4` `use std::io::{self};`
- `use` `codex-rs/login/src/server.rs:5` `use std::net::SocketAddr;`
- `use` `codex-rs/login/src/server.rs:6` `use std::net::TcpStream;`
- `use` `codex-rs/login/src/server.rs:7` `use std::path::Path;`
- `use` `codex-rs/login/src/server.rs:8` `use std::path::PathBuf;`
- `use` `codex-rs/login/src/server.rs:9` `use std::sync::Arc;`
- `use` `codex-rs/login/src/server.rs:10` `use std::thread;`
- `use` `codex-rs/login/src/server.rs:11` `use std::time::Duration;`
- `use` `codex-rs/login/src/server.rs:13` `use crate::pkce::PkceCodes;`
- `use` `codex-rs/login/src/server.rs:14` `use crate::pkce::generate_pkce;`
- `use` `codex-rs/login/src/server.rs:15` `use base64::Engine;`
- `use` `codex-rs/login/src/server.rs:16` `use chrono::Utc;`
- `use` `codex-rs/login/src/server.rs:17` `use codex_app_server_protocol::AuthMode;`
- `use` `codex-rs/login/src/server.rs:18` `use codex_core::auth::AuthCredentialsStoreMode;`
- `use` `codex-rs/login/src/server.rs:19` `use codex_core::auth::AuthDotJson;`
- `use` `codex-rs/login/src/server.rs:20` `use codex_core::auth::save_auth;`
- `use` `codex-rs/login/src/server.rs:21` `use codex_core::default_client::originator;`
- `use` `codex-rs/login/src/server.rs:22` `use codex_core::token_data::TokenData;`
- `use` `codex-rs/login/src/server.rs:23` `use codex_core::token_data::parse_id_token;`
- `use` `codex-rs/login/src/server.rs:24` `use rand::RngCore;`
- `use` `codex-rs/login/src/server.rs:25` `use serde_json::Value as JsonValue;`
- `use` `codex-rs/login/src/server.rs:26` `use tiny_http::Header;`
- `use` `codex-rs/login/src/server.rs:27` `use tiny_http::Request;`
- `use` `codex-rs/login/src/server.rs:28` `use tiny_http::Response;`
- `use` `codex-rs/login/src/server.rs:29` `use tiny_http::Server;`
- `use` `codex-rs/login/src/server.rs:30` `use tiny_http::StatusCode;`
- `const` `codex-rs/login/src/server.rs:32` `const DEFAULT_ISSUER: &str = "https://auth.openai.com";`
- `const` `codex-rs/login/src/server.rs:33` `const DEFAULT_PORT: u16 = 1455;`
- `struct` `codex-rs/login/src/server.rs:36` `pub struct ServerOptions {`
- `impl` `codex-rs/login/src/server.rs:47` `impl ServerOptions {`
- `fn` `codex-rs/login/src/server.rs:48` `pub fn new(`
- `struct` `codex-rs/login/src/server.rs:67` `pub struct LoginServer {`
- `impl` `codex-rs/login/src/server.rs:74` `impl LoginServer {`
- `fn` `codex-rs/login/src/server.rs:75` `pub async fn block_until_done(self) -> io::Result<()> {`
- `fn` `codex-rs/login/src/server.rs:81` `pub fn cancel(&self) {`
- `fn` `codex-rs/login/src/server.rs:85` `pub fn cancel_handle(&self) -> ShutdownHandle {`
- `struct` `codex-rs/login/src/server.rs:91` `pub struct ShutdownHandle {`
- `impl` `codex-rs/login/src/server.rs:95` `impl ShutdownHandle {`
- `fn` `codex-rs/login/src/server.rs:96` `pub fn shutdown(&self) {`
- `fn` `codex-rs/login/src/server.rs:101` `pub fn run_login_server(opts: ServerOptions) -> io::Result<LoginServer> {`
- `enum` `codex-rs/login/src/server.rs:210` `enum HandledRequest {`
- `fn` `codex-rs/login/src/server.rs:220` `async fn process_request(`
- `fn` `codex-rs/login/src/server.rs:346` `fn send_response_with_disconnect(`
- `fn` `codex-rs/login/src/server.rs:381` `fn build_authorize_url(`
- `fn` `codex-rs/login/src/server.rs:421` `fn generate_state() -> String {`
- `fn` `codex-rs/login/src/server.rs:427` `fn send_cancel_request(port: u16) -> io::Result<()> {`
- `fn` `codex-rs/login/src/server.rs:444` `fn bind_server(port: u16) -> io::Result<Server> {`
- `const` `codex-rs/login/src/server.rs:448` `const MAX_ATTEMPTS: u32 = 10;`
- `const` `codex-rs/login/src/server.rs:449` `const RETRY_DELAY: Duration = Duration::from_millis(200);`
- `struct` `codex-rs/login/src/server.rs:503` `struct TokenResponse {`
- `fn` `codex-rs/login/src/server.rs:574` `fn compose_success_url(port: u16, issuer: &str, id_token: &str, access_token: &str) -> String {`
- `fn` `codex-rs/login/src/server.rs:622` `fn jwt_auth_claims(jwt: &str) -> serde_json::Map<String, serde_json::Value> {`
- `fn` `codex-rs/login/src/server.rs:674` `fn login_error_response(message: &str) -> HandledRequest {`
- `struct` `codex-rs/login/src/server.rs:697` `struct ExchangeResp {`

## Dependencies (auto sample)
### Imports / Includes
- `use std::io::Cursor;`
- `use std::io::Read;`
- `use std::io::Write;`
- `use std::io::{self};`
- `use std::net::SocketAddr;`
- `use std::net::TcpStream;`
- `use std::path::Path;`
- `use std::path::PathBuf;`
- `use std::sync::Arc;`
- `use std::thread;`
- `use std::time::Duration;`
- `use crate::pkce::PkceCodes;`
- `use crate::pkce::generate_pkce;`
- `use base64::Engine;`
- `use chrono::Utc;`
- `use codex_app_server_protocol::AuthMode;`
- `use codex_core::auth::AuthCredentialsStoreMode;`
- `use codex_core::auth::AuthDotJson;`
- `use codex_core::auth::save_auth;`
- `use codex_core::default_client::originator;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- has retry/timeout/backoff logic
- returns structured errors (Result/ErrorKind)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
