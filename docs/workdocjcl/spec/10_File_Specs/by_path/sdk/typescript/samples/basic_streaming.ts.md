# `sdk/typescript/samples/basic_streaming.ts`

## Identity
- kind: `source`
- ext: `.ts`
- size_bytes: `2552`
- sha256: `825eacaa496f3b9046d204b1d1dddd733e8fc97db03fcb65412f9f9bff71fa45`
- generated_utc: `2026-02-03T16:08:31Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `sdk/typescript/samples/basic_streaming.ts` (read)

### Outputs / Side Effects
- writes to stdout/stderr

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `import` `sdk/typescript/samples/basic_streaming.ts:3` `import { createInterface } from "node:readline/promises";`
- `import` `sdk/typescript/samples/basic_streaming.ts:4` `import { stdin as input, stdout as output } from "node:process";`
- `import` `sdk/typescript/samples/basic_streaming.ts:6` `import { Codex } from "@openai/codex-sdk";`
- `import` `sdk/typescript/samples/basic_streaming.ts:7` `import type { ThreadEvent, ThreadItem } from "@openai/codex-sdk";`
- `import` `sdk/typescript/samples/basic_streaming.ts:8` `import { codexPathOverride } from "./helpers.ts";`
- `const` `sdk/typescript/samples/basic_streaming.ts:10` `const codex = new Codex({ codexPathOverride: codexPathOverride() });`
- `const` `sdk/typescript/samples/basic_streaming.ts:11` `const thread = codex.startThread();`
- `const` `sdk/typescript/samples/basic_streaming.ts:12` `const rl = createInterface({ input, output });`
- `const` `sdk/typescript/samples/basic_streaming.ts:14` `const handleItemCompleted = (item: ThreadItem): void => {`
- `const` `sdk/typescript/samples/basic_streaming.ts:23` `const exitText = item.exit_code !== undefined ? ` Exit code ${item.exit_code}.` : "";`
- `const` `sdk/typescript/samples/basic_streaming.ts:36` `const handleItemUpdated = (item: ThreadItem): void => {`
- `const` `sdk/typescript/samples/basic_streaming.ts:48` `const handleEvent = (event: ThreadEvent): void => {`
- `const` `sdk/typescript/samples/basic_streaming.ts:68` `const main = async (): Promise<void> => {`
- `const` `sdk/typescript/samples/basic_streaming.ts:71` `const inputText = await rl.question(">");`
- `const` `sdk/typescript/samples/basic_streaming.ts:72` `const trimmed = inputText.trim();`
- `const` `sdk/typescript/samples/basic_streaming.ts:87` `const message = err instanceof Error ? err.message : String(err);`

## Dependencies (auto sample)
### Imports / Includes
- `import { createInterface } from "node:readline/promises";`
- `import { stdin as input, stdout as output } from "node:process";`
- `import { Codex } from "@openai/codex-sdk";`
- `import type { ThreadEvent, ThreadItem } from "@openai/codex-sdk";`
- `import { codexPathOverride } from "./helpers.ts";`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- calls process.exit(...)

## Spec Links
- `workdocjcl/spec/00_Overview/PROJECT.md`
