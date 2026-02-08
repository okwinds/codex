# `scripts/asciicheck.py`

## Identity
- kind: `source`
- ext: `.py`
- size_bytes: `3973`
- sha256: `5bf0bf3b147d14d38a5494db467a60487618aa188bffa655e5e37adc9e4ee9ef`
- generated_utc: `2026-02-03T16:08:31Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `scripts/asciicheck.py` (read)

### Outputs / Side Effects
- writes to stdout/stderr

## Public Surface (auto)
- `def main() -> int:`
- `def lint_utf8_ascii(filename: Path, fix: bool) -> bool:`
- `if __name__ == "__main__":`

## Definitions (auto, per-file)
- `import` `scripts/asciicheck.py:3` `import argparse`
- `import` `scripts/asciicheck.py:4` `import sys`
- `import` `scripts/asciicheck.py:5` `from pathlib import Path`
- `def` `scripts/asciicheck.py:49` `def main() -> int:`
- `def` `scripts/asciicheck.py:72` `def lint_utf8_ascii(filename: Path, fix: bool) -> bool:`
- `main` `scripts/asciicheck.py:126` `if __name__ == "__main__":`

## Dependencies (auto sample)
### Imports / Includes
- `import argparse`
- `import sys`
- `from pathlib import Path`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
