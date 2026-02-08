# `codex-rs/core/src/skills/assets/samples/skill-creator/scripts/init_skill.py`

## Identity
- kind: `source`
- ext: `.py`
- size_bytes: `14483`
- sha256: `bcb8982d3f033a094f2f1be43123ac8537e2562d25d8ba4d8ef2196ae514d96d`
- generated_utc: `2026-02-03T16:08:29Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/skills/assets/samples/skill-creator/scripts/init_skill.py` (read)

### Outputs / Side Effects
- writes to stdout/stderr

## Public Surface (auto)
- `def main():`
- `if __name__ == "__main__":`
- `def normalize_skill_name(skill_name):`
- `def title_case_skill_name(skill_name):`
- `def parse_resources(raw_resources):`
- `def create_resource_dirs(skill_dir, skill_name, skill_title, resources, include_examples):`
- `def init_skill(skill_name, path, resources, include_examples, interface_overrides):`
- `def main():`
- `if __name__ == "__main__":`

## Definitions (auto, per-file)
- `import` `codex-rs/core/src/skills/assets/samples/skill-creator/scripts/init_skill.py:16` `import argparse`
- `import` `codex-rs/core/src/skills/assets/samples/skill-creator/scripts/init_skill.py:17` `import re`
- `import` `codex-rs/core/src/skills/assets/samples/skill-creator/scripts/init_skill.py:18` `import sys`
- `import` `codex-rs/core/src/skills/assets/samples/skill-creator/scripts/init_skill.py:19` `from pathlib import Path`
- `import` `codex-rs/core/src/skills/assets/samples/skill-creator/scripts/init_skill.py:21` `from generate_openai_yaml import write_openai_yaml`
- `def` `codex-rs/core/src/skills/assets/samples/skill-creator/scripts/init_skill.py:125` `def main():`
- `main` `codex-rs/core/src/skills/assets/samples/skill-creator/scripts/init_skill.py:130` `if __name__ == "__main__":`
- `def` `codex-rs/core/src/skills/assets/samples/skill-creator/scripts/init_skill.py:197` `def normalize_skill_name(skill_name):`
- `def` `codex-rs/core/src/skills/assets/samples/skill-creator/scripts/init_skill.py:206` `def title_case_skill_name(skill_name):`
- `def` `codex-rs/core/src/skills/assets/samples/skill-creator/scripts/init_skill.py:211` `def parse_resources(raw_resources):`
- `def` `codex-rs/core/src/skills/assets/samples/skill-creator/scripts/init_skill.py:230` `def create_resource_dirs(skill_dir, skill_name, skill_title, resources, include_examples):`
- `def` `codex-rs/core/src/skills/assets/samples/skill-creator/scripts/init_skill.py:258` `def init_skill(skill_name, path, resources, include_examples, interface_overrides):`
- `def` `codex-rs/core/src/skills/assets/samples/skill-creator/scripts/init_skill.py:333` `def main():`
- `main` `codex-rs/core/src/skills/assets/samples/skill-creator/scripts/init_skill.py:396` `if __name__ == "__main__":`

## Dependencies (auto sample)
### Imports / Includes
- `import argparse`
- `import re`
- `import sys`
- `from pathlib import Path`
- `from generate_openai_yaml import write_openai_yaml`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- `workdocjcl/spec/00_Overview/ARCHITECTURE.md`
