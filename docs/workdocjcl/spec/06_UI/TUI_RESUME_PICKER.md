# TUI：Resume/Fork Session Picker 复刻级规格

本章目标：复刻 TUI 的“选择历史会话（rollout）”全屏选择器（Alt screen），用于：
- **Resume**：恢复继续某个历史 session（rollout）
- **Fork**：从某个历史 session fork 出新线程

该选择器只负责“列出候选 + 搜索 + 选中返回 path”；真正的 resume/fork 语义（rollout 截断、cwd 处理、线程初始化）由 core/上层调用方完成：
- Rollout 语义：`docs/workdocjcl/spec/02_Data/ROLLOUT_SEMANTICS.md`

---

## 1. 入口与返回值

实现：`codex-rs/tui/src/resume_picker.rs`

入口：
- `run_resume_picker(tui, codex_home, default_provider, show_all) -> SessionSelection`
- `run_fork_picker(tui, codex_home, default_provider, show_all) -> SessionSelection`

返回枚举：
- `SessionSelection::StartFresh`：用户取消/选择开始新会话（Esc）
- `SessionSelection::Resume(path)`：用户选中某条历史 session（Enter）
- `SessionSelection::Fork(path)`：用户选中某条历史 session（Enter）
- `SessionSelection::Exit`：用户请求退出（Ctrl+C）

其中 `path` 是 rollout 文件路径（来自 `ThreadItem.path`）。

---

## 2. 运行形态：Alt screen + RAII 退出保证

run_session_picker 进入时：
- `AltScreenGuard::enter(tui)` → `tui.enter_alt_screen()`

退出时（无论正常返回还是异常 unwinding）：
- `AltScreenGuard::drop` 会 `tui.leave_alt_screen()`

这保证 picker 结束后回到主 UI。

来源：
- `codex-rs/tui/src/resume_picker.rs:AltScreenGuard`

---

## 3. 数据源：RolloutRecorder::list_threads（分页）

后台加载器：`page_loader: PageLoader`

每次加载 page（固定参数）：
- `PAGE_SIZE = 25`
- `ThreadSortKey::CreatedAt`
- `sources = INTERACTIVE_SESSION_SOURCES`（仅交互式来源）
- `provider_filter = [default_provider]`（只列默认 provider 的 session）
- `default_provider` 同时作为 list_threads 的默认 provider 参数传入

实现调用：
- `RolloutRecorder::list_threads(codex_home, PAGE_SIZE, cursor, ThreadSortKey::CreatedAt, INTERACTIVE_SESSION_SOURCES, Some(provider_filter), default_provider)`

分页 cursor：
- 首次 `cursor=None`
- 后续使用 `ThreadsPage.next_cursor` 作为 `pagination.next_cursor`

限制：
- page 返回还包含 `num_scanned_files` 与 `reached_scan_cap`，用于在搜索无结果时展示“只扫描了前 N 条”的提示。

来源：
- `codex-rs/tui/src/resume_picker.rs:run_session_picker`（page_loader）
- `codex-rs/core/src/rollout/recorder.rs`（真实 list_threads 行为在 core；本章描述 UI 消费方式）

---

## 4. 行模型（Row）与元信息抽取

### 4.1 Row 字段
`Row`（UI 内部）字段：
- `path: PathBuf`：rollout 路径
- `preview: String`：预览文本（通常是第一条真实用户问题）
- `thread_id: Option<ThreadId>`：从 head 元信息抽取
- `thread_name: Option<String>`：异步从索引加载（见 §4.3）
- `created_at` / `updated_at: Option<DateTime<Utc>>`
- `cwd: Option<PathBuf>`：从 head 中的 `SessionMetaLine` 抽取
- `git_branch: Option<String>`：从 head 中的 `SessionMetaLine.git.branch` 抽取

### 4.2 created/updated 时间来源
构造规则（`head_to_row`）：
- `created_at`：
  1) 优先使用 `ThreadItem.created_at`（RFC3339）
  2) 否则从 `head` 中寻找 `extract_timestamp`（value["timestamp"]，RFC3339）
- `updated_at`：
  1) 优先使用 `ThreadItem.updated_at`（RFC3339）
  2) 否则退回 `created_at`

列表显示使用 `updated_at` 优先（若无则 created_at），格式化为相对时间（秒/分/小时/天）。

### 4.3 Thread name 的异步填充
Row 初始 `thread_name=None`；加载 page 后调用 `update_thread_names()`：
1. 收集所有 `row.thread_id` 中尚未缓存的 id
2. 调用 `find_thread_names_by_ids(codex_home, &missing_ids)` 获取映射（失败则视为空）
3. 填充 `thread_name_cache`，并回写到 `all_rows`
4. 若发生变化：重新 `apply_filter()`（可能影响搜索命中）

显示预览文案规则：
- `display_preview()`：若 `thread_name` 有值则优先显示 thread name；否则显示 preview。

---

## 5. 过滤与 show_all 语义（按 cwd）

调用者传入 `show_all`：
- `show_all == true`：不按 cwd 过滤，显示所有 rows；并在 UI 中增加 `CWD` 列
- `show_all == false`：按 cwd 过滤：
  - `filter_cwd = std::env::current_dir()`（picker 运行时的 cwd）
  - 对每个 row：
    - 若 `row.cwd` 缺失：**该 row 被过滤掉**（不会显示）
    - 若 `paths_match(row.cwd, filter_cwd)` 为 true：保留；否则过滤

`paths_match`：
- 优先使用 `path_utils::normalize_for_path_comparison` 标准化后比较；失败则直接 path 比较。

来源：
- `codex-rs/tui/src/resume_picker.rs:row_matches_filter` / `paths_match`

---

## 6. 搜索（query）与“加载更多直到命中”

### 6.1 输入与匹配规则
- 用户在 picker 中输入字符（不含 Ctrl/Alt 修饰）会追加到 `query`
- `Backspace` 删除末尾字符

匹配字段（case-insensitive）：
- `preview`（转小写）
- `thread_name`（若有值，转小写）

### 6.2 搜索行为（无结果时的自动分页）
当 `query` 非空且当前过滤后 `filtered_rows` 为空：
1. 若已 `reached_scan_cap` 或 `next_cursor == None`：停止搜索（显示 “No results” 或 “Search scanned first N sessions; more may exist”）
2. 否则进入 `SearchState::Active { token }` 并触发 `load_more_if_needed(Search{token})`
3. 每次 page 加载完成后：
   - ingest + 更新 thread name + 重新过滤
   - 若仍无结果且仍可分页：继续加载下一页
   - token 不匹配时（用户已输入新 query）：忽略旧 search 的 completed_token

UI 空态提示：
- 搜索中：`Searching…`
- 扫描到 cap：`Search scanned first {num_scanned_files} sessions; more may exist`
- 否则：`No results for your search`

---

## 7. 分页触发（Scroll）

### 7.1 下移触发 near-bottom 加载
当用户 `Down` 或 `PageDown` 导航时：
- 若剩余未选中的行数 `remaining <= LOAD_NEAR_THRESHOLD`（阈值 5），触发 `load_more_if_needed(Scroll)`

### 7.2 视窗填充触发
在 `Draw` 时会计算 `list_height = terminal.height - 4`，并：
- `update_view_rows(list_height)`
- `ensure_minimum_rows_for_view(list_height)`

如果当前 rows 数量不足以填满视窗，并且仍有 next_cursor、且未在 loading，则会自动加载更多（search 模式或 scroll 模式取决于 `search_state`）。

---

## 8. 按键（Keybindings）

实现：`PickerState::handle_key`

| 按键 | 作用 | 返回值 |
|---|---|---|
| `Esc` | 开始新会话（退出 picker） | `StartFresh` |
| `Ctrl+C` | 退出程序 | `Exit` |
| `Enter` | 对当前选中项执行 action | `Resume(path)` / `Fork(path)` |
| `Up` / `Down` | 移动选中项 | - |
| `PageUp` / `PageDown` | 按页移动选中项（步长 = view_rows 或 10） | - |
| `Backspace` | 删除 query 末尾 | - |
| `Char(c)` | 追加到 query（仅当无 Ctrl/Alt 修饰） | - |

提示栏（UI 渲染的 hint line）固定展示：
- `Enter` to resume/fork
- `Esc` to start new
- `Ctrl+C` to quit
- `Up/Down` to browse

---

## 9. 渲染（布局与列）

draw 布局（纵向 5 行块）：
1. Header（1 行）：标题（cyan + bold）
2. Search（1 行）：空 query 显示 “Type to search” dim；否则 “Search: {query}”
3. Columns header（1 行）：`Updated`、`Branch`、（可选）`CWD`、`Conversation`
4. List（剩余）：逐行渲染 rows；选中项前缀 `> `（bold），未选中为 `  `
5. Hint（1 行）：快捷键提示（见 §8）

列宽策略：
- `Updated` / `Branch` / `CWD` 的最大宽度按当前 rows 的 label 宽度计算（同时至少覆盖列名宽度）
- `Branch` 与 `CWD` 的 label 会右侧省略（右端保留，前缀 `…`），最大 24 字符
- `Conversation` 预览会按剩余宽度 `truncate_text(...)`

空态：
- 若 rows 为空：渲染空态提示行（见 §6.2）
- 若正在 loading 且 list 还有空间：底部追加 `Loading older sessions…` 行（dim + italic）

来源：
- `codex-rs/tui/src/resume_picker.rs:draw_picker` / `render_list` / `calculate_column_metrics`

## 来源（Source）
- `codex-rs/tui/src/resume_picker.rs`
- `codex-rs/cli/src/main.rs`
- `codex-rs/state/src/runtime.rs`
