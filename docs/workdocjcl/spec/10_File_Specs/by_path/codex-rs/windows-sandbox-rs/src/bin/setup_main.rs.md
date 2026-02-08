# `codex-rs/windows-sandbox-rs/src/bin/setup_main.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `234`
- sha256: `2027b4d24db2685c75c72a9dfee546522f05d8ad95b80b66c3ee1d1a5a821122`
- generated_utc: `2026-02-08T10:45:41Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/windows-sandbox-rs/src/bin/setup_main.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `fn main() -> anyhow::Result<()> {`
- `fn main() {`

## Definitions (auto, per-file)
- `mod` `codex-rs/windows-sandbox-rs/src/bin/setup_main.rs:2` `mod win;`
- `fn` `codex-rs/windows-sandbox-rs/src/bin/setup_main.rs:5` `fn main() -> anyhow::Result<()> {`
- `fn` `codex-rs/windows-sandbox-rs/src/bin/setup_main.rs:10` `fn main() {`

## Dependencies (auto sample)
### Imports / Includes
- (none detected)
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
