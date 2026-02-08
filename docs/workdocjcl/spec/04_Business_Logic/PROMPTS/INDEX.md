# Prompt 资产索引（System Preset Prompts Artifacts）

本目录存放“复刻 Codex 行为所需的 prompt 资产”的**规范化副本**（verbatim copy），用于满足：
- 仅依赖规格文档即可复刻（不读取原仓库源码文件）
- prompt 文本可校验（通过 `MANIFEST.json` 的 sha256）

这些文件来自 `codex-rs/core/` 与其 `templates/` 子目录（见 `MANIFEST.json` 的 `source_path`）。

## 1. 清单与校验
- 规范副本的完整清单与校验和：`docs/workdocjcl/spec/04_Business_Logic/PROMPTS/MANIFEST.json`
- 复刻实现应当在构建阶段校验 sha256，以确保 prompt 文本未漂移。

## 2. 如何在运行时被使用（导航）
prompt 的“选择/覆盖/注入顺序”属于运行时语义，见：
- BaseInstructions 决议、initial context 注入：`docs/workdocjcl/spec/04_Business_Logic/PROMPT_ASSEMBLY.md`
- 模型 slug → preset prompt 的选择矩阵：`docs/workdocjcl/spec/04_Business_Logic/SYSTEM_PRESET_PROMPTS.md`

## 3. 资产分组（按用途）
- `prompt.md`：默认 base instructions（通用）
- `prompt_with_apply_patch_instructions.md`：当模型/工具类型需要显式 apply_patch 指令时使用
- `review_prompt.md`：review 工作流专用 prompt（review mode）
- `hierarchical_agents_message.md`：collaboration/多代理场景的分层说明
- `gpt_5*_prompt.md` / `gpt-5.*-codex*_prompt.md`：不同模型族的 preset base instructions
- `templates/model_instructions/*`：模板化 instructions（配合 personality variables）
- `templates/personalities/*`：personality 文本片段（friendly/pragmatic）

