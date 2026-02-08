# `sdk/typescript/tests/run.test.ts`

## Identity
- kind: `test`
- ext: `.ts`
- size_bytes: `25959`
- sha256: `c77f0099c7f14d11704ca30235d52573a154bdaefe555327283b6df50c22613e`
- generated_utc: `2026-02-03T16:08:31Z`

## Purpose (Why)
Test or snapshot file used for automated verification.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `sdk/typescript/tests/run.test.ts` (read)
- env: `CODEX_ENV_SHOULD_NOT_LEAK`

### Outputs / Side Effects
- none (file is declarative: doc/config/test/asset)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- (not extracted)

## Dependencies (auto sample)
### Imports / Includes
- `import fs from "node:fs";`
- `import os from "node:os";`
- `import path from "node:path";`
- `import { codexExecSpy } from "./codexExecSpy";`
- `import { describe, expect, it } from "@jest/globals";`
- `import { Codex } from "../src/codex";`
- `import {`
### Referenced env vars
- `CODEX_ENV_SHOULD_NOT_LEAK`

## Error Handling / Edge Cases
- (none detected)

## Spec Links
- `workdocjcl/spec/00_Overview/PROJECT.md`
