# `codex-rs/responses-api-proxy/src/lib.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `7522`
- sha256: `ab6cca54f064c4c88b4db86c82f39dad64595cf8d5ed4e8622ec4d436c0ad858`
- generated_utc: `2026-02-08T10:45:38Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/responses-api-proxy/src/lib.rs` (read)

### Outputs / Side Effects
- performs network I/O
- spawns subprocesses
- writes to filesystem
- writes to stdout/stderr

## Public Surface (auto)
- `pub struct Args {`
- `pub fn run_main(args: Args) -> Result<()> {`

## Definitions (auto, per-file)
- `use` `codex-rs/responses-api-proxy/src/lib.rs:1` `use std::fs::File;`
- `use` `codex-rs/responses-api-proxy/src/lib.rs:2` `use std::fs::{self};`
- `use` `codex-rs/responses-api-proxy/src/lib.rs:3` `use std::io::Write;`
- `use` `codex-rs/responses-api-proxy/src/lib.rs:4` `use std::net::SocketAddr;`
- `use` `codex-rs/responses-api-proxy/src/lib.rs:5` `use std::net::TcpListener;`
- `use` `codex-rs/responses-api-proxy/src/lib.rs:6` `use std::path::Path;`
- `use` `codex-rs/responses-api-proxy/src/lib.rs:7` `use std::path::PathBuf;`
- `use` `codex-rs/responses-api-proxy/src/lib.rs:8` `use std::sync::Arc;`
- `use` `codex-rs/responses-api-proxy/src/lib.rs:9` `use std::time::Duration;`
- `use` `codex-rs/responses-api-proxy/src/lib.rs:11` `use anyhow::Context;`
- `use` `codex-rs/responses-api-proxy/src/lib.rs:12` `use anyhow::Result;`
- `use` `codex-rs/responses-api-proxy/src/lib.rs:13` `use anyhow::anyhow;`
- `use` `codex-rs/responses-api-proxy/src/lib.rs:14` `use clap::Parser;`
- `use` `codex-rs/responses-api-proxy/src/lib.rs:15` `use reqwest::Url;`
- `use` `codex-rs/responses-api-proxy/src/lib.rs:16` `use reqwest::blocking::Client;`
- `use` `codex-rs/responses-api-proxy/src/lib.rs:17` `use reqwest::header::AUTHORIZATION;`
- `use` `codex-rs/responses-api-proxy/src/lib.rs:18` `use reqwest::header::HOST;`
- `use` `codex-rs/responses-api-proxy/src/lib.rs:19` `use reqwest::header::HeaderMap;`
- `use` `codex-rs/responses-api-proxy/src/lib.rs:20` `use reqwest::header::HeaderName;`
- `use` `codex-rs/responses-api-proxy/src/lib.rs:21` `use reqwest::header::HeaderValue;`
- `use` `codex-rs/responses-api-proxy/src/lib.rs:22` `use serde::Serialize;`
- `use` `codex-rs/responses-api-proxy/src/lib.rs:23` `use tiny_http::Header;`
- `use` `codex-rs/responses-api-proxy/src/lib.rs:24` `use tiny_http::Method;`
- `use` `codex-rs/responses-api-proxy/src/lib.rs:25` `use tiny_http::Request;`
- `use` `codex-rs/responses-api-proxy/src/lib.rs:26` `use tiny_http::Response;`
- `use` `codex-rs/responses-api-proxy/src/lib.rs:27` `use tiny_http::Server;`
- `use` `codex-rs/responses-api-proxy/src/lib.rs:28` `use tiny_http::StatusCode;`
- `mod` `codex-rs/responses-api-proxy/src/lib.rs:30` `mod read_api_key;`
- `use` `codex-rs/responses-api-proxy/src/lib.rs:31` `use read_api_key::read_auth_header_from_stdin;`
- `struct` `codex-rs/responses-api-proxy/src/lib.rs:36` `pub struct Args {`
- `struct` `codex-rs/responses-api-proxy/src/lib.rs:55` `struct ServerInfo {`
- `struct` `codex-rs/responses-api-proxy/src/lib.rs:60` `struct ForwardConfig {`
- `fn` `codex-rs/responses-api-proxy/src/lib.rs:66` `pub fn run_main(args: Args) -> Result<()> {`
- `fn` `codex-rs/responses-api-proxy/src/lib.rs:118` `fn bind_listener(port: Option<u16>) -> Result<(TcpListener, SocketAddr)> {`
- `fn` `codex-rs/responses-api-proxy/src/lib.rs:125` `fn write_server_info(path: &Path, port: u16) -> Result<()> {`
- `fn` `codex-rs/responses-api-proxy/src/lib.rs:143` `fn forward_request(`

## Dependencies (auto sample)
### Imports / Includes
- `use std::fs::File;`
- `use std::fs::{self};`
- `use std::io::Write;`
- `use std::net::SocketAddr;`
- `use std::net::TcpListener;`
- `use std::path::Path;`
- `use std::path::PathBuf;`
- `use std::sync::Arc;`
- `use std::time::Duration;`
- `use anyhow::Context;`
- `use anyhow::Result;`
- `use anyhow::anyhow;`
- `use clap::Parser;`
- `use reqwest::Url;`
- `use reqwest::blocking::Client;`
- `use reqwest::header::AUTHORIZATION;`
- `use reqwest::header::HOST;`
- `use reqwest::header::HeaderMap;`
- `use reqwest::header::HeaderName;`
- `use reqwest::header::HeaderValue;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- has retry/timeout/backoff logic
- returns structured errors (Result/ErrorKind)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
