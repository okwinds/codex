# `codex-rs/ollama/src/lib.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `3451`
- sha256: `a1cc5e2fff7548f893b5a708f185745ed7c63b198c84f102854cc309f10a8aad`
- generated_utc: `2026-02-03T16:08:30Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/ollama/src/lib.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub struct WireApiDetection {`

## Definitions (auto, per-file)
- `mod` `codex-rs/ollama/src/lib.rs:1` `mod client;`
- `mod` `codex-rs/ollama/src/lib.rs:2` `mod parser;`
- `mod` `codex-rs/ollama/src/lib.rs:3` `mod pull;`
- `mod` `codex-rs/ollama/src/lib.rs:4` `mod url;`
- `use` `codex-rs/ollama/src/lib.rs:7` `use codex_core::ModelProviderInfo;`
- `use` `codex-rs/ollama/src/lib.rs:8` `use codex_core::WireApi;`
- `use` `codex-rs/ollama/src/lib.rs:9` `use codex_core::config::Config;`
- `use` `codex-rs/ollama/src/lib.rs:14` `use semver::Version;`
- `const` `codex-rs/ollama/src/lib.rs:17` `pub const DEFAULT_OSS_MODEL: &str = "gpt-oss:20b";`
- `struct` `codex-rs/ollama/src/lib.rs:19` `pub struct WireApiDetection {`
- `fn` `codex-rs/ollama/src/lib.rs:28` `pub async fn ensure_oss_ready(config: &Config) -> std::io::Result<()> {`
- `fn` `codex-rs/ollama/src/lib.rs:57` `fn min_responses_version() -> Version {`
- `fn` `codex-rs/ollama/src/lib.rs:61` `fn wire_api_for_version(version: &Version) -> WireApi {`
- `fn` `codex-rs/ollama/src/lib.rs:72` `pub async fn detect_wire_api(`
- `use` `codex-rs/ollama/src/lib.rs:90` `use super::*;`
- `use` `codex-rs/ollama/src/lib.rs:91` `use pretty_assertions::assert_eq;`
- `fn` `codex-rs/ollama/src/lib.rs:94` `fn test_wire_api_for_version_dev_zero_keeps_responses() {`
- `fn` `codex-rs/ollama/src/lib.rs:102` `fn test_wire_api_for_version_before_cutoff_is_chat() {`
- `fn` `codex-rs/ollama/src/lib.rs:107` `fn test_wire_api_for_version_at_or_after_cutoff_is_responses() {`

## Dependencies (auto sample)
### Imports / Includes
- `use codex_core::ModelProviderInfo;`
- `use codex_core::WireApi;`
- `use codex_core::config::Config;`
- `use semver::Version;`
- `use super::*;`
- `use pretty_assertions::assert_eq;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
