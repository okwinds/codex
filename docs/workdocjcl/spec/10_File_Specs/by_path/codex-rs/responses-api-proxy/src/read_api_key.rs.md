# `codex-rs/responses-api-proxy/src/read_api_key.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `10349`
- sha256: `fc338d516d5d00239001dbd1f7ed358993e25d08bc6f34b3dfa4bb3f715b0f71`
- generated_utc: `2026-02-03T16:08:30Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/responses-api-proxy/src/read_api_key.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `use` `codex-rs/responses-api-proxy/src/read_api_key.rs:1` `use anyhow::Context;`
- `use` `codex-rs/responses-api-proxy/src/read_api_key.rs:2` `use anyhow::Result;`
- `use` `codex-rs/responses-api-proxy/src/read_api_key.rs:3` `use anyhow::anyhow;`
- `use` `codex-rs/responses-api-proxy/src/read_api_key.rs:4` `use zeroize::Zeroize;`
- `const` `codex-rs/responses-api-proxy/src/read_api_key.rs:8` `const BUFFER_SIZE: usize = 1024;`
- `const` `codex-rs/responses-api-proxy/src/read_api_key.rs:9` `const AUTH_HEADER_PREFIX: &[u8] = b"Bearer ";`
- `use` `codex-rs/responses-api-proxy/src/read_api_key.rs:22` `use std::io::Read;`
- `fn` `codex-rs/responses-api-proxy/src/read_api_key.rs:41` `fn read_from_unix_stdin(buffer: &mut [u8]) -> std::io::Result<usize> {`
- `use` `codex-rs/responses-api-proxy/src/read_api_key.rs:42` `use libc::c_void;`
- `use` `codex-rs/responses-api-proxy/src/read_api_key.rs:43` `use libc::read;`
- `fn` `codex-rs/responses-api-proxy/src/read_api_key.rs:165` `fn mlock_str(value: &str) {`
- `use` `codex-rs/responses-api-proxy/src/read_api_key.rs:166` `use libc::_SC_PAGESIZE;`
- `use` `codex-rs/responses-api-proxy/src/read_api_key.rs:167` `use libc::c_void;`
- `use` `codex-rs/responses-api-proxy/src/read_api_key.rs:168` `use libc::mlock;`
- `use` `codex-rs/responses-api-proxy/src/read_api_key.rs:169` `use libc::sysconf;`
- `fn` `codex-rs/responses-api-proxy/src/read_api_key.rs:204` `fn mlock_str(_value: &str) {}`
- `fn` `codex-rs/responses-api-proxy/src/read_api_key.rs:208` `fn validate_auth_header_bytes(key_bytes: &[u8]) -> Result<()> {`
- `use` `codex-rs/responses-api-proxy/src/read_api_key.rs:223` `use super::*;`
- `use` `codex-rs/responses-api-proxy/src/read_api_key.rs:224` `use std::collections::VecDeque;`
- `use` `codex-rs/responses-api-proxy/src/read_api_key.rs:225` `use std::io;`
- `fn` `codex-rs/responses-api-proxy/src/read_api_key.rs:228` `fn reads_key_with_no_newlines() {`
- `fn` `codex-rs/responses-api-proxy/src/read_api_key.rs:245` `fn reads_key_with_short_reads() {`
- `fn` `codex-rs/responses-api-proxy/src/read_api_key.rs:261` `fn reads_key_and_trims_newlines() {`
- `fn` `codex-rs/responses-api-proxy/src/read_api_key.rs:278` `fn errors_when_no_input_provided() {`
- `fn` `codex-rs/responses-api-proxy/src/read_api_key.rs:285` `fn errors_when_buffer_filled() {`
- `fn` `codex-rs/responses-api-proxy/src/read_api_key.rs:299` `fn propagates_io_error() {`
- `fn` `codex-rs/responses-api-proxy/src/read_api_key.rs:308` `fn errors_on_invalid_utf8() {`
- `fn` `codex-rs/responses-api-proxy/src/read_api_key.rs:326` `fn errors_on_invalid_characters() {`

## Dependencies (auto sample)
### Imports / Includes
- `use anyhow::Context;`
- `use anyhow::Result;`
- `use anyhow::anyhow;`
- `use zeroize::Zeroize;`
- `use std::io::Read;`
- `use libc::c_void;`
- `use libc::read;`
- `use libc::_SC_PAGESIZE;`
- `use libc::c_void;`
- `use libc::mlock;`
- `use libc::sysconf;`
- `use super::*;`
- `use std::collections::VecDeque;`
- `use std::io;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
