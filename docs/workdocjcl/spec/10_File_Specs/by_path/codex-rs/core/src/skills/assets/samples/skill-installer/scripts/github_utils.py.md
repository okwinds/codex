# `codex-rs/core/src/skills/assets/samples/skill-installer/scripts/github_utils.py`

## Identity
- kind: `source`
- ext: `.py`
- size_bytes: `659`
- sha256: `61c1bbe2ae217433b4b6f9f09f21aca4df52c12598068343ade719f706e4859b`
- generated_utc: `2026-02-03T16:08:29Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/skills/assets/samples/skill-installer/scripts/github_utils.py` (read)
- env: `GH_TOKEN`, `GITHUB_TOKEN`

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `def github_request(url: str, user_agent: str) -> bytes:`
- `def github_api_contents_url(repo: str, path: str, ref: str) -> str:`

## Definitions (auto, per-file)
- `import` `codex-rs/core/src/skills/assets/samples/skill-installer/scripts/github_utils.py:4` `from __future__ import annotations`
- `import` `codex-rs/core/src/skills/assets/samples/skill-installer/scripts/github_utils.py:6` `import os`
- `import` `codex-rs/core/src/skills/assets/samples/skill-installer/scripts/github_utils.py:7` `import urllib.request`
- `def` `codex-rs/core/src/skills/assets/samples/skill-installer/scripts/github_utils.py:10` `def github_request(url: str, user_agent: str) -> bytes:`
- `def` `codex-rs/core/src/skills/assets/samples/skill-installer/scripts/github_utils.py:20` `def github_api_contents_url(repo: str, path: str, ref: str) -> str:`

## Dependencies (auto sample)
### Imports / Includes
- `from __future__ import annotations`
- `import os`
- `import urllib.request`
### Referenced env vars
- `GH_TOKEN`
- `GITHUB_TOKEN`

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- `workdocjcl/spec/00_Overview/ARCHITECTURE.md`
