# `scripts/readme_toc.py`

## Identity
- kind: `source`
- ext: `.py`
- size_bytes: `3872`
- sha256: `5c866752be5b7bd477548bb09805a41d85d2598881237ce185411e6a649d3e55`
- generated_utc: `2026-02-03T16:08:31Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `scripts/readme_toc.py` (read)

### Outputs / Side Effects
- writes to stdout/stderr

## Public Surface (auto)
- `def main() -> int:`
- `def generate_toc_lines(content: str) -> List[str]:`
- `def check_or_fix(readme_path: Path, fix: bool) -> int:`
- `if __name__ == "__main__":`

## Definitions (auto, per-file)
- `import` `scripts/readme_toc.py:10` `import argparse`
- `import` `scripts/readme_toc.py:11` `import sys`
- `import` `scripts/readme_toc.py:12` `import re`
- `import` `scripts/readme_toc.py:13` `import difflib`
- `import` `scripts/readme_toc.py:14` `from pathlib import Path`
- `import` `scripts/readme_toc.py:15` `from typing import List`
- `def` `scripts/readme_toc.py:22` `def main() -> int:`
- `def` `scripts/readme_toc.py:37` `def generate_toc_lines(content: str) -> List[str]:`
- `def` `scripts/readme_toc.py:71` `def check_or_fix(readme_path: Path, fix: bool) -> int:`
- `main` `scripts/readme_toc.py:119` `if __name__ == "__main__":`

## Dependencies (auto sample)
### Imports / Includes
- `import argparse`
- `import sys`
- `import re`
- `import difflib`
- `from pathlib import Path`
- `from typing import List`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
