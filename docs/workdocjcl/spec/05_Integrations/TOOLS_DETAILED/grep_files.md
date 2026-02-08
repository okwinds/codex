# Tool: `grep_files` (function)

## 0. 目的（Purpose）
在指定路径下使用 `rg`（ripgrep）搜索匹配的文件路径（返回“包含匹配的文件列表”，不是逐行匹配内容）。

## 1. 暴露/启用条件
入口：`codex-rs/core/src/tools/spec.rs::build_specs`

仅当 `experimental_supported_tools` 包含 `"grep_files"` 时：
- `builder.push_spec_with_parallel_support(create_grep_files_tool(), true)`
- `builder.register_handler("grep_files", GrepFilesHandler)`

## 2. 输入（Input arguments）
权威 schema：`codex-rs/core/src/tools/spec.rs::create_grep_files_tool`
权威解析类型：`codex-rs/core/src/tools/handlers/grep_files.rs::GrepFilesArgs`

字段：
- `pattern`（必填）：正则/搜索模式（trim 后不能为空）
- `include`（可选）：glob 过滤（传递给 `rg --glob`）
- `path`（可选）：搜索路径（相对 turn cwd，会被 `turn.resolve_path`）
- `limit`（默认 100，最大 2000）：最多返回的匹配文件路径数量

## 3. 运行时语义（Runtime semantics）
handler：`codex-rs/core/src/tools/handlers/grep_files.rs::GrepFilesHandler`

### 3.1 参数校验/规范化
- `pattern.trim()` 不能为空
- `limit > 0`
- `limit = min(limit, MAX_LIMIT=2000)`
- `search_path = turn.resolve_path(path)` 并验证 `metadata` 可访问
- `include`：空字符串会被视为 None

### 3.2 执行 rg
`run_rg_search(pattern, include, search_path, limit, cwd=turn.cwd)`：
- 命令形态：
  - `rg --files-with-matches --sortr=modified --regexp <pattern> --no-messages [--glob <include>] -- <search_path>`
- 运行超时：30 秒（`COMMAND_TIMEOUT=30s`）
- exit code 语义：
  - `0`：有匹配 → 解析 stdout，每行一个文件路径，截断到 `limit`
  - `1`：无匹配 → 返回空列表
  - 其他：报错 `"rg failed: <stderr>"`
- 若无法启动 rg：报错并提示 “Ensure ripgrep is installed and on PATH.”

### 3.3 handler 的 success 标志（注意）
- 若无匹配：返回 `content="No matches found."`，且 `success: Some(false)`
- 若有匹配：返回多行路径文本，`success: Some(true)`

> 注意：`success` 字段是否出现在 provider wire output 取决于序列化策略（见 `_COMMON_OUTPUT_ENVELOPE.md`）。复刻时建议保留内部 success 字段语义。

## 4. 输出（Output）
多行文本，每行一个匹配文件路径（字符串）。

## 5. 代码映射
- tool spec：`codex-rs/core/src/tools/spec.rs::create_grep_files_tool`
- handler：`codex-rs/core/src/tools/handlers/grep_files.rs`

