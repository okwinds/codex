# `shell-tool-mcp/src/index.ts`

## Identity
- kind: `source`
- ext: `.ts`
- size_bytes: `2593`
- sha256: `736f526b1b2793c66a93a8f27b60ae8551d02672ac067f3a05408bf6c73d3b2b`
- generated_utc: `2026-02-08T10:45:42Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `shell-tool-mcp/src/index.ts` (read)

### Outputs / Side Effects
- spawns subprocesses
- writes to stdout/stderr

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `import` `shell-tool-mcp/src/index.ts:3` `import { spawn } from "node:child_process";`
- `import` `shell-tool-mcp/src/index.ts:4` `import { accessSync, constants } from "node:fs";`
- `import` `shell-tool-mcp/src/index.ts:5` `import os from "node:os";`
- `import` `shell-tool-mcp/src/index.ts:6` `import path from "node:path";`
- `import` `shell-tool-mcp/src/index.ts:7` `import { resolveBashPath } from "./bashSelection";`
- `import` `shell-tool-mcp/src/index.ts:8` `import { readOsRelease } from "./osRelease";`
- `import` `shell-tool-mcp/src/index.ts:9` `import { resolveTargetTriple } from "./platform";`
- `function` `shell-tool-mcp/src/index.ts:11` `async function main(): Promise<void> {`
- `const` `shell-tool-mcp/src/index.ts:12` `const targetTriple = resolveTargetTriple(process.platform, process.arch);`
- `const` `shell-tool-mcp/src/index.ts:13` `const vendorRoot = path.resolve(__dirname, "..", "vendor");`
- `const` `shell-tool-mcp/src/index.ts:14` `const targetRoot = path.join(vendorRoot, targetTriple);`
- `const` `shell-tool-mcp/src/index.ts:15` `const execveWrapperPath = path.join(targetRoot, "codex-execve-wrapper");`
- `const` `shell-tool-mcp/src/index.ts:16` `const serverPath = path.join(targetRoot, "codex-exec-mcp-server");`
- `const` `shell-tool-mcp/src/index.ts:18` `const osInfo = process.platform === "linux" ? readOsRelease() : null;`
- `const` `shell-tool-mcp/src/index.ts:34` `const args = [`
- `const` `shell-tool-mcp/src/index.ts:41` `const child = spawn(serverPath, args, {`
- `const` `shell-tool-mcp/src/index.ts:45` `const forwardSignal = (signal: NodeJS.Signals) => {`
- `const` `shell-tool-mcp/src/index.ts:66` `const childResult = await new Promise<`

## Dependencies (auto sample)
### Imports / Includes
- `import { spawn } from "node:child_process";`
- `import { accessSync, constants } from "node:fs";`
- `import os from "node:os";`
- `import path from "node:path";`
- `import { resolveBashPath } from "./bashSelection";`
- `import { readOsRelease } from "./osRelease";`
- `import { resolveTargetTriple } from "./platform";`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- calls process.exit(...)
- throws exceptions

## Spec Links
- `docs/workdocjcl/spec/05_Integrations/MCP.md`
