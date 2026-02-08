# `codex-rs/utils/absolute-path/src/lib.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `9155`
- sha256: `420ddc787d03254560f7bb3dfc8f1d089408e54b5f82f50e8cef9026b9aaa448`
- generated_utc: `2026-02-08T10:45:41Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/utils/absolute-path/src/lib.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub struct AbsolutePathBuf(PathBuf);`
- `pub fn current_dir() -> std::io::Result<Self> {`
- `pub fn parent(&self) -> Option<Self> {`
- `pub fn as_path(&self) -> &Path {`
- `pub fn into_path_buf(self) -> PathBuf {`
- `pub fn to_path_buf(&self) -> PathBuf {`
- `pub fn to_string_lossy(&self) -> std::borrow::Cow<'_, str> {`
- `pub fn display(&self) -> Display<'_> {`
- `pub struct AbsolutePathBufGuard;`
- `pub fn new(base_path: &Path) -> Self {`

## Definitions (auto, per-file)
- `use` `codex-rs/utils/absolute-path/src/lib.rs:1` `use dirs::home_dir;`
- `use` `codex-rs/utils/absolute-path/src/lib.rs:2` `use path_absolutize::Absolutize;`
- `use` `codex-rs/utils/absolute-path/src/lib.rs:3` `use schemars::JsonSchema;`
- `use` `codex-rs/utils/absolute-path/src/lib.rs:4` `use serde::Deserialize;`
- `use` `codex-rs/utils/absolute-path/src/lib.rs:5` `use serde::Deserializer;`
- `use` `codex-rs/utils/absolute-path/src/lib.rs:6` `use serde::Serialize;`
- `use` `codex-rs/utils/absolute-path/src/lib.rs:7` `use serde::de::Error as SerdeError;`
- `use` `codex-rs/utils/absolute-path/src/lib.rs:8` `use std::cell::RefCell;`
- `use` `codex-rs/utils/absolute-path/src/lib.rs:9` `use std::path::Display;`
- `use` `codex-rs/utils/absolute-path/src/lib.rs:10` `use std::path::Path;`
- `use` `codex-rs/utils/absolute-path/src/lib.rs:11` `use std::path::PathBuf;`
- `use` `codex-rs/utils/absolute-path/src/lib.rs:12` `use ts_rs::TS;`
- `struct` `codex-rs/utils/absolute-path/src/lib.rs:22` `pub struct AbsolutePathBuf(PathBuf);`
- `impl` `codex-rs/utils/absolute-path/src/lib.rs:24` `impl AbsolutePathBuf {`
- `fn` `codex-rs/utils/absolute-path/src/lib.rs:25` `fn maybe_expand_home_directory(path: &Path) -> PathBuf {`
- `fn` `codex-rs/utils/absolute-path/src/lib.rs:61` `pub fn current_dir() -> std::io::Result<Self> {`
- `fn` `codex-rs/utils/absolute-path/src/lib.rs:70` `pub fn parent(&self) -> Option<Self> {`
- `fn` `codex-rs/utils/absolute-path/src/lib.rs:77` `pub fn as_path(&self) -> &Path {`
- `fn` `codex-rs/utils/absolute-path/src/lib.rs:81` `pub fn into_path_buf(self) -> PathBuf {`
- `fn` `codex-rs/utils/absolute-path/src/lib.rs:85` `pub fn to_path_buf(&self) -> PathBuf {`
- `fn` `codex-rs/utils/absolute-path/src/lib.rs:89` `pub fn to_string_lossy(&self) -> std::borrow::Cow<'_, str> {`
- `fn` `codex-rs/utils/absolute-path/src/lib.rs:93` `pub fn display(&self) -> Display<'_> {`
- `impl` `codex-rs/utils/absolute-path/src/lib.rs:98` `impl AsRef<Path> for AbsolutePathBuf {`
- `fn` `codex-rs/utils/absolute-path/src/lib.rs:99` `fn as_ref(&self) -> &Path {`
- `impl` `codex-rs/utils/absolute-path/src/lib.rs:104` `impl From<AbsolutePathBuf> for PathBuf {`
- `fn` `codex-rs/utils/absolute-path/src/lib.rs:105` `fn from(path: AbsolutePathBuf) -> Self {`
- `impl` `codex-rs/utils/absolute-path/src/lib.rs:110` `impl TryFrom<&Path> for AbsolutePathBuf {`
- `type` `codex-rs/utils/absolute-path/src/lib.rs:111` `type Error = std::io::Error;`
- `fn` `codex-rs/utils/absolute-path/src/lib.rs:113` `fn try_from(value: &Path) -> Result<Self, Self::Error> {`
- `impl` `codex-rs/utils/absolute-path/src/lib.rs:118` `impl TryFrom<PathBuf> for AbsolutePathBuf {`
- `type` `codex-rs/utils/absolute-path/src/lib.rs:119` `type Error = std::io::Error;`
- `fn` `codex-rs/utils/absolute-path/src/lib.rs:121` `fn try_from(value: PathBuf) -> Result<Self, Self::Error> {`
- `impl` `codex-rs/utils/absolute-path/src/lib.rs:126` `impl TryFrom<&str> for AbsolutePathBuf {`
- `type` `codex-rs/utils/absolute-path/src/lib.rs:127` `type Error = std::io::Error;`
- `fn` `codex-rs/utils/absolute-path/src/lib.rs:129` `fn try_from(value: &str) -> Result<Self, Self::Error> {`
- `impl` `codex-rs/utils/absolute-path/src/lib.rs:134` `impl TryFrom<String> for AbsolutePathBuf {`
- `type` `codex-rs/utils/absolute-path/src/lib.rs:135` `type Error = std::io::Error;`
- `fn` `codex-rs/utils/absolute-path/src/lib.rs:137` `fn try_from(value: String) -> Result<Self, Self::Error> {`
- `static` `codex-rs/utils/absolute-path/src/lib.rs:143` `static ABSOLUTE_PATH_BASE: RefCell<Option<PathBuf>> = const { RefCell::new(None) };`
- `struct` `codex-rs/utils/absolute-path/src/lib.rs:150` `pub struct AbsolutePathBufGuard;`
- `impl` `codex-rs/utils/absolute-path/src/lib.rs:152` `impl AbsolutePathBufGuard {`
- `fn` `codex-rs/utils/absolute-path/src/lib.rs:153` `pub fn new(base_path: &Path) -> Self {`
- `impl` `codex-rs/utils/absolute-path/src/lib.rs:161` `impl Drop for AbsolutePathBufGuard {`
- `fn` `codex-rs/utils/absolute-path/src/lib.rs:162` `fn drop(&mut self) {`
- `impl` `codex-rs/utils/absolute-path/src/lib.rs:169` `impl<'de> Deserialize<'de> for AbsolutePathBuf {`
- `use` `codex-rs/utils/absolute-path/src/lib.rs:191` `use super::*;`
- `use` `codex-rs/utils/absolute-path/src/lib.rs:192` `use pretty_assertions::assert_eq;`
- `use` `codex-rs/utils/absolute-path/src/lib.rs:193` `use tempfile::tempdir;`
- `fn` `codex-rs/utils/absolute-path/src/lib.rs:196` `fn create_with_absolute_path_ignores_base_path() {`
- `fn` `codex-rs/utils/absolute-path/src/lib.rs:208` `fn relative_path_is_resolved_against_base_path() {`
- `fn` `codex-rs/utils/absolute-path/src/lib.rs:217` `fn guard_used_in_deserialization() {`
- `fn` `codex-rs/utils/absolute-path/src/lib.rs:234` `fn home_directory_root_on_non_windows_is_expanded_in_deserialization() {`
- `fn` `codex-rs/utils/absolute-path/src/lib.rs:248` `fn home_directory_subpath_on_non_windows_is_expanded_in_deserialization() {`
- `fn` `codex-rs/utils/absolute-path/src/lib.rs:262` `fn home_directory_double_slash_on_non_windows_is_expanded_in_deserialization() {`
- `fn` `codex-rs/utils/absolute-path/src/lib.rs:276` `fn home_directory_on_windows_is_not_expanded_in_deserialization() {`

## Dependencies (auto sample)
### Imports / Includes
- `use dirs::home_dir;`
- `use path_absolutize::Absolutize;`
- `use schemars::JsonSchema;`
- `use serde::Deserialize;`
- `use serde::Deserializer;`
- `use serde::Serialize;`
- `use serde::de::Error as SerdeError;`
- `use std::cell::RefCell;`
- `use std::path::Display;`
- `use std::path::Path;`
- `use std::path::PathBuf;`
- `use ts_rs::TS;`
- `use super::*;`
- `use pretty_assertions::assert_eq;`
- `use tempfile::tempdir;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
