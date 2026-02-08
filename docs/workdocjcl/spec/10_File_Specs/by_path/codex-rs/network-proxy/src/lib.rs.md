# `codex-rs/network-proxy/src/lib.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `743`
- sha256: `a71526767ffcd09ac35f39732909946b24ebcdd8e86d0cbc20f24195494c87a0`
- generated_utc: `2026-02-08T10:45:38Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/network-proxy/src/lib.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `mod` `codex-rs/network-proxy/src/lib.rs:3` `mod admin;`
- `mod` `codex-rs/network-proxy/src/lib.rs:4` `mod config;`
- `mod` `codex-rs/network-proxy/src/lib.rs:5` `mod http_proxy;`
- `mod` `codex-rs/network-proxy/src/lib.rs:6` `mod network_policy;`
- `mod` `codex-rs/network-proxy/src/lib.rs:7` `mod policy;`
- `mod` `codex-rs/network-proxy/src/lib.rs:8` `mod proxy;`
- `mod` `codex-rs/network-proxy/src/lib.rs:9` `mod reasons;`
- `mod` `codex-rs/network-proxy/src/lib.rs:10` `mod responses;`
- `mod` `codex-rs/network-proxy/src/lib.rs:11` `mod runtime;`
- `mod` `codex-rs/network-proxy/src/lib.rs:12` `mod socks5;`
- `mod` `codex-rs/network-proxy/src/lib.rs:13` `mod state;`
- `mod` `codex-rs/network-proxy/src/lib.rs:14` `mod upstream;`
- `use` `codex-rs/network-proxy/src/lib.rs:16` `use anyhow::Result;`
- `fn` `codex-rs/network-proxy/src/lib.rs:27` `pub async fn run_main(args: Args) -> Result<()> {`

## Dependencies (auto sample)
### Imports / Includes
- `use anyhow::Result;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
