#!/usr/bin/env python3
"""
Generate an accurate (best-effort) Tools schema reference from Rust sources.

Why:
- “params/required only” is insufficient for replication.
- Tools are a public interface between the model and runtime; a replica must match schema + semantics.

Outputs:
- workdocjcl/spec/05_Integrations/TOOLS_SCHEMA_REFERENCE.md (human summary)
- workdocjcl/spec/05_Integrations/TOOLS_SCHEMA_REFERENCE.json (machine-readable dump)
"""

from __future__ import annotations

import json
import re
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Optional


ROOT = Path(__file__).resolve().parents[3]
WORKDOC_ROOT = ROOT / "docs" / "workdocjcl"

SPEC_RS = ROOT / "codex-rs" / "core" / "src" / "tools" / "spec.rs"
PLAN_RS = ROOT / "codex-rs" / "core" / "src" / "tools" / "handlers" / "plan.rs"
APPLY_PATCH_RS = (
    ROOT / "codex-rs" / "core" / "src" / "tools" / "handlers" / "apply_patch.rs"
)
MODELS_RS = ROOT / "codex-rs" / "protocol" / "src" / "models.rs"

OUT_MD = WORKDOC_ROOT / "spec" / "05_Integrations" / "TOOLS_SCHEMA_REFERENCE.md"
OUT_JSON = WORKDOC_ROOT / "spec" / "05_Integrations" / "TOOLS_SCHEMA_REFERENCE.json"


def utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def load_text(path: Path) -> str:
    return path.read_text("utf-8", errors="replace")


def iter_lines_with_offsets(text: str) -> list[int]:
    # offsets[i] = byte offset at start of line i (0-indexed)
    offsets = [0]
    for m in re.finditer(r"\n", text):
        offsets.append(m.end())
    return offsets


def offset_to_line(offsets: list[int], pos: int) -> int:
    # 1-indexed line number
    lo, hi = 0, len(offsets) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if offsets[mid] <= pos:
            lo = mid + 1
        else:
            hi = mid - 1
    return hi + 1


def parse_const_str_map(models_rs_text: str) -> dict[str, str]:
    # e.g. pub const VIEW_IMAGE_TOOL_NAME: &str = "view_image";
    out: dict[str, str] = {}
    for m in re.finditer(
        r"pub\s+const\s+([A-Z0-9_]+)\s*:\s*&str\s*=\s*\"([^\"]+)\"\s*;",
        models_rs_text,
    ):
        out[m.group(1)] = m.group(2)
    return out


class RustScanner:
    def __init__(self, text: str) -> None:
        self.text = text
        self.n = len(text)

    def _skip_ws(self, i: int) -> int:
        while i < self.n and self.text[i].isspace():
            i += 1
        return i

    def _skip_line_comment(self, i: int) -> int:
        # assumes starts at "//"
        j = self.text.find("\n", i)
        return self.n if j == -1 else j + 1

    def _skip_block_comment(self, i: int) -> int:
        # assumes starts at "/*"
        j = self.text.find("*/", i + 2)
        return self.n if j == -1 else j + 2

    def _skip_string(self, i: int) -> int:
        # normal string starting at "
        i += 1
        while i < self.n:
            c = self.text[i]
            if c == "\\":
                i += 2
                continue
            if c == '"':
                return i + 1
            i += 1
        return self.n

    def _skip_char(self, i: int) -> int:
        # char literal starting at '
        i += 1
        while i < self.n:
            c = self.text[i]
            if c == "\\":
                i += 2
                continue
            if c == "'":
                return i + 1
            i += 1
        return self.n

    def _skip_raw_string(self, i: int) -> int:
        # raw string starting at r###"
        assert self.text[i] == "r"
        j = i + 1
        hashes = 0
        while j < self.n and self.text[j] == "#":
            hashes += 1
            j += 1
        if j >= self.n or self.text[j] != '"':
            return i + 1
        j += 1
        end_pat = '"' + ("#" * hashes)
        k = self.text.find(end_pat, j)
        return self.n if k == -1 else k + len(end_pat)

    def find_matching(self, start: int, open_ch: str, close_ch: str) -> int:
        # start points at open_ch
        assert self.text[start] == open_ch
        depth = 1
        i = start + 1
        while i < self.n:
            c = self.text[i]
            if c == "/" and i + 1 < self.n and self.text[i + 1] == "/":
                i = self._skip_line_comment(i)
                continue
            if c == "/" and i + 1 < self.n and self.text[i + 1] == "*":
                i = self._skip_block_comment(i)
                continue
            if c == "r" and i + 1 < self.n and self.text[i + 1] in ['"', "#"]:
                i = self._skip_raw_string(i)
                continue
            if c == '"':
                i = self._skip_string(i)
                continue
            if c == "'":
                i = self._skip_char(i)
                continue
            if c == open_ch:
                depth += 1
                i += 1
                continue
            if c == close_ch:
                depth -= 1
                i += 1
                if depth == 0:
                    return i - 1
                continue
            i += 1
        return -1

    def split_top_level(self, s: str, sep: str = ",") -> list[str]:
        # Splits s by sep, ignoring nested (), [], {} and strings/comments.
        out: list[str] = []
        buf: list[str] = []
        depth_paren = 0
        depth_brack = 0
        depth_brace = 0
        i = 0
        n = len(s)
        while i < n:
            c = s[i]
            if c == "/" and i + 1 < n and s[i + 1] == "/":
                # line comment
                j = s.find("\n", i)
                if j == -1:
                    break
                buf.append(s[i:j])
                i = j
                continue
            if c == "/" and i + 1 < n and s[i + 1] == "*":
                j = s.find("*/", i + 2)
                if j == -1:
                    buf.append(s[i:])
                    break
                buf.append(s[i : j + 2])
                i = j + 2
                continue
            if c == "r" and i + 1 < n and s[i + 1] in ['"', "#"]:
                # raw string
                j = i + 1
                hashes = 0
                while j < n and s[j] == "#":
                    hashes += 1
                    j += 1
                if j < n and s[j] == '"':
                    j += 1
                    end_pat = '"' + ("#" * hashes)
                    k = s.find(end_pat, j)
                    k = n if k == -1 else k + len(end_pat)
                    buf.append(s[i:k])
                    i = k
                    continue
            if c == '"':
                # normal string
                j = i + 1
                while j < n:
                    if s[j] == "\\":
                        j += 2
                        continue
                    if s[j] == '"':
                        j += 1
                        break
                    j += 1
                buf.append(s[i:j])
                i = j
                continue
            if c == "'":
                j = i + 1
                while j < n:
                    if s[j] == "\\":
                        j += 2
                        continue
                    if s[j] == "'":
                        j += 1
                        break
                    j += 1
                buf.append(s[i:j])
                i = j
                continue
            if c == "(":
                depth_paren += 1
            elif c == ")":
                depth_paren = max(0, depth_paren - 1)
            elif c == "[":
                depth_brack += 1
            elif c == "]":
                depth_brack = max(0, depth_brack - 1)
            elif c == "{":
                depth_brace += 1
            elif c == "}":
                depth_brace = max(0, depth_brace - 1)

            if (
                c == sep
                and depth_paren == 0
                and depth_brack == 0
                and depth_brace == 0
            ):
                out.append("".join(buf).strip())
                buf = []
                i += 1
                continue
            buf.append(c)
            i += 1
        tail = "".join(buf).strip()
        if tail:
            out.append(tail)
        return [p for p in out if p]

    def split_statements(self, block: str) -> list[tuple[int, str]]:
        # Split by top-level ';' and keep each statement's start offset within block.
        out: list[tuple[int, str]] = []
        buf: list[str] = []
        stmt_start = 0
        depth_paren = 0
        depth_brack = 0
        depth_brace = 0
        i = 0
        n = len(block)
        while i < n:
            c = block[i]
            # reuse same logic as split_top_level for strings/comments
            if c == "/" and i + 1 < n and block[i + 1] == "/":
                j = block.find("\n", i)
                j = n if j == -1 else j
                buf.append(block[i:j])
                i = j
                continue
            if c == "/" and i + 1 < n and block[i + 1] == "*":
                j = block.find("*/", i + 2)
                j = n if j == -1 else j + 2
                buf.append(block[i:j])
                i = j
                continue
            if c == "r" and i + 1 < n and block[i + 1] in ['"', "#"]:
                j = i + 1
                hashes = 0
                while j < n and block[j] == "#":
                    hashes += 1
                    j += 1
                if j < n and block[j] == '"':
                    j += 1
                    end_pat = '"' + ("#" * hashes)
                    k = block.find(end_pat, j)
                    k = n if k == -1 else k + len(end_pat)
                    buf.append(block[i:k])
                    i = k
                    continue
            if c == '"':
                j = i + 1
                while j < n:
                    if block[j] == "\\":
                        j += 2
                        continue
                    if block[j] == '"':
                        j += 1
                        break
                    j += 1
                buf.append(block[i:j])
                i = j
                continue
            if c == "'":
                j = i + 1
                while j < n:
                    if block[j] == "\\":
                        j += 2
                        continue
                    if block[j] == "'":
                        j += 1
                        break
                    j += 1
                buf.append(block[i:j])
                i = j
                continue

            if c == "(":
                depth_paren += 1
            elif c == ")":
                depth_paren = max(0, depth_paren - 1)
            elif c == "[":
                depth_brack += 1
            elif c == "]":
                depth_brack = max(0, depth_brack - 1)
            elif c == "{":
                depth_brace += 1
            elif c == "}":
                depth_brace = max(0, depth_brace - 1)

            if (
                c == ";"
                and depth_paren == 0
                and depth_brack == 0
                and depth_brace == 0
            ):
                stmt = "".join(buf).strip()
                if stmt:
                    out.append((stmt_start, stmt))
                buf = []
                stmt_start = i + 1
                i += 1
                continue
            buf.append(c)
            i += 1
        tail = "".join(buf).strip()
        if tail:
            out.append((stmt_start, tail))
        return out


def normalize_string_expr(expr: str, const_map: dict[str, str]) -> dict[str, Any]:
    # Returns a structured representation so we don't lie about evaluation.
    e = expr.strip()
    e = re.sub(r"\.to_string\(\)\s*$", "", e)
    if m := re.fullmatch(r"\"([^\"]*)\"", e, flags=re.S):
        return {"kind": "literal", "value": m.group(1)}
    if m := re.fullmatch(r'r#+"(.*)"#+', e, flags=re.S):
        # rough; content capture is greedy but ok for docs
        raw = m.group(0)
        # strip r###" and "###
        prefix = raw.split('"', 1)[0]
        hashes = prefix.count("#")
        inner = raw[len("r" + "#" * hashes + '"') : -len('"' + "#" * hashes)]
        return {"kind": "raw_literal", "value": inner}
    if m := re.fullmatch(r"([A-Z0-9_]+)", e):
        name = m.group(1)
        if name in const_map:
            return {"kind": "const", "name": name, "value": const_map[name]}
        return {"kind": "const", "name": name}
    if e.startswith("format!("):
        return {"kind": "format", "expr": e}
    if e.startswith("if cfg!(windows)"):
        return {"kind": "conditional", "expr": e}
    return {"kind": "expr", "expr": e}


def extract_required_list(expr: str) -> list[str]:
    # required: Some(vec!["a".to_string(), "b".to_string()])
    out: list[str] = []
    for m in re.finditer(r"\"([A-Za-z0-9_]+)\"\.to_string\(\)", expr):
        out.append(m.group(1))
    # sometimes vec![ "x".to_string() ] without quotes? not observed
    return out


def parse_additional_properties(expr: str) -> Any:
    e = expr.strip()
    if e.startswith("Some(") and e.endswith(")"):
        inner = e[len("Some(") : -1].strip()
        if inner == "false.into()":
            return False
        if inner == "true.into()":
            return True
        if inner.endswith(".into()"):
            return {"kind": "into_expr", "expr": inner}
        return {"kind": "expr", "expr": inner}
    if e == "None":
        return None
    return {"kind": "expr", "expr": e}


def _desc_field_to_value(expr: str, const_map: dict[str, str]) -> dict[str, Any]:
    # expr is Option<String> value like Some("...".to_string()) or Some(format!(...))
    e = expr.strip()
    if e == "None":
        return {"kind": "none"}
    m = re.match(r"Some\((.+)\)\s*$", e, flags=re.S)
    if not m:
        return {"kind": "expr", "expr": e}
    inner_expr = m.group(1).strip()
    # Common pattern: Some("...".to_string(),)
    if inner_expr.endswith(","):
        inner_expr = inner_expr[:-1].rstrip()
    inner = normalize_string_expr(inner_expr, const_map)
    if inner.get("kind") in ("literal", "raw_literal") and "value" in inner:
        return {"kind": "string", "value": inner["value"]}
    if inner.get("kind") == "const" and "value" in inner:
        return {"kind": "string", "value": inner["value"], "source": inner}
    return {"kind": "expr", "expr": inner_expr}


def parse_jsonschema(expr: str, env: dict[str, Any], const_map: dict[str, str]) -> Any:
    e = expr.strip()
    # variable reference
    if re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*", e) and e in env:
        return env[e]

    # JsonSchema::<Type> { ... }
    m = re.match(r"JsonSchema::([A-Za-z_][A-Za-z0-9_]*)\s*\{", e)
    if not m:
        return {"kind": "unparsed", "expr": e}
    ty = m.group(1)
    # find body braces (string-aware, on this small expr)
    scanner = RustScanner(e)
    body_start = e.find("{", m.end() - 1)
    body_end = scanner.find_matching(body_start, "{", "}")
    if body_end == -1:
        return {"kind": "unparsed", "expr": e}
    body = e[body_start + 1 : body_end].strip()
    fields = {}
    for part in scanner.split_top_level(body, sep=","):
        if not part:
            continue
        if ":" in part:
            k, v = part.split(":", 1)
            fields[k.strip()] = v.strip()
            continue
        # Rust struct shorthand field (e.g., `properties,` or `description,`)
        sm = re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*", part.strip())
        if sm:
            fields[sm.group(0)] = sm.group(0)

    if ty.lower() in ("string", "boolean", "number"):
        desc = fields.get("description")
        out: dict[str, Any] = {"type": ty.lower() if ty.lower() != "number" else "number"}
        if desc:
            d = _desc_field_to_value(desc, const_map)
            if d.get("kind") == "string":
                out["description"] = d["value"]
            elif d.get("kind") != "none":
                out["description_expr"] = d
        return out

    if ty == "Array":
        items_expr = fields.get("items", "")
        items_expr = re.sub(r"^Box::new\((.*)\)\s*$", r"\1", items_expr, flags=re.S)
        out = {"type": "array", "items": parse_jsonschema(items_expr, env, const_map)}
        desc = fields.get("description")
        if desc:
            d = _desc_field_to_value(desc, const_map)
            if d.get("kind") == "string":
                out["description"] = d["value"]
            elif d.get("kind") != "none":
                out["description_expr"] = d
        return out

    if ty == "Object":
        props_expr = fields.get("properties", "")
        props = None
        if re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*", props_expr) and props_expr in env:
            props = env[props_expr]
        else:
            props = {"kind": "unresolved_properties", "expr": props_expr}
        required = fields.get("required")
        req_list: Optional[list[str]] = None
        if required and required != "None":
            # Some(vec![...])
            rm = re.match(r"Some\((.+)\)", required, flags=re.S)
            if rm:
                req_list = extract_required_list(rm.group(1))
        ap = parse_additional_properties(fields.get("additional_properties", "None"))
        out = {
            "type": "object",
            "properties": props,
            "additionalProperties": ap if ap is not None else None,
        }
        if req_list is not None:
            out["required"] = req_list
        return out

    return {"kind": "unhandled_jsonschema_type", "type": ty, "expr": e}


def parse_btreemap_from(expr: str, env: dict[str, Any], const_map: dict[str, str]) -> dict[str, Any]:
    # BTreeMap::from([ ( "k".to_string(), JsonSchema::... ), ... ])
    e = expr.strip()
    m = re.match(r"BTreeMap::from\s*\(\s*\[", e)
    if not m:
        return {}
    # find closing '])'
    idx = e.find("[", m.end() - 1)
    scanner = RustScanner(e)
    end = scanner.find_matching(idx, "[", "]")
    if end == -1:
        return {}
    inner = e[idx + 1 : end].strip()
    out: dict[str, Any] = {}
    for item in scanner.split_top_level(inner, sep=","):
        it = item.strip()
        if not it:
            continue
        if it.startswith("(") and it.endswith(")"):
            it_inner = it[1:-1].strip()
        else:
            it_inner = it
        parts = scanner.split_top_level(it_inner, sep=",")
        if len(parts) < 2:
            continue
        key_expr = parts[0].strip()
        val_expr = ",".join(parts[1:]).strip()
        km = re.match(r"\"([^\"]+)\"\.to_string\(\)", key_expr)
        if not km:
            continue
        key = km.group(1)
        out[key] = parse_jsonschema(val_expr, env, const_map)
    return out


@dataclass
class ToolDef:
    name: str
    kind: str  # function|freeform|local_shell|web_search
    source_file: str
    source_line: int
    description: Any
    strict: Optional[bool] = None
    parameters: Any = None


def extract_tool_defs_from_block(
    block: str,
    *,
    file_rel: str,
    block_start_line: int,
    const_map: dict[str, str],
    approval_params_no_prefix: dict[str, Any],
    approval_params_with_prefix: dict[str, Any],
) -> list[ToolDef]:
    env: dict[str, Any] = {}
    scanner = RustScanner(block)

    tools: list[ToolDef] = []

    def strip_leading_comments(stmt: str) -> str:
        s = stmt
        while True:
            s2 = s.lstrip()
            if s2.startswith("//"):
                nl = s2.find("\n")
                s = "" if nl == -1 else s2[nl + 1 :]
                continue
            if s2.startswith("/*"):
                end = s2.find("*/")
                s = "" if end == -1 else s2[end + 2 :]
                continue
            return s2

    for stmt_offset, stmt in scanner.split_statements(block):
        s = stmt.strip()
        if not s:
            continue
        s2 = strip_leading_comments(s)
        if not s2:
            continue
        stmt_line_delta = block[: max(0, stmt_offset)].count("\n")
        stmt_line = block_start_line + stmt_line_delta

        # let mut x = BTreeMap::new()
        m = re.match(
            r"let\s+(?:mut\s+)?([A-Za-z_][A-Za-z0-9_]*)\s*=\s*BTreeMap::new\(\)\s*$",
            s2,
        )
        if m:
            env[m.group(1)] = {}
            continue

        # let x = BTreeMap::from([...])
        m = re.match(
            r"let\s+(?:mut\s+)?([A-Za-z_][A-Za-z0-9_]*)\s*=\s*(BTreeMap::from\s*\(.+)\)\s*$",
            s2,
            flags=re.S,
        )
        if m:
            env[m.group(1)] = parse_btreemap_from(m.group(2), env, const_map)
            continue

        # x.insert(...)
        m = re.match(r"([A-Za-z_][A-Za-z0-9_]*)\.insert\s*\(", s2)
        if m:
            var = m.group(1)
            start = s2.find("(")
            end = RustScanner(s2).find_matching(start, "(", ")")
            if end != -1:
                args = s2[start + 1 : end]
                parts = RustScanner(args).split_top_level(args, sep=",")
                if len(parts) >= 2 and var in env and isinstance(env[var], dict):
                    key_expr = parts[0].strip()
                    val_expr = ",".join(parts[1:]).strip()
                    km = re.match(r"\"([^\"]+)\"\.to_string\(\)", key_expr)
                    if km:
                        env[var][km.group(1)] = parse_jsonschema(val_expr, env, const_map)
            continue

        # x.extend(create_approval_parameters(...))
        m = re.match(
            r"([A-Za-z_][A-Za-z0-9_]*)\.extend\s*\(\s*create_approval_parameters\((.+)\)\s*\)\s*$",
            s2,
        )
        if m:
            var = m.group(1)
            arg = m.group(2).strip()
            if var in env and isinstance(env[var], dict):
                if arg == "false":
                    env[var].update(approval_params_no_prefix)
                elif arg == "true":
                    env[var].update(approval_params_with_prefix)
                else:
                    # Unknown/variable: include required base fields + mark prefix_rule conditional.
                    env[var].update(approval_params_no_prefix)
                    # annotate conditional presence for replication
                    prefix_schema = dict(approval_params_with_prefix.get("prefix_rule", {}))
                    if prefix_schema:
                        prefix_schema["x_present_if"] = arg
                        env[var]["prefix_rule"] = prefix_schema
            continue

        # let x = JsonSchema::Array/Object/etc...
        m = re.match(
            r"let\s+(?:mut\s+)?([A-Za-z_][A-Za-z0-9_]*)\s*=\s*(JsonSchema::.+)\s*$",
            s2,
            flags=re.S,
        )
        if m:
            env[m.group(1)] = parse_jsonschema(m.group(2), env, const_map)
            continue

        # ToolSpec::Function(ResponsesApiTool { ... })
        idx = s.find("ToolSpec::Function")
        if idx != -1 and "ResponsesApiTool" in s:
            # Parse struct literal
            start = s.find("ResponsesApiTool", idx)
            brace = s.find("{", start)
            if brace == -1:
                continue
            end = RustScanner(s).find_matching(brace, "{", "}")
            if end == -1:
                continue
            body = s[brace + 1 : end].strip()
            fields: dict[str, str] = {}
            for part in RustScanner(body).split_top_level(body, sep=","):
                if not part:
                    continue
                if ":" in part:
                    k, v = part.split(":", 1)
                    fields[k.strip()] = v.strip()
                    continue
                sm = re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*", part.strip())
                if sm:
                    fields[sm.group(0)] = sm.group(0)

            name_expr = fields.get("name")
            if not name_expr:
                continue
            name_norm = normalize_string_expr(name_expr, const_map)
            tool_name = name_norm.get("value") if name_norm.get("kind") in ("literal", "raw_literal", "const") and "value" in name_norm else None
            tool_name = tool_name or name_norm.get("name") or name_expr.strip()

            desc_expr = fields.get("description", "")
            desc_norm = normalize_string_expr(desc_expr, const_map)

            strict_val = None
            if "strict" in fields:
                if fields["strict"].strip() in ("true", "false"):
                    strict_val = fields["strict"].strip() == "true"

            params_expr = fields.get("parameters")
            params_schema = None
            if params_expr:
                params_schema = parse_jsonschema(params_expr, env, const_map)

            tools.append(
                ToolDef(
                    name=tool_name,
                    kind="function",
                    source_file=file_rel,
                    source_line=stmt_line,
                    description=desc_norm,
                    strict=strict_val,
                    parameters=params_schema,
                )
            )
            continue

        # ToolSpec::Freeform(FreeformTool { ... })
        idx = s.find("ToolSpec::Freeform")
        if idx != -1 and "FreeformTool" in s:
            start = s.find("FreeformTool", idx)
            brace = s.find("{", start)
            if brace == -1:
                continue
            end = RustScanner(s).find_matching(brace, "{", "}")
            if end == -1:
                continue
            body = s[brace + 1 : end].strip()
            fields: dict[str, str] = {}
            for part in RustScanner(body).split_top_level(body, sep=","):
                if not part:
                    continue
                if ":" in part:
                    k, v = part.split(":", 1)
                    fields[k.strip()] = v.strip()
                    continue
                sm = re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*", part.strip())
                if sm:
                    fields[sm.group(0)] = sm.group(0)

            name_expr = fields.get("name")
            if not name_expr:
                continue
            name_norm = normalize_string_expr(name_expr, const_map)
            tool_name = name_norm.get("value") if name_norm.get("kind") in ("literal", "raw_literal", "const") and "value" in name_norm else None
            tool_name = tool_name or name_norm.get("name") or name_expr.strip()

            desc_expr = fields.get("description", "")
            desc_norm = normalize_string_expr(desc_expr, const_map)

            tools.append(
                ToolDef(
                    name=tool_name,
                    kind="freeform",
                    source_file=file_rel,
                    source_line=stmt_line,
                    description=desc_norm,
                    strict=None,
                    parameters=None,
                )
            )
            continue

    return tools


def extract_blocks(text: str, *, file_rel: str) -> list[tuple[int, str]]:
    # returns (start_pos, block_text) for create_* and certain LazyLock blocks
    blocks: list[tuple[int, str]] = []
    scanner = RustScanner(text)

    for m in re.finditer(
        r"\n(?:pub\(crate\)\s+)?fn\s+[A-Za-z0-9_]+\s*\([^)]*\)\s*->\s*ToolSpec\s*\{",
        text,
    ):
        brace = text.find("{", m.end() - 1)
        if brace == -1:
            continue
        end = scanner.find_matching(brace, "{", "}")
        if end == -1:
            continue
        blocks.append((m.start() + 1, text[brace + 1 : end]))

    # LazyLock::new(|| { ... ToolSpec::Function ... })
    for m in re.finditer(r"LazyLock::new\(\|\|\s*\{", text):
        brace = text.find("{", m.end() - 1)
        if brace == -1:
            continue
        end = scanner.find_matching(brace, "{", "}")
        if end == -1:
            continue
        blocks.append((m.start(), text[brace + 1 : end]))

    return blocks


def summarize_schema(schema: Any) -> dict[str, str]:
    if not isinstance(schema, dict):
        return {}
    props = schema.get("properties")
    if not isinstance(props, dict):
        return {}
    out: dict[str, str] = {}
    for k, v in props.items():
        if isinstance(v, dict) and "type" in v:
            out[k] = v["type"]
        else:
            out[k] = "?"
    return out


def main() -> int:
    spec_text = load_text(SPEC_RS)
    plan_text = load_text(PLAN_RS)
    apply_patch_text = load_text(APPLY_PATCH_RS)
    models_text = load_text(MODELS_RS)

    const_map = parse_const_str_map(models_text)

    # approval parameters are defined in spec.rs; compute both variants from the function body.
    # If parsing fails, fall back to a minimal schema.
    approval_no_prefix: dict[str, Any] = {}
    approval_with_prefix: dict[str, Any] = {}
    m = re.search(
        r"\nfn\s+create_approval_parameters\s*\(\s*include_prefix_rule\s*:\s*bool\s*\)\s*->\s*BTreeMap<[^>]+>\s*\{",
        spec_text,
    )
    if m:
        brace = spec_text.find("{", m.end() - 1)
        end = RustScanner(spec_text).find_matching(brace, "{", "}")
        if end != -1:
            body = spec_text[brace + 1 : end]
            # interpret twice by injecting include_prefix_rule value; we handle the
            # conditional insert with a simple scan.
            # Start with the initial properties BTreeMap::from([...]).
            init_m = re.search(r"let\s+mut\s+properties\s*=\s*(BTreeMap::from\s*\(.+\)\s*);", body, flags=re.S)
            if init_m:
                base_env: dict[str, Any] = {}
                base_props = parse_btreemap_from(init_m.group(1), base_env, const_map)
                approval_no_prefix = dict(base_props)
                approval_with_prefix = dict(base_props)
                # detect prefix_rule insert block
                if "properties.insert" in body and "prefix_rule" in body:
                    # Extract the JsonSchema::Array {...} expression via brace matching
                    pr_pos = body.find('"prefix_rule".to_string()')
                    if pr_pos != -1:
                        arr_pos = body.find("JsonSchema::Array", pr_pos)
                        if arr_pos != -1:
                            arr_brace = body.find("{", arr_pos)
                            if arr_brace != -1:
                                arr_end = RustScanner(body).find_matching(
                                    arr_brace, "{", "}"
                                )
                                if arr_end != -1:
                                    arr_expr = body[arr_pos : arr_end + 1]
                                    approval_with_prefix["prefix_rule"] = parse_jsonschema(
                                        arr_expr, {}, const_map
                                    )
    if not approval_no_prefix:
        approval_no_prefix = {
            "sandbox_permissions": {"type": "string"},
            "justification": {"type": "string"},
        }
    if not approval_with_prefix:
        approval_with_prefix = dict(approval_no_prefix)
        approval_with_prefix["prefix_rule"] = {"type": "array", "items": {"type": "string"}}

    all_tools: list[ToolDef] = []
    sources = [
        (SPEC_RS, spec_text),
        (PLAN_RS, plan_text),
        (APPLY_PATCH_RS, apply_patch_text),
    ]

    for path, text in sources:
        rel = str(path.relative_to(ROOT))
        offsets = iter_lines_with_offsets(text)
        for start_pos, block in extract_blocks(text, file_rel=rel):
            start_line = offset_to_line(offsets, start_pos)
            all_tools.extend(
                extract_tool_defs_from_block(
                    block,
                    file_rel=rel,
                    block_start_line=start_line,
                    const_map=const_map,
                    approval_params_no_prefix=approval_no_prefix,
                    approval_params_with_prefix=approval_with_prefix,
                )
            )

    # Add implicit ToolSpec variants referenced by build_specs (non-function tool types).
    spec_offsets = iter_lines_with_offsets(spec_text)
    local_shell_line = 1
    if m := re.search(r"push_spec\s*\(\s*ToolSpec::LocalShell\s*\{\s*\}\s*\)", spec_text):
        local_shell_line = offset_to_line(spec_offsets, m.start())
    web_search_line = 1
    if m := re.search(r"ToolSpec::WebSearch\s*\{", spec_text):
        web_search_line = offset_to_line(spec_offsets, m.start())

    all_tools.append(
        ToolDef(
            name="local_shell",
            kind="local_shell",
            source_file=str(SPEC_RS.relative_to(ROOT)),
            source_line=local_shell_line,
            description={
                "kind": "note",
                "value": "ToolSpec::LocalShell {} (no JSON schema; uses protocol LocalShellCall params).",
            },
        )
    )
    all_tools.append(
        ToolDef(
            name="web_search",
            kind="web_search",
            source_file=str(SPEC_RS.relative_to(ROOT)),
            source_line=web_search_line,
            description={
                "kind": "note",
                "value": "ToolSpec::WebSearch { external_web_access: Option<bool> } (no JSON schema).",
            },
        )
    )

    # Deduplicate by (name, kind) keeping first, but keep duplicates list in warnings.
    seen: set[tuple[str, str]] = set()
    uniq: list[ToolDef] = []
    dupes: list[ToolDef] = []
    for t in all_tools:
        key = (t.name, t.kind)
        if key in seen:
            dupes.append(t)
            continue
        seen.add(key)
        uniq.append(t)

    # Write JSON dump
    dump = {
        "generated_utc": utc_now(),
        "sources": [str(p.relative_to(ROOT)) for p, _ in sources] + [str(MODELS_RS.relative_to(ROOT))],
        "tool_count": len(uniq),
        "tools": [
            {
                "name": t.name,
                "kind": t.kind,
                "source": {"file": t.source_file, "line": t.source_line},
                "description": t.description,
                "strict": t.strict,
                "parameters": t.parameters,
            }
            for t in sorted(uniq, key=lambda x: (x.name, x.kind))
        ],
        "duplicates": [
            {"name": t.name, "kind": t.kind, "source": {"file": t.source_file, "line": t.source_line}}
            for t in dupes
        ],
    }
    OUT_JSON.write_text(json.dumps(dump, ensure_ascii=False, indent=2) + "\n", "utf-8")

    # Write Markdown summary
    md: list[str] = []
    md.append("# Tools Schema Reference (Best-effort)")
    md.append("")
    md.append(f"- generated_utc: `{dump['generated_utc']}`")
    md.append("- sources:")
    for s in dump["sources"]:
        md.append(f"  - `{s}`")
    md.append("")
    md.append("说明：本文件尝试从 Rust 源码中提取 tool schema（JSON Schema 子集）。")
    md.append("若某字段为 `kind=expr` 或 `kind=unparsed`，表示这是源码表达式，未做求值。")
    md.append("")
    md.append("- 逐工具语义规格：`workdocjcl/spec/05_Integrations/TOOLS_DETAILED/INDEX.md`")
    md.append(f"- tool_count: `{dump['tool_count']}`")
    md.append(f"- duplicates_detected: `{len(dupes)}`")
    md.append("")

    md.append("| Tool | Kind | Required | Params (name:type) | Source |")
    md.append("|---|---|---|---|---|")
    for t in sorted(uniq, key=lambda x: (x.name, x.kind)):
        required = ""
        params_sig = ""
        if isinstance(t.parameters, dict) and t.parameters.get("type") == "object":
            req = t.parameters.get("required", [])
            required = ", ".join(f"`{x}`" for x in req) if req else "(none)"
            sig = summarize_schema(t.parameters)
            params_sig = ", ".join(f"`{k}:{v}`" for k, v in sorted(sig.items())) if sig else "(none)"
        else:
            required = "(n/a)"
            params_sig = "(n/a)"
        md.append(
            f"| `{t.name}` | `{t.kind}` | {required} | {params_sig} | `{t.source_file}:{t.source_line}` |"
        )

    md.append("")
    md.append("机器可读版本：`workdocjcl/spec/05_Integrations/TOOLS_SCHEMA_REFERENCE.json`")
    OUT_MD.write_text("\n".join(md) + "\n", "utf-8")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
