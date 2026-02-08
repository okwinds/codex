# `codex-rs/linux-sandbox/src/landlock.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `6659`
- sha256: `2503747327c8b08ab54156073546f572d38d275d08ad1467bda28cef147376a8`
- generated_utc: `2026-02-08T10:45:37Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/linux-sandbox/src/landlock.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `use` `codex-rs/linux-sandbox/src/landlock.rs:5` `use std::collections::BTreeMap;`
- `use` `codex-rs/linux-sandbox/src/landlock.rs:6` `use std::path::Path;`
- `use` `codex-rs/linux-sandbox/src/landlock.rs:8` `use codex_core::error::CodexErr;`
- `use` `codex-rs/linux-sandbox/src/landlock.rs:9` `use codex_core::error::Result;`
- `use` `codex-rs/linux-sandbox/src/landlock.rs:10` `use codex_core::error::SandboxErr;`
- `use` `codex-rs/linux-sandbox/src/landlock.rs:11` `use codex_core::protocol::SandboxPolicy;`
- `use` `codex-rs/linux-sandbox/src/landlock.rs:12` `use codex_utils_absolute_path::AbsolutePathBuf;`
- `use` `codex-rs/linux-sandbox/src/landlock.rs:14` `use landlock::ABI;`
- `use` `codex-rs/linux-sandbox/src/landlock.rs:16` `use landlock::Access;`
- `use` `codex-rs/linux-sandbox/src/landlock.rs:17` `use landlock::AccessFs;`
- `use` `codex-rs/linux-sandbox/src/landlock.rs:18` `use landlock::CompatLevel;`
- `use` `codex-rs/linux-sandbox/src/landlock.rs:19` `use landlock::Compatible;`
- `use` `codex-rs/linux-sandbox/src/landlock.rs:20` `use landlock::Ruleset;`
- `use` `codex-rs/linux-sandbox/src/landlock.rs:21` `use landlock::RulesetAttr;`
- `use` `codex-rs/linux-sandbox/src/landlock.rs:22` `use landlock::RulesetCreatedAttr;`
- `use` `codex-rs/linux-sandbox/src/landlock.rs:23` `use seccompiler::BpfProgram;`
- `use` `codex-rs/linux-sandbox/src/landlock.rs:24` `use seccompiler::SeccompAction;`
- `use` `codex-rs/linux-sandbox/src/landlock.rs:25` `use seccompiler::SeccompCmpArgLen;`
- `use` `codex-rs/linux-sandbox/src/landlock.rs:26` `use seccompiler::SeccompCmpOp;`
- `use` `codex-rs/linux-sandbox/src/landlock.rs:27` `use seccompiler::SeccompCondition;`
- `use` `codex-rs/linux-sandbox/src/landlock.rs:28` `use seccompiler::SeccompFilter;`
- `use` `codex-rs/linux-sandbox/src/landlock.rs:29` `use seccompiler::SeccompRule;`
- `use` `codex-rs/linux-sandbox/src/landlock.rs:30` `use seccompiler::TargetArch;`
- `use` `codex-rs/linux-sandbox/src/landlock.rs:31` `use seccompiler::apply_filter;`
- `fn` `codex-rs/linux-sandbox/src/landlock.rs:76` `fn set_no_new_privs() -> Result<()> {`
- `fn` `codex-rs/linux-sandbox/src/landlock.rs:93` `fn install_filesystem_landlock_rules_on_current_thread(`
- `fn` `codex-rs/linux-sandbox/src/landlock.rs:126` `fn install_network_seccomp_filter_on_current_thread() -> std::result::Result<(), SandboxErr> {`

## Dependencies (auto sample)
### Imports / Includes
- `use std::collections::BTreeMap;`
- `use std::path::Path;`
- `use codex_core::error::CodexErr;`
- `use codex_core::error::Result;`
- `use codex_core::error::SandboxErr;`
- `use codex_core::protocol::SandboxPolicy;`
- `use codex_utils_absolute_path::AbsolutePathBuf;`
- `use landlock::ABI;`
- `use landlock::Access;`
- `use landlock::AccessFs;`
- `use landlock::CompatLevel;`
- `use landlock::Compatible;`
- `use landlock::Ruleset;`
- `use landlock::RulesetAttr;`
- `use landlock::RulesetCreatedAttr;`
- `use seccompiler::BpfProgram;`
- `use seccompiler::SeccompAction;`
- `use seccompiler::SeccompCmpArgLen;`
- `use seccompiler::SeccompCmpOp;`
- `use seccompiler::SeccompCondition;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
