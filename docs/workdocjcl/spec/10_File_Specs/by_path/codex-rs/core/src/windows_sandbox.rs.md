# `codex-rs/core/src/windows_sandbox.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `4933`
- sha256: `7385a26cc1873fe93d5d53a5adffb3f169ce4fce2c168006dd3332b22215fb19`
- generated_utc: `2026-02-03T16:08:29Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/windows_sandbox.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub trait WindowsSandboxLevelExt {`
- `pub fn windows_sandbox_level_from_config(config: &Config) -> WindowsSandboxLevel {`
- `pub fn windows_sandbox_level_from_features(features: &Features) -> WindowsSandboxLevel {`
- `pub fn sandbox_setup_is_complete(codex_home: &Path) -> bool {`
- `pub fn sandbox_setup_is_complete(_codex_home: &Path) -> bool {`
- `pub fn elevated_setup_failure_details(err: &anyhow::Error) -> Option<(String, String)> {`
- `pub fn elevated_setup_failure_details(_err: &anyhow::Error) -> Option<(String, String)> {`
- `pub fn elevated_setup_failure_metric_name(err: &anyhow::Error) -> &'static str {`
- `pub fn elevated_setup_failure_metric_name(_err: &anyhow::Error) -> &'static str {`
- `pub fn run_elevated_setup(`
- `pub fn run_elevated_setup(`

## Definitions (auto, per-file)
- `use` `codex-rs/core/src/windows_sandbox.rs:1` `use crate::config::Config;`
- `use` `codex-rs/core/src/windows_sandbox.rs:2` `use crate::features::Feature;`
- `use` `codex-rs/core/src/windows_sandbox.rs:3` `use crate::features::Features;`
- `use` `codex-rs/core/src/windows_sandbox.rs:4` `use crate::protocol::SandboxPolicy;`
- `use` `codex-rs/core/src/windows_sandbox.rs:5` `use codex_protocol::config_types::WindowsSandboxLevel;`
- `use` `codex-rs/core/src/windows_sandbox.rs:6` `use std::collections::HashMap;`
- `use` `codex-rs/core/src/windows_sandbox.rs:7` `use std::path::Path;`
- `const` `codex-rs/core/src/windows_sandbox.rs:13` `pub const ELEVATED_SANDBOX_NUX_ENABLED: bool = true;`
- `trait` `codex-rs/core/src/windows_sandbox.rs:15` `pub trait WindowsSandboxLevelExt {`
- `fn` `codex-rs/core/src/windows_sandbox.rs:16` `fn from_config(config: &Config) -> WindowsSandboxLevel;`
- `fn` `codex-rs/core/src/windows_sandbox.rs:17` `fn from_features(features: &Features) -> WindowsSandboxLevel;`
- `impl` `codex-rs/core/src/windows_sandbox.rs:20` `impl WindowsSandboxLevelExt for WindowsSandboxLevel {`
- `fn` `codex-rs/core/src/windows_sandbox.rs:21` `fn from_config(config: &Config) -> WindowsSandboxLevel {`
- `fn` `codex-rs/core/src/windows_sandbox.rs:25` `fn from_features(features: &Features) -> WindowsSandboxLevel {`
- `fn` `codex-rs/core/src/windows_sandbox.rs:37` `pub fn windows_sandbox_level_from_config(config: &Config) -> WindowsSandboxLevel {`
- `fn` `codex-rs/core/src/windows_sandbox.rs:41` `pub fn windows_sandbox_level_from_features(features: &Features) -> WindowsSandboxLevel {`
- `fn` `codex-rs/core/src/windows_sandbox.rs:46` `pub fn sandbox_setup_is_complete(codex_home: &Path) -> bool {`
- `fn` `codex-rs/core/src/windows_sandbox.rs:51` `pub fn sandbox_setup_is_complete(_codex_home: &Path) -> bool {`
- `fn` `codex-rs/core/src/windows_sandbox.rs:56` `pub fn elevated_setup_failure_details(err: &anyhow::Error) -> Option<(String, String)> {`
- `fn` `codex-rs/core/src/windows_sandbox.rs:64` `pub fn elevated_setup_failure_details(_err: &anyhow::Error) -> Option<(String, String)> {`
- `fn` `codex-rs/core/src/windows_sandbox.rs:69` `pub fn elevated_setup_failure_metric_name(err: &anyhow::Error) -> &'static str {`
- `fn` `codex-rs/core/src/windows_sandbox.rs:83` `pub fn elevated_setup_failure_metric_name(_err: &anyhow::Error) -> &'static str {`
- `fn` `codex-rs/core/src/windows_sandbox.rs:88` `pub fn run_elevated_setup(`
- `fn` `codex-rs/core/src/windows_sandbox.rs:107` `pub fn run_elevated_setup(`
- `use` `codex-rs/core/src/windows_sandbox.rs:119` `use super::*;`
- `use` `codex-rs/core/src/windows_sandbox.rs:120` `use crate::features::Features;`
- `use` `codex-rs/core/src/windows_sandbox.rs:121` `use pretty_assertions::assert_eq;`
- `fn` `codex-rs/core/src/windows_sandbox.rs:124` `fn elevated_flag_works_by_itself() {`
- `fn` `codex-rs/core/src/windows_sandbox.rs:135` `fn restricted_token_flag_works_by_itself() {`
- `fn` `codex-rs/core/src/windows_sandbox.rs:146` `fn no_flags_means_no_sandbox() {`
- `fn` `codex-rs/core/src/windows_sandbox.rs:156` `fn elevated_wins_when_both_flags_are_enabled() {`

## Dependencies (auto sample)
### Imports / Includes
- `use crate::config::Config;`
- `use crate::features::Feature;`
- `use crate::features::Features;`
- `use crate::protocol::SandboxPolicy;`
- `use codex_protocol::config_types::WindowsSandboxLevel;`
- `use std::collections::HashMap;`
- `use std::path::Path;`
- `use super::*;`
- `use crate::features::Features;`
- `use pretty_assertions::assert_eq;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- `workdocjcl/spec/00_Overview/ARCHITECTURE.md`
