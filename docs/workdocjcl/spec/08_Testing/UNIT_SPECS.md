# 单元测试规格（Unit Specs）

本仓库（尤其 `codex-rs/`）包含大量单元测试与模块内测试。由于覆盖面广，本章给出“必须等价的关键规格”与测试组织方式，并提供清单文件用于防遗漏。

## 1. 必须等价的关键单元规格（选摘）

### 1.1 模块：CLI config overrides（`-c key=value`）
实现应满足以下用例（参见 `codex-rs/common/src/config_override.rs` 的测试）：

| ID | 场景 | 输入 | 预期 | Notes |
|---|---|---|---|---|
| U001 | 标量解析 | `42` | TOML integer | |
| U002 | bool 解析 | `true`/`false` | TOML bool | |
| U003 | 数组解析 | `[1, 2, 3]` | TOML array(len=3) | |
| U004 | inline table | `{a = 1, b = 2}` | TOML table | |
| U005 | 失败回退 | `hello` | 解析失败 | 作为字符串回退发生在上层（parse_overrides） |

### 1.2 模块：CODEX_HOME 解析
实现应满足以下用例（参见 `codex-rs/utils/home-dir/src/lib.rs` 的测试）：

| ID | 场景 | 输入 | 预期 | Notes |
|---|---|---|---|---|
| U101 | env 缺失 | unset | `~/.codex` | |
| U102 | env 指向不存在 | missing path | Err(NotFound) | |
| U103 | env 指向文件 | file path | Err(InvalidInput) | |
| U104 | env 指向目录 | valid dir | canonicalize 后返回 | |

### 1.3 模块：state.sqlite（基础读写）
建议复刻时增加等价测试覆盖：
- init 会创建 DB 并应用 migrations
- `insert_logs`/`query_logs`：排序与过滤一致
- `get_dynamic_tools`：空返回 None；非空按 position ASC

## 2. 测试组织方式（代码结构）
- Rust：
  - crate 内 `#[cfg(test)] mod tests`：单元级
  - `cratename/tests/*`：集成测试（cargo test 会运行）
  - `codex-rs/tui`：大量 snapshot tests（insta）
- Node/TS：
  - `sdk/typescript/tests/*`：jest
  - `shell-tool-mcp/tests/*`：jest

## 3. 防遗漏清单（自动生成）
- Rust 测试文件清单：`docs/workdocjcl/inventory/rust_test_manifest.txt`

## 4. 来源（Source）
- config override：`codex-rs/common/src/config_override.rs`
- CODEX_HOME：`codex-rs/utils/home-dir/src/lib.rs`
- state runtime：`codex-rs/state/src/runtime.rs`
