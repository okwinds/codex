# `codex-rs/core/src/features/legacy.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `3088`
- sha256: `cccca6cc86c11fb559b9f74182d30e8d7992135b9e3f041f9fa218e7c0dfa4a6`
- generated_utc: `2026-02-03T16:08:29Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/features/legacy.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub struct LegacyFeatureToggles {`
- `pub fn apply(self, features: &mut Features) {`

## Definitions (auto, per-file)
- `use` `codex-rs/core/src/features/legacy.rs:1` `use super::Feature;`
- `use` `codex-rs/core/src/features/legacy.rs:2` `use super::Features;`
- `use` `codex-rs/core/src/features/legacy.rs:3` `use tracing::info;`
- `struct` `codex-rs/core/src/features/legacy.rs:6` `struct Alias {`
- `const` `codex-rs/core/src/features/legacy.rs:11` `const ALIASES: &[Alias] = &[`
- `struct` `codex-rs/core/src/features/legacy.rs:53` `pub struct LegacyFeatureToggles {`
- `impl` `codex-rs/core/src/features/legacy.rs:60` `impl LegacyFeatureToggles {`
- `fn` `codex-rs/core/src/features/legacy.rs:61` `pub fn apply(self, features: &mut Features) {`
- `fn` `codex-rs/core/src/features/legacy.rs:89` `fn set_if_some(`
- `fn` `codex-rs/core/src/features/legacy.rs:102` `fn set_feature(features: &mut Features, feature: Feature, enabled: bool) {`
- `fn` `codex-rs/core/src/features/legacy.rs:110` `fn log_alias(alias: &str, feature: Feature) {`

## Dependencies (auto sample)
### Imports / Includes
- `use super::Feature;`
- `use super::Features;`
- `use tracing::info;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- `workdocjcl/spec/00_Overview/ARCHITECTURE.md`
