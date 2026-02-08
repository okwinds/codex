# `codex-rs/core/src/skills/assets/samples/skill-installer/scripts/install-skill-from-github.py`

## Identity
- kind: `source`
- ext: `.py`
- size_bytes: `10096`
- sha256: `0fbbd36e8ea294442c0bd48d6f610a2e8656216bfef5c322f1dcf448ef2f09f1`
- generated_utc: `2026-02-03T16:08:29Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/skills/assets/samples/skill-installer/scripts/install-skill-from-github.py` (read)
- env: `CODEX_HOME`

### Outputs / Side Effects
- writes to stdout/stderr

## Public Surface (auto)
- `class Args:`
- `class Source:`
- `class InstallError(Exception):`
- `def _codex_home() -> str:`
- `def _tmp_root() -> str:`
- `def _request(url: str) -> bytes:`
- `def _parse_github_url(url: str, default_ref: str) -> tuple[str, str, str, str | None]:`
- `def _download_repo_zip(owner: str, repo: str, ref: str, dest_dir: str) -> str:`
- `def _run_git(args: list[str]) -> None:`
- `def _safe_extract_zip(zip_file: zipfile.ZipFile, dest_dir: str) -> None:`
- `def _validate_relative_path(path: str) -> None:`
- `def _validate_skill_name(name: str) -> None:`
- `def _git_sparse_checkout(repo_url: str, ref: str, paths: list[str], dest_dir: str) -> str:`
- `def _validate_skill(path: str) -> None:`
- `def _copy_skill(src: str, dest_dir: str) -> None:`
- `def _build_repo_url(owner: str, repo: str) -> str:`
- `def _build_repo_ssh(owner: str, repo: str) -> str:`
- `def _prepare_repo(source: Source, method: str, tmp_dir: str) -> str:`
- `def _resolve_source(args: Args) -> Source:`
- `def _default_dest() -> str:`
- `def _parse_args(argv: list[str]) -> Args:`
- `def main(argv: list[str]) -> int:`
- `if __name__ == "__main__":`

## Definitions (auto, per-file)
- `import` `codex-rs/core/src/skills/assets/samples/skill-installer/scripts/install-skill-from-github.py:4` `from __future__ import annotations`
- `import` `codex-rs/core/src/skills/assets/samples/skill-installer/scripts/install-skill-from-github.py:6` `import argparse`
- `import` `codex-rs/core/src/skills/assets/samples/skill-installer/scripts/install-skill-from-github.py:7` `from dataclasses import dataclass`
- `import` `codex-rs/core/src/skills/assets/samples/skill-installer/scripts/install-skill-from-github.py:8` `import os`
- `import` `codex-rs/core/src/skills/assets/samples/skill-installer/scripts/install-skill-from-github.py:9` `import shutil`
- `import` `codex-rs/core/src/skills/assets/samples/skill-installer/scripts/install-skill-from-github.py:10` `import subprocess`
- `import` `codex-rs/core/src/skills/assets/samples/skill-installer/scripts/install-skill-from-github.py:11` `import sys`
- `import` `codex-rs/core/src/skills/assets/samples/skill-installer/scripts/install-skill-from-github.py:12` `import tempfile`
- `import` `codex-rs/core/src/skills/assets/samples/skill-installer/scripts/install-skill-from-github.py:13` `import urllib.error`
- `import` `codex-rs/core/src/skills/assets/samples/skill-installer/scripts/install-skill-from-github.py:14` `import urllib.parse`
- `import` `codex-rs/core/src/skills/assets/samples/skill-installer/scripts/install-skill-from-github.py:15` `import zipfile`
- `import` `codex-rs/core/src/skills/assets/samples/skill-installer/scripts/install-skill-from-github.py:17` `from github_utils import github_request`
- `class` `codex-rs/core/src/skills/assets/samples/skill-installer/scripts/install-skill-from-github.py:22` `class Args:`
- `class` `codex-rs/core/src/skills/assets/samples/skill-installer/scripts/install-skill-from-github.py:33` `class Source:`
- `class` `codex-rs/core/src/skills/assets/samples/skill-installer/scripts/install-skill-from-github.py:41` `class InstallError(Exception):`
- `def` `codex-rs/core/src/skills/assets/samples/skill-installer/scripts/install-skill-from-github.py:45` `def _codex_home() -> str:`
- `def` `codex-rs/core/src/skills/assets/samples/skill-installer/scripts/install-skill-from-github.py:49` `def _tmp_root() -> str:`
- `def` `codex-rs/core/src/skills/assets/samples/skill-installer/scripts/install-skill-from-github.py:55` `def _request(url: str) -> bytes:`
- `def` `codex-rs/core/src/skills/assets/samples/skill-installer/scripts/install-skill-from-github.py:59` `def _parse_github_url(url: str, default_ref: str) -> tuple[str, str, str, str | None]:`
- `def` `codex-rs/core/src/skills/assets/samples/skill-installer/scripts/install-skill-from-github.py:80` `def _download_repo_zip(owner: str, repo: str, ref: str, dest_dir: str) -> str:`
- `def` `codex-rs/core/src/skills/assets/samples/skill-installer/scripts/install-skill-from-github.py:99` `def _run_git(args: list[str]) -> None:`
- `def` `codex-rs/core/src/skills/assets/samples/skill-installer/scripts/install-skill-from-github.py:105` `def _safe_extract_zip(zip_file: zipfile.ZipFile, dest_dir: str) -> None:`
- `def` `codex-rs/core/src/skills/assets/samples/skill-installer/scripts/install-skill-from-github.py:115` `def _validate_relative_path(path: str) -> None:`
- `def` `codex-rs/core/src/skills/assets/samples/skill-installer/scripts/install-skill-from-github.py:120` `def _validate_skill_name(name: str) -> None:`
- `def` `codex-rs/core/src/skills/assets/samples/skill-installer/scripts/install-skill-from-github.py:128` `def _git_sparse_checkout(repo_url: str, ref: str, paths: list[str], dest_dir: str) -> str:`
- `def` `codex-rs/core/src/skills/assets/samples/skill-installer/scripts/install-skill-from-github.py:164` `def _validate_skill(path: str) -> None:`
- `def` `codex-rs/core/src/skills/assets/samples/skill-installer/scripts/install-skill-from-github.py:172` `def _copy_skill(src: str, dest_dir: str) -> None:`
- `def` `codex-rs/core/src/skills/assets/samples/skill-installer/scripts/install-skill-from-github.py:179` `def _build_repo_url(owner: str, repo: str) -> str:`
- `def` `codex-rs/core/src/skills/assets/samples/skill-installer/scripts/install-skill-from-github.py:183` `def _build_repo_ssh(owner: str, repo: str) -> str:`
- `def` `codex-rs/core/src/skills/assets/samples/skill-installer/scripts/install-skill-from-github.py:187` `def _prepare_repo(source: Source, method: str, tmp_dir: str) -> str:`
- `def` `codex-rs/core/src/skills/assets/samples/skill-installer/scripts/install-skill-from-github.py:209` `def _resolve_source(args: Args) -> Source:`
- `def` `codex-rs/core/src/skills/assets/samples/skill-installer/scripts/install-skill-from-github.py:243` `def _default_dest() -> str:`
- `def` `codex-rs/core/src/skills/assets/samples/skill-installer/scripts/install-skill-from-github.py:247` `def _parse_args(argv: list[str]) -> Args:`
- `def` `codex-rs/core/src/skills/assets/samples/skill-installer/scripts/install-skill-from-github.py:269` `def main(argv: list[str]) -> int:`
- `main` `codex-rs/core/src/skills/assets/samples/skill-installer/scripts/install-skill-from-github.py:307` `if __name__ == "__main__":`

## Dependencies (auto sample)
### Imports / Includes
- `from __future__ import annotations`
- `import argparse`
- `from dataclasses import dataclass`
- `import os`
- `import shutil`
- `import subprocess`
- `import sys`
- `import tempfile`
- `import urllib.error`
- `import urllib.parse`
- `import zipfile`
- `from github_utils import github_request`
### Referenced env vars
- `CODEX_HOME`

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- `workdocjcl/spec/00_Overview/ARCHITECTURE.md`
