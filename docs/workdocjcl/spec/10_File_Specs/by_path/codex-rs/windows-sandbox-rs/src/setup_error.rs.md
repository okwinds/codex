# `codex-rs/windows-sandbox-rs/src/setup_error.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `11312`
- sha256: `87432386061ccfc41539a7ad785c3c6098189481542933837163d8b5684f3446`
- generated_utc: `2026-02-03T16:08:31Z`

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
- `pub fn sanitize_tag_value(value: &str) -> String {`

## Definitions (auto, per-file)
- `use` `codex-rs/windows-sandbox-rs/src/setup_error.rs:1` `use anyhow::Context;`
- `use` `codex-rs/windows-sandbox-rs/src/setup_error.rs:2` `use anyhow::Result;`
- `use` `codex-rs/windows-sandbox-rs/src/setup_error.rs:3` `use serde::Deserialize;`
- `use` `codex-rs/windows-sandbox-rs/src/setup_error.rs:4` `use serde::Serialize;`
- `use` `codex-rs/windows-sandbox-rs/src/setup_error.rs:5` `use std::fs;`
- `use` `codex-rs/windows-sandbox-rs/src/setup_error.rs:6` `use std::io::ErrorKind;`
- `use` `codex-rs/windows-sandbox-rs/src/setup_error.rs:7` `use std::path::Path;`
- `use` `codex-rs/windows-sandbox-rs/src/setup_error.rs:8` `use std::path::PathBuf;`
- `enum` `codex-rs/windows-sandbox-rs/src/setup_error.rs:15` `pub enum SetupErrorCode {`
- `impl` `codex-rs/windows-sandbox-rs/src/setup_error.rs:70` `impl SetupErrorCode {`
- `fn` `codex-rs/windows-sandbox-rs/src/setup_error.rs:71` `pub fn as_str(self) -> &'static str {`
- `struct` `codex-rs/windows-sandbox-rs/src/setup_error.rs:105` `pub struct SetupErrorReport {`
- `struct` `codex-rs/windows-sandbox-rs/src/setup_error.rs:111` `pub struct SetupFailure {`
- `impl` `codex-rs/windows-sandbox-rs/src/setup_error.rs:116` `impl SetupFailure {`
- `fn` `codex-rs/windows-sandbox-rs/src/setup_error.rs:117` `pub fn new(code: SetupErrorCode, message: impl Into<String>) -> Self {`
- `fn` `codex-rs/windows-sandbox-rs/src/setup_error.rs:124` `pub fn from_report(report: SetupErrorReport) -> Self {`
- `fn` `codex-rs/windows-sandbox-rs/src/setup_error.rs:128` `pub fn metric_message(&self) -> String {`
- `impl` `codex-rs/windows-sandbox-rs/src/setup_error.rs:133` `impl std::fmt::Display for SetupFailure {`
- `fn` `codex-rs/windows-sandbox-rs/src/setup_error.rs:134` `fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {`
- `fn` `codex-rs/windows-sandbox-rs/src/setup_error.rs:141` `pub fn failure(code: SetupErrorCode, message: impl Into<String>) -> anyhow::Error {`
- `fn` `codex-rs/windows-sandbox-rs/src/setup_error.rs:145` `pub fn extract_failure(err: &anyhow::Error) -> Option<&SetupFailure> {`
- `fn` `codex-rs/windows-sandbox-rs/src/setup_error.rs:149` `pub fn setup_error_path(codex_home: &Path) -> PathBuf {`
- `fn` `codex-rs/windows-sandbox-rs/src/setup_error.rs:153` `pub fn clear_setup_error_report(codex_home: &Path) -> Result<()> {`
- `fn` `codex-rs/windows-sandbox-rs/src/setup_error.rs:162` `pub fn write_setup_error_report(codex_home: &Path, report: &SetupErrorReport) -> Result<()> {`
- `fn` `codex-rs/windows-sandbox-rs/src/setup_error.rs:172` `pub fn read_setup_error_report(codex_home: &Path) -> Result<Option<SetupErrorReport>> {`
- `fn` `codex-rs/windows-sandbox-rs/src/setup_error.rs:186` `pub fn sanitize_tag_value(value: &str) -> String {`
- `const` `codex-rs/windows-sandbox-rs/src/setup_error.rs:187` `const MAX_LEN: usize = 256;`
- `fn` `codex-rs/windows-sandbox-rs/src/setup_error.rs:210` `fn redact_home_paths(value: &str) -> String {`
- `fn` `codex-rs/windows-sandbox-rs/src/setup_error.rs:226` `fn redact_username_segments(value: &str, usernames: &[String]) -> String {`
- `use` `codex-rs/windows-sandbox-rs/src/setup_error.rs:270` `use super::*;`
- `use` `codex-rs/windows-sandbox-rs/src/setup_error.rs:271` `use pretty_assertions::assert_eq;`
- `fn` `codex-rs/windows-sandbox-rs/src/setup_error.rs:274` `fn sanitize_tag_value_redacts_username_segments() {`
- `fn` `codex-rs/windows-sandbox-rs/src/setup_error.rs:285` `fn sanitize_tag_value_leaves_unknown_segments() {`
- `fn` `codex-rs/windows-sandbox-rs/src/setup_error.rs:293` `fn sanitize_tag_value_redacts_multiple_occurrences() {`

## Dependencies (auto sample)
### Imports / Includes
- `use anyhow::Context;`
- `use anyhow::Result;`
- `use serde::Deserialize;`
- `use serde::Serialize;`
- `use std::fs;`
- `use std::io::ErrorKind;`
- `use std::path::Path;`
- `use std::path::PathBuf;`
- `use super::*;`
- `use pretty_assertions::assert_eq;`
### Referenced env vars
- `USER`
- `USERNAME`

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
