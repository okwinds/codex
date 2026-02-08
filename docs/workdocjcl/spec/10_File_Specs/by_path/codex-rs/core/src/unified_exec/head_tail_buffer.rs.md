# `codex-rs/core/src/unified_exec/head_tail_buffer.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `9470`
- sha256: `27b956beeaca66a385e6d5d50dc879e8ec9e2798ce3df265cd746091f6e1398a`
- generated_utc: `2026-02-03T16:08:29Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/unified_exec/head_tail_buffer.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `use` `codex-rs/core/src/unified_exec/head_tail_buffer.rs:1` `use crate::unified_exec::UNIFIED_EXEC_OUTPUT_MAX_BYTES;`
- `use` `codex-rs/core/src/unified_exec/head_tail_buffer.rs:2` `use std::collections::VecDeque;`
- `impl` `codex-rs/core/src/unified_exec/head_tail_buffer.rs:20` `impl Default for HeadTailBuffer {`
- `fn` `codex-rs/core/src/unified_exec/head_tail_buffer.rs:21` `fn default() -> Self {`
- `impl` `codex-rs/core/src/unified_exec/head_tail_buffer.rs:26` `impl HeadTailBuffer {`
- `fn` `codex-rs/core/src/unified_exec/head_tail_buffer.rs:132` `fn push_to_tail(&mut self, chunk: Vec<u8>) {`
- `fn` `codex-rs/core/src/unified_exec/head_tail_buffer.rs:159` `fn trim_tail_to_budget(&mut self) {`
- `use` `codex-rs/core/src/unified_exec/head_tail_buffer.rs:183` `use super::HeadTailBuffer;`
- `use` `codex-rs/core/src/unified_exec/head_tail_buffer.rs:185` `use pretty_assertions::assert_eq;`
- `fn` `codex-rs/core/src/unified_exec/head_tail_buffer.rs:188` `fn keeps_prefix_and_suffix_when_over_budget() {`
- `fn` `codex-rs/core/src/unified_exec/head_tail_buffer.rs:204` `fn max_bytes_zero_drops_everything() {`
- `fn` `codex-rs/core/src/unified_exec/head_tail_buffer.rs:215` `fn head_budget_zero_keeps_only_last_byte_in_tail() {`
- `fn` `codex-rs/core/src/unified_exec/head_tail_buffer.rs:225` `fn draining_resets_state() {`
- `fn` `codex-rs/core/src/unified_exec/head_tail_buffer.rs:239` `fn chunk_larger_than_tail_budget_keeps_only_tail_end() {`
- `fn` `codex-rs/core/src/unified_exec/head_tail_buffer.rs:253` `fn fills_head_then_tail_across_multiple_chunks() {`

## Dependencies (auto sample)
### Imports / Includes
- `use crate::unified_exec::UNIFIED_EXEC_OUTPUT_MAX_BYTES;`
- `use std::collections::VecDeque;`
- `use super::HeadTailBuffer;`
- `use pretty_assertions::assert_eq;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- `workdocjcl/spec/00_Overview/ARCHITECTURE.md`
