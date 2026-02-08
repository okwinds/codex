# Tool: `list_dir` (function)

## 0. 目的（Purpose）
列出本地目录条目（可递归到指定深度），以可读文本返回。

## 1. 暴露/启用条件
入口：`codex-rs/core/src/tools/spec.rs::build_specs`

仅当 `experimental_supported_tools` 包含 `"list_dir"` 时：
- `builder.push_spec_with_parallel_support(create_list_dir_tool(), true)`
- `builder.register_handler("list_dir", ListDirHandler)`

## 2. 输入（Input arguments）
权威 schema：`codex-rs/core/src/tools/spec.rs::create_list_dir_tool`
权威解析类型：`codex-rs/core/src/tools/handlers/list_dir.rs::ListDirArgs`

字段：
- `dir_path`（必填）：**必须是绝对路径**
- `offset`（默认 1）：1-indexed 起始 entry 序号（按排序后的列表）
- `limit`（默认 25）：返回条目数上限
- `depth`（默认 2）：递归深度（>=1）

## 3. 运行时语义（Runtime semantics）
handler：`codex-rs/core/src/tools/handlers/list_dir.rs::ListDirHandler`

### 3.1 参数校验
- `offset >= 1`，否则 `"offset must be a 1-indexed entry number"`
- `limit > 0`，否则 `"limit must be greater than zero"`
- `depth > 0`，否则 `"depth must be greater than zero"`
- `dir_path` 必须绝对路径，否则 `"dir_path must be an absolute path"`

### 3.2 递归收集与排序
实现：`collect_entries(...)` + `list_dir_slice(...)`

算法要点：
1) BFS 队列：从 `dir_path` 开始，递归到 `depth`（目录才入队，且剩余深度 > 1）
2) 每个目录下：
   - `tokio::fs::read_dir` 读取条目
   - 异步读取 `file_type`
   - 计算 `relative_path`（相对初始 dir）
   - 计算 `display_name`（单组件名，长度硬上限 `MAX_ENTRY_LENGTH=500`）
   - 计算 `sort_key = relative_path.to_string_lossy().replace("\\","/")`（同样受长度上限）
   - `depth = prefix.components().count()` 用于输出缩进
3) 对条目按 `sort_key` 排序后追加到 entries
4) 在 `list_dir_slice` 内对全量 entries 再排序一次，然后做 offset/limit 截取
   - 若 `offset` 超出 entries.len → `"offset exceeds directory entry count"`
   - 若未返回完全部 entries，会追加一行：`"More than {capped_limit} entries found"`

### 3.3 输出格式
第一行固定输出：`Absolute path: <path.display()>`
每个条目输出为：
- `<indent><name>`，indent = `depth * 2` spaces（`INDENTATION_SPACES=2`）
- 目录以 `/` 结尾
- symlink 以 `@` 结尾
- unknown 以 `?` 结尾

## 4. 输出（Output）
`ToolOutput::Function { content: <多行文本>, success: Some(true) }`

## 5. 代码映射
- tool spec：`codex-rs/core/src/tools/spec.rs::create_list_dir_tool`
- handler：`codex-rs/core/src/tools/handlers/list_dir.rs`

