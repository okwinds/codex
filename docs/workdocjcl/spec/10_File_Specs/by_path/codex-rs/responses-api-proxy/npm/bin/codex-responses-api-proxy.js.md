# `codex-rs/responses-api-proxy/npm/bin/codex-responses-api-proxy.js`

## Identity
- kind: `source`
- ext: `.js`
- size_bytes: `2250`
- sha256: `3d04284bd6102e856b73e6ce83cf62ae215f420e656442043b6e70c8bc835b82`
- generated_utc: `2026-02-03T16:08:30Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/responses-api-proxy/npm/bin/codex-responses-api-proxy.js` (read)

### Outputs / Side Effects
- spawns subprocesses
- writes to stdout/stderr

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `import` `codex-rs/responses-api-proxy/npm/bin/codex-responses-api-proxy.js:4` `import { spawn } from "node:child_process";`
- `import` `codex-rs/responses-api-proxy/npm/bin/codex-responses-api-proxy.js:5` `import path from "path";`
- `import` `codex-rs/responses-api-proxy/npm/bin/codex-responses-api-proxy.js:6` `import { fileURLToPath } from "url";`
- `const` `codex-rs/responses-api-proxy/npm/bin/codex-responses-api-proxy.js:8` `const __filename = fileURLToPath(import.meta.url);`
- `const` `codex-rs/responses-api-proxy/npm/bin/codex-responses-api-proxy.js:9` `const __dirname = path.dirname(__filename);`
- `function` `codex-rs/responses-api-proxy/npm/bin/codex-responses-api-proxy.js:11` `function determineTargetTriple(platform, arch) {`
- `const` `codex-rs/responses-api-proxy/npm/bin/codex-responses-api-proxy.js:44` `const targetTriple = determineTargetTriple(process.platform, process.arch);`
- `const` `codex-rs/responses-api-proxy/npm/bin/codex-responses-api-proxy.js:51` `const vendorRoot = path.join(__dirname, "..", "vendor");`
- `const` `codex-rs/responses-api-proxy/npm/bin/codex-responses-api-proxy.js:52` `const archRoot = path.join(vendorRoot, targetTriple);`
- `const` `codex-rs/responses-api-proxy/npm/bin/codex-responses-api-proxy.js:53` `const binaryBaseName = "codex-responses-api-proxy";`
- `const` `codex-rs/responses-api-proxy/npm/bin/codex-responses-api-proxy.js:54` `const binaryPath = path.join(`
- `const` `codex-rs/responses-api-proxy/npm/bin/codex-responses-api-proxy.js:60` `const child = spawn(binaryPath, process.argv.slice(2), {`
- `const` `codex-rs/responses-api-proxy/npm/bin/codex-responses-api-proxy.js:69` `const forwardSignal = (signal) => {`
- `const` `codex-rs/responses-api-proxy/npm/bin/codex-responses-api-proxy.js:83` `const childResult = await new Promise((resolve) => {`

## Dependencies (auto sample)
### Imports / Includes
- `import { spawn } from "node:child_process";`
- `import path from "path";`
- `import { fileURLToPath } from "url";`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- calls process.exit(...)
- throws exceptions

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
