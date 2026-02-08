# `codex-rs/core/src/shell.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `16423`
- sha256: `0792fffbe310eaf9ff99292848b6a91441dbadae9848d8805b27b9061ac321fa`
- generated_utc: `2026-02-03T16:08:29Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/shell.rs` (read)

### Outputs / Side Effects
- spawns subprocesses

## Public Surface (auto)
- `pub enum ShellType {`
- `pub struct Shell {`
- `pub fn name(&self) -> &'static str {`
- `pub fn derive_exec_args(&self, command: &str, use_login_shell: bool) -> Vec<String> {`
- `pub fn shell_snapshot(&self) -> Option<Arc<ShellSnapshot>> {`
- `pub fn get_shell_by_model_provided_path(shell_path: &PathBuf) -> Shell {`
- `pub fn get_shell(shell_type: ShellType, path: Option<&PathBuf>) -> Option<Shell> {`
- `pub fn detect_shell_type(shell_path: &PathBuf) -> Option<ShellType> {`
- `pub fn default_user_shell() -> Shell {`

## Definitions (auto, per-file)
- `use` `codex-rs/core/src/shell.rs:1` `use crate::shell_snapshot::ShellSnapshot;`
- `use` `codex-rs/core/src/shell.rs:2` `use serde::Deserialize;`
- `use` `codex-rs/core/src/shell.rs:3` `use serde::Serialize;`
- `use` `codex-rs/core/src/shell.rs:4` `use std::path::PathBuf;`
- `use` `codex-rs/core/src/shell.rs:5` `use std::sync::Arc;`
- `use` `codex-rs/core/src/shell.rs:6` `use tokio::sync::watch;`
- `enum` `codex-rs/core/src/shell.rs:9` `pub enum ShellType {`
- `struct` `codex-rs/core/src/shell.rs:18` `pub struct Shell {`
- `impl` `codex-rs/core/src/shell.rs:29` `impl Shell {`
- `fn` `codex-rs/core/src/shell.rs:30` `pub fn name(&self) -> &'static str {`
- `fn` `codex-rs/core/src/shell.rs:42` `pub fn derive_exec_args(&self, command: &str, use_login_shell: bool) -> Vec<String> {`
- `fn` `codex-rs/core/src/shell.rs:72` `pub fn shell_snapshot(&self) -> Option<Arc<ShellSnapshot>> {`
- `impl` `codex-rs/core/src/shell.rs:82` `impl PartialEq for Shell {`
- `fn` `codex-rs/core/src/shell.rs:83` `fn eq(&self, other: &Self) -> bool {`
- `fn` `codex-rs/core/src/shell.rs:91` `fn get_user_shell_path() -> Option<PathBuf> {`
- `use` `codex-rs/core/src/shell.rs:92` `use libc::getpwuid;`
- `use` `codex-rs/core/src/shell.rs:93` `use libc::getuid;`
- `use` `codex-rs/core/src/shell.rs:94` `use std::ffi::CStr;`
- `fn` `codex-rs/core/src/shell.rs:112` `fn get_user_shell_path() -> Option<PathBuf> {`
- `fn` `codex-rs/core/src/shell.rs:116` `fn file_exists(path: &PathBuf) -> Option<PathBuf> {`
- `fn` `codex-rs/core/src/shell.rs:124` `fn get_shell_path(`
- `fn` `codex-rs/core/src/shell.rs:159` `fn get_zsh_shell(path: Option<&PathBuf>) -> Option<Shell> {`
- `fn` `codex-rs/core/src/shell.rs:169` `fn get_bash_shell(path: Option<&PathBuf>) -> Option<Shell> {`
- `fn` `codex-rs/core/src/shell.rs:179` `fn get_sh_shell(path: Option<&PathBuf>) -> Option<Shell> {`
- `fn` `codex-rs/core/src/shell.rs:189` `fn get_powershell_shell(path: Option<&PathBuf>) -> Option<Shell> {`
- `fn` `codex-rs/core/src/shell.rs:205` `fn get_cmd_shell(path: Option<&PathBuf>) -> Option<Shell> {`
- `fn` `codex-rs/core/src/shell.rs:215` `fn ultimate_fallback_shell() -> Shell {`
- `fn` `codex-rs/core/src/shell.rs:231` `pub fn get_shell_by_model_provided_path(shell_path: &PathBuf) -> Shell {`
- `fn` `codex-rs/core/src/shell.rs:237` `pub fn get_shell(shell_type: ShellType, path: Option<&PathBuf>) -> Option<Shell> {`
- `fn` `codex-rs/core/src/shell.rs:247` `pub fn detect_shell_type(shell_path: &PathBuf) -> Option<ShellType> {`
- `fn` `codex-rs/core/src/shell.rs:268` `pub fn default_user_shell() -> Shell {`
- `fn` `codex-rs/core/src/shell.rs:272` `fn default_user_shell_from_path(user_shell_path: Option<PathBuf>) -> Shell {`
- `use` `codex-rs/core/src/shell.rs:296` `use super::*;`
- `fn` `codex-rs/core/src/shell.rs:299` `fn test_detect_shell_type() {`
- `use` `codex-rs/core/src/shell.rs:365` `use super::*;`
- `use` `codex-rs/core/src/shell.rs:366` `use std::path::Path;`
- `use` `codex-rs/core/src/shell.rs:367` `use std::path::PathBuf;`
- `use` `codex-rs/core/src/shell.rs:368` `use std::process::Command;`
- `fn` `codex-rs/core/src/shell.rs:372` `fn detects_zsh() {`
- `fn` `codex-rs/core/src/shell.rs:382` `fn fish_fallback_to_zsh() {`
- `fn` `codex-rs/core/src/shell.rs:391` `fn detects_bash() {`
- `fn` `codex-rs/core/src/shell.rs:404` `fn detects_sh() {`
- `fn` `codex-rs/core/src/shell.rs:414` `fn can_run_on_shell_test() {`
- `fn` `codex-rs/core/src/shell.rs:432` `fn shell_works(shell: Option<Shell>, command: &str, required: bool) -> bool {`
- `fn` `codex-rs/core/src/shell.rs:448` `fn derive_exec_args() {`
- `fn` `codex-rs/core/src/shell.rs:493` `async fn test_current_shell_detects_zsh() {`
- `fn` `codex-rs/core/src/shell.rs:514` `async fn detects_powershell_as_default() {`
- `fn` `codex-rs/core/src/shell.rs:526` `fn finds_poweshell() {`

## Dependencies (auto sample)
### Imports / Includes
- `use crate::shell_snapshot::ShellSnapshot;`
- `use serde::Deserialize;`
- `use serde::Serialize;`
- `use std::path::PathBuf;`
- `use std::sync::Arc;`
- `use tokio::sync::watch;`
- `use libc::getpwuid;`
- `use libc::getuid;`
- `use std::ffi::CStr;`
- `use super::*;`
- `use super::*;`
- `use std::path::Path;`
- `use std::path::PathBuf;`
- `use std::process::Command;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- `workdocjcl/spec/00_Overview/ARCHITECTURE.md`
