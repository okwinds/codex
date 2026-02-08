# `codex-rs/core/src/review_prompts.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `3888`
- sha256: `e34602dde2053797b7cf2f3ccd37a43b778ac334770cacecb27250a70cb7ce31`
- generated_utc: `2026-02-08T10:45:33Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/review_prompts.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub struct ResolvedReviewRequest {`
- `pub fn resolve_review_request(`
- `pub fn review_prompt(target: &ReviewTarget, cwd: &Path) -> anyhow::Result<String> {`
- `pub fn user_facing_hint(target: &ReviewTarget) -> String {`

## Definitions (auto, per-file)
- `use` `codex-rs/core/src/review_prompts.rs:1` `use codex_git::merge_base_with_head;`
- `use` `codex-rs/core/src/review_prompts.rs:2` `use codex_protocol::protocol::ReviewRequest;`
- `use` `codex-rs/core/src/review_prompts.rs:3` `use codex_protocol::protocol::ReviewTarget;`
- `use` `codex-rs/core/src/review_prompts.rs:4` `use std::path::Path;`
- `struct` `codex-rs/core/src/review_prompts.rs:7` `pub struct ResolvedReviewRequest {`
- `const` `codex-rs/core/src/review_prompts.rs:13` `const UNCOMMITTED_PROMPT: &str = "Review the current code changes (staged, unstaged, and untracked files) and provide prioritized findings.";`
- `const` `codex-rs/core/src/review_prompts.rs:15` `const BASE_BRANCH_PROMPT_BACKUP: &str = "Review the code changes against the base branch '{branch}'. Start by finding the merge diff between the current branch and {branch}'s upstream e.g. (`git merge-base HEAD \"$(git rev-parse --abbrev-ref \"{branch}@{upstream}\")\"`), then run `git diff` against that SHA to see what changes we would merge into the {branch} branch. Provide prioritized, actionable findings.";`
- `const` `codex-rs/core/src/review_prompts.rs:16` `const BASE_BRANCH_PROMPT: &str = "Review the code changes against the base branch '{baseBranch}'. The merge base commit for this comparison is {mergeBaseSha}. Run `git diff {mergeBaseSha}` to inspect the changes relative to {baseBranch}. Provide prioritized, actionable findings.";`
- `const` `codex-rs/core/src/review_prompts.rs:18` `const COMMIT_PROMPT_WITH_TITLE: &str = "Review the code changes introduced by commit {sha} (\"{title}\"). Provide prioritized, actionable findings.";`
- `const` `codex-rs/core/src/review_prompts.rs:19` `const COMMIT_PROMPT: &str =`
- `fn` `codex-rs/core/src/review_prompts.rs:22` `pub fn resolve_review_request(`
- `fn` `codex-rs/core/src/review_prompts.rs:39` `pub fn review_prompt(target: &ReviewTarget, cwd: &Path) -> anyhow::Result<String> {`
- `fn` `codex-rs/core/src/review_prompts.rs:70` `pub fn user_facing_hint(target: &ReviewTarget) -> String {`
- `impl` `codex-rs/core/src/review_prompts.rs:86` `impl From<ResolvedReviewRequest> for ReviewRequest {`
- `fn` `codex-rs/core/src/review_prompts.rs:87` `fn from(resolved: ResolvedReviewRequest) -> Self {`

## Dependencies (auto sample)
### Imports / Includes
- `use codex_git::merge_base_with_head;`
- `use codex_protocol::protocol::ReviewRequest;`
- `use codex_protocol::protocol::ReviewTarget;`
- `use std::path::Path;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- `docs/workdocjcl/spec/00_Overview/ARCHITECTURE.md`
