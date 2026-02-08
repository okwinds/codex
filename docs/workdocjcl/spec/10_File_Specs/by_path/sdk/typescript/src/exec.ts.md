# `sdk/typescript/src/exec.ts`

## Identity
- kind: `source`
- ext: `.ts`
- size_bytes: `9990`
- sha256: `46265d82a9fa657083b78165a27a480c549f30516e4ebb5e47e2659bc06e612b`
- generated_utc: `2026-02-08T10:45:42Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `sdk/typescript/src/exec.ts` (read)

### Outputs / Side Effects
- spawns subprocesses

## Public Surface (auto)
- `export type CodexExecArgs = {`
- `export class CodexExec {`

## Definitions (auto, per-file)
- `import` `sdk/typescript/src/exec.ts:1` `import { spawn } from "node:child_process";`
- `import` `sdk/typescript/src/exec.ts:2` `import path from "node:path";`
- `import` `sdk/typescript/src/exec.ts:3` `import readline from "node:readline";`
- `import` `sdk/typescript/src/exec.ts:4` `import { fileURLToPath } from "node:url";`
- `import` `sdk/typescript/src/exec.ts:6` `import type { CodexConfigObject, CodexConfigValue } from "./codexOptions";`
- `import` `sdk/typescript/src/exec.ts:7` `import { SandboxMode, ModelReasoningEffort, ApprovalMode, WebSearchMode } from "./threadOptions";`
- `export` `sdk/typescript/src/exec.ts:9` `export type CodexExecArgs = {`
- `const` `sdk/typescript/src/exec.ts:42` `const INTERNAL_ORIGINATOR_ENV = "CODEX_INTERNAL_ORIGINATOR_OVERRIDE";`
- `const` `sdk/typescript/src/exec.ts:43` `const TYPESCRIPT_SDK_ORIGINATOR = "codex_sdk_ts";`
- `export` `sdk/typescript/src/exec.ts:45` `export class CodexExec {`
- `const` `sdk/typescript/src/exec.ts:61` `const commandArgs: string[] = ["exec", "--experimental-json"];`
- `const` `sdk/typescript/src/exec.ts:128` `const env: Record<string, string> = {};`
- `const` `sdk/typescript/src/exec.ts:148` `const child = spawn(this.executablePath, commandArgs, {`
- `const` `sdk/typescript/src/exec.ts:167` `const stderrChunks: Buffer[] = [];`
- `const` `sdk/typescript/src/exec.ts:175` `const exitPromise = new Promise<{ code: number | null; signal: NodeJS.Signals | null }>(`
- `const` `sdk/typescript/src/exec.ts:183` `const rl = readline.createInterface({`
- `const` `sdk/typescript/src/exec.ts:197` `const stderrBuffer = Buffer.concat(stderrChunks);`
- `const` `sdk/typescript/src/exec.ts:198` `const detail = signal ? `signal ${signal}` : `code ${code ?? 1}`;`
- `function` `sdk/typescript/src/exec.ts:213` `function serializeConfigOverrides(configOverrides: CodexConfigObject): string[] {`
- `const` `sdk/typescript/src/exec.ts:214` `const overrides: string[] = [];`
- `function` `sdk/typescript/src/exec.ts:219` `function flattenConfigOverrides(`
- `const` `sdk/typescript/src/exec.ts:233` `const entries = Object.entries(value);`
- `const` `sdk/typescript/src/exec.ts:250` `const path = prefix ? `${prefix}.${key}` : key;`
- `function` `sdk/typescript/src/exec.ts:259` `function toTomlValue(value: CodexConfigValue, path: string): string {`
- `const` `sdk/typescript/src/exec.ts:270` `const rendered = value.map((item, index) => toTomlValue(item, `${path}[${index}]`));`
- `const` `sdk/typescript/src/exec.ts:273` `const parts: string[] = [];`
- `const` `sdk/typescript/src/exec.ts:287` `const typeName = typeof value;`
- `const` `sdk/typescript/src/exec.ts:292` `const TOML_BARE_KEY = /^[A-Za-z0-9_-]+$/;`
- `function` `sdk/typescript/src/exec.ts:293` `function formatTomlKey(key: string): string {`
- `function` `sdk/typescript/src/exec.ts:297` `function isPlainObject(value: unknown): value is CodexConfigObject {`
- `const` `sdk/typescript/src/exec.ts:301` `const scriptFileName = fileURLToPath(import.meta.url);`
- `const` `sdk/typescript/src/exec.ts:302` `const scriptDirName = path.dirname(scriptFileName);`
- `function` `sdk/typescript/src/exec.ts:304` `function findCodexPath() {`
- `const` `sdk/typescript/src/exec.ts:354` `const vendorRoot = path.join(scriptDirName, "..", "vendor");`
- `const` `sdk/typescript/src/exec.ts:355` `const archRoot = path.join(vendorRoot, targetTriple);`
- `const` `sdk/typescript/src/exec.ts:356` `const codexBinaryName = process.platform === "win32" ? "codex.exe" : "codex";`
- `const` `sdk/typescript/src/exec.ts:357` `const binaryPath = path.join(archRoot, "codex", codexBinaryName);`

## Dependencies (auto sample)
### Imports / Includes
- `import { spawn } from "node:child_process";`
- `import path from "node:path";`
- `import readline from "node:readline";`
- `import { fileURLToPath } from "node:url";`
- `import type { CodexConfigObject, CodexConfigValue } from "./codexOptions";`
- `import { SandboxMode, ModelReasoningEffort, ApprovalMode, WebSearchMode } from "./threadOptions";`
- `export type CodexExecArgs = {`
- `export class CodexExec {`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- throws exceptions

## Spec Links
- `docs/workdocjcl/spec/00_Overview/PROJECT.md`
