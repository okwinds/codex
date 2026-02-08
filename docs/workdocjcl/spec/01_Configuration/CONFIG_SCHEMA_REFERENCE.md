# config.toml JSON Schema Reference (Flattened)

- generated_utc: `2026-02-08T10:34:52Z`
- schema_source: `codex-rs/core/config.schema.json`

本文件把 `config.schema.json` 展平为 `dot.path` 形式，作为“无遗漏”配置键参考。

| Key path | Type | Description |
|---|---|---|
| `agents` | `allOf` | Agent-related settings (thread limits, etc.). |
| `agents.max_threads` | `integer` | Maximum number of agent threads that can be open concurrently. When unset, no limit is enforced. |
| `analytics` | `allOf` | When `false`, disables analytics across Codex product surfaces in this machine. Defaults to `true`. |
| `analytics.enabled` | `boolean` | When `false`, disables analytics across Codex product surfaces in this profile. |
| `approval_policy` | `allOf` | Default approval policy for executing commands. |
| `apps` | `allOf` | Settings for app-specific controls. |
| `apps.<key>` | `object` | Config values for a single app/connector. |
| `apps.<key>.disabled_reason` | `allOf` | Reason this app was disabled. |
| `apps.<key>.enabled` | `boolean` | When `false`, Codex does not surface this app. |
| `chatgpt_base_url` | `string` | Base URL for requests to ChatGPT (as opposed to the OpenAI API). |
| `check_for_update_on_startup` | `boolean` | When `true`, checks for Codex updates on startup and surfaces update prompts. Set to `false` only if your Codex updates are centrally managed. Defaults to `true`. |
| `cli_auth_credentials_store` | `allOf` | Preferred backend for storing CLI auth credentials. file (default): Use a file in the Codex home directory. keyring: Use an OS-specific keyring service. auto: Use the keyring if available, otherwise use a file. |
| `compact_prompt` | `string` | Compact prompt used for history compaction. |
| `developer_instructions` | `string` | Developer instructions inserted as a `developer` role message. |
| `disable_paste_burst` | `boolean` | When true, disables burst-paste detection for typed input entirely. All characters are inserted as they are received, and no buffering or placeholder replacement will occur for fast keypress bursts. |
| `experimental_compact_prompt_file` | `string` | A path that is guaranteed to be absolute and normalized (though it is not guaranteed to be canonicalized or exist on the filesystem).  IMPORTANT: When deserializing an `AbsolutePathBuf`, a base path must be set using [AbsolutePathBufGuard::new]. If no base path is set, the deserialization will fail unless the path being deserialized is already absolute. |
| `experimental_use_freeform_apply_patch` | `boolean` |  |
| `experimental_use_unified_exec_tool` | `boolean` |  |
| `features` | `object` | Centralized feature flags (new). Prefer this over individual toggles. |
| `features.apply_patch_freeform` | `boolean` |  |
| `features.apps` | `boolean` |  |
| `features.child_agents_md` | `boolean` |  |
| `features.collab` | `boolean` |  |
| `features.collaboration_modes` | `boolean` |  |
| `features.connectors` | `boolean` |  |
| `features.elevated_windows_sandbox` | `boolean` |  |
| `features.enable_experimental_windows_sandbox` | `boolean` |  |
| `features.enable_request_compression` | `boolean` |  |
| `features.experimental_use_freeform_apply_patch` | `boolean` |  |
| `features.experimental_use_unified_exec_tool` | `boolean` |  |
| `features.experimental_windows_sandbox` | `boolean` |  |
| `features.include_apply_patch_tool` | `boolean` |  |
| `features.memory_tool` | `boolean` |  |
| `features.personality` | `boolean` |  |
| `features.powershell_utf8` | `boolean` |  |
| `features.remote_models` | `boolean` |  |
| `features.request_rule` | `boolean` |  |
| `features.responses_websockets` | `boolean` |  |
| `features.responses_websockets_v2` | `boolean` |  |
| `features.runtime_metrics` | `boolean` |  |
| `features.shell_snapshot` | `boolean` |  |
| `features.shell_tool` | `boolean` |  |
| `features.skill_env_var_dependency_prompt` | `boolean` |  |
| `features.skill_mcp_dependency_install` | `boolean` |  |
| `features.sqlite` | `boolean` |  |
| `features.steer` | `boolean` |  |
| `features.undo` | `boolean` |  |
| `features.unified_exec` | `boolean` |  |
| `features.use_linux_sandbox_bwrap` | `boolean` |  |
| `features.web_search` | `boolean` |  |
| `features.web_search_cached` | `boolean` |  |
| `features.web_search_request` | `boolean` |  |
| `feedback` | `allOf` | When `false`, disables feedback collection across Codex product surfaces. Defaults to `true`. |
| `feedback.enabled` | `boolean` | When `false`, disables the feedback flow across Codex product surfaces. |
| `file_opener` | `allOf` | Optional URI-based file opener. If set, citations to files in the model output will be hyperlinked using the specified URI scheme. |
| `forced_chatgpt_workspace_id` | `string` | When set, restricts ChatGPT login to a specific workspace identifier. |
| `forced_login_method` | `allOf` | When set, restricts the login mechanism users may use. |
| `ghost_snapshot` | `allOf` | Settings for ghost snapshots (used for undo). |
| `ghost_snapshot.disable_warnings` | `boolean` | Disable all ghost snapshot warning events. |
| `ghost_snapshot.ignore_large_untracked_dirs` | `integer` | Ignore untracked directories that contain this many files or more. (Still emits a warning unless warnings are disabled.) |
| `ghost_snapshot.ignore_large_untracked_files` | `integer` | Exclude untracked files larger than this many bytes from ghost snapshots. |
| `hide_agent_reasoning` | `boolean` | When set to `true`, `AgentReasoning` events will be hidden from the UI/output. Defaults to `false`. |
| `history` | `allOf` | Settings that govern if and what will be written to `~/.codex/history.jsonl`. |
| `history.max_bytes` | `integer` | If set, the maximum size of the history file in bytes. The oldest entries are dropped once the file exceeds this limit. |
| `history.persistence` | `allOf` | If true, history entries will not be written to disk. |
| `instructions` | `string` | System instructions. |
| `log_dir` | `allOf` | Directory where Codex writes log files, for example `codex-tui.log`. Defaults to `$CODEX_HOME/log`. |
| `mcp_oauth_callback_port` | `integer` | Optional fixed port for the local HTTP callback server used during MCP OAuth login. When unset, Codex will bind to an ephemeral port chosen by the OS. |
| `mcp_oauth_credentials_store` | `allOf` | Preferred backend for storing MCP OAuth credentials. keyring: Use an OS-specific keyring service. https://github.com/openai/codex/blob/main/codex-rs/rmcp-client/src/oauth.rs#L2 file: Use a file in the Codex home directory. auto (default): Use the OS-specific keyring service if available, otherwise use a file. |
| `mcp_servers` | `object` | Definition for MCP servers that Codex can reach out to for tool calls. |
| `mcp_servers.<key>` | `object` |  |
| `mcp_servers.<key>.args` | `array` |  |
| `mcp_servers.<key>.args[]` | `string` |  |
| `mcp_servers.<key>.bearer_token` | `string` |  |
| `mcp_servers.<key>.bearer_token_env_var` | `string` |  |
| `mcp_servers.<key>.command` | `string` |  |
| `mcp_servers.<key>.cwd` | `string` |  |
| `mcp_servers.<key>.disabled_tools` | `array` |  |
| `mcp_servers.<key>.disabled_tools[]` | `string` |  |
| `mcp_servers.<key>.enabled` | `boolean` |  |
| `mcp_servers.<key>.enabled_tools` | `array` |  |
| `mcp_servers.<key>.enabled_tools[]` | `string` |  |
| `mcp_servers.<key>.env` | `object` |  |
| `mcp_servers.<key>.env.<key>` | `string` |  |
| `mcp_servers.<key>.env_http_headers` | `object` |  |
| `mcp_servers.<key>.env_http_headers.<key>` | `string` |  |
| `mcp_servers.<key>.env_vars` | `array` |  |
| `mcp_servers.<key>.env_vars[]` | `string` |  |
| `mcp_servers.<key>.http_headers` | `object` |  |
| `mcp_servers.<key>.http_headers.<key>` | `string` |  |
| `mcp_servers.<key>.required` | `boolean` |  |
| `mcp_servers.<key>.scopes` | `array` |  |
| `mcp_servers.<key>.scopes[]` | `string` |  |
| `mcp_servers.<key>.startup_timeout_ms` | `integer` |  |
| `mcp_servers.<key>.startup_timeout_sec` | `number` |  |
| `mcp_servers.<key>.tool_timeout_sec` | `number` |  |
| `mcp_servers.<key>.url` | `string` |  |
| `model` | `string` | Optional override of model selection. |
| `model_auto_compact_token_limit` | `integer` | Token usage threshold triggering auto-compaction of conversation history. |
| `model_context_window` | `integer` | Size of the context window for the model, in tokens. |
| `model_instructions_file` | `allOf` | Optional path to a file containing model instructions that will override the built-in instructions for the selected model. Users are STRONGLY DISCOURAGED from using this field, as deviating from the instructions sanctioned by Codex will likely degrade model performance. |
| `model_provider` | `string` | Provider to use from the model_providers map. |
| `model_providers` | `object` | User-defined provider entries that extend/override the built-in list. |
| `model_providers.<key>` | `object` | Serializable representation of a provider definition. |
| `model_providers.<key>.base_url` | `string` | Base URL for the provider's OpenAI-compatible API. |
| `model_providers.<key>.env_http_headers` | `object` | Optional HTTP headers to include in requests to this provider where the (key, value) pairs are the header name and _environment variable_ whose value should be used. If the environment variable is not set, or the value is empty, the header will not be included in the request. |
| `model_providers.<key>.env_http_headers.<key>` | `string` |  |
| `model_providers.<key>.env_key` | `string` | Environment variable that stores the user's API key for this provider. |
| `model_providers.<key>.env_key_instructions` | `string` | Optional instructions to help the user get a valid value for the variable and set it. |
| `model_providers.<key>.experimental_bearer_token` | `string` | Value to use with `Authorization: Bearer <token>` header. Use of this config is discouraged in favor of `env_key` for security reasons, but this may be necessary when using this programmatically. |
| `model_providers.<key>.http_headers` | `object` | Additional HTTP headers to include in requests to this provider where the (key, value) pairs are the header name and value. |
| `model_providers.<key>.http_headers.<key>` | `string` |  |
| `model_providers.<key>.name` | `string` | Friendly display name. |
| `model_providers.<key>.query_params` | `object` | Optional query parameters to append to the base URL. |
| `model_providers.<key>.query_params.<key>` | `string` |  |
| `model_providers.<key>.request_max_retries` | `integer` | Maximum number of times to retry a failed HTTP request to this provider. |
| `model_providers.<key>.requires_openai_auth` | `boolean` | Does this provider require an OpenAI API Key or ChatGPT login token? If true, user is presented with login screen on first run, and login preference and token/key are stored in auth.json. If false (which is the default), login screen is skipped, and API key (if needed) comes from the "env_key" environment variable. |
| `model_providers.<key>.stream_idle_timeout_ms` | `integer` | Idle timeout (in milliseconds) to wait for activity on a streaming response before treating the connection as lost. |
| `model_providers.<key>.stream_max_retries` | `integer` | Number of times to retry reconnecting a dropped streaming response before failing. |
| `model_providers.<key>.supports_websockets` | `boolean` | Whether this provider supports the Responses API WebSocket transport. |
| `model_providers.<key>.wire_api` | `allOf` | Which wire protocol this provider expects. |
| `model_reasoning_effort` | `string` | See https://platform.openai.com/docs/guides/reasoning?api-mode=responses#get-started-with-reasoning |
| `model_reasoning_summary` | `oneOf` | A summary of the reasoning performed by the model. This can be useful for debugging and understanding the model's reasoning process. See https://platform.openai.com/docs/guides/reasoning?api-mode=responses#reasoning-summaries |
| `model_supports_reasoning_summaries` | `boolean` | Override to force-enable reasoning summaries for the configured model. |
| `model_verbosity` | `allOf` | Optional verbosity control for GPT-5 models (Responses API `text.verbosity`). |
| `notice` | `allOf` | Collection of in-product notices (different from notifications) See [`crate::config::types::Notices`] for more details |
| `notice.hide_full_access_warning` | `boolean` | Tracks whether the user has acknowledged the full access warning prompt. |
| `notice.hide_gpt-5.1-codex-max_migration_prompt` | `boolean` | Tracks whether the user has seen the gpt-5.1-codex-max migration prompt |
| `notice.hide_gpt5_1_migration_prompt` | `boolean` | Tracks whether the user has seen the model migration prompt |
| `notice.hide_rate_limit_model_nudge` | `boolean` | Tracks whether the user opted out of the rate limit model switch reminder. |
| `notice.hide_world_writable_warning` | `boolean` | Tracks whether the user has acknowledged the Windows world-writable directories warning. |
| `notice.model_migrations` | `object` | Tracks acknowledged model migrations as old->new model slug mappings. |
| `notice.model_migrations.<key>` | `string` |  |
| `notify` | `array` | Optional external command to spawn for end-user notifications. |
| `notify[]` | `string` |  |
| `oss_provider` | `string` | Preferred OSS provider for local models, e.g. "lmstudio" or "ollama". |
| `otel` | `allOf` | OTEL configuration. |
| `otel.environment` | `string` | Mark traces with environment (dev, staging, prod, test). Defaults to dev. |
| `otel.exporter` | `allOf` | Optional log exporter |
| `otel.exporter.otlp-grpc` | `object` |  |
| `otel.exporter.otlp-grpc.endpoint` | `string` |  |
| `otel.exporter.otlp-grpc.headers` | `object` |  |
| `otel.exporter.otlp-grpc.headers.<key>` | `string` |  |
| `otel.exporter.otlp-grpc.tls` | `allOf` |  |
| `otel.exporter.otlp-grpc.tls.ca-certificate` | `string` | A path that is guaranteed to be absolute and normalized (though it is not guaranteed to be canonicalized or exist on the filesystem).  IMPORTANT: When deserializing an `AbsolutePathBuf`, a base path must be set using [AbsolutePathBufGuard::new]. If no base path is set, the deserialization will fail unless the path being deserialized is already absolute. |
| `otel.exporter.otlp-grpc.tls.client-certificate` | `string` | A path that is guaranteed to be absolute and normalized (though it is not guaranteed to be canonicalized or exist on the filesystem).  IMPORTANT: When deserializing an `AbsolutePathBuf`, a base path must be set using [AbsolutePathBufGuard::new]. If no base path is set, the deserialization will fail unless the path being deserialized is already absolute. |
| `otel.exporter.otlp-grpc.tls.client-private-key` | `string` | A path that is guaranteed to be absolute and normalized (though it is not guaranteed to be canonicalized or exist on the filesystem).  IMPORTANT: When deserializing an `AbsolutePathBuf`, a base path must be set using [AbsolutePathBufGuard::new]. If no base path is set, the deserialization will fail unless the path being deserialized is already absolute. |
| `otel.exporter.otlp-http` | `object` |  |
| `otel.exporter.otlp-http.endpoint` | `string` |  |
| `otel.exporter.otlp-http.headers` | `object` |  |
| `otel.exporter.otlp-http.headers.<key>` | `string` |  |
| `otel.exporter.otlp-http.protocol` | `oneOf` |  |
| `otel.exporter.otlp-http.tls` | `allOf` |  |
| `otel.exporter.otlp-http.tls.ca-certificate` | `string` | A path that is guaranteed to be absolute and normalized (though it is not guaranteed to be canonicalized or exist on the filesystem).  IMPORTANT: When deserializing an `AbsolutePathBuf`, a base path must be set using [AbsolutePathBufGuard::new]. If no base path is set, the deserialization will fail unless the path being deserialized is already absolute. |
| `otel.exporter.otlp-http.tls.client-certificate` | `string` | A path that is guaranteed to be absolute and normalized (though it is not guaranteed to be canonicalized or exist on the filesystem).  IMPORTANT: When deserializing an `AbsolutePathBuf`, a base path must be set using [AbsolutePathBufGuard::new]. If no base path is set, the deserialization will fail unless the path being deserialized is already absolute. |
| `otel.exporter.otlp-http.tls.client-private-key` | `string` | A path that is guaranteed to be absolute and normalized (though it is not guaranteed to be canonicalized or exist on the filesystem).  IMPORTANT: When deserializing an `AbsolutePathBuf`, a base path must be set using [AbsolutePathBufGuard::new]. If no base path is set, the deserialization will fail unless the path being deserialized is already absolute. |
| `otel.log_user_prompt` | `boolean` | Log user prompt in traces |
| `otel.trace_exporter` | `allOf` | Optional trace exporter |
| `otel.trace_exporter.otlp-grpc` | `object` |  |
| `otel.trace_exporter.otlp-grpc.endpoint` | `string` |  |
| `otel.trace_exporter.otlp-grpc.headers` | `object` |  |
| `otel.trace_exporter.otlp-grpc.headers.<key>` | `string` |  |
| `otel.trace_exporter.otlp-grpc.tls` | `allOf` |  |
| `otel.trace_exporter.otlp-grpc.tls.ca-certificate` | `string` | A path that is guaranteed to be absolute and normalized (though it is not guaranteed to be canonicalized or exist on the filesystem).  IMPORTANT: When deserializing an `AbsolutePathBuf`, a base path must be set using [AbsolutePathBufGuard::new]. If no base path is set, the deserialization will fail unless the path being deserialized is already absolute. |
| `otel.trace_exporter.otlp-grpc.tls.client-certificate` | `string` | A path that is guaranteed to be absolute and normalized (though it is not guaranteed to be canonicalized or exist on the filesystem).  IMPORTANT: When deserializing an `AbsolutePathBuf`, a base path must be set using [AbsolutePathBufGuard::new]. If no base path is set, the deserialization will fail unless the path being deserialized is already absolute. |
| `otel.trace_exporter.otlp-grpc.tls.client-private-key` | `string` | A path that is guaranteed to be absolute and normalized (though it is not guaranteed to be canonicalized or exist on the filesystem).  IMPORTANT: When deserializing an `AbsolutePathBuf`, a base path must be set using [AbsolutePathBufGuard::new]. If no base path is set, the deserialization will fail unless the path being deserialized is already absolute. |
| `otel.trace_exporter.otlp-http` | `object` |  |
| `otel.trace_exporter.otlp-http.endpoint` | `string` |  |
| `otel.trace_exporter.otlp-http.headers` | `object` |  |
| `otel.trace_exporter.otlp-http.headers.<key>` | `string` |  |
| `otel.trace_exporter.otlp-http.protocol` | `oneOf` |  |
| `otel.trace_exporter.otlp-http.tls` | `allOf` |  |
| `otel.trace_exporter.otlp-http.tls.ca-certificate` | `string` | A path that is guaranteed to be absolute and normalized (though it is not guaranteed to be canonicalized or exist on the filesystem).  IMPORTANT: When deserializing an `AbsolutePathBuf`, a base path must be set using [AbsolutePathBufGuard::new]. If no base path is set, the deserialization will fail unless the path being deserialized is already absolute. |
| `otel.trace_exporter.otlp-http.tls.client-certificate` | `string` | A path that is guaranteed to be absolute and normalized (though it is not guaranteed to be canonicalized or exist on the filesystem).  IMPORTANT: When deserializing an `AbsolutePathBuf`, a base path must be set using [AbsolutePathBufGuard::new]. If no base path is set, the deserialization will fail unless the path being deserialized is already absolute. |
| `otel.trace_exporter.otlp-http.tls.client-private-key` | `string` | A path that is guaranteed to be absolute and normalized (though it is not guaranteed to be canonicalized or exist on the filesystem).  IMPORTANT: When deserializing an `AbsolutePathBuf`, a base path must be set using [AbsolutePathBufGuard::new]. If no base path is set, the deserialization will fail unless the path being deserialized is already absolute. |
| `personality` | `allOf` | Optionally specify a personality for the model |
| `profile` | `string` | Profile to use from the `profiles` map. |
| `profiles` | `object` | Named profiles to facilitate switching between different configurations. |
| `profiles.<key>` | `object` | Collection of common configuration options that a user can define as a unit in `config.toml`. |
| `profiles.<key>.analytics` | `object` | Analytics settings loaded from config.toml. Fields are optional so we can apply defaults. |
| `profiles.<key>.analytics.enabled` | `boolean` | When `false`, disables analytics across Codex product surfaces in this profile. |
| `profiles.<key>.approval_policy` | `oneOf` | Determines the conditions under which the user is consulted to approve running the command proposed by Codex. |
| `profiles.<key>.chatgpt_base_url` | `string` |  |
| `profiles.<key>.experimental_compact_prompt_file` | `string` | A path that is guaranteed to be absolute and normalized (though it is not guaranteed to be canonicalized or exist on the filesystem).  IMPORTANT: When deserializing an `AbsolutePathBuf`, a base path must be set using [AbsolutePathBufGuard::new]. If no base path is set, the deserialization will fail unless the path being deserialized is already absolute. |
| `profiles.<key>.experimental_use_freeform_apply_patch` | `boolean` |  |
| `profiles.<key>.experimental_use_unified_exec_tool` | `boolean` |  |
| `profiles.<key>.features` | `object` | Optional feature toggles scoped to this profile. |
| `profiles.<key>.features.apply_patch_freeform` | `boolean` |  |
| `profiles.<key>.features.apps` | `boolean` |  |
| `profiles.<key>.features.child_agents_md` | `boolean` |  |
| `profiles.<key>.features.collab` | `boolean` |  |
| `profiles.<key>.features.collaboration_modes` | `boolean` |  |
| `profiles.<key>.features.connectors` | `boolean` |  |
| `profiles.<key>.features.elevated_windows_sandbox` | `boolean` |  |
| `profiles.<key>.features.enable_experimental_windows_sandbox` | `boolean` |  |
| `profiles.<key>.features.enable_request_compression` | `boolean` |  |
| `profiles.<key>.features.experimental_use_freeform_apply_patch` | `boolean` |  |
| `profiles.<key>.features.experimental_use_unified_exec_tool` | `boolean` |  |
| `profiles.<key>.features.experimental_windows_sandbox` | `boolean` |  |
| `profiles.<key>.features.include_apply_patch_tool` | `boolean` |  |
| `profiles.<key>.features.memory_tool` | `boolean` |  |
| `profiles.<key>.features.personality` | `boolean` |  |
| `profiles.<key>.features.powershell_utf8` | `boolean` |  |
| `profiles.<key>.features.remote_models` | `boolean` |  |
| `profiles.<key>.features.request_rule` | `boolean` |  |
| `profiles.<key>.features.responses_websockets` | `boolean` |  |
| `profiles.<key>.features.responses_websockets_v2` | `boolean` |  |
| `profiles.<key>.features.runtime_metrics` | `boolean` |  |
| `profiles.<key>.features.shell_snapshot` | `boolean` |  |
| `profiles.<key>.features.shell_tool` | `boolean` |  |
| `profiles.<key>.features.skill_env_var_dependency_prompt` | `boolean` |  |
| `profiles.<key>.features.skill_mcp_dependency_install` | `boolean` |  |
| `profiles.<key>.features.sqlite` | `boolean` |  |
| `profiles.<key>.features.steer` | `boolean` |  |
| `profiles.<key>.features.undo` | `boolean` |  |
| `profiles.<key>.features.unified_exec` | `boolean` |  |
| `profiles.<key>.features.use_linux_sandbox_bwrap` | `boolean` |  |
| `profiles.<key>.features.web_search` | `boolean` |  |
| `profiles.<key>.features.web_search_cached` | `boolean` |  |
| `profiles.<key>.features.web_search_request` | `boolean` |  |
| `profiles.<key>.include_apply_patch_tool` | `boolean` |  |
| `profiles.<key>.model` | `string` |  |
| `profiles.<key>.model_instructions_file` | `allOf` | Optional path to a file containing model instructions. |
| `profiles.<key>.model_provider` | `string` | The key in the `model_providers` map identifying the [`ModelProviderInfo`] to use. |
| `profiles.<key>.model_reasoning_effort` | `string` | See https://platform.openai.com/docs/guides/reasoning?api-mode=responses#get-started-with-reasoning |
| `profiles.<key>.model_reasoning_summary` | `oneOf` | A summary of the reasoning performed by the model. This can be useful for debugging and understanding the model's reasoning process. See https://platform.openai.com/docs/guides/reasoning?api-mode=responses#reasoning-summaries |
| `profiles.<key>.model_verbosity` | `string` | Controls output length/detail on GPT-5 models via the Responses API. Serialized with lowercase values to match the OpenAI API. |
| `profiles.<key>.oss_provider` | `string` |  |
| `profiles.<key>.personality` | `string` |  |
| `profiles.<key>.sandbox_mode` | `string` |  |
| `profiles.<key>.tools_view_image` | `boolean` |  |
| `profiles.<key>.tools_web_search` | `boolean` |  |
| `profiles.<key>.web_search` | `string` |  |
| `project_doc_fallback_filenames` | `array` | Ordered list of fallback filenames to look for when AGENTS.md is missing. |
| `project_doc_fallback_filenames[]` | `string` |  |
| `project_doc_max_bytes` | `integer` | Maximum number of bytes to include from an AGENTS.md project doc file. |
| `project_root_markers` | `array` | Markers used to detect the project root when searching parent directories for `.codex` folders. Defaults to [".git"] when unset. |
| `project_root_markers[]` | `string` |  |
| `projects` | `object` |  |
| `projects.<key>` | `object` |  |
| `projects.<key>.trust_level` | `string` | Represents the trust level for a project directory. This determines the approval policy and sandbox mode applied. |
| `review_model` | `string` | Review model override used by the `/review` feature. |
| `sandbox_mode` | `allOf` | Sandbox mode to use. |
| `sandbox_workspace_write` | `allOf` | Sandbox configuration to apply if `sandbox` is `WorkspaceWrite`. |
| `sandbox_workspace_write.exclude_slash_tmp` | `boolean` |  |
| `sandbox_workspace_write.exclude_tmpdir_env_var` | `boolean` |  |
| `sandbox_workspace_write.network_access` | `boolean` |  |
| `sandbox_workspace_write.writable_roots` | `array` |  |
| `sandbox_workspace_write.writable_roots[]` | `string` | A path that is guaranteed to be absolute and normalized (though it is not guaranteed to be canonicalized or exist on the filesystem).  IMPORTANT: When deserializing an `AbsolutePathBuf`, a base path must be set using [AbsolutePathBufGuard::new]. If no base path is set, the deserialization will fail unless the path being deserialized is already absolute. |
| `shell_environment_policy` | `allOf` |  |
| `shell_environment_policy.exclude` | `array` | List of regular expressions. |
| `shell_environment_policy.exclude[]` | `string` |  |
| `shell_environment_policy.experimental_use_profile` | `boolean` |  |
| `shell_environment_policy.ignore_default_excludes` | `boolean` |  |
| `shell_environment_policy.include_only` | `array` | List of regular expressions. |
| `shell_environment_policy.include_only[]` | `string` |  |
| `shell_environment_policy.inherit` | `oneOf` |  |
| `shell_environment_policy.set` | `object` |  |
| `shell_environment_policy.set.<key>` | `string` |  |
| `show_raw_agent_reasoning` | `boolean` | When set to `true`, `AgentReasoningRawContentEvent` events will be shown in the UI/output. Defaults to `false`. |
| `skills` | `allOf` | User-level skill config entries keyed by SKILL.md path. |
| `skills.config` | `array` |  |
| `skills.config[]` | `object` |  |
| `skills.config[].enabled` | `boolean` |  |
| `skills.config[].path` | `string` | A path that is guaranteed to be absolute and normalized (though it is not guaranteed to be canonicalized or exist on the filesystem).  IMPORTANT: When deserializing an `AbsolutePathBuf`, a base path must be set using [AbsolutePathBufGuard::new]. If no base path is set, the deserialization will fail unless the path being deserialized is already absolute. |
| `suppress_unstable_features_warning` | `boolean` | Suppress warnings about unstable (under development) features. |
| `tool_output_token_limit` | `integer` | Token budget applied when storing tool/function outputs in the context manager. |
| `tools` | `allOf` | Nested tools section for feature toggles |
| `tools.view_image` | `boolean` | Enable the `view_image` tool that lets the agent attach local images. |
| `tools.web_search` | `boolean` |  |
| `tui` | `allOf` | Collection of settings that are specific to the TUI. |
| `tui.alternate_screen` | `allOf` | Controls whether the TUI uses the terminal's alternate screen buffer.  - `auto` (default): Disable alternate screen in Zellij, enable elsewhere. - `always`: Always use alternate screen (original behavior). - `never`: Never use alternate screen (inline mode only, preserves scrollback).  Using alternate screen provides a cleaner fullscreen experience but prevents scrollback in terminal multiplexers like Zellij that follow the xterm spec. |
| `tui.animations` | `boolean` | Enable animations (welcome screen, shimmer effects, spinners). Defaults to `true`. |
| `tui.experimental_mode` | `allOf` | Start the TUI in the specified collaboration mode (plan/default). Defaults to unset. |
| `tui.notification_method` | `allOf` | Notification method to use for unfocused terminal notifications. Defaults to `auto`. |
| `tui.notifications` | `allOf` | Enable desktop notifications from the TUI when the terminal is unfocused. Defaults to `true`. |
| `tui.notifications[]` | `string` |  |
| `tui.show_tooltips` | `boolean` | Show startup tooltips in the TUI welcome screen. Defaults to `true`. |
| `tui.status_line` | `array` | Ordered list of status line item identifiers.  When set, the TUI renders the selected items as the status line. |
| `tui.status_line[]` | `string` |  |
| `web_search` | `allOf` | Controls the web search tool mode: disabled, cached, or live. |
| `windows_wsl_setup_acknowledged` | `boolean` | Tracks whether the Windows onboarding screen has been acknowledged. |
