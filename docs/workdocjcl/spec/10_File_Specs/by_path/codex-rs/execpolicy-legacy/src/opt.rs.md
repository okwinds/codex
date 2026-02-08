# `codex-rs/execpolicy-legacy/src/opt.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `2124`
- sha256: `7300a6a22df696b61fbe6d2217f718f0b2e3c2af23b7564350f26bec622e1801`
- generated_utc: `2026-02-03T16:08:30Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/execpolicy-legacy/src/opt.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub struct Opt {`
- `pub enum OptMeta {`
- `pub fn new(opt: String, meta: OptMeta, required: bool) -> Self {`
- `pub fn name(&self) -> &str {`

## Definitions (auto, per-file)
- `use` `codex-rs/execpolicy-legacy/src/opt.rs:3` `use crate::ArgType;`
- `use` `codex-rs/execpolicy-legacy/src/opt.rs:4` `use crate::starlark::values::ValueLike;`
- `use` `codex-rs/execpolicy-legacy/src/opt.rs:5` `use allocative::Allocative;`
- `use` `codex-rs/execpolicy-legacy/src/opt.rs:6` `use derive_more::derive::Display;`
- `use` `codex-rs/execpolicy-legacy/src/opt.rs:7` `use starlark::any::ProvidesStaticType;`
- `use` `codex-rs/execpolicy-legacy/src/opt.rs:8` `use starlark::values::AllocValue;`
- `use` `codex-rs/execpolicy-legacy/src/opt.rs:9` `use starlark::values::Heap;`
- `use` `codex-rs/execpolicy-legacy/src/opt.rs:10` `use starlark::values::NoSerialize;`
- `use` `codex-rs/execpolicy-legacy/src/opt.rs:11` `use starlark::values::StarlarkValue;`
- `use` `codex-rs/execpolicy-legacy/src/opt.rs:12` `use starlark::values::UnpackValue;`
- `use` `codex-rs/execpolicy-legacy/src/opt.rs:13` `use starlark::values::Value;`
- `use` `codex-rs/execpolicy-legacy/src/opt.rs:14` `use starlark::values::starlark_value;`
- `struct` `codex-rs/execpolicy-legacy/src/opt.rs:19` `pub struct Opt {`
- `enum` `codex-rs/execpolicy-legacy/src/opt.rs:31` `pub enum OptMeta {`
- `impl` `codex-rs/execpolicy-legacy/src/opt.rs:39` `impl Opt {`
- `fn` `codex-rs/execpolicy-legacy/src/opt.rs:40` `pub fn new(opt: String, meta: OptMeta, required: bool) -> Self {`
- `fn` `codex-rs/execpolicy-legacy/src/opt.rs:48` `pub fn name(&self) -> &str {`
- `impl` `codex-rs/execpolicy-legacy/src/opt.rs:54` `impl<'v> StarlarkValue<'v> for Opt {`
- `type` `codex-rs/execpolicy-legacy/src/opt.rs:55` `type Canonical = Opt;`
- `impl` `codex-rs/execpolicy-legacy/src/opt.rs:58` `impl<'v> UnpackValue<'v> for Opt {`
- `type` `codex-rs/execpolicy-legacy/src/opt.rs:59` `type Error = starlark::Error;`
- `fn` `codex-rs/execpolicy-legacy/src/opt.rs:61` `fn unpack_value_impl(value: Value<'v>) -> starlark::Result<Option<Self>> {`
- `impl` `codex-rs/execpolicy-legacy/src/opt.rs:68` `impl<'v> AllocValue<'v> for Opt {`
- `fn` `codex-rs/execpolicy-legacy/src/opt.rs:69` `fn alloc_value(self, heap: &'v Heap) -> Value<'v> {`
- `impl` `codex-rs/execpolicy-legacy/src/opt.rs:75` `impl<'v> StarlarkValue<'v> for OptMeta {`
- `type` `codex-rs/execpolicy-legacy/src/opt.rs:76` `type Canonical = OptMeta;`

## Dependencies (auto sample)
### Imports / Includes
- `use crate::ArgType;`
- `use crate::starlark::values::ValueLike;`
- `use allocative::Allocative;`
- `use derive_more::derive::Display;`
- `use starlark::any::ProvidesStaticType;`
- `use starlark::values::AllocValue;`
- `use starlark::values::Heap;`
- `use starlark::values::NoSerialize;`
- `use starlark::values::StarlarkValue;`
- `use starlark::values::UnpackValue;`
- `use starlark::values::Value;`
- `use starlark::values::starlark_value;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
