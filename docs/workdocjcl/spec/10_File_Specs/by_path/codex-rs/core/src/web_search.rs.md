# `codex-rs/core/src/web_search.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `1421`
- sha256: `c6122d1c69a87eac163acd8743d02fc4949038e5b0fee7ecb569be242c2d2d50`
- generated_utc: `2026-02-08T10:45:34Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/web_search.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub fn web_search_action_detail(action: &WebSearchAction) -> String {`
- `pub fn web_search_detail(action: Option<&WebSearchAction>, query: &str) -> String {`

## Definitions (auto, per-file)
- `use` `codex-rs/core/src/web_search.rs:1` `use codex_protocol::models::WebSearchAction;`
- `fn` `codex-rs/core/src/web_search.rs:3` `fn search_action_detail(query: &Option<String>, queries: &Option<Vec<String>>) -> String {`
- `fn` `codex-rs/core/src/web_search.rs:18` `pub fn web_search_action_detail(action: &WebSearchAction) -> String {`
- `fn` `codex-rs/core/src/web_search.rs:32` `pub fn web_search_detail(action: Option<&WebSearchAction>, query: &str) -> String {`

## Dependencies (auto sample)
### Imports / Includes
- `use codex_protocol::models::WebSearchAction;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- `docs/workdocjcl/spec/00_Overview/ARCHITECTURE.md`
