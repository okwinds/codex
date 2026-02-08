# `scripts/stage_npm_packages.py`

## Identity
- kind: `source`
- ext: `.py`
- size_bytes: `5752`
- sha256: `89bba6590fb6f781799b867852ffe9d95c9e6ac3d8e139d241253f1c0b3a7ce9`
- generated_utc: `2026-02-03T16:08:31Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `scripts/stage_npm_packages.py` (read)
- env: `RUNNER_TEMP`

### Outputs / Side Effects
- writes to stdout/stderr

## Public Surface (auto)
- `def parse_args() -> argparse.Namespace:`
- `def collect_native_components(packages: list[str]) -> set[str]:`
- `def resolve_release_workflow(version: str) -> dict:`
- `def resolve_workflow_url(version: str, override: str | None) -> tuple[str, str | None]:`
- `def install_native_components(`
- `def run_command(cmd: list[str]) -> None:`
- `def main() -> int:`
- `if __name__ == "__main__":`

## Definitions (auto, per-file)
- `import` `scripts/stage_npm_packages.py:4` `from __future__ import annotations`
- `import` `scripts/stage_npm_packages.py:6` `import argparse`
- `import` `scripts/stage_npm_packages.py:7` `import importlib.util`
- `import` `scripts/stage_npm_packages.py:8` `import json`
- `import` `scripts/stage_npm_packages.py:9` `import os`
- `import` `scripts/stage_npm_packages.py:10` `import shutil`
- `import` `scripts/stage_npm_packages.py:11` `import subprocess`
- `import` `scripts/stage_npm_packages.py:12` `import tempfile`
- `import` `scripts/stage_npm_packages.py:13` `from pathlib import Path`
- `def` `scripts/stage_npm_packages.py:31` `def parse_args() -> argparse.Namespace:`
- `def` `scripts/stage_npm_packages.py:63` `def collect_native_components(packages: list[str]) -> set[str]:`
- `def` `scripts/stage_npm_packages.py:71` `def resolve_release_workflow(version: str) -> dict:`
- `def` `scripts/stage_npm_packages.py:95` `def resolve_workflow_url(version: str, override: str | None) -> tuple[str, str | None]:`
- `def` `scripts/stage_npm_packages.py:103` `def install_native_components(`
- `def` `scripts/stage_npm_packages.py:118` `def run_command(cmd: list[str]) -> None:`
- `def` `scripts/stage_npm_packages.py:123` `def main() -> int:`
- `main` `scripts/stage_npm_packages.py:188` `if __name__ == "__main__":`

## Dependencies (auto sample)
### Imports / Includes
- `from __future__ import annotations`
- `import argparse`
- `import importlib.util`
- `import json`
- `import os`
- `import shutil`
- `import subprocess`
- `import tempfile`
- `from pathlib import Path`
### Referenced env vars
- `RUNNER_TEMP`

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
