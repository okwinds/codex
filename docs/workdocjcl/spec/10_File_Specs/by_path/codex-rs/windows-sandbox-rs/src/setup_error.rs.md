# `codex-rs/windows-sandbox-rs/src/setup_error.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `10821`
- sha256: `2c71f811e432ed8e2052e19863ee9ed02c5a6445b6332f579cf0c63bdadbae5a`
- generated_utc: `2026-02-08T10:45:41Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/windows-sandbox-rs/src/setup_error.rs` (read)
- env: `USER`, `USERNAME`

### Outputs / Side Effects
- writes to filesystem

## Public Surface (auto)
- `pub enum SetupErrorCode {`
- `pub fn as_str(self) -> &'static str {`
- `pub struct SetupErrorReport {`
- `pub struct SetupFailure {`
- `pub fn new(code: SetupErrorCode, message: impl Into<String>) -> Self {`
- `pub fn from_report(report: SetupErrorReport) -> Self {`
- `pub fn metric_message(&self) -> String {`
- `pub fn failure(code: SetupErrorCode, message: impl Into<String>) -> anyhow::Error {`
- `pub fn extract_failure(err: &anyhow::Error) -> Option<&SetupFailure> {`
- `pub fn setup_error_path(codex_home: &Path) -> PathBuf {`
- `pub fn clear_setup_error_report(codex_home: &Path) -> Result<()> {`
- `pub fn write_setup_error_report(codex_home: &Path, report: &SetupErrorReport) -> Result<()> {`
- `pub fn read_setup_error_report(codex_home: &Path) -> Result<Option<SetupErrorReport>> {`
- `pub fn sanitize_setup_metric_tag_value(value: &str) -> String {`

## Definitions (auto, per-file)
- `use` `codex-rs/windows-sandbox-rs/src/setup_error.rs:1` `use anyhow::Context;`
- `use` `codex-rs/windows-sandbox-rs/src/setup_error.rs:2` `use anyhow::Result;`
- `use` `codex-rs/windows-sandbox-rs/src/setup_error.rs:3` `use codex_utils_string::sanitize_metric_tag_value;`
- `use` `codex-rs/windows-sandbox-rs/src/setup_error.rs:4` `use serde::Deserialize;`
- `use` `codex-rs/windows-sandbox-rs/src/setup_error.rs:5` `use serde::Serialize;`
- `use` `codex-rs/windows-sandbox-rs/src/setup_error.rs:6` `use std::fs;`
- `use` `codex-rs/windows-sandbox-rs/src/setup_error.rs:7` `use std::io::ErrorKind;`
- `use` `codex-rs/windows-sandbox-rs/src/setup_error.rs:8` `use std::path::Path;`
- `use` `codex-rs/windows-sandbox-rs/src/setup_error.rs:9` `use std::path::PathBuf;`
- `enum` `codex-rs/windows-sandbox-rs/src/setup_error.rs:16` `pub enum SetupErrorCode {`
- `impl` `codex-rs/windows-sandbox-rs/src/setup_error.rs:71` `impl SetupErrorCode {`
- `fn` `codex-rs/windows-sandbox-rs/src/setup_error.rs:72` `pub fn as_str(self) -> &'static str {`
- `struct` `codex-rs/windows-sandbox-rs/src/setup_error.rs:106` `pub struct SetupErrorReport {`
- `struct` `codex-rs/windows-sandbox-rs/src/setup_error.rs:112` `pub struct SetupFailure {`
- `impl` `codex-rs/windows-sandbox-rs/src/setup_error.rs:117` `impl SetupFailure {`
- `fn` `codex-rs/windows-sandbox-rs/src/setup_error.rs:118` `pub fn new(code: SetupErrorCode, message: impl Into<String>) -> Self {`
- `fn` `codex-rs/windows-sandbox-rs/src/setup_error.rs:125` `pub fn from_report(report: SetupErrorReport) -> Self {`
- `fn` `codex-rs/windows-sandbox-rs/src/setup_error.rs:129` `pub fn metric_message(&self) -> String {`
- `impl` `codex-rs/windows-sandbox-rs/src/setup_error.rs:134` `impl std::fmt::Display for SetupFailure {`
- `fn` `codex-rs/windows-sandbox-rs/src/setup_error.rs:135` `fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {`
- `fn` `codex-rs/windows-sandbox-rs/src/setup_error.rs:142` `pub fn failure(code: SetupErrorCode, message: impl Into<String>) -> anyhow::Error {`
- `fn` `codex-rs/windows-sandbox-rs/src/setup_error.rs:146` `pub fn extract_failure(err: &anyhow::Error) -> Option<&SetupFailure> {`
- `fn` `codex-rs/windows-sandbox-rs/src/setup_error.rs:150` `pub fn setup_error_path(codex_home: &Path) -> PathBuf {`
- `fn` `codex-rs/windows-sandbox-rs/src/setup_error.rs:154` `pub fn clear_setup_error_report(codex_home: &Path) -> Result<()> {`
- `fn` `codex-rs/windows-sandbox-rs/src/setup_error.rs:163` `pub fn write_setup_error_report(codex_home: &Path, report: &SetupErrorReport) -> Result<()> {`
- `fn` `codex-rs/windows-sandbox-rs/src/setup_error.rs:173` `pub fn read_setup_error_report(codex_home: &Path) -> Result<Option<SetupErrorReport>> {`
- `fn` `codex-rs/windows-sandbox-rs/src/setup_error.rs:186` `pub fn sanitize_setup_metric_tag_value(value: &str) -> String {`
- `fn` `codex-rs/windows-sandbox-rs/src/setup_error.rs:190` `fn redact_home_paths(value: &str) -> String {`
- `fn` `codex-rs/windows-sandbox-rs/src/setup_error.rs:206` `fn redact_username_segments(value: &str, usernames: &[String]) -> String {`
- `use` `codex-rs/windows-sandbox-rs/src/setup_error.rs:250` `use super::redact_username_segments;`
- `use` `codex-rs/windows-sandbox-rs/src/setup_error.rs:251` `use pretty_assertions::assert_eq;`
- `fn` `codex-rs/windows-sandbox-rs/src/setup_error.rs:254` `fn sanitize_tag_value_redacts_username_segments() {`
- `fn` `codex-rs/windows-sandbox-rs/src/setup_error.rs:265` `fn sanitize_tag_value_leaves_unknown_segments() {`
- `fn` `codex-rs/windows-sandbox-rs/src/setup_error.rs:273` `fn sanitize_tag_value_redacts_multiple_occurrences() {`

## Dependencies (auto sample)
### Imports / Includes
- `use anyhow::Context;`
- `use anyhow::Result;`
- `use codex_utils_string::sanitize_metric_tag_value;`
- `use serde::Deserialize;`
- `use serde::Serialize;`
- `use std::fs;`
- `use std::io::ErrorKind;`
- `use std::path::Path;`
- `use std::path::PathBuf;`
- `use super::redact_username_segments;`
- `use pretty_assertions::assert_eq;`
### Referenced env vars
- `USER`
- `USERNAME`

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
