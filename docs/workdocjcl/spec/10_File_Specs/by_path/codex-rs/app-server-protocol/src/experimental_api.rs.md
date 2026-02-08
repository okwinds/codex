# `codex-rs/app-server-protocol/src/experimental_api.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `2286`
- sha256: `af3b01f592d0b27e7922c8402c8e97402acfec37f20b29163b2acc5247c2b9b4`
- generated_utc: `2026-02-08T10:45:14Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server-protocol/src/experimental_api.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub trait ExperimentalApi {`
- `pub struct ExperimentalField {`
- `pub fn experimental_fields() -> Vec<&'static ExperimentalField> {`
- `pub fn experimental_required_message(reason: &str) -> String {`

## Definitions (auto, per-file)
- `trait` `codex-rs/app-server-protocol/src/experimental_api.rs:2` `pub trait ExperimentalApi {`
- `fn` `codex-rs/app-server-protocol/src/experimental_api.rs:5` `fn experimental_reason(&self) -> Option<&'static str>;`
- `struct` `codex-rs/app-server-protocol/src/experimental_api.rs:10` `pub struct ExperimentalField {`
- `fn` `codex-rs/app-server-protocol/src/experimental_api.rs:22` `pub fn experimental_fields() -> Vec<&'static ExperimentalField> {`
- `fn` `codex-rs/app-server-protocol/src/experimental_api.rs:27` `pub fn experimental_required_message(reason: &str) -> String {`
- `use` `codex-rs/app-server-protocol/src/experimental_api.rs:33` `use super::ExperimentalApi as ExperimentalApiTrait;`
- `use` `codex-rs/app-server-protocol/src/experimental_api.rs:34` `use codex_experimental_api_macros::ExperimentalApi;`
- `use` `codex-rs/app-server-protocol/src/experimental_api.rs:35` `use pretty_assertions::assert_eq;`
- `enum` `codex-rs/app-server-protocol/src/experimental_api.rs:39` `enum EnumVariantShapes {`
- `fn` `codex-rs/app-server-protocol/src/experimental_api.rs:52` `fn derive_supports_all_enum_variant_shapes() {`

## Dependencies (auto sample)
### Imports / Includes
- `use super::ExperimentalApi as ExperimentalApiTrait;`
- `use codex_experimental_api_macros::ExperimentalApi;`
- `use pretty_assertions::assert_eq;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
