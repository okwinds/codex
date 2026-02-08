# `codex-rs/windows-sandbox-rs/src/policy.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `1838`
- sha256: `82606be20a81be57f1352f1b4604ed2baae0f0caf95cfdf26a5c4236ab1b0c20`
- generated_utc: `2026-02-08T10:45:41Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/windows-sandbox-rs/src/policy.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub fn parse_policy(value: &str) -> Result<SandboxPolicy> {`

## Definitions (auto, per-file)
- `use` `codex-rs/windows-sandbox-rs/src/policy.rs:1` `use anyhow::Result;`
- `fn` `codex-rs/windows-sandbox-rs/src/policy.rs:4` `pub fn parse_policy(value: &str) -> Result<SandboxPolicy> {`
- `use` `codex-rs/windows-sandbox-rs/src/policy.rs:28` `use super::*;`
- `use` `codex-rs/windows-sandbox-rs/src/policy.rs:29` `use pretty_assertions::assert_eq;`
- `fn` `codex-rs/windows-sandbox-rs/src/policy.rs:32` `fn rejects_external_sandbox_preset() {`
- `fn` `codex-rs/windows-sandbox-rs/src/policy.rs:40` `fn rejects_external_sandbox_json() {`
- `fn` `codex-rs/windows-sandbox-rs/src/policy.rs:54` `fn parses_read_only_policy() {`

## Dependencies (auto sample)
### Imports / Includes
- `use anyhow::Result;`
- `use super::*;`
- `use pretty_assertions::assert_eq;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
