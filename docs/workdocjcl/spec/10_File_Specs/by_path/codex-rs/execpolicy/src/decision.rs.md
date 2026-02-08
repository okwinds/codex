# `codex-rs/execpolicy/src/decision.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `791`
- sha256: `9a706dbee5301bb81b2c89a69380dab15b68abafad4e102521d81b6009de2e03`
- generated_utc: `2026-02-08T10:45:37Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/execpolicy/src/decision.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub enum Decision {`
- `pub fn parse(raw: &str) -> Result<Self> {`

## Definitions (auto, per-file)
- `use` `codex-rs/execpolicy/src/decision.rs:1` `use serde::Deserialize;`
- `use` `codex-rs/execpolicy/src/decision.rs:2` `use serde::Serialize;`
- `use` `codex-rs/execpolicy/src/decision.rs:4` `use crate::error::Error;`
- `use` `codex-rs/execpolicy/src/decision.rs:5` `use crate::error::Result;`
- `enum` `codex-rs/execpolicy/src/decision.rs:9` `pub enum Decision {`
- `impl` `codex-rs/execpolicy/src/decision.rs:18` `impl Decision {`
- `fn` `codex-rs/execpolicy/src/decision.rs:19` `pub fn parse(raw: &str) -> Result<Self> {`

## Dependencies (auto sample)
### Imports / Includes
- `use serde::Deserialize;`
- `use serde::Serialize;`
- `use crate::error::Error;`
- `use crate::error::Result;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
