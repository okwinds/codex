# `codex-rs/ollama/src/lib.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `2983`
- sha256: `689e1601e42302b2dd5446361a34ff36af869cfd54acb0eecfd2903ccfcc82c5`
- generated_utc: `2026-02-08T10:45:38Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/ollama/src/lib.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `mod` `codex-rs/ollama/src/lib.rs:1` `mod client;`
- `mod` `codex-rs/ollama/src/lib.rs:2` `mod parser;`
- `mod` `codex-rs/ollama/src/lib.rs:3` `mod pull;`
- `mod` `codex-rs/ollama/src/lib.rs:4` `mod url;`
- `use` `codex-rs/ollama/src/lib.rs:7` `use codex_core::ModelProviderInfo;`
- `use` `codex-rs/ollama/src/lib.rs:8` `use codex_core::config::Config;`
- `use` `codex-rs/ollama/src/lib.rs:13` `use semver::Version;`
- `const` `codex-rs/ollama/src/lib.rs:16` `pub const DEFAULT_OSS_MODEL: &str = "gpt-oss:20b";`
- `fn` `codex-rs/ollama/src/lib.rs:22` `pub async fn ensure_oss_ready(config: &Config) -> std::io::Result<()> {`
- `fn` `codex-rs/ollama/src/lib.rs:51` `fn min_responses_version() -> Version {`
- `fn` `codex-rs/ollama/src/lib.rs:55` `fn supports_responses(version: &Version) -> bool {`
- `fn` `codex-rs/ollama/src/lib.rs:62` `pub async fn ensure_responses_supported(provider: &ModelProviderInfo) -> std::io::Result<()> {`
- `use` `codex-rs/ollama/src/lib.rs:80` `use super::*;`
- `fn` `codex-rs/ollama/src/lib.rs:83` `fn supports_responses_for_dev_zero() {`
- `fn` `codex-rs/ollama/src/lib.rs:88` `fn does_not_support_responses_before_cutoff() {`
- `fn` `codex-rs/ollama/src/lib.rs:93` `fn supports_responses_at_or_after_cutoff() {`

## Dependencies (auto sample)
### Imports / Includes
- `use codex_core::ModelProviderInfo;`
- `use codex_core::config::Config;`
- `use semver::Version;`
- `use super::*;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
