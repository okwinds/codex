# `codex-cli/scripts/build_npm_package.py`

## Identity
- kind: `source`
- ext: `.py`
- size_bytes: `11227`
- sha256: `150afa9a25aa542a3db086b7c4692f551f968c28bd9175cf783050ff480bfc85`
- generated_utc: `2026-02-03T16:08:28Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-cli/scripts/build_npm_package.py` (read)

### Outputs / Side Effects
- writes to stdout/stderr

## Public Surface (auto)
- `def parse_args() -> argparse.Namespace:`
- `def main() -> int:`
- `def prepare_staging_dir(staging_dir: Path | None) -> tuple[Path, bool]:`
- `def stage_sources(staging_dir: Path, version: str, package: str) -> None:`
- `def run_command(cmd: list[str], cwd: Path | None = None) -> None:`
- `def stage_codex_sdk_sources(staging_dir: Path) -> None:`
- `def copy_native_binaries(`
- `def run_npm_pack(staging_dir: Path, output_path: Path) -> Path:`
- `if __name__ == "__main__":`

## Definitions (auto, per-file)
- `import` `codex-cli/scripts/build_npm_package.py:4` `import argparse`
- `import` `codex-cli/scripts/build_npm_package.py:5` `import json`
- `import` `codex-cli/scripts/build_npm_package.py:6` `import shutil`
- `import` `codex-cli/scripts/build_npm_package.py:7` `import subprocess`
- `import` `codex-cli/scripts/build_npm_package.py:8` `import sys`
- `import` `codex-cli/scripts/build_npm_package.py:9` `import tempfile`
- `import` `codex-cli/scripts/build_npm_package.py:10` `from pathlib import Path`
- `def` `codex-cli/scripts/build_npm_package.py:35` `def parse_args() -> argparse.Namespace:`
- `def` `codex-cli/scripts/build_npm_package.py:80` `def main() -> int:`
- `def` `codex-cli/scripts/build_npm_package.py:150` `def prepare_staging_dir(staging_dir: Path | None) -> tuple[Path, bool]:`
- `def` `codex-cli/scripts/build_npm_package.py:162` `def stage_sources(staging_dir: Path, version: str, package: str) -> None:`
- `def` `codex-cli/scripts/build_npm_package.py:214` `def run_command(cmd: list[str], cwd: Path | None = None) -> None:`
- `def` `codex-cli/scripts/build_npm_package.py:219` `def stage_codex_sdk_sources(staging_dir: Path) -> None:`
- `def` `codex-cli/scripts/build_npm_package.py:240` `def copy_native_binaries(`
- `def` `codex-cli/scripts/build_npm_package.py:286` `def run_npm_pack(staging_dir: Path, output_path: Path) -> Path:`
- `main` `codex-cli/scripts/build_npm_package.py:318` `if __name__ == "__main__":`
- `import` `codex-cli/scripts/build_npm_package.py:319` `import sys`

## Dependencies (auto sample)
### Imports / Includes
- `import argparse`
- `import json`
- `import shutil`
- `import subprocess`
- `import sys`
- `import tempfile`
- `from pathlib import Path`
- `import sys`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- `workdocjcl/spec/07_Infrastructure/PACKAGING.md`
