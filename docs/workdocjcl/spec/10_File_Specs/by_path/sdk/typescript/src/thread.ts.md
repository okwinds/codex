# `sdk/typescript/src/thread.ts`

## Identity
- kind: `source`
- ext: `.ts`
- size_bytes: `4818`
- sha256: `582e68eec324633c087aa791eb2e202575fdb5eb467f488113aeabfc66c92738`
- generated_utc: `2026-02-03T16:08:31Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `sdk/typescript/src/thread.ts` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `export type Turn = {`
- `export type RunResult = Turn;`
- `export type StreamedTurn = {`
- `export type RunStreamedResult = StreamedTurn;`
- `export type UserInput =`
- `export type Input = string | UserInput[];`
- `export class Thread {`

## Definitions (auto, per-file)
- `import` `sdk/typescript/src/thread.ts:1` `import { CodexOptions } from "./codexOptions";`
- `import` `sdk/typescript/src/thread.ts:2` `import { ThreadEvent, ThreadError, Usage } from "./events";`
- `import` `sdk/typescript/src/thread.ts:3` `import { CodexExec } from "./exec";`
- `import` `sdk/typescript/src/thread.ts:4` `import { ThreadItem } from "./items";`
- `import` `sdk/typescript/src/thread.ts:5` `import { ThreadOptions } from "./threadOptions";`
- `import` `sdk/typescript/src/thread.ts:6` `import { TurnOptions } from "./turnOptions";`
- `import` `sdk/typescript/src/thread.ts:7` `import { createOutputSchemaFile } from "./outputSchemaFile";`
- `export` `sdk/typescript/src/thread.ts:10` `export type Turn = {`
- `export` `sdk/typescript/src/thread.ts:17` `export type RunResult = Turn;`
- `export` `sdk/typescript/src/thread.ts:20` `export type StreamedTurn = {`
- `export` `sdk/typescript/src/thread.ts:25` `export type RunStreamedResult = StreamedTurn;`
- `export` `sdk/typescript/src/thread.ts:28` `export type UserInput =`
- `export` `sdk/typescript/src/thread.ts:38` `export type Input = string | UserInput[];`
- `export` `sdk/typescript/src/thread.ts:41` `export class Thread {`
- `const` `sdk/typescript/src/thread.ts:75` `const options = this._threadOptions;`
- `const` `sdk/typescript/src/thread.ts:77` `const generator = this._exec.run({`
- `const` `sdk/typescript/src/thread.ts:116` `const generator = this.runStreamedInternal(input, turnOptions);`
- `const` `sdk/typescript/src/thread.ts:117` `const items: ThreadItem[] = [];`
- `function` `sdk/typescript/src/thread.ts:141` `function normalizeInput(input: Input): { prompt: string; images: string[] } {`
- `const` `sdk/typescript/src/thread.ts:145` `const promptParts: string[] = [];`
- `const` `sdk/typescript/src/thread.ts:146` `const images: string[] = [];`

## Dependencies (auto sample)
### Imports / Includes
- `import { CodexOptions } from "./codexOptions";`
- `import { ThreadEvent, ThreadError, Usage } from "./events";`
- `import { CodexExec } from "./exec";`
- `import { ThreadItem } from "./items";`
- `import { ThreadOptions } from "./threadOptions";`
- `import { TurnOptions } from "./turnOptions";`
- `import { createOutputSchemaFile } from "./outputSchemaFile";`
- `export type Turn = {`
- `export type RunResult = Turn;`
- `export type StreamedTurn = {`
- `export type RunStreamedResult = StreamedTurn;`
- `export type UserInput =`
- `export type Input = string | UserInput[];`
- `export class Thread {`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- throws exceptions

## Spec Links
- `workdocjcl/spec/00_Overview/PROJECT.md`
