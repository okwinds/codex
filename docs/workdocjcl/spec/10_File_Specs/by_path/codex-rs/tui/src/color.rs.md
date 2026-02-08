# `codex-rs/tui/src/color.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `2207`
- sha256: `fdb5acf38aff891574b59950f8ac78c6d41bd9b0a0c2f186ddf9f63169082412`
- generated_utc: `2026-02-03T16:08:30Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/tui/src/color.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `fn` `codex-rs/tui/src/color.rs:18` `fn srgb_to_linear(c: u8) -> f32 {`
- `fn` `codex-rs/tui/src/color.rs:28` `fn rgb_to_xyz(r: u8, g: u8, b: u8) -> (f32, f32, f32) {`
- `fn` `codex-rs/tui/src/color.rs:40` `fn xyz_to_lab(x: f32, y: f32, z: f32) -> (f32, f32, f32) {`
- `fn` `codex-rs/tui/src/color.rs:46` `fn f(t: f32) -> f32 {`

## Dependencies (auto sample)
### Imports / Includes
- (none detected)
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- `workdocjcl/spec/06_UI/TUI.md`
