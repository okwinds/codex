# `shell-tool-mcp/src/bashSelection.ts`

## Identity
- kind: `source`
- ext: `.ts`
- size_bytes: `3191`
- sha256: `170685e0ff4d9f9e1d4f949e2da8724fd929d5dcb66e0c7daecfd72fa295771f`
- generated_utc: `2026-02-08T10:45:42Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `shell-tool-mcp/src/bashSelection.ts` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `export function selectLinuxBash(`
- `export function selectDarwinBash(`
- `export function resolveBashPath(`

## Definitions (auto, per-file)
- `import` `shell-tool-mcp/src/bashSelection.ts:1` `import path from "node:path";`
- `import` `shell-tool-mcp/src/bashSelection.ts:2` `import os from "node:os";`
- `import` `shell-tool-mcp/src/bashSelection.ts:3` `import { DARWIN_BASH_VARIANTS, LINUX_BASH_VARIANTS } from "./constants";`
- `import` `shell-tool-mcp/src/bashSelection.ts:4` `import { BashSelection, OsReleaseInfo } from "./types";`
- `function` `shell-tool-mcp/src/bashSelection.ts:6` `function supportedDetail(variants: ReadonlyArray<{ name: string }>): string {`
- `export` `shell-tool-mcp/src/bashSelection.ts:10` `export function selectLinuxBash(`
- `const` `shell-tool-mcp/src/bashSelection.ts:14` `const versionId = info.versionId;`
- `const` `shell-tool-mcp/src/bashSelection.ts:15` `const candidates: Array<{`
- `const` `shell-tool-mcp/src/bashSelection.ts:20` `const matchesId =`
- `const` `shell-tool-mcp/src/bashSelection.ts:26` `const matchesVersion = Boolean(`
- `const` `shell-tool-mcp/src/bashSelection.ts:33` `const pickVariant = (list: typeof candidates) =>`
- `const` `shell-tool-mcp/src/bashSelection.ts:36` `const preferred = pickVariant(`
- `const` `shell-tool-mcp/src/bashSelection.ts:46` `const fallbackMatch = pickVariant(candidates);`
- `const` `shell-tool-mcp/src/bashSelection.ts:54` `const fallback = LINUX_BASH_VARIANTS[0];`
- `const` `shell-tool-mcp/src/bashSelection.ts:62` `const detail = supportedDetail(LINUX_BASH_VARIANTS);`
- `export` `shell-tool-mcp/src/bashSelection.ts:68` `export function selectDarwinBash(`
- `const` `shell-tool-mcp/src/bashSelection.ts:72` `const darwinMajor = Number.parseInt(darwinRelease.split(".")[0] || "0", 10);`
- `const` `shell-tool-mcp/src/bashSelection.ts:73` `const preferred = DARWIN_BASH_VARIANTS.find(`
- `const` `shell-tool-mcp/src/bashSelection.ts:83` `const fallback = DARWIN_BASH_VARIANTS[0];`
- `const` `shell-tool-mcp/src/bashSelection.ts:91` `const detail = supportedDetail(DARWIN_BASH_VARIANTS);`
- `export` `shell-tool-mcp/src/bashSelection.ts:97` `export function resolveBashPath(`
- `const` `shell-tool-mcp/src/bashSelection.ts:103` `const bashRoot = path.join(targetRoot, "bash");`

## Dependencies (auto sample)
### Imports / Includes
- `import path from "node:path";`
- `import os from "node:os";`
- `import { DARWIN_BASH_VARIANTS, LINUX_BASH_VARIANTS } from "./constants";`
- `import { BashSelection, OsReleaseInfo } from "./types";`
- `export function selectLinuxBash(`
- `export function selectDarwinBash(`
- `export function resolveBashPath(`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- throws exceptions

## Spec Links
- `docs/workdocjcl/spec/05_Integrations/MCP.md`
