# `codex-rs/core/src/skills/remote.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `9652`
- sha256: `b432cab1ed639c4b96bde1b0cddcf3194d49c1438a101cfabcbbe6c9e1021334`
- generated_utc: `2026-02-08T10:45:33Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/skills/remote.rs` (read)

### Outputs / Side Effects
- writes to filesystem

## Public Surface (auto)
- `pub struct RemoteSkillSummary {`
- `pub struct RemoteSkillDownload {`
- `pub struct RemoteSkillDownloadResult {`
- `pub struct RemoteSkillFileRange {`

## Definitions (auto, per-file)
- `use` `codex-rs/core/src/skills/remote.rs:1` `use anyhow::Context;`
- `use` `codex-rs/core/src/skills/remote.rs:2` `use anyhow::Result;`
- `use` `codex-rs/core/src/skills/remote.rs:3` `use serde::Deserialize;`
- `use` `codex-rs/core/src/skills/remote.rs:4` `use std::collections::HashMap;`
- `use` `codex-rs/core/src/skills/remote.rs:5` `use std::collections::HashSet;`
- `use` `codex-rs/core/src/skills/remote.rs:6` `use std::path::Component;`
- `use` `codex-rs/core/src/skills/remote.rs:7` `use std::path::Path;`
- `use` `codex-rs/core/src/skills/remote.rs:8` `use std::path::PathBuf;`
- `use` `codex-rs/core/src/skills/remote.rs:9` `use std::time::Duration;`
- `use` `codex-rs/core/src/skills/remote.rs:11` `use crate::config::Config;`
- `use` `codex-rs/core/src/skills/remote.rs:12` `use crate::default_client::build_reqwest_client;`
- `const` `codex-rs/core/src/skills/remote.rs:14` `const REMOTE_SKILLS_API_TIMEOUT: Duration = Duration::from_secs(30);`
- `struct` `codex-rs/core/src/skills/remote.rs:17` `pub struct RemoteSkillSummary {`
- `struct` `codex-rs/core/src/skills/remote.rs:24` `pub struct RemoteSkillDownload {`
- `struct` `codex-rs/core/src/skills/remote.rs:32` `pub struct RemoteSkillDownloadResult {`
- `struct` `codex-rs/core/src/skills/remote.rs:39` `pub struct RemoteSkillFileRange {`
- `struct` `codex-rs/core/src/skills/remote.rs:45` `struct RemoteSkillsResponse {`
- `struct` `codex-rs/core/src/skills/remote.rs:50` `struct RemoteSkill {`
- `struct` `codex-rs/core/src/skills/remote.rs:57` `struct RemoteSkillsDownloadResponse {`
- `struct` `codex-rs/core/src/skills/remote.rs:62` `struct RemoteSkillDownloadPayload {`
- `struct` `codex-rs/core/src/skills/remote.rs:71` `struct RemoteSkillFileRangePayload {`
- `fn` `codex-rs/core/src/skills/remote.rs:76` `pub async fn list_remote_skills(config: &Config) -> Result<Vec<RemoteSkillSummary>> {`
- `fn` `codex-rs/core/src/skills/remote.rs:110` `pub async fn download_remote_skill(`
- `fn` `codex-rs/core/src/skills/remote.rs:185` `fn safe_join(base: &Path, name: &str) -> Result<PathBuf> {`
- `fn` `codex-rs/core/src/skills/remote.rs:198` `fn validate_dir_name_format(name: &str) -> Option<String> {`
- `fn` `codex-rs/core/src/skills/remote.rs:209` `fn is_zip_payload(bytes: &[u8]) -> bool {`
- `fn` `codex-rs/core/src/skills/remote.rs:215` `fn extract_zip_to_dir(`
- `fn` `codex-rs/core/src/skills/remote.rs:249` `fn normalize_zip_name(name: &str, prefix_candidates: &[String]) -> Option<String> {`
- `fn` `codex-rs/core/src/skills/remote.rs:268` `async fn fetch_remote_skill(config: &Config, hazelnut_id: &str) -> Result<RemoteSkillDownload> {`

## Dependencies (auto sample)
### Imports / Includes
- `use anyhow::Context;`
- `use anyhow::Result;`
- `use serde::Deserialize;`
- `use std::collections::HashMap;`
- `use std::collections::HashSet;`
- `use std::path::Component;`
- `use std::path::Path;`
- `use std::path::PathBuf;`
- `use std::time::Duration;`
- `use crate::config::Config;`
- `use crate::default_client::build_reqwest_client;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- has retry/timeout/backoff logic
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- `docs/workdocjcl/spec/00_Overview/ARCHITECTURE.md`
