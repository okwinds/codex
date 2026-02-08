# `sdk/typescript/samples/structured_output_zod.ts`

## Identity
- kind: `source`
- ext: `.ts`
- size_bytes: `596`
- sha256: `33314312549e5aef2a739707bcb9591ea0c0b40138c9dc459400d9bd2ed37d75`
- generated_utc: `2026-02-08T10:45:42Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `sdk/typescript/samples/structured_output_zod.ts` (read)

### Outputs / Side Effects
- writes to stdout/stderr

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `import` `sdk/typescript/samples/structured_output_zod.ts:3` `import { Codex } from "@openai/codex-sdk";`
- `import` `sdk/typescript/samples/structured_output_zod.ts:4` `import { codexPathOverride } from "./helpers.ts";`
- `import` `sdk/typescript/samples/structured_output_zod.ts:5` `import z from "zod";`
- `import` `sdk/typescript/samples/structured_output_zod.ts:6` `import zodToJsonSchema from "zod-to-json-schema";`
- `const` `sdk/typescript/samples/structured_output_zod.ts:8` `const codex = new Codex({ codexPathOverride: codexPathOverride() });`
- `const` `sdk/typescript/samples/structured_output_zod.ts:9` `const thread = codex.startThread();`
- `const` `sdk/typescript/samples/structured_output_zod.ts:11` `const schema = z.object({`
- `const` `sdk/typescript/samples/structured_output_zod.ts:16` `const turn = await thread.run("Summarize repository status", {`

## Dependencies (auto sample)
### Imports / Includes
- `import { Codex } from "@openai/codex-sdk";`
- `import { codexPathOverride } from "./helpers.ts";`
- `import z from "zod";`
- `import zodToJsonSchema from "zod-to-json-schema";`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- `docs/workdocjcl/spec/00_Overview/PROJECT.md`
