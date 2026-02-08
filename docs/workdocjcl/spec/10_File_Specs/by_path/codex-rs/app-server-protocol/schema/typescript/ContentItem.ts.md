# `codex-rs/app-server-protocol/schema/typescript/ContentItem.ts`

## Identity
- kind: `source`
- ext: `.ts`
- size_bytes: `311`
- sha256: `edaeb4bdd06c50a2fc47b709101ebeab2036fd95aeadc26eccdc243ac0f0c06f`
- generated_utc: `2026-02-03T16:08:28Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server-protocol/schema/typescript/ContentItem.ts` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `export type ContentItem = { "type": "input_text", text: string, } | { "type": "input_image", image_url: string, } | { "type": "output_text", text: string, };`

## Definitions (auto, per-file)
- `export` `codex-rs/app-server-protocol/schema/typescript/ContentItem.ts:5` `export type ContentItem = { "type": "input_text", text: string, } | { "type": "input_image", image_url: string, } | { "type": "output_text", text: string, };`

## Dependencies (auto sample)
### Imports / Includes
- `export type ContentItem = { "type": "input_text", text: string, } | { "type": "input_image", image_url: string, } | { "type": "output_text", text: string, };`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
