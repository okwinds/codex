# `codex-rs/vendor/bubblewrap/tests/test-seccomp.py`

## Identity
- kind: `test`
- ext: `.py`
- size_bytes: `19642`
- sha256: `dcf11f0b49fb3a3d8639cc6f91bf52838d7de27b45c4c7e85c338abbcda8ead8`
- generated_utc: `2026-02-08T10:45:41Z`

## Purpose (Why)
Test or snapshot file used for automated verification.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/vendor/bubblewrap/tests/test-seccomp.py` (read)

### Outputs / Side Effects
- none (file is declarative: doc/config/test/asset)

## Public Surface (auto)
- `class Test(unittest.TestCase):`
- `def setUp(self) -> None:`
- `def tearDown(self) -> None:`
- `def test_no_seccomp(self) -> None:`
- `def test_seccomp_allowlist(self) -> None:`
- `def test_seccomp_denylist(self) -> None:`
- `def test_seccomp_stacked(self, allowlist_first=False) -> None:`
- `def test_seccomp_stacked_allowlist_first(self) -> None:`
- `def test_seccomp_invalid(self) -> None:`
- `def main():`
- `if __name__ == '__main__':`

## Definitions (auto, per-file)
- (not extracted)

## Dependencies (auto sample)
### Imports / Includes
- `import errno`
- `import logging`
- `import os`
- `import subprocess`
- `import sys`
- `import tempfile`
- `import termios`
- `import unittest`
- `import seccomp`
- `from tap.runner import TAPTestRunner`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (none detected)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
