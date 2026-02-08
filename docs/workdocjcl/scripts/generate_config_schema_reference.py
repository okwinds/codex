#!/usr/bin/env python3
# Flatten codex-rs/core/config.schema.json into a markdown reference table.

import json
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
WORKDOC_ROOT = ROOT / "docs" / "workdocjcl"
SCHEMA = ROOT / "codex-rs" / "core" / "config.schema.json"
OUT = WORKDOC_ROOT / "spec" / "01_Configuration" / "CONFIG_SCHEMA_REFERENCE.md"


def utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def load_schema() -> dict:
    return json.loads(SCHEMA.read_text("utf-8"))


def type_repr(s: dict) -> str:
    t = s.get("type")
    if isinstance(t, list):
        return "|".join(t)
    if isinstance(t, str):
        return t
    if "$ref" in s:
        return s["$ref"]
    if "oneOf" in s:
        return "oneOf"
    if "anyOf" in s:
        return "anyOf"
    if "allOf" in s:
        return "allOf"
    return "unknown"

def walk(path: str, schema: dict, defs: dict, rows_by_key: dict, seen_refs: set) -> None:
    if "$ref" in schema:
        ref = schema["$ref"]
        if ref in seen_refs:
            rows_by_key.setdefault(path, (ref, "(ref cycle/seen)"))
            return
        seen_refs.add(ref)
        if ref.startswith("#/definitions/"):
            key = ref.split("/", 2)[-1]
            target = defs.get(key, {})
            walk(path, target, defs, rows_by_key, seen_refs)
        else:
            rows_by_key.setdefault(path, (ref, "(unresolved ref)"))
        return

    desc = schema.get("description", "")
    # Record this node once.
    if path:
        # Prefer keeping the first-seen description if later variants repeat.
        rows_by_key.setdefault(path, (type_repr(schema), desc))

    # Traverse union/merge schemas.
    for key in ("oneOf", "anyOf", "allOf"):
        if key in schema and isinstance(schema[key], list):
            for variant in schema[key]:
                if isinstance(variant, dict):
                    walk(path, variant, defs, rows_by_key, set(seen_refs))

    # Treat as object if it has properties, even if type is omitted or unioned.
    props = schema.get("properties")
    if isinstance(props, dict):
        for k, v in props.items():
            if not isinstance(v, dict):
                continue
            child_path = f"{path}.{k}" if path else k
            walk(child_path, v, defs, rows_by_key, set(seen_refs))

    # Map/dict shape: additionalProperties can be a schema.
    ap = schema.get("additionalProperties")
    if isinstance(ap, dict):
        map_path = f"{path}.<key>" if path else "<key>"
        walk(map_path, ap, defs, rows_by_key, set(seen_refs))

    # Array shape: items can be a schema.
    items = schema.get("items")
    if isinstance(items, dict):
        arr_path = f"{path}[]" if path else "[]"
        walk(arr_path, items, defs, rows_by_key, set(seen_refs))

    # patternProperties: treat as <pattern:...>
    pp = schema.get("patternProperties")
    if isinstance(pp, dict):
        for pat, sub in pp.items():
            if not isinstance(sub, dict):
                continue
            pat_path = f"{path}.<pattern:{pat}>" if path else f"<pattern:{pat}>"
            walk(pat_path, sub, defs, rows_by_key, set(seen_refs))


def main() -> int:
    doc = load_schema()
    defs = doc.get("definitions") or {}
    rows_by_key = {}
    # Root: traverse its properties but don't record empty path.
    walk("", doc, defs, rows_by_key, set())

    md = []
    md.append("# config.toml JSON Schema Reference (Flattened)")
    md.append("")
    md.append(f"- generated_utc: `{utc_now()}`")
    md.append(f"- schema_source: `{SCHEMA.relative_to(ROOT)}`")
    md.append("")
    md.append("本文件把 `config.schema.json` 展平为 `dot.path` 形式，作为“无遗漏”配置键参考。")
    md.append("")
    md.append("| Key path | Type | Description |")
    md.append("|---|---|---|")
    for key in sorted(rows_by_key.keys()):
        t, d = rows_by_key[key]
        d = (d or "").replace("\n", " ").strip()
        md.append(f"| `{key}` | `{t}` | {d} |")

    OUT.write_text("\n".join(md) + "\n", "utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
