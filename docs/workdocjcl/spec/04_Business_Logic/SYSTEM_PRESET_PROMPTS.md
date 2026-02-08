# 业务逻辑：系统预置 Prompt 规格（model slug → prompt 资产映射）

本章目标：把 Codex 内置的“系统预置 prompt（system preset prompts）”完整落盘到规格层，确保复刻者在**不查看原仓库源码**的情况下，也能：
- 得到与 Codex 相同的 base instructions 文本
- 在相同 model slug 下选择同一份 preset prompt
- 理解 personality/template 与 base instructions 的组合关系

本章不重复描述 initial context 注入顺序（developer/user/skills/personality/env），见：
- `docs/workdocjcl/spec/04_Business_Logic/PROMPT_ASSEMBLY.md`

---

## 1. 规范化 prompt 资产（verbatim）
本仓库的 preset prompt 文本以静态文件形式存在于 `codex-rs/core/`，并在 Rust 编译期用 `include_str!` 内嵌到二进制中。

为满足“规格文档可独立复刻”，这些文件的规范副本已拷贝到：
- `docs/workdocjcl/spec/04_Business_Logic/PROMPTS/`
- 完整清单与 sha256：`docs/workdocjcl/spec/04_Business_Logic/PROMPTS/MANIFEST.json`

复刻要求：
- 复刻实现必须使用这些规范副本的**原文**（非摘要/非改写）。

---

## 2. 选择逻辑总入口（ModelInfo）
模型预置 prompt 的选择在离线路径中由如下函数决定：
- `codex-rs/core/src/models_manager/model_info.rs::find_model_info_for_slug(slug)`

该函数根据 `slug` 的前缀（`starts_with`）分支选择：
- base_instructions（对应某个 preset prompt 文件）
- tool 能力（例如 `apply_patch` 是 function 还是 freeform）
- shell tool 类型、reasoning/verbosity 支持、truncation policy、context window 等
- 部分模型还会设置 `ModelMessages.instructions_template` 与 personality variables（模板化 instructions）

> 复刻注意：本函数是有序 if/else-if 链，分支顺序本身就是契约的一部分。

---

## 3. model slug → base instructions 映射矩阵（必须逐条一致）

下面表格描述 **base_instructions** 的来源（即“系统预置 prompt 文本”），以及该分支是否启用 `instructions_template/personality`。

约定：
- “base prompt 文件”指 `docs/workdocjcl/spec/04_Business_Logic/PROMPTS/` 下的同名文件。
- “模板/人格”指 `PROMPTS/templates/*` 下的文件。

| 分支条件（按源码顺序） | base_instructions 资产 | 模板化 instructions | 备注（复刻关键点） |
|---|---|---|---|
| `slug` starts_with `o3` 或 `o4-mini` | `prompt_with_apply_patch_instructions.md` | 无 | 支持 reasoning summaries；context_window=200k |
| `slug` starts_with `codex-mini-latest` | `prompt_with_apply_patch_instructions.md` | 无 | shell_type=Local；支持 reasoning summaries；context_window=200k |
| `slug` starts_with `gpt-4.1` | `prompt_with_apply_patch_instructions.md` | 无 | context_window≈1,047,576 |
| `slug` starts_with `gpt-oss` 或 `openai/gpt-oss` | `prompt.md`（默认） | 无 | apply_patch_tool_type=Function；context_window=96k |
| `slug` starts_with `gpt-4o` | `prompt_with_apply_patch_instructions.md` | 无 | context_window=128k |
| `slug` starts_with `gpt-3.5` | `prompt_with_apply_patch_instructions.md` | 无 | context_window=16385 |
| `slug` starts_with `test-gpt-5` | `gpt_5_codex_prompt.md` | 无 | 用于测试：限定 tools 列表；parallel_tool_calls=true；verbosity=true |
| `slug` starts_with `exp-codex` 或 `codex-1p` | `gpt-5.2-codex_prompt.md` | `templates/model_instructions/gpt-5.2-codex_instructions_template.md` + personalities | apply_patch=Freeform；shell=ShellCommand；parallel_tool_calls=true；272k |
| `slug` starts_with `exp-` | `prompt.md` | 无 | apply_patch=Freeform；shell=UnifiedExec；verbosity=true；272k |
| `slug` starts_with `gpt-5.2-codex` 或 `bengalfox` | `gpt-5.2-codex_prompt.md` | `templates/model_instructions/gpt-5.2-codex_instructions_template.md` + personalities | apply_patch=Freeform；shell=ShellCommand；parallel_tool_calls=true；272k；reasoning_levels=low/med/high/xhigh |
| `slug` starts_with `gpt-5.1-codex-max` | `gpt-5.1-codex-max_prompt.md` | 无 | parallel_tool_calls=false；272k |
| (`slug` starts_with `gpt-5-codex`/`gpt-5.1-codex`/`codex-`) 且不包含 `-mini` | `gpt_5_codex_prompt.md` | 无 | parallel_tool_calls=false；272k；reasoning_levels=low/med/high |
| `slug` starts_with `gpt-5-codex`/`gpt-5.1-codex`/`codex-`（包含 `-mini` 等） | `gpt_5_codex_prompt.md` | 无 | 与上条差异：reasoning_levels 默认（未显式设置） |
| `slug` starts_with `gpt-5.2` 或 `boomslang` | `gpt_5_2_prompt.md` | 无 | verbosity=true；default_verbosity=Low；shell=ShellCommand；272k；reasoning_levels=non-codex variant |
| `slug` starts_with `gpt-5.1` | `gpt_5_1_prompt.md` | 无 | verbosity=true；default_verbosity=Low；shell=ShellCommand；272k |
| `slug` starts_with `gpt-5`（兜底在上述之后） | `prompt_with_apply_patch_instructions.md` | 无 | shell_type=Default；verbosity=true；272k |
| 其他未知 slug | （无明确 preset；仍会生成 ModelInfo，但会 warn） | 无 | base_instructions 使用默认（实现中是 macro 默认 `prompt.md`，但该分支显式清空 reasoning levels） |

> 复刻注意：上表只列出 prompt 选择相关字段；其它能力字段（tools/verbosity/truncation等）属于 ModelInfo 全规格的一部分，若要完全复刻需按源码逐字段对齐。

---

## 4. personality/template 的组合契约（Codex 5.2 系列）
当 `ModelInfo.model_messages.instructions_template` 存在时，base instructions 可能并非最终下发给模型的 instructions 文本。

关键点（复刻必须一致）：
- 最终 instructions 的生成由 `ModelInfo.get_model_instructions(personality)` 决定
- 其中 `instructions_template` 会结合 `ModelInstructionsVariables`（personality_default/friendly/pragmatic）进行渲染

规范副本：
- 模板：`docs/workdocjcl/spec/04_Business_Logic/PROMPTS/templates/model_instructions/gpt-5.2-codex_instructions_template.md`
- personalities：
  - `docs/workdocjcl/spec/04_Business_Logic/PROMPTS/templates/personalities/gpt-5.2-codex_friendly.md`
  - `docs/workdocjcl/spec/04_Business_Logic/PROMPTS/templates/personalities/gpt-5.2-codex_pragmatic.md`

运行时注入顺序与“baked vs injected personality”判定见：
- `docs/workdocjcl/spec/04_Business_Logic/PROMPT_ASSEMBLY.md`

## 来源（Source）
- `codex-rs/core/src/models_manager/model_info.rs#find_model_info_for_slug`
- `codex-rs/core/src/models_manager/model_info.rs`
- `codex-rs/core/prompt.md`
- `codex-rs/core/prompt_with_apply_patch_instructions.md`
- `codex-rs/core/gpt-5.2-codex_prompt.md`
- `codex-rs/core/templates/model_instructions/gpt-5.2-codex_instructions_template.md`
