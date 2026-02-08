# 集成：Skills（SKILL.md）体系复刻级规格

本章目标：完整复刻 Codex 的 “Skills” 落地实现，使复刻系统在 **同一目录结构/同一 config layer stack/同一用户输入** 下能得到：
- 同样的 skills 发现结果（roots、scope、去重、排序）
- 同样的启用/禁用语义（user-layer-only 的 `skills` 配置）
- 同样的显式 mention 解析与消歧（`$name` 与 `[$name](path)`）
- 同样的 skill 注入形态（把 `SKILL.md` 正文注入为 `<skill>...</skill>` user message）
- 同样的依赖提示行为（仅 `env_var` 依赖会触发 `request_user_input`）
- 同样的协议输出（`Op::ListSkills` / `ListSkillsResponseEvent`）

“Skills”在 Codex 中的作用不是“工具调用”，而是 **额外的本地指令来源**：模型只在用户显式 mention 时才会看到某个 skill 的全文。与此同时，Codex 会把“可用 skills 的列表清单”始终注入到 `UserInstructions` 中，让模型知道有哪些 skills 可被 `$name` 引用（见 `docs/workdocjcl/spec/04_Business_Logic/PROMPT_ASSEMBLY.md`）。

---

## 0. 数据结构（core vs protocol 必须区分）

### 0.1 core：`codex_core::skills::model::SkillMetadata`
字段：
- `name: String`（来自 SKILL.md frontmatter）
- `description: String`（来自 SKILL.md frontmatter）
- `short_description: Option<String>`（来自 SKILL.md frontmatter metadata.short-description）
- `interface: Option<SkillInterface>`（来自 `agents/openai.yaml`，可选）
- `dependencies: Option<SkillDependencies>`（来自 `agents/openai.yaml`，可选）
- `path: PathBuf`（canonicalize 后的 SKILL.md 路径）
- `scope: SkillScope`（Repo/User/System/Admin）

### 0.2 protocol：`codex_protocol::protocol::SkillMetadata`
在 core → UI 的 ListSkills 输出中，协议类型额外包含：
- `enabled: bool`（由 `disabled_paths` 计算得出：`!disabled_paths.contains(path)`）

### 0.3 注入形态：`SkillInstructions`（role=user）
当某个 skill 被选中注入时，core 会读取 `SKILL.md` 全文并生成：
```
<skill>
<name>{name}</name>
<path>{path}</path>
{SKILL.md full contents}
</skill>
```
这是模型侧消费 skill 的唯一“正文入口”。（skills 列表清单不包含正文。）

---

## 1. Skills Roots（发现根目录）与 scope 语义

Skills roots 的来源由两部分组成，并最终 **按 path 去重**：
1) 来自 config layer stack（`ConfigLayerSource`）
2) 来自 repo 内 `.agents/skills`（沿 project_root → cwd 的层级）

### 1.1 来自 config layer stack 的 roots（按 layer 类型）
按 layer 遍历（最高优先级在前）并追加 roots：

- `Project` layer：
  - `<project_config_folder>/skills` → scope = `Repo`

- `User` layer：
  - `<user_config_folder>/skills`（deprecated，但仍支持）→ scope = `User`
  - `$HOME/.agents/skills`（user-installed skills）→ scope = `User`
  - `<CODEX_HOME>/skills/.system`（embedded system skills cache）→ scope = `System`

- `System` layer：
  - `<system_config_folder>/skills`（例如 Unix 的 `/etc/codex/skills`）→ scope = `Admin`

> 复刻重点：System layer 的 skills 被当作 Admin-scope（不是 System-scope）。

### 1.2 来自 repo `.agents/skills` 的 roots（project_root → cwd）
Codex 还会在 repo 工作树内查找 `.agents/skills`：
1) 先用 `project_root_markers` 找 project root（默认 markers + 来自非 Project layers 的合并覆盖）
2) 构造 project_root → cwd 的目录链
3) 对链上的每一层目录，若存在 `.<agents>/skills` 目录则加入 root（scope=Repo）

复刻注意：
- 这是 “层级覆盖” 的基础：越靠近 cwd 的 `.agents/skills` 不会覆盖上层，但都会被扫描并合并去重。

---

## 2. 扫描规则：如何在 root 下发现 `SKILL.md`

### 2.1 扫描策略与限制
对每个 root：
- root 先 canonicalize；不是目录则跳过
- BFS/队列遍历子目录
- 忽略以 `.` 开头的 entry（文件/目录/链接）
- 最大遍历深度：`MAX_SCAN_DEPTH = 6`
- 每个 root 最多遍历目录数：`MAX_SKILLS_DIRS_PER_ROOT = 2000`（超过则截断并 warn）

### 2.2 symlink 处理（scope 影响 follow 行为）
当 entry 为 symlink：
- scope ∈ {Repo, User, Admin}：允许 follow symlinked directories
- scope == System：**不**follow（system skills 由 Codex 自己写入缓存，避免外部污染）

### 2.3 `SKILL.md` 命名要求
只有当文件名严格等于 `SKILL.md` 时才会尝试 parse 并加载为 skill（扫描阶段的匹配是字符串相等）。

---

## 3. `SKILL.md` 解析规范（frontmatter 是硬要求）

### 3.1 frontmatter 形态（必须在文件起始处）
`SKILL.md` 必须以 YAML frontmatter 开头，且由 `---` 包裹：
```
---
name: <required>
description: <required>
metadata:
  short-description: <optional>
---

<body markdown...>
```

解析规则：
- 必须存在 opening `---` 且存在 closing `---`
- 必须包含 `name`、`description`，缺失即 parse error
- `name/description/short-description` 会被“单行化”：
  - `split_whitespace().join(" ")`（折叠多空白/换行）

长度限制（超限即 parse error）：
- `name`: ≤ 64 chars
- `description`: ≤ 1024 chars
- `metadata.short-description`: ≤ 1024 chars

错误处理：
- 对非 System scope：parse error 会记录到 `SkillLoadOutcome.errors`
- 对 System scope：parse error 不进 errors（fail open；system skills 理论上可控）

---

## 4. 可选元数据：`agents/openai.yaml`（fail-open）

在 `SKILL.md` 所在目录下，若存在：
- `agents/openai.yaml`

则会尝试解析两块内容：

### 4.1 interface（展示与默认提示）
可选字段：
- `display_name`
- `short_description`
- `icon_small` / `icon_large`（路径）
- `brand_color`（`#RRGGBB`）
- `default_prompt`

校验规则（不通过则忽略对应字段并 warn；整体 fail-open）：
- 字符串字段：空值忽略；长度受限（同 64/1024 的约束）
- `brand_color`：必须是 `#RRGGBB` 且全为 hex digit
- icon 路径：
  - 必须是相对路径
  - 必须位于 skill 目录的 `assets/` 下
  - 不允许包含 `..`

### 4.2 dependencies（工具依赖声明）
形态：`dependencies.tools[]`，每项可含：
- 必填：`type`、`value`
- 可选：`description`、`transport`、`command`、`url`

字段长度均有上限（同类约束，超限则该字段被忽略或该 dependency 被丢弃）。

复刻注意：
- 当前 core 的“自动提示/收集”只对 `type == "env_var"` 生效（见 §7）。
- 其他类型主要用于 UI/规范表达（例如 mcp/cli 依赖），但不会自动安装或自动验证存在性，除非另有 feature 逻辑介入（见 MCP 章节与相关 feature）。

---

## 5. Embedded System Skills：安装到本地缓存（必须复刻指纹语义）

Codex 编译时内置了一组 system skills（样例/系统工作流），运行时会在启动 `SkillsManager` 时把它们写入：
- `<CODEX_HOME>/skills/.system`

安装规则：
1) 计算 embedded skills 的 fingerprint：
   - 遍历 embedded 目录所有 entry
   - 对每个目录记录 path（contents_hash=None）
   - 对每个文件记录 path + contents hash
   - 排序后用 hash 聚合，并混入固定 salt `"v1"`
2) 若 `.system` 已存在且 marker 文件 `.codex-system-skills.marker` 的内容等于 fingerprint：跳过安装
3) 否则：
   - 删除既有 `.system` 目录（`remove_dir_all`）
   - 把 embedded 目录完整写入
   - 写入 marker：`{fingerprint}\n`

复刻注意：
- 这是“避免每次启动重写系统技能”的关键；若你不实现 marker 指纹，会导致大量 IO 与用户目录被反复 churn。

---

## 6. 启用/禁用：`skills` 配置（user-layer only）

### 6.1 配置入口
技能启用/禁用只读 **User config layer** 的 `skills` 配置（更高优先级 layers 会被忽略）。

配置结构（概念；schema 见 `docs/workdocjcl/spec/01_Configuration/CONFIG_SCHEMA_REFERENCE.md` 的 `skills`）：
- `skills.config[]`：
  - `path: PathBuf`（指向某个 SKILL.md）
  - `enabled: bool`

### 6.2 disabled_paths 的构造（canonicalize + 最终禁用集）
规则：
1) 读出 user layer 的 `skills` 值并解析为 `SkillsConfig`
2) 对每个 entry.path 做 canonicalize（失败则用原值）
3) 建立 map：`path -> enabled`
4) 所有 `enabled == false` 的 path 进入 `disabled_paths: HashSet<PathBuf>`

语义：
- 未出现在 config 的 skill：默认 enabled
- 出现且 enabled=false：禁用（不会出现在 mentions 注入结果中；UI 仍可列出但标记 disabled）

---

## 7. 显式 mentions：从用户输入选择要注入的 skills（消歧规则必须一致）

### 7.1 只扫描 Text inputs
skills mentions 只从 `UserInput::Text { text, ... }` 中解析；结构化输入（例如图像、或带结构的输入项）不会触发 skills 选择。

### 7.2 支持的 mention 语法
两类：
1) 纯文本 `$name`
   - name 字符集：`[A-Za-z0-9_-]`（连续）
   - 必须是边界匹配：`$alpha-skill` 匹配 `alpha-skill`，但 `$alpha-skillx` 不匹配
2) Markdown 链接 `[$name](path)`
   - path 会被记录用于“按 path 精确匹配”
   - 同时也会把 name 记录为 fallback（但 App/MCP kinds 例外，见下）

特殊规则：
- 常见 env var 名称会被忽略（避免 `$PATH` 等被误判为 skill）：
  - PATH, HOME, USER, SHELL, PWD, TMPDIR, TEMP, TMP, LANG, TERM, XDG_CONFIG_HOME

### 7.3 path kind 与过滤（App/MCP/Skill）
对链接型 mention，会识别 path 前缀：
- `app://` → App（不计入 names，用于 connectors/apps 体系）
- `mcp://` → Mcp（不计入 names）
- `skill://` 或 “看起来是 SKILL.md 文件路径” → Skill

复刻注意：
- 这套解析器是“工具 mentions”的统一入口，skills 只消费其中的 Skill kind。

### 7.4 选择顺序与消歧策略（两阶段）
输入中的 mentions 解析完成后，对所有 skills 按其既有排序（见 §1/§2 的 scope/name/path 排序）进行选择。选择分两阶段：

**阶段 A：按 path 精确匹配**
- 取所有 mentions.paths 中非 App/Mcp 的 path（若以 `skill://` 开头则先 strip 前缀）
- 对 `skills` 逐个遍历：
  - 若 skill.path ∈ disabled_paths：跳过
  - 若 skill.path 已被选中过：跳过
  - 若 `skill.path.to_string_lossy()` 在 mentions.path 集合中：选中

**阶段 B：按 plain name 匹配（仅当不歧义且无 connector 冲突）**
- 仅当某个 `skill.name` 出现在 mentions.plain_names 中，且满足：
  - `skill_name_counts[skill.name] == 1`（在“enabled skills”里不歧义）
  - `connector_slug_counts[skill.name.lowercase()] == 0`（避免与 connectors/apps slug 冲突）
  - 且未被选中过（按 name/path 去重）
才会选中。

复刻注意：
- 该算法的核心性质是：**选择顺序由 skills 列表顺序决定，而不是用户文本中 mention 出现的先后**（测试明确要求“respects skill order”）。
- 显式 path mention 的优先级高于 plain name mention。

---

## 8. 注入执行：读取 SKILL.md 正文并写入 prompt history

当 mention 选择得到 `mentioned_skills[]` 后，core 会：
1) 按 `mentioned_skills` 顺序逐个 `read_to_string(skill.path)`
2) 成功则生成 `SkillInstructions`（role=user）并追加到 `SkillInjections.items`
3) 失败则把错误字符串放入 `SkillInjections.warnings`，并继续处理其它 skills（fail open）

观测/埋点（复刻可选但建议保留）：
- OTel counter：`codex.skill.injected`，labels：`status=ok|error`、`skill=<name>`
- analytics：记录 `SkillInvocation { skill_name, skill_scope, skill_path }`

---

## 9. Skill 依赖提示：env var（`request_user_input`）闭环

### 9.1 只支持 `type == "env_var"`
从 `mentioned_skills[].dependencies.tools[]` 中收集：
- `type == "env_var"`
- `value` 非空

形成 dependency list：`{ skill_name, name=<env var>, description }`

### 9.2 解析顺序：session cache → process env → UI prompt
对每个 env var name：
1) 若 session `dependency_env` 已有值：跳过
2) 否则尝试读取 `std::env::var(name)`：
   - 若存在：写入 session `dependency_env`（本 turn 继续使用）
3) 若仍缺失：通过 `request_user_input` 向 UI 询问（is_secret=true）

### 9.3 request_user_input 的问题结构（必须一致）
每个缺失 env var 会生成一个 question：
- `header`: `"Skill requires environment variable"`
- `id`: env var name（例如 `"OPENAI_API_KEY"`）
- `question`: 固定句式 + description（若有）+ 提示“experimental internal feature；仅 session 内存保存”
- `options`: None（自由输入，secret）

call_id：
- `skill-deps-<turn_context.sub_id>`

响应解析：
- 只接受 `answer.answers[]` 中以 `"user_note: "` 为前缀的条目
- 取前缀后的非空文本作为 env var 值写入 session `dependency_env`

复刻注意：
- 这些值不会写入系统环境变量；也不会持久化到磁盘。

---

## 10. `Op::ListSkills` 协议：core → UI 数据面

### 10.1 请求
`Op::ListSkills { cwds, force_reload }`
- 当 `cwds` 为空：等价于 `[session.cwd]`
- 当 `force_reload` 为 true：绕过 `SkillsManager` 的 per-cwd cache，重新扫描/解析

### 10.2 响应
`EventMsg::ListSkillsResponse(ListSkillsResponseEvent { skills })`：
- `skills: Vec<SkillsListEntry>`
  - `cwd: PathBuf`
  - `skills: Vec<protocol::SkillMetadata>`（包含 `enabled`）
  - `errors: Vec<SkillErrorInfo>`

UI 典型行为：
- 列表展示：按 cwd 分组显示技能与错误
- 管理启用：UI 写入 user-layer `skills` config（path+enabled），再 `ListSkills(force_reload=true)` 刷新

---

## 11. Source Map（本章关键源码锚点）

至少需要对齐以下源码的细节：
- skills roots + 扫描 + frontmatter/metadata 校验：`codex-rs/core/src/skills/loader.rs`
- embedded system skills 安装与 marker 指纹：`codex-rs/core/src/skills/system.rs`
- per-cwd cache、disabled_paths（user-layer-only）：`codex-rs/core/src/skills/manager.rs`
- mentions 解析与消歧、`skill://`、env var 忽略集：`codex-rs/core/src/skills/injection.rs`
- 注入编码 `<skill>...</skill>`：`codex-rs/core/src/instructions/user_instructions.rs`
- env var dependencies prompt：`codex-rs/core/src/skills/env_var_dependencies.rs`
- 列表协议定义：`codex-rs/protocol/src/protocol.rs`（`Op::ListSkills`、`ListSkillsResponseEvent`）
- core handler：`codex-rs/core/src/codex.rs`（`handlers::list_skills`）
- UI enable/disable 落盘：`codex-rs/tui/src/app.rs`（`AppEvent::SetSkillEnabled`）

