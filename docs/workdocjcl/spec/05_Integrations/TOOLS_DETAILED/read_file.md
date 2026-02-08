# Tool: `read_file` (function)

## 0. 目的（Purpose）
读取本地文件内容并以带行号的文本返回，支持两种模式：
- `slice`：简单区间读取（offset + limit）
- `indentation`：基于缩进的“块扩展读取”（围绕 anchor line 选择代码块，支持 include_siblings/include_header 等）

## 1. 暴露/启用条件
入口：`codex-rs/core/src/tools/spec.rs::build_specs`

仅当 `experimental_supported_tools` 包含 `"read_file"` 时：
- `builder.push_spec_with_parallel_support(create_read_file_tool(), true)`
- `builder.register_handler("read_file", ReadFileHandler)`

## 2. 输入（Input arguments）
权威 schema：`codex-rs/core/src/tools/spec.rs::create_read_file_tool`
权威解析类型：`codex-rs/core/src/tools/handlers/read_file.rs::ReadFileArgs`

字段：
- `file_path`（必填）：**必须是绝对路径**
- `offset`（默认 1）：1-indexed 起始行号
- `limit`（默认 2000）：返回行数上限
- `mode`（默认 `"slice"`）：`"slice"` 或 `"indentation"`
- `indentation`（可选 object）：仅 `mode="indentation"` 时使用
  - `anchor_line`：默认等于 offset
  - `max_levels`：默认 4（见 `defaults::max_levels`）；0 表示不限制
  - `include_siblings`：默认 false
  - `include_header`：默认 false
  - `max_lines`：可选；默认等于全局 limit

> 结构化 schema 参考：`workdocjcl/spec/05_Integrations/TOOLS_SCHEMA_REFERENCE.json`（条目：`name=read_file kind=function`）

## 3. 运行时语义（Runtime semantics）
handler：`codex-rs/core/src/tools/handlers/read_file.rs::ReadFileHandler`

### 3.1 参数校验
- `offset >= 1`，否则错误 `"offset must be a 1-indexed line number"`
- `limit > 0`，否则错误 `"limit must be greater than zero"`
- `file_path` 必须是绝对路径，否则错误 `"file_path must be an absolute path"`

### 3.2 Slice 模式
实现：`codex-rs/core/src/tools/handlers/read_file.rs::slice::read`

算法：
1) 逐行读取文件（`\n`/`\r\n` 处理）
2) 从第 `offset` 行开始收集，最多 `limit` 行
3) 每行格式化为：`L{line_number}: {formatted_line}`
   - 单行长度硬上限 `MAX_LINE_LENGTH=500`（按字符边界截断）
   - `TAB_WIDTH=4` 用于 display 缩进计算
4) 如果文件总行数 `< offset` → 错误 `"offset exceeds file length"`

### 3.3 Indentation 模式（块扩展）
实现：`codex-rs/core/src/tools/handlers/read_file.rs::indentation::read_block`

核心规则（复刻需要逐条实现）：
1) `anchor_line = indentation.anchor_line.unwrap_or(offset)`，必须 >=1 且 <= file_len
2) 先把全文件读入内存为 `LineRecord { number, raw, display, indent }`
3) 以 `anchor_line` 为中心选择“anchor block”，并按 `max_levels/include_siblings/include_header` 扩展
4) 过滤/裁剪：
   - 行长度同样受 `MAX_LINE_LENGTH` 限制
   - 最终输出行数受 `max_lines.unwrap_or(limit)` 保护
5) 输出依然是带 `L{n}:` 前缀的文本行

> 细节非常多（注释行识别、空行 trim、缩进计算、siblings 扩展等）。完整实现应以 `read_file.rs` 中的辅助函数与逻辑为准。

## 4. 输出（Output）
`ToolOutput::Function { content: <多行文本>, success: Some(true) }`

## 5. 错误（Errors）
- 文件打开/读取失败：`"failed to read file: ..."`
- slice：`offset exceeds file length`
- indentation：`anchor_line exceeds file length` / `anchor_line must be...` / `max_lines must be...`

## 6. 代码映射
- tool spec：`codex-rs/core/src/tools/spec.rs::create_read_file_tool`
- handler：`codex-rs/core/src/tools/handlers/read_file.rs`

