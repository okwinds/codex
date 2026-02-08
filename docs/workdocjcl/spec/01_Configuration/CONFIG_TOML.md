# 配置文件：`config.toml`

本章定义 Codex 的主配置文件 `config.toml` 的位置、加载顺序与“权威 schema 来源”。

## 1. 位置（Location）
- 默认：`~/.codex/config.toml`
- 可通过 `CODEX_HOME` 改为：`<CODEX_HOME>/config.toml`

## 2. 权威 Schema（强烈建议复刻时直接使用）
- JSON Schema：`codex-rs/core/config.schema.json`
  - 该文件由 `ConfigToml` 与 schema helpers 生成（仓库注释建议通过 `just write-config-schema` 更新）。
- 展平键参考（无遗漏 key 列表）：`workdocjcl/spec/01_Configuration/CONFIG_SCHEMA_REFERENCE.md`

复刻建议：
- 直接把 schema 当作“配置契约”，并对 config 做：
  - unknown fields 拒绝（deny_unknown_fields）
  - 类型校验与默认值补齐
  - 生成清晰的错误提示（指出哪一行、哪个键、期望类型）

## 3. 结构概览（高层字段）
`ConfigToml` 的字段非常多，复刻时最重要的高层字段包括：
- `model` / `review_model`
- `model_provider` / `model_providers`
- `model_context_window` / `model_auto_compact_token_limit`
- `approval_policy`
- `sandbox_mode` / `sandbox_workspace_write`
- `notify`
- `instructions` / `developer_instructions`
- `mcp_servers` / `mcp_oauth_*`
- `profiles` / `profile`
- `history`
- `tui`
- `web_search`
- `tools`
- `agents`
- `skills`
- `features`
- `otel` / `analytics` / `feedback`

## 4. 覆盖与优先级（Overrides）
除 config.toml 外，还存在覆盖来源：
- CLI `-c key=value`（可多次）
- feature 相关 legacy flags（保留兼容）
- project-level config（`projects`）与 profile 机制

复刻要求：
- 明确实现“多层配置叠加”的优先级（一般为：CLI overrides > profile/project > base config > defaults）。

## 5. 来源（Source）
- `ConfigToml` 定义：`codex-rs/core/src/config/mod.rs`
- JSON Schema：`codex-rs/core/config.schema.json`
- CLI overrides：`codex-rs/common/src/config_override.rs`
