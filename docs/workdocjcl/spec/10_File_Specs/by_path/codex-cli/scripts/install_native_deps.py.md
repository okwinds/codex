# `codex-cli/scripts/install_native_deps.py`

## Identity
- kind: `source`
- ext: `.py`
- size_bytes: `15930`
- sha256: `befc82851c36cff9bd5412fed8277a35acf96c9fea7c00d7204196e5f6bf05e7`
- generated_utc: `2026-02-03T16:08:28Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-cli/scripts/install_native_deps.py` (read)
- env: `GITHUB_ACTIONS`

### Outputs / Side Effects
- writes to stdout/stderr

## Public Surface (auto)
- `class BinaryComponent:`
- `def _gha_enabled() -> bool:`
- `def _gha_escape(value: str) -> str:`
- `def _gha_error(*, title: str, message: str) -> None:`
- `def _gha_group(title: str):`
- `def parse_args() -> argparse.Namespace:`
- `def main() -> int:`
- `def fetch_rg(`
- `def _download_artifacts(workflow_id: str, dest_dir: Path) -> None:`
- `def install_binary_components(`
- `def _install_single_binary(`
- `def _archive_name_for_target(artifact_prefix: str, target: str) -> str:`
- `def _fetch_single_rg(`
- `def _download_file(url: str, dest: Path) -> None:`
- `def extract_archive(`
- `def _load_manifest(manifest_path: Path) -> dict:`
- `if __name__ == "__main__":`

## Definitions (auto, per-file)
- `import` `codex-cli/scripts/install_native_deps.py:4` `import argparse`
- `import` `codex-cli/scripts/install_native_deps.py:5` `from contextlib import contextmanager`
- `import` `codex-cli/scripts/install_native_deps.py:6` `import json`
- `import` `codex-cli/scripts/install_native_deps.py:7` `import os`
- `import` `codex-cli/scripts/install_native_deps.py:8` `import shutil`
- `import` `codex-cli/scripts/install_native_deps.py:9` `import subprocess`
- `import` `codex-cli/scripts/install_native_deps.py:10` `import tarfile`
- `import` `codex-cli/scripts/install_native_deps.py:11` `import tempfile`
- `import` `codex-cli/scripts/install_native_deps.py:12` `import zipfile`
- `import` `codex-cli/scripts/install_native_deps.py:13` `from dataclasses import dataclass`
- `import` `codex-cli/scripts/install_native_deps.py:14` `from concurrent.futures import ThreadPoolExecutor, as_completed`
- `import` `codex-cli/scripts/install_native_deps.py:15` `from pathlib import Path`
- `import` `codex-cli/scripts/install_native_deps.py:16` `import sys`
- `import` `codex-cli/scripts/install_native_deps.py:17` `from typing import Iterable, Sequence`
- `import` `codex-cli/scripts/install_native_deps.py:18` `from urllib.parse import urlparse`
- `import` `codex-cli/scripts/install_native_deps.py:19` `from urllib.request import urlopen`
- `class` `codex-cli/scripts/install_native_deps.py:37` `class BinaryComponent:`
- `def` `codex-cli/scripts/install_native_deps.py:86` `def _gha_enabled() -> bool:`
- `def` `codex-cli/scripts/install_native_deps.py:93` `def _gha_escape(value: str) -> str:`
- `def` `codex-cli/scripts/install_native_deps.py:98` `def _gha_error(*, title: str, message: str) -> None:`
- `def` `codex-cli/scripts/install_native_deps.py:110` `def _gha_group(title: str):`
- `def` `codex-cli/scripts/install_native_deps.py:122` `def parse_args() -> argparse.Namespace:`
- `def` `codex-cli/scripts/install_native_deps.py:154` `def main() -> int:`
- `def` `codex-cli/scripts/install_native_deps.py:194` `def fetch_rg(`
- `def` `codex-cli/scripts/install_native_deps.py:262` `def _download_artifacts(workflow_id: str, dest_dir: Path) -> None:`
- `def` `codex-cli/scripts/install_native_deps.py:276` `def install_binary_components(`
- `def` `codex-cli/scripts/install_native_deps.py:308` `def _install_single_binary(`
- `def` `codex-cli/scripts/install_native_deps.py:334` `def _archive_name_for_target(artifact_prefix: str, target: str) -> str:`
- `def` `codex-cli/scripts/install_native_deps.py:340` `def _fetch_single_rg(`
- `def` `codex-cli/scripts/install_native_deps.py:401` `def _download_file(url: str, dest: Path) -> None:`
- `def` `codex-cli/scripts/install_native_deps.py:409` `def extract_archive(`
- `def` `codex-cli/scripts/install_native_deps.py:456` `def _load_manifest(manifest_path: Path) -> dict:`
- `main` `codex-cli/scripts/install_native_deps.py:472` `if __name__ == "__main__":`
- `import` `codex-cli/scripts/install_native_deps.py:473` `import sys`

## Dependencies (auto sample)
### Imports / Includes
- `import argparse`
- `from contextlib import contextmanager`
- `import json`
- `import os`
- `import shutil`
- `import subprocess`
- `import tarfile`
- `import tempfile`
- `import zipfile`
- `from dataclasses import dataclass`
- `from concurrent.futures import ThreadPoolExecutor, as_completed`
- `from pathlib import Path`
- `import sys`
- `from typing import Iterable, Sequence`
- `from urllib.parse import urlparse`
- `from urllib.request import urlopen`
- `import sys`
### Referenced env vars
- `GITHUB_ACTIONS`

## Error Handling / Edge Cases
- has retry/timeout/backoff logic

## Spec Links
- `workdocjcl/spec/07_Infrastructure/PACKAGING.md`
