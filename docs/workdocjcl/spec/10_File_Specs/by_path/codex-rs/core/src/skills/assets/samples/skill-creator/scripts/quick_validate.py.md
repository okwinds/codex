# `codex-rs/core/src/skills/assets/samples/skill-creator/scripts/quick_validate.py`

## Identity
- kind: `source`
- ext: `.py`
- size_bytes: `3293`
- sha256: `6cc9dc3199c935916cf6f73fcbbbb0e3bb1b58c8f5109fefa499978908164f51`
- generated_utc: `2026-02-03T16:08:29Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/skills/assets/samples/skill-creator/scripts/quick_validate.py` (read)

### Outputs / Side Effects
- writes to stdout/stderr

## Public Surface (auto)
- `def validate_skill(skill_path):`
- `if __name__ == "__main__":`

## Definitions (auto, per-file)
- `import` `codex-rs/core/src/skills/assets/samples/skill-creator/scripts/quick_validate.py:6` `import re`
- `import` `codex-rs/core/src/skills/assets/samples/skill-creator/scripts/quick_validate.py:7` `import sys`
- `import` `codex-rs/core/src/skills/assets/samples/skill-creator/scripts/quick_validate.py:8` `from pathlib import Path`
- `import` `codex-rs/core/src/skills/assets/samples/skill-creator/scripts/quick_validate.py:10` `import yaml`
- `def` `codex-rs/core/src/skills/assets/samples/skill-creator/scripts/quick_validate.py:15` `def validate_skill(skill_path):`
- `main` `codex-rs/core/src/skills/assets/samples/skill-creator/scripts/quick_validate.py:94` `if __name__ == "__main__":`

## Dependencies (auto sample)
### Imports / Includes
- `import re`
- `import sys`
- `from pathlib import Path`
- `import yaml`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- `workdocjcl/spec/00_Overview/ARCHITECTURE.md`
