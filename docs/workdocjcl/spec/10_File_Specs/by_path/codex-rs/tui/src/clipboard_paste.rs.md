# `codex-rs/tui/src/clipboard_paste.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `18916`
- sha256: `708f1f4e6b365edc16583787a71fc3505ed56526789af711508fd0b7920a1d44`
- generated_utc: `2026-02-03T16:08:30Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/tui/src/clipboard_paste.rs` (read)
- env: `WSL_DISTRO_NAME`, `WSL_INTEROP`

### Outputs / Side Effects
- spawns subprocesses
- writes to filesystem

## Public Surface (auto)
- `pub enum PasteImageError {`
- `pub enum EncodedImageFormat {`
- `pub fn label(self) -> &'static str {`
- `pub struct PastedImageInfo {`
- `pub fn paste_image_as_png() -> Result<(Vec<u8>, PastedImageInfo), PasteImageError> {`
- `pub fn paste_image_as_png() -> Result<(Vec<u8>, PastedImageInfo), PasteImageError> {`
- `pub fn paste_image_to_temp_png() -> Result<(PathBuf, PastedImageInfo), PasteImageError> {`
- `pub fn paste_image_to_temp_png() -> Result<(PathBuf, PastedImageInfo), PasteImageError> {`
- `pub fn normalize_pasted_path(pasted: &str) -> Option<PathBuf> {`
- `pub fn pasted_image_format(path: &Path) -> EncodedImageFormat {`

## Definitions (auto, per-file)
- `use` `codex-rs/tui/src/clipboard_paste.rs:1` `use std::path::Path;`
- `use` `codex-rs/tui/src/clipboard_paste.rs:2` `use std::path::PathBuf;`
- `use` `codex-rs/tui/src/clipboard_paste.rs:3` `use tempfile::Builder;`
- `enum` `codex-rs/tui/src/clipboard_paste.rs:6` `pub enum PasteImageError {`
- `impl` `codex-rs/tui/src/clipboard_paste.rs:13` `impl std::fmt::Display for PasteImageError {`
- `fn` `codex-rs/tui/src/clipboard_paste.rs:14` `fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {`
- `enum` `codex-rs/tui/src/clipboard_paste.rs:26` `pub enum EncodedImageFormat {`
- `impl` `codex-rs/tui/src/clipboard_paste.rs:32` `impl EncodedImageFormat {`
- `fn` `codex-rs/tui/src/clipboard_paste.rs:33` `pub fn label(self) -> &'static str {`
- `struct` `codex-rs/tui/src/clipboard_paste.rs:43` `pub struct PastedImageInfo {`
- `fn` `codex-rs/tui/src/clipboard_paste.rs:51` `pub fn paste_image_as_png() -> Result<(Vec<u8>, PastedImageInfo), PasteImageError> {`
- `fn` `codex-rs/tui/src/clipboard_paste.rs:113` `pub fn paste_image_as_png() -> Result<(Vec<u8>, PastedImageInfo), PasteImageError> {`
- `fn` `codex-rs/tui/src/clipboard_paste.rs:121` `pub fn paste_image_to_temp_png() -> Result<(PathBuf, PastedImageInfo), PasteImageError> {`
- `fn` `codex-rs/tui/src/clipboard_paste.rs:159` `fn try_wsl_clipboard_fallback(`
- `use` `codex-rs/tui/src/clipboard_paste.rs:162` `use PasteImageError::ClipboardUnavailable;`
- `use` `codex-rs/tui/src/clipboard_paste.rs:163` `use PasteImageError::NoImage;`
- `fn` `codex-rs/tui/src/clipboard_paste.rs:199` `fn try_dump_windows_clipboard_image() -> Option<String> {`
- `fn` `codex-rs/tui/src/clipboard_paste.rs:232` `pub fn paste_image_to_temp_png() -> Result<(PathBuf, PastedImageInfo), PasteImageError> {`
- `fn` `codex-rs/tui/src/clipboard_paste.rs:245` `pub fn normalize_pasted_path(pasted: &str) -> Option<PathBuf> {`
- `fn` `codex-rs/tui/src/clipboard_paste.rs:300` `fn convert_windows_path_to_wsl(input: &str) -> Option<PathBuf> {`
- `fn` `codex-rs/tui/src/clipboard_paste.rs:327` `fn normalize_windows_path(input: &str) -> Option<PathBuf> {`
- `fn` `codex-rs/tui/src/clipboard_paste.rs:358` `pub fn pasted_image_format(path: &Path) -> EncodedImageFormat {`
- `use` `codex-rs/tui/src/clipboard_paste.rs:373` `use super::*;`
- `fn` `codex-rs/tui/src/clipboard_paste.rs:377` `fn normalize_file_url() {`
- `fn` `codex-rs/tui/src/clipboard_paste.rs:384` `fn normalize_file_url_windows() {`
- `fn` `codex-rs/tui/src/clipboard_paste.rs:401` `fn normalize_shell_escaped_single_path() {`
- `fn` `codex-rs/tui/src/clipboard_paste.rs:408` `fn normalize_simple_quoted_path_fallback() {`
- `fn` `codex-rs/tui/src/clipboard_paste.rs:415` `fn normalize_single_quoted_unix_path() {`
- `fn` `codex-rs/tui/src/clipboard_paste.rs:422` `fn normalize_multiple_tokens_returns_none() {`
- `fn` `codex-rs/tui/src/clipboard_paste.rs:430` `fn pasted_image_format_png_jpeg_unknown() {`
- `fn` `codex-rs/tui/src/clipboard_paste.rs:454` `fn normalize_single_quoted_windows_path() {`
- `fn` `codex-rs/tui/src/clipboard_paste.rs:473` `fn normalize_double_quoted_windows_path() {`
- `fn` `codex-rs/tui/src/clipboard_paste.rs:492` `fn normalize_unquoted_windows_path_with_spaces() {`
- `fn` `codex-rs/tui/src/clipboard_paste.rs:509` `fn normalize_unc_windows_path() {`
- `fn` `codex-rs/tui/src/clipboard_paste.rs:519` `fn pasted_image_format_with_windows_style_paths() {`
- `fn` `codex-rs/tui/src/clipboard_paste.rs:536` `fn normalize_windows_path_in_wsl() {`

## Dependencies (auto sample)
### Imports / Includes
- `use std::path::Path;`
- `use std::path::PathBuf;`
- `use tempfile::Builder;`
- `use PasteImageError::ClipboardUnavailable;`
- `use PasteImageError::NoImage;`
- `use super::*;`
### Referenced env vars
- `WSL_DISTRO_NAME`
- `WSL_INTEROP`

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- `workdocjcl/spec/06_UI/TUI.md`
