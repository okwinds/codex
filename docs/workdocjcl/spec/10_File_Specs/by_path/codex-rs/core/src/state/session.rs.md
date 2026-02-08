# `codex-rs/core/src/state/session.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `4851`
- sha256: `2610014e12704f097cb86c441958af3117ca5f50c028bfb192fa1c798dc79f1d`
- generated_utc: `2026-02-08T10:45:33Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/state/session.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `use` `codex-rs/core/src/state/session.rs:3` `use codex_protocol::models::ResponseItem;`
- `use` `codex-rs/core/src/state/session.rs:4` `use std::collections::HashMap;`
- `use` `codex-rs/core/src/state/session.rs:5` `use std::collections::HashSet;`
- `use` `codex-rs/core/src/state/session.rs:7` `use crate::codex::SessionConfiguration;`
- `use` `codex-rs/core/src/state/session.rs:8` `use crate::context_manager::ContextManager;`
- `use` `codex-rs/core/src/state/session.rs:9` `use crate::protocol::RateLimitSnapshot;`
- `use` `codex-rs/core/src/state/session.rs:10` `use crate::protocol::TokenUsage;`
- `use` `codex-rs/core/src/state/session.rs:11` `use crate::protocol::TokenUsageInfo;`
- `use` `codex-rs/core/src/state/session.rs:12` `use crate::truncate::TruncationPolicy;`
- `impl` `codex-rs/core/src/state/session.rs:31` `impl SessionState {`
- `fn` `codex-rs/core/src/state/session.rs:134` `fn merge_rate_limit_fields(`

## Dependencies (auto sample)
### Imports / Includes
- `use codex_protocol::models::ResponseItem;`
- `use std::collections::HashMap;`
- `use std::collections::HashSet;`
- `use crate::codex::SessionConfiguration;`
- `use crate::context_manager::ContextManager;`
- `use crate::protocol::RateLimitSnapshot;`
- `use crate::protocol::TokenUsage;`
- `use crate::protocol::TokenUsageInfo;`
- `use crate::truncate::TruncationPolicy;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- `docs/workdocjcl/spec/00_Overview/ARCHITECTURE.md`
