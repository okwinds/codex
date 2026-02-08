# `codex-rs/core/src/skills/assets/samples/skill-creator/scripts/generate_openai_yaml.py`

## Identity
- kind: `source`
- ext: `.py`
- size_bytes: `6614`
- sha256: `b8f6be33a9d72dd7a8da02e7a9fffea23dc79e94862e6dd6358b57a8899d8f73`
- generated_utc: `2026-02-08T10:45:33Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/skills/assets/samples/skill-creator/scripts/generate_openai_yaml.py` (read)

### Outputs / Side Effects
- writes to stdout/stderr

## Public Surface (auto)
- `def yaml_quote(value):`
- `def format_display_name(skill_name):`
- `def generate_short_description(display_name):`
- `def read_frontmatter_name(skill_dir):`
- `def parse_interface_overrides(raw_overrides):`
- `def write_openai_yaml(skill_dir, skill_name, raw_overrides):`
- `def main():`
- `if __name__ == "__main__":`

## Definitions (auto, per-file)
- `import` `codex-rs/core/src/skills/assets/samples/skill-creator/scripts/generate_openai_yaml.py:9` `import argparse`
- `import` `codex-rs/core/src/skills/assets/samples/skill-creator/scripts/generate_openai_yaml.py:10` `import re`
- `import` `codex-rs/core/src/skills/assets/samples/skill-creator/scripts/generate_openai_yaml.py:11` `import sys`
- `import` `codex-rs/core/src/skills/assets/samples/skill-creator/scripts/generate_openai_yaml.py:12` `from pathlib import Path`
- `import` `codex-rs/core/src/skills/assets/samples/skill-creator/scripts/generate_openai_yaml.py:14` `import yaml`
- `def` `codex-rs/core/src/skills/assets/samples/skill-creator/scripts/generate_openai_yaml.py:52` `def yaml_quote(value):`
- `def` `codex-rs/core/src/skills/assets/samples/skill-creator/scripts/generate_openai_yaml.py:57` `def format_display_name(skill_name):`
- `def` `codex-rs/core/src/skills/assets/samples/skill-creator/scripts/generate_openai_yaml.py:76` `def generate_short_description(display_name):`
- `def` `codex-rs/core/src/skills/assets/samples/skill-creator/scripts/generate_openai_yaml.py:106` `def read_frontmatter_name(skill_dir):`
- `def` `codex-rs/core/src/skills/assets/samples/skill-creator/scripts/generate_openai_yaml.py:132` `def parse_interface_overrides(raw_overrides):`
- `def` `codex-rs/core/src/skills/assets/samples/skill-creator/scripts/generate_openai_yaml.py:155` `def write_openai_yaml(skill_dir, skill_name, raw_overrides):`
- `def` `codex-rs/core/src/skills/assets/samples/skill-creator/scripts/generate_openai_yaml.py:189` `def main():`
- `main` `codex-rs/core/src/skills/assets/samples/skill-creator/scripts/generate_openai_yaml.py:224` `if __name__ == "__main__":`

## Dependencies (auto sample)
### Imports / Includes
- `import argparse`
- `import re`
- `import sys`
- `from pathlib import Path`
- `import yaml`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- `docs/workdocjcl/spec/00_Overview/ARCHITECTURE.md`
