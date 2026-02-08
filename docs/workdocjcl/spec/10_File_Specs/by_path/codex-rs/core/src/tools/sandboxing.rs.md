# `codex-rs/core/src/tools/sandboxing.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `10343`
- sha256: `645d62532a39ec0b3c75d41db8a006663133b2908322bd121a0fa9179d35d66a`
- generated_utc: `2026-02-03T16:08:29Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/tools/sandboxing.rs` (read)

### Outputs / Side Effects
- performs network I/O

## Public Surface (auto)
- `pub fn proposed_execpolicy_amendment(&self) -> Option<&ExecPolicyAmendment> {`
- `pub fn env_for(`

## Definitions (auto, per-file)
- `use` `codex-rs/core/src/tools/sandboxing.rs:7` `use crate::codex::Session;`
- `use` `codex-rs/core/src/tools/sandboxing.rs:8` `use crate::codex::TurnContext;`
- `use` `codex-rs/core/src/tools/sandboxing.rs:9` `use crate::error::CodexErr;`
- `use` `codex-rs/core/src/tools/sandboxing.rs:10` `use crate::protocol::SandboxPolicy;`
- `use` `codex-rs/core/src/tools/sandboxing.rs:11` `use crate::sandboxing::CommandSpec;`
- `use` `codex-rs/core/src/tools/sandboxing.rs:12` `use crate::sandboxing::SandboxManager;`
- `use` `codex-rs/core/src/tools/sandboxing.rs:13` `use crate::sandboxing::SandboxTransformError;`
- `use` `codex-rs/core/src/tools/sandboxing.rs:14` `use crate::state::SessionServices;`
- `use` `codex-rs/core/src/tools/sandboxing.rs:15` `use codex_protocol::approvals::ExecPolicyAmendment;`
- `use` `codex-rs/core/src/tools/sandboxing.rs:16` `use codex_protocol::protocol::AskForApproval;`
- `use` `codex-rs/core/src/tools/sandboxing.rs:17` `use codex_protocol::protocol::ReviewDecision;`
- `use` `codex-rs/core/src/tools/sandboxing.rs:18` `use std::collections::HashMap;`
- `use` `codex-rs/core/src/tools/sandboxing.rs:19` `use std::fmt::Debug;`
- `use` `codex-rs/core/src/tools/sandboxing.rs:20` `use std::hash::Hash;`
- `use` `codex-rs/core/src/tools/sandboxing.rs:21` `use std::path::Path;`
- `use` `codex-rs/core/src/tools/sandboxing.rs:23` `use futures::Future;`
- `use` `codex-rs/core/src/tools/sandboxing.rs:24` `use futures::future::BoxFuture;`
- `use` `codex-rs/core/src/tools/sandboxing.rs:25` `use serde::Serialize;`
- `impl` `codex-rs/core/src/tools/sandboxing.rs:33` `impl ApprovalStore {`
- `impl` `codex-rs/core/src/tools/sandboxing.rs:137` `impl ExecApprovalRequirement {`
- `fn` `codex-rs/core/src/tools/sandboxing.rs:138` `pub fn proposed_execpolicy_amendment(&self) -> Option<&ExecPolicyAmendment> {`
- `type` `codex-rs/core/src/tools/sandboxing.rs:189` `type ApprovalKey: Hash + Eq + Clone + Debug + Serialize;`
- `fn` `codex-rs/core/src/tools/sandboxing.rs:198` `fn approval_keys(&self, req: &Req) -> Vec<Self::ApprovalKey>;`
- `fn` `codex-rs/core/src/tools/sandboxing.rs:203` `fn sandbox_mode_for_first_attempt(&self, _req: &Req) -> SandboxOverride {`
- `fn` `codex-rs/core/src/tools/sandboxing.rs:207` `fn should_bypass_approval(&self, policy: AskForApproval, already_approved: bool) -> bool {`
- `fn` `codex-rs/core/src/tools/sandboxing.rs:217` `fn exec_approval_requirement(&self, _req: &Req) -> Option<ExecApprovalRequirement> {`
- `fn` `codex-rs/core/src/tools/sandboxing.rs:222` `fn wants_no_sandbox_approval(&self, policy: AskForApproval) -> bool {`
- `fn` `codex-rs/core/src/tools/sandboxing.rs:243` `fn sandbox_preference(&self) -> SandboxablePreference;`
- `fn` `codex-rs/core/src/tools/sandboxing.rs:244` `fn escalate_on_failure(&self) -> bool {`
- `fn` `codex-rs/core/src/tools/sandboxing.rs:263` `async fn run(`
- `impl` `codex-rs/core/src/tools/sandboxing.rs:280` `impl<'a> SandboxAttempt<'a> {`
- `fn` `codex-rs/core/src/tools/sandboxing.rs:281` `pub fn env_for(`
- `use` `codex-rs/core/src/tools/sandboxing.rs:298` `use super::*;`
- `use` `codex-rs/core/src/tools/sandboxing.rs:299` `use codex_protocol::protocol::NetworkAccess;`
- `use` `codex-rs/core/src/tools/sandboxing.rs:300` `use pretty_assertions::assert_eq;`
- `fn` `codex-rs/core/src/tools/sandboxing.rs:303` `fn external_sandbox_skips_exec_approval_on_request() {`
- `fn` `codex-rs/core/src/tools/sandboxing.rs:319` `fn restricted_sandbox_requires_exec_approval_on_request() {`

## Dependencies (auto sample)
### Imports / Includes
- `use crate::codex::Session;`
- `use crate::codex::TurnContext;`
- `use crate::error::CodexErr;`
- `use crate::protocol::SandboxPolicy;`
- `use crate::sandboxing::CommandSpec;`
- `use crate::sandboxing::SandboxManager;`
- `use crate::sandboxing::SandboxTransformError;`
- `use crate::state::SessionServices;`
- `use codex_protocol::approvals::ExecPolicyAmendment;`
- `use codex_protocol::protocol::AskForApproval;`
- `use codex_protocol::protocol::ReviewDecision;`
- `use std::collections::HashMap;`
- `use std::fmt::Debug;`
- `use std::hash::Hash;`
- `use std::path::Path;`
- `use futures::Future;`
- `use futures::future::BoxFuture;`
- `use serde::Serialize;`
- `use super::*;`
- `use codex_protocol::protocol::NetworkAccess;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- has retry/timeout/backoff logic
- returns structured errors (Result/ErrorKind)

## Spec Links
- `workdocjcl/spec/00_Overview/ARCHITECTURE.md`
