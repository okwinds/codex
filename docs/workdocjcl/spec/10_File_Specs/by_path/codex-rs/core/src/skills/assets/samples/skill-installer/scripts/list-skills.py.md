# `codex-rs/core/src/skills/assets/samples/skill-installer/scripts/list-skills.py`

## Identity
- kind: `source`
- ext: `.py`
- size_bytes: `2967`
- sha256: `e4e1f78ca3d045827f2a05cfd99fae57cc7c1a1bfeba8704029108834debff35`
- generated_utc: `2026-02-03T16:08:29Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/skills/assets/samples/skill-installer/scripts/list-skills.py` (read)
- env: `CODEX_HOME`

### Outputs / Side Effects
- writes to stdout/stderr

## Public Surface (auto)
- `class ListError(Exception):`
- `class Args(argparse.Namespace):`
- `def _request(url: str) -> bytes:`
- `def _codex_home() -> str:`
- `def _installed_skills() -> set[str]:`
- `def _list_skills(repo: str, path: str, ref: str) -> list[str]:`
- `def _parse_args(argv: list[str]) -> Args:`
- `def main(argv: list[str]) -> int:`
- `if __name__ == "__main__":`

## Definitions (auto, per-file)
- `import` `codex-rs/core/src/skills/assets/samples/skill-installer/scripts/list-skills.py:4` `from __future__ import annotations`
- `import` `codex-rs/core/src/skills/assets/samples/skill-installer/scripts/list-skills.py:6` `import argparse`
- `import` `codex-rs/core/src/skills/assets/samples/skill-installer/scripts/list-skills.py:7` `import json`
- `import` `codex-rs/core/src/skills/assets/samples/skill-installer/scripts/list-skills.py:8` `import os`
- `import` `codex-rs/core/src/skills/assets/samples/skill-installer/scripts/list-skills.py:9` `import sys`
- `import` `codex-rs/core/src/skills/assets/samples/skill-installer/scripts/list-skills.py:10` `import urllib.error`
- `import` `codex-rs/core/src/skills/assets/samples/skill-installer/scripts/list-skills.py:12` `from github_utils import github_api_contents_url, github_request`
- `class` `codex-rs/core/src/skills/assets/samples/skill-installer/scripts/list-skills.py:19` `class ListError(Exception):`
- `class` `codex-rs/core/src/skills/assets/samples/skill-installer/scripts/list-skills.py:23` `class Args(argparse.Namespace):`
- `def` `codex-rs/core/src/skills/assets/samples/skill-installer/scripts/list-skills.py:30` `def _request(url: str) -> bytes:`
- `def` `codex-rs/core/src/skills/assets/samples/skill-installer/scripts/list-skills.py:34` `def _codex_home() -> str:`
- `def` `codex-rs/core/src/skills/assets/samples/skill-installer/scripts/list-skills.py:38` `def _installed_skills() -> set[str]:`
- `def` `codex-rs/core/src/skills/assets/samples/skill-installer/scripts/list-skills.py:50` `def _list_skills(repo: str, path: str, ref: str) -> list[str]:`
- `def` `codex-rs/core/src/skills/assets/samples/skill-installer/scripts/list-skills.py:68` `def _parse_args(argv: list[str]) -> Args:`
- `def` `codex-rs/core/src/skills/assets/samples/skill-installer/scripts/list-skills.py:86` `def main(argv: list[str]) -> int:`
- `main` `codex-rs/core/src/skills/assets/samples/skill-installer/scripts/list-skills.py:106` `if __name__ == "__main__":`

## Dependencies (auto sample)
### Imports / Includes
- `from __future__ import annotations`
- `import argparse`
- `import json`
- `import os`
- `import sys`
- `import urllib.error`
- `from github_utils import github_api_contents_url, github_request`
### Referenced env vars
- `CODEX_HOME`

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- `workdocjcl/spec/00_Overview/ARCHITECTURE.md`
