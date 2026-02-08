# `codex-rs/exec-server/src/posix/socket.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `17094`
- sha256: `e533fa89dffbc6c85ad106b1b32c1b34c5d9b303338cdd0c9c891cac454c284f`
- generated_utc: `2026-02-08T10:45:36Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/exec-server/src/posix/socket.rs` (read)

### Outputs / Side Effects
- spawns subprocesses

## Public Surface (auto)
- `pub fn from_fd(fd: OwnedFd) -> std::io::Result<AsyncSocket> {`
- `pub fn pair() -> std::io::Result<(AsyncSocket, AsyncSocket)> {`
- `pub fn into_inner(self) -> Socket {`
- `pub fn pair() -> std::io::Result<(Self, Self)> {`
- `pub fn into_inner(self) -> Socket {`

## Definitions (auto, per-file)
- `use` `codex-rs/exec-server/src/posix/socket.rs:1` `use libc::c_uint;`
- `use` `codex-rs/exec-server/src/posix/socket.rs:2` `use serde::Deserialize;`
- `use` `codex-rs/exec-server/src/posix/socket.rs:3` `use serde::Serialize;`
- `use` `codex-rs/exec-server/src/posix/socket.rs:4` `use socket2::Domain;`
- `use` `codex-rs/exec-server/src/posix/socket.rs:5` `use socket2::MaybeUninitSlice;`
- `use` `codex-rs/exec-server/src/posix/socket.rs:6` `use socket2::MsgHdr;`
- `use` `codex-rs/exec-server/src/posix/socket.rs:7` `use socket2::MsgHdrMut;`
- `use` `codex-rs/exec-server/src/posix/socket.rs:8` `use socket2::Socket;`
- `use` `codex-rs/exec-server/src/posix/socket.rs:9` `use socket2::Type;`
- `use` `codex-rs/exec-server/src/posix/socket.rs:10` `use std::io::IoSlice;`
- `use` `codex-rs/exec-server/src/posix/socket.rs:11` `use std::mem::MaybeUninit;`
- `use` `codex-rs/exec-server/src/posix/socket.rs:12` `use std::os::fd::AsRawFd;`
- `use` `codex-rs/exec-server/src/posix/socket.rs:13` `use std::os::fd::FromRawFd;`
- `use` `codex-rs/exec-server/src/posix/socket.rs:14` `use std::os::fd::OwnedFd;`
- `use` `codex-rs/exec-server/src/posix/socket.rs:15` `use std::os::fd::RawFd;`
- `use` `codex-rs/exec-server/src/posix/socket.rs:16` `use tokio::io::Interest;`
- `use` `codex-rs/exec-server/src/posix/socket.rs:17` `use tokio::io::unix::AsyncFd;`
- `const` `codex-rs/exec-server/src/posix/socket.rs:19` `const MAX_FDS_PER_MESSAGE: usize = 16;`
- `const` `codex-rs/exec-server/src/posix/socket.rs:20` `const LENGTH_PREFIX_SIZE: usize = size_of::<u32>();`
- `const` `codex-rs/exec-server/src/posix/socket.rs:21` `const MAX_DATAGRAM_SIZE: usize = 8192;`
- `fn` `codex-rs/exec-server/src/posix/socket.rs:44` `fn control_space_for_fds(count: usize) -> usize {`
- `fn` `codex-rs/exec-server/src/posix/socket.rs:49` `fn extract_fds(control: &[u8]) -> Vec<OwnedFd> {`
- `fn` `codex-rs/exec-server/src/posix/socket.rs:81` `async fn read_frame(async_socket: &AsyncFd<Socket>) -> std::io::Result<(Vec<u8>, Vec<OwnedFd>)> {`
- `fn` `codex-rs/exec-server/src/posix/socket.rs:88` `async fn read_frame_header(`
- `fn` `codex-rs/exec-server/src/posix/socket.rs:142` `async fn read_frame_payload(`
- `fn` `codex-rs/exec-server/src/posix/socket.rs:174` `fn send_datagram_bytes(socket: &Socket, data: &[u8], fds: &[OwnedFd]) -> std::io::Result<()> {`
- `fn` `codex-rs/exec-server/src/posix/socket.rs:195` `fn encode_length(len: usize) -> std::io::Result<[u8; LENGTH_PREFIX_SIZE]> {`
- `fn` `codex-rs/exec-server/src/posix/socket.rs:205` `fn make_control_message(fds: &[OwnedFd]) -> std::io::Result<Vec<u8>> {`
- `fn` `codex-rs/exec-server/src/posix/socket.rs:230` `fn receive_datagram_bytes(socket: &Socket) -> std::io::Result<(Vec<u8>, Vec<OwnedFd>)> {`
- `impl` `codex-rs/exec-server/src/posix/socket.rs:250` `impl AsyncSocket {`
- `fn` `codex-rs/exec-server/src/posix/socket.rs:251` `fn new(socket: Socket) -> std::io::Result<AsyncSocket> {`
- `fn` `codex-rs/exec-server/src/posix/socket.rs:259` `pub fn from_fd(fd: OwnedFd) -> std::io::Result<AsyncSocket> {`
- `fn` `codex-rs/exec-server/src/posix/socket.rs:263` `pub fn pair() -> std::io::Result<(AsyncSocket, AsyncSocket)> {`
- `fn` `codex-rs/exec-server/src/posix/socket.rs:303` `pub fn into_inner(self) -> Socket {`
- `fn` `codex-rs/exec-server/src/posix/socket.rs:308` `async fn send_stream_frame(`
- `fn` `codex-rs/exec-server/src/posix/socket.rs:336` `fn send_stream_chunk(`
- `impl` `codex-rs/exec-server/src/posix/socket.rs:360` `impl AsyncDatagramSocket {`
- `fn` `codex-rs/exec-server/src/posix/socket.rs:361` `fn new(socket: Socket) -> std::io::Result<Self> {`
- `fn` `codex-rs/exec-server/src/posix/socket.rs:372` `pub fn pair() -> std::io::Result<(Self, Self)> {`
- `fn` `codex-rs/exec-server/src/posix/socket.rs:377` `pub async fn send_with_fds(&self, data: &[u8], fds: &[OwnedFd]) -> std::io::Result<()> {`
- `fn` `codex-rs/exec-server/src/posix/socket.rs:385` `pub async fn receive_with_fds(&self) -> std::io::Result<(Vec<u8>, Vec<OwnedFd>)> {`
- `fn` `codex-rs/exec-server/src/posix/socket.rs:391` `pub fn into_inner(self) -> Socket {`
- `use` `codex-rs/exec-server/src/posix/socket.rs:398` `use super::*;`
- `use` `codex-rs/exec-server/src/posix/socket.rs:399` `use pretty_assertions::assert_eq;`
- `use` `codex-rs/exec-server/src/posix/socket.rs:400` `use serde::Deserialize;`
- `use` `codex-rs/exec-server/src/posix/socket.rs:401` `use serde::Serialize;`
- `use` `codex-rs/exec-server/src/posix/socket.rs:402` `use std::os::fd::AsFd;`
- `use` `codex-rs/exec-server/src/posix/socket.rs:403` `use std::os::fd::AsRawFd;`
- `use` `codex-rs/exec-server/src/posix/socket.rs:404` `use tempfile::NamedTempFile;`
- `struct` `codex-rs/exec-server/src/posix/socket.rs:407` `struct TestPayload {`
- `fn` `codex-rs/exec-server/src/posix/socket.rs:412` `fn fd_list(count: usize) -> std::io::Result<Vec<OwnedFd>> {`
- `fn` `codex-rs/exec-server/src/posix/socket.rs:422` `async fn async_socket_round_trips_payload_and_fds() -> std::io::Result<()> {`
- `fn` `codex-rs/exec-server/src/posix/socket.rs:447` `async fn async_socket_handles_large_payload() -> std::io::Result<()> {`
- `fn` `codex-rs/exec-server/src/posix/socket.rs:458` `async fn async_datagram_sockets_round_trip_messages() -> std::io::Result<()> {`
- `fn` `codex-rs/exec-server/src/posix/socket.rs:474` `fn send_datagram_bytes_rejects_excessive_fd_counts() -> std::io::Result<()> {`
- `fn` `codex-rs/exec-server/src/posix/socket.rs:483` `fn send_stream_chunk_rejects_excessive_fd_counts() -> std::io::Result<()> {`
- `fn` `codex-rs/exec-server/src/posix/socket.rs:492` `fn encode_length_errors_for_oversized_messages() {`
- `fn` `codex-rs/exec-server/src/posix/socket.rs:498` `async fn receive_fails_when_peer_closes_before_header() {`

## Dependencies (auto sample)
### Imports / Includes
- `use libc::c_uint;`
- `use serde::Deserialize;`
- `use serde::Serialize;`
- `use socket2::Domain;`
- `use socket2::MaybeUninitSlice;`
- `use socket2::MsgHdr;`
- `use socket2::MsgHdrMut;`
- `use socket2::Socket;`
- `use socket2::Type;`
- `use std::io::IoSlice;`
- `use std::mem::MaybeUninit;`
- `use std::os::fd::AsRawFd;`
- `use std::os::fd::FromRawFd;`
- `use std::os::fd::OwnedFd;`
- `use std::os::fd::RawFd;`
- `use tokio::io::Interest;`
- `use tokio::io::unix::AsyncFd;`
- `use super::*;`
- `use pretty_assertions::assert_eq;`
- `use serde::Deserialize;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
