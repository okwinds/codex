# `codex-rs/windows-sandbox-rs/sandbox_smoketests.py`

## Identity
- kind: `source`
- ext: `.py`
- size_bytes: `22202`
- sha256: `1fc8e340ec17164bc24e4fc091da393fc1fdad5ac55373674e12f3292747fdb6`
- generated_utc: `2026-02-03T16:08:31Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/windows-sandbox-rs/sandbox_smoketests.py` (read)
- env: `CARGO_TARGET_DIR`

### Outputs / Side Effects
- writes to stdout/stderr

## Public Surface (auto)
- `def _resolve_codex_cmd() -> List[str]:`
- `class CaseResult:`
- `def __init__(self, name: str, ok: bool, detail: str = ""):`
- `def run_sbx(`
- `def have(cmd: str) -> bool:`
- `def make_dir_clean(p: Path) -> None:`
- `def write_file(p: Path, content: str = "x") -> None:`
- `def remove_if_exists(p: Path) -> None:`
- `def assert_exists(p: Path) -> bool:`
- `def assert_not_exists(p: Path) -> bool:`
- `def make_junction(link: Path, target: Path) -> bool:`
- `def make_symlink(link: Path, target: Path) -> bool:`
- `def summarize(results: List[CaseResult]) -> int:`
- `def main() -> int:`
- `def add(name: str, ok: bool, detail: str = ""):`
- `if __name__ == "__main__":`

## Definitions (auto, per-file)
- `import` `codex-rs/windows-sandbox-rs/sandbox_smoketests.py:5` `import os`
- `import` `codex-rs/windows-sandbox-rs/sandbox_smoketests.py:6` `import sys`
- `import` `codex-rs/windows-sandbox-rs/sandbox_smoketests.py:7` `import shutil`
- `import` `codex-rs/windows-sandbox-rs/sandbox_smoketests.py:8` `import subprocess`
- `import` `codex-rs/windows-sandbox-rs/sandbox_smoketests.py:9` `from pathlib import Path`
- `import` `codex-rs/windows-sandbox-rs/sandbox_smoketests.py:10` `from typing import List, Optional, Tuple`
- `def` `codex-rs/windows-sandbox-rs/sandbox_smoketests.py:12` `def _resolve_codex_cmd() -> List[str]:`
- `class` `codex-rs/windows-sandbox-rs/sandbox_smoketests.py:57` `class CaseResult:`
- `def` `codex-rs/windows-sandbox-rs/sandbox_smoketests.py:58` `def __init__(self, name: str, ok: bool, detail: str = ""):`
- `def` `codex-rs/windows-sandbox-rs/sandbox_smoketests.py:61` `def run_sbx(`
- `def` `codex-rs/windows-sandbox-rs/sandbox_smoketests.py:93` `def have(cmd: str) -> bool:`
- `def` `codex-rs/windows-sandbox-rs/sandbox_smoketests.py:96` `def make_dir_clean(p: Path) -> None:`
- `def` `codex-rs/windows-sandbox-rs/sandbox_smoketests.py:101` `def write_file(p: Path, content: str = "x") -> None:`
- `def` `codex-rs/windows-sandbox-rs/sandbox_smoketests.py:105` `def remove_if_exists(p: Path) -> None:`
- `def` `codex-rs/windows-sandbox-rs/sandbox_smoketests.py:112` `def assert_exists(p: Path) -> bool:`
- `def` `codex-rs/windows-sandbox-rs/sandbox_smoketests.py:115` `def assert_not_exists(p: Path) -> bool:`
- `def` `codex-rs/windows-sandbox-rs/sandbox_smoketests.py:118` `def make_junction(link: Path, target: Path) -> bool:`
- `def` `codex-rs/windows-sandbox-rs/sandbox_smoketests.py:126` `def make_symlink(link: Path, target: Path) -> bool:`
- `def` `codex-rs/windows-sandbox-rs/sandbox_smoketests.py:138` `def summarize(results: List[CaseResult]) -> int:`
- `def` `codex-rs/windows-sandbox-rs/sandbox_smoketests.py:148` `def main() -> int:`
- `def` `codex-rs/windows-sandbox-rs/sandbox_smoketests.py:162` `def add(name: str, ok: bool, detail: str = ""):`
- `main` `codex-rs/windows-sandbox-rs/sandbox_smoketests.py:500` `if __name__ == "__main__":`

## Dependencies (auto sample)
### Imports / Includes
- `import os`
- `import sys`
- `import shutil`
- `import subprocess`
- `from pathlib import Path`
- `from typing import List, Optional, Tuple`
### Referenced env vars
- `CARGO_TARGET_DIR`

## Error Handling / Edge Cases
- has retry/timeout/backoff logic

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
