# `sdk/typescript/samples/structured_output.ts`

## Identity
- kind: `source`
- ext: `.ts`
- size_bytes: `619`
- sha256: `2c83a7715ec0e5c4355838d016dd207614289796405c86b15df2a07fba7b4d7c`
- generated_utc: `2026-02-03T16:08:31Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `sdk/typescript/samples/structured_output.ts` (read)

### Outputs / Side Effects
- writes to stdout/stderr

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `import` `sdk/typescript/samples/structured_output.ts:3` `import { Codex } from "@openai/codex-sdk";`
- `import` `sdk/typescript/samples/structured_output.ts:5` `import { codexPathOverride } from "./helpers.ts";`
- `const` `sdk/typescript/samples/structured_output.ts:7` `const codex = new Codex({ codexPathOverride: codexPathOverride() });`
- `const` `sdk/typescript/samples/structured_output.ts:9` `const thread = codex.startThread();`
- `const` `sdk/typescript/samples/structured_output.ts:11` `const schema = {`
- `const` `sdk/typescript/samples/structured_output.ts:21` `const turn = await thread.run("Summarize repository status", { outputSchema: schema });`

## Dependencies (auto sample)
### Imports / Includes
- `import { Codex } from "@openai/codex-sdk";`
- `import { codexPathOverride } from "./helpers.ts";`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- `workdocjcl/spec/00_Overview/PROJECT.md`
