# 认证（Authentication）

Codex CLI 的“认证”主要是为了：
- 获取与模型服务（OpenAI/ChatGPT 等）交互所需的凭据（API key / OAuth tokens）。
- 把凭据安全地存储在本机（文件或 keyring），供后续会话复用。

> 注意：这不是“服务端鉴权”。Codex CLI 是客户端，因此这里的 auth 是“客户端凭据管理”。

## 1. 支持的登录方式（Auth Methods）

### 1.1 ChatGPT 登录（browser login server）
- 子命令：`codex login`（默认倾向此路径，具体由环境与 feature 决定）
- 行为：
  1) 在本机启动 login server（`http://localhost:<port>`）
  2) 打开浏览器到 auth URL（用户完成授权）
  3) server 收到回调后将凭据写入 `CODEX_HOME`（或 keyring）
  4) CLI 输出 “Successfully logged in”

### 1.2 Device code flow（适合 headless）
- 子命令：`codex login --device-code`（或内部 fallback 逻辑触发）
- 行为：
  1) 请求 device code（issuer/client_id 可被覆盖）
  2) 用户在外部浏览器输入 code 完成授权
  3) 写入凭据存储

### 1.3 API key 登录（从 stdin 读取，避免落盘/历史泄露）
- 子命令：`codex login --with-api-key`
- 输入：API key 必须从 stdin 读取（若 stdin 是 TTY 会直接报错退出）
- 推荐用法：
```bash
printenv OPENAI_API_KEY | codex login --with-api-key
```

### 1.4 禁用/强制登录方式（forced_login_method）
配置项：`ConfigToml.forced_login_method`
- `Api`：禁用 ChatGPT 登录，只允许 API key
- `Chatgpt`：禁用 API key 登录，只允许 ChatGPT

## 2. 凭据存储（Credentials Store）

### 2.1 存储后端选择
配置项：`ConfigToml.cli_auth_credentials_store`
- `file`（默认）：写入 `CODEX_HOME` 下的文件
- `keyring`：使用 OS keyring
- `auto`：优先 keyring，否则 file

### 2.2 MCP OAuth 凭据存储
配置项：`ConfigToml.mcp_oauth_credentials_store`
- 同样支持 `auto/keyring/file`（但语义为 MCP OAuth 凭据）

## 3. 认证状态查询与登出

### 3.1 状态查询
- 子命令：`codex login status`
- 输出：是否已登录以及登录类型（API key 或 ChatGPT）

### 3.2 登出
- 子命令：`codex logout`
- 行为：删除/清理已保存的凭据

## 4. Token/凭据结构（复刻约束）
本仓库对 token 的具体 JSON 结构依赖上游服务与 login crate 的实现，可能随时间演进；复刻时应把它当作“opaque token”，保证以下行为一致：
- 能被正确注入到模型请求中（Authorization header 或 provider-specific headers/params）
- 能按存储后端正确保存/读取/删除
- 不在不必要的输出/日志中泄露（尤其 API key）

## 5. 来源（Source）
- CLI 层登录逻辑：`codex-rs/cli/src/login.rs`
- login server / device code：`codex-rs/login/`
- API key 常量与读取：`codex-rs/core/src/auth.rs`
- 配置项（存储后端等）：`codex-rs/core/src/config/mod.rs`（`ConfigToml`）
