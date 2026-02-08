# `codex-cli/bin/codex.js`

## Identity
- kind: `source`
- ext: `.js`
- size_bytes: `4997`
- sha256: `69b5cbe73a947e9532b1be337e27a1988bfba98a77148f8a96804fdfbf7a6903`
- generated_utc: `2026-02-03T16:08:28Z`

## Purpose (Why)
Node wrapper entrypoint for @openai/codex: selects the correct platform-specific native binary and executes it with signal forwarding.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-cli/bin/codex.js` (read)
- env: `PATH`, `npm_config_user_agent`, `npm_execpath`

### Outputs / Side Effects
- spawns subprocesses
- writes to stdout/stderr

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `import` `codex-cli/bin/codex.js:4` `import { spawn } from "node:child_process";`
- `import` `codex-cli/bin/codex.js:5` `import { existsSync } from "fs";`
- `import` `codex-cli/bin/codex.js:6` `import path from "path";`
- `import` `codex-cli/bin/codex.js:7` `import { fileURLToPath } from "url";`
- `const` `codex-cli/bin/codex.js:10` `const __filename = fileURLToPath(import.meta.url);`
- `const` `codex-cli/bin/codex.js:11` `const __dirname = path.dirname(__filename);`
- `const` `codex-cli/bin/codex.js:62` `const vendorRoot = path.join(__dirname, "..", "vendor");`
- `const` `codex-cli/bin/codex.js:63` `const archRoot = path.join(vendorRoot, targetTriple);`
- `const` `codex-cli/bin/codex.js:64` `const codexBinaryName = process.platform === "win32" ? "codex.exe" : "codex";`
- `const` `codex-cli/bin/codex.js:65` `const binaryPath = path.join(archRoot, "codex", codexBinaryName);`
- `function` `codex-cli/bin/codex.js:73` `function getUpdatedPath(newDirs) {`
- `const` `codex-cli/bin/codex.js:74` `const pathSep = process.platform === "win32" ? ";" : ":";`
- `const` `codex-cli/bin/codex.js:75` `const existingPath = process.env.PATH || "";`
- `const` `codex-cli/bin/codex.js:76` `const updatedPath = [`
- `function` `codex-cli/bin/codex.js:87` `function detectPackageManager() {`
- `const` `codex-cli/bin/codex.js:88` `const userAgent = process.env.npm_config_user_agent || "";`
- `const` `codex-cli/bin/codex.js:93` `const execPath = process.env.npm_execpath || "";`
- `const` `codex-cli/bin/codex.js:108` `const additionalDirs = [];`
- `const` `codex-cli/bin/codex.js:109` `const pathDir = path.join(archRoot, "path");`
- `const` `codex-cli/bin/codex.js:113` `const updatedPath = getUpdatedPath(additionalDirs);`
- `const` `codex-cli/bin/codex.js:115` `const env = { ...process.env, PATH: updatedPath };`
- `const` `codex-cli/bin/codex.js:116` `const packageManagerEnvVar =`
- `const` `codex-cli/bin/codex.js:122` `const child = spawn(binaryPath, process.argv.slice(2), {`
- `const` `codex-cli/bin/codex.js:140` `const forwardSignal = (signal) => {`
- `const` `codex-cli/bin/codex.js:160` `const childResult = await new Promise((resolve) => {`

## Dependencies (auto sample)
### Imports / Includes
- `import { spawn } from "node:child_process";`
- `import { existsSync } from "fs";`
- `import path from "path";`
- `import { fileURLToPath } from "url";`
### Referenced env vars
- `PATH`
- `npm_config_user_agent`
- `npm_execpath`

## Error Handling / Edge Cases
- calls process.exit(...)
- throws exceptions

## Spec Links
- `workdocjcl/spec/07_Infrastructure/PACKAGING.md`
