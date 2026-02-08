# `codex-rs/tui/src/notifications/mod.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `4469`
- sha256: `d6f2397300650d8b785cabe024c75c182c4ee2e7bbad9a6205f43c7a81148551`
- generated_utc: `2026-02-03T16:08:30Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/tui/src/notifications/mod.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub enum DesktopNotificationBackend {`
- `pub fn for_method(method: NotificationMethod) -> Self {`
- `pub fn method(&self) -> NotificationMethod {`
- `pub fn notify(&mut self, message: &str) -> io::Result<()> {`
- `pub fn detect_backend(method: NotificationMethod) -> DesktopNotificationBackend {`

## Definitions (auto, per-file)
- `mod` `codex-rs/tui/src/notifications/mod.rs:1` `mod bel;`
- `mod` `codex-rs/tui/src/notifications/mod.rs:2` `mod osc9;`
- `use` `codex-rs/tui/src/notifications/mod.rs:4` `use std::env;`
- `use` `codex-rs/tui/src/notifications/mod.rs:5` `use std::io;`
- `use` `codex-rs/tui/src/notifications/mod.rs:7` `use bel::BelBackend;`
- `use` `codex-rs/tui/src/notifications/mod.rs:8` `use codex_core::config::types::NotificationMethod;`
- `use` `codex-rs/tui/src/notifications/mod.rs:9` `use osc9::Osc9Backend;`
- `enum` `codex-rs/tui/src/notifications/mod.rs:12` `pub enum DesktopNotificationBackend {`
- `impl` `codex-rs/tui/src/notifications/mod.rs:17` `impl DesktopNotificationBackend {`
- `fn` `codex-rs/tui/src/notifications/mod.rs:18` `pub fn for_method(method: NotificationMethod) -> Self {`
- `fn` `codex-rs/tui/src/notifications/mod.rs:32` `pub fn method(&self) -> NotificationMethod {`
- `fn` `codex-rs/tui/src/notifications/mod.rs:39` `pub fn notify(&mut self, message: &str) -> io::Result<()> {`
- `fn` `codex-rs/tui/src/notifications/mod.rs:47` `pub fn detect_backend(method: NotificationMethod) -> DesktopNotificationBackend {`
- `fn` `codex-rs/tui/src/notifications/mod.rs:51` `fn supports_osc9() -> bool {`
- `use` `codex-rs/tui/src/notifications/mod.rs:76` `use super::detect_backend;`
- `use` `codex-rs/tui/src/notifications/mod.rs:77` `use codex_core::config::types::NotificationMethod;`
- `use` `codex-rs/tui/src/notifications/mod.rs:78` `use serial_test::serial;`
- `use` `codex-rs/tui/src/notifications/mod.rs:79` `use std::ffi::OsString;`
- `struct` `codex-rs/tui/src/notifications/mod.rs:81` `struct EnvVarGuard {`
- `impl` `codex-rs/tui/src/notifications/mod.rs:86` `impl EnvVarGuard {`
- `fn` `codex-rs/tui/src/notifications/mod.rs:87` `fn set(key: &'static str, value: &str) -> Self {`
- `fn` `codex-rs/tui/src/notifications/mod.rs:95` `fn remove(key: &'static str) -> Self {`
- `impl` `codex-rs/tui/src/notifications/mod.rs:104` `impl Drop for EnvVarGuard {`
- `fn` `codex-rs/tui/src/notifications/mod.rs:105` `fn drop(&mut self) {`
- `fn` `codex-rs/tui/src/notifications/mod.rs:116` `fn selects_osc9_method() {`
- `fn` `codex-rs/tui/src/notifications/mod.rs:124` `fn selects_bel_method() {`
- `fn` `codex-rs/tui/src/notifications/mod.rs:133` `fn auto_prefers_bel_without_hints() {`
- `fn` `codex-rs/tui/src/notifications/mod.rs:146` `fn auto_uses_osc9_for_iterm() {`

## Dependencies (auto sample)
### Imports / Includes
- `use std::env;`
- `use std::io;`
- `use bel::BelBackend;`
- `use codex_core::config::types::NotificationMethod;`
- `use osc9::Osc9Backend;`
- `use super::detect_backend;`
- `use codex_core::config::types::NotificationMethod;`
- `use serial_test::serial;`
- `use std::ffi::OsString;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)

## Spec Links
- `workdocjcl/spec/06_UI/TUI.md`
