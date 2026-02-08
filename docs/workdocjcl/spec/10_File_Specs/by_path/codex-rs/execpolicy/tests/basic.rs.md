# `codex-rs/execpolicy/tests/basic.rs`

## Identity
- kind: `test`
- ext: `.rs`
- size_bytes: `16611`
- sha256: `9d9a88dc23828c09873ae18d7431f92482fe083e04fb9e2d72d7eef5057811ac`
- generated_utc: `2026-02-08T10:45:37Z`

## Purpose (Why)
Test or snapshot file used for automated verification.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/execpolicy/tests/basic.rs` (read)

### Outputs / Side Effects
- none (file is declarative: doc/config/test/asset)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- (not extracted)

## Dependencies (auto sample)
### Imports / Includes
- `use std::any::Any;`
- `use std::fs;`
- `use std::sync::Arc;`
- `use anyhow::Context;`
- `use anyhow::Result;`
- `use codex_execpolicy::Decision;`
- `use codex_execpolicy::Error;`
- `use codex_execpolicy::Evaluation;`
- `use codex_execpolicy::Policy;`
- `use codex_execpolicy::PolicyParser;`
- `use codex_execpolicy::RuleMatch;`
- `use codex_execpolicy::RuleRef;`
- `use codex_execpolicy::blocking_append_allow_prefix_rule;`
- `use codex_execpolicy::rule::PatternToken;`
- `use codex_execpolicy::rule::PrefixPattern;`
- `use codex_execpolicy::rule::PrefixRule;`
- `use pretty_assertions::assert_eq;`
- `use tempfile::tempdir;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (none detected)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
