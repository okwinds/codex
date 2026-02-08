# `shell-tool-mcp/src/osRelease.ts`

## Identity
- kind: `source`
- ext: `.ts`
- size_bytes: `997`
- sha256: `ee0fa1281cfcf4fbbfcae78a65256ea0f5148b386dd7641d71ed456e1ca06d5c`
- generated_utc: `2026-02-03T16:08:31Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `shell-tool-mcp/src/osRelease.ts` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `export function parseOsRelease(contents: string): OsReleaseInfo {`
- `export function readOsRelease(pathname = "/etc/os-release"): OsReleaseInfo {`

## Definitions (auto, per-file)
- `import` `shell-tool-mcp/src/osRelease.ts:1` `import { readFileSync } from "node:fs";`
- `import` `shell-tool-mcp/src/osRelease.ts:2` `import { OsReleaseInfo } from "./types";`
- `export` `shell-tool-mcp/src/osRelease.ts:4` `export function parseOsRelease(contents: string): OsReleaseInfo {`
- `const` `shell-tool-mcp/src/osRelease.ts:5` `const lines = contents.split("\n").filter(Boolean);`
- `const` `shell-tool-mcp/src/osRelease.ts:6` `const info: Record<string, string> = {};`
- `const` `shell-tool-mcp/src/osRelease.ts:12` `const key = rawKey.toLowerCase();`
- `const` `shell-tool-mcp/src/osRelease.ts:13` `const value = rawValue.replace(/^"/, "").replace(/"$/, "");`
- `const` `shell-tool-mcp/src/osRelease.ts:16` `const idLike = (info.id_like || "")`
- `export` `shell-tool-mcp/src/osRelease.ts:27` `export function readOsRelease(pathname = "/etc/os-release"): OsReleaseInfo {`
- `const` `shell-tool-mcp/src/osRelease.ts:29` `const contents = readFileSync(pathname, "utf8");`

## Dependencies (auto sample)
### Imports / Includes
- `import { readFileSync } from "node:fs";`
- `import { OsReleaseInfo } from "./types";`
- `export function parseOsRelease(contents: string): OsReleaseInfo {`
- `export function readOsRelease(pathname = "/etc/os-release"): OsReleaseInfo {`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- `workdocjcl/spec/05_Integrations/MCP.md`
