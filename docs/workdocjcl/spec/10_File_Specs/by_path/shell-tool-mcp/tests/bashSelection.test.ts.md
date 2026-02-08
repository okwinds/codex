# `shell-tool-mcp/tests/bashSelection.test.ts`

## Identity
- kind: `test`
- ext: `.ts`
- size_bytes: `1481`
- sha256: `d517c4492b420833cefdcdd807e89aa38e623bd2b5ceec1b399f7c778fa553d2`
- generated_utc: `2026-02-08T10:45:42Z`

## Purpose (Why)
Test or snapshot file used for automated verification.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `shell-tool-mcp/tests/bashSelection.test.ts` (read)

### Outputs / Side Effects
- none (file is declarative: doc/config/test/asset)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- (not extracted)

## Dependencies (auto sample)
### Imports / Includes
- `import { selectDarwinBash, selectLinuxBash } from "../src/bashSelection";`
- `import { DARWIN_BASH_VARIANTS, LINUX_BASH_VARIANTS } from "../src/constants";`
- `import { OsReleaseInfo } from "../src/types";`
- `import path from "node:path";`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (none detected)

## Spec Links
- `docs/workdocjcl/spec/05_Integrations/MCP.md`
