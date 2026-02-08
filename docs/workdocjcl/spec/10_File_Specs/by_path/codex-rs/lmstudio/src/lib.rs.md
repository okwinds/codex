# `codex-rs/lmstudio/src/lib.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `1483`
- sha256: `905e95e91e94c49a30e3b321a5f17da26ec2d11b7075cf8213b5a6168a9192d9`
- generated_utc: `2026-02-03T16:08:30Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/lmstudio/src/lib.rs` (read)

### Outputs / Side Effects
- spawns subprocesses

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `mod` `codex-rs/lmstudio/src/lib.rs:1` `mod client;`
- `use` `codex-rs/lmstudio/src/lib.rs:4` `use codex_core::config::Config;`
- `const` `codex-rs/lmstudio/src/lib.rs:7` `pub const DEFAULT_OSS_MODEL: &str = "openai/gpt-oss-20b";`
- `fn` `codex-rs/lmstudio/src/lib.rs:13` `pub async fn ensure_oss_ready(config: &Config) -> std::io::Result<()> {`

## Dependencies (auto sample)
### Imports / Includes
- `use codex_core::config::Config;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
