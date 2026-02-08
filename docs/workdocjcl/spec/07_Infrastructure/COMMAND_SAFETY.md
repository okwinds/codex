# Command Safety Heuristics（已知安全/危险命令启发式）复刻级规格

本章目标：完整复刻 Codex CLI 在“未命中 execpolicy 规则时”的两类启发式判定：
- **已知安全**：`is_known_safe_command(...)`（允许自动执行）
- **可能危险**：`command_might_be_dangerous(...)`（触发审批/禁止的强信号）

这些启发式被 `render_decision_for_unmatched_command(...)` 直接使用（参见 `docs/workdocjcl/spec/07_Infrastructure/EXEC_POLICY.md` §3）。

---

## 1. 已知安全：`is_known_safe_command(command: &[String]) -> bool`

### 1.1 总体算法（必须按顺序）
实现文件：`codex-rs/core/src/command_safety/is_safe_command.rs`

步骤：
1. 预处理：将 token `"zsh"` 统一替换为 `"bash"`（其余 token 原样保留）。
   - 目的：让 zsh 与 bash 的安全判定规则一致（至少在该启发式层面）。
2. Windows 特判：
   - 若 `is_safe_command_windows(&command)` 返回 true，则整体返回 true。
3. 非 shell 脚本形式：
   - 若 `is_safe_to_call_with_exec(&command)` 返回 true，则整体返回 true。
4. shell `-lc` 脚本形式（严格子集）：
   - 若 `parse_shell_lc_plain_commands(&command)` 成功返回 `all_commands`：
     - 要求 `all_commands` 非空
     - 且 `all_commands` 中每个 inner 命令 `cmd_i` 都满足 `is_safe_to_call_with_exec(cmd_i)`
     - 才返回 true
5. 否则返回 false

关键点：
- `bash -lc "..."` **只有在脚本可被解析为“word-only command sequence”且每条内命令本身已知安全**时，才会被认定为安全。
- 任意不支持的 shell 结构（变量展开、重定向、subshell、命令替换等）都会导致 `parse_shell_lc_plain_commands` 返回 None，从而整条命令不被视为已知安全。

`parse_shell_lc_plain_commands` 的可解析子集见：`docs/workdocjcl/spec/07_Infrastructure/EXEC_POLICY.md` §4。

---

## 2. 已知安全子集：`is_safe_to_call_with_exec(command: &[String]) -> bool`

实现文件：`codex-rs/core/src/command_safety/is_safe_command.rs`

总体规则：`cmd0` 取 `Path::new(cmd0).file_name()`；无法取到 file name 则返回 false。

### 2.1 Linux-only 允许项
当 `cfg!(target_os = "linux")` 时：
- `numfmt`：允许
- `tac`：允许

其它 OS：这两者一律不安全（返回 false）。

### 2.2 “无副作用/只读”命令白名单（直接允许）
以下命令名直接返回 true（不进一步检查 flags）：

`cat`, `cd`, `cut`, `echo`, `expr`, `false`, `grep`, `head`, `id`, `ls`, `nl`, `paste`, `pwd`, `rev`, `seq`, `stat`, `tail`, `tr`, `true`, `uname`, `uniq`, `wc`, `which`, `whoami`

> 注意：这只是启发式白名单；真实执行仍受 sandbox/execpolicy 影响。

### 2.3 `base64`：输出到文件的选项一律不安全
允许条件：
- 命令名为 `base64`
- 且参数中不存在以下形式（任一出现即不安全）：
  - `-o`（并且会把 `-ob64.txt` 这种“短选项+内联 value”也视为不安全）
  - `--output`
  - `--output=<...>`

实现策略（判定为不安全的条件）：
- 任一 arg 满足：
  - `arg == "-o"` 或 `arg == "--output"`
  - 或 `arg.starts_with("--output=")`
  - 或 (`arg.starts_with("-o")` 且 `arg != "-o"`)

### 2.4 `find`：包含可执行/删除/写文件类 option 一律不安全
`find` 允许条件：
- 参数中 **不包含** 以下任何 option（出现即不安全）：
  - `-exec`, `-execdir`, `-ok`, `-okdir`（执行任意命令）
  - `-delete`（删除文件）
  - `-fls`, `-fprint`, `-fprint0`, `-fprintf`（写入文件）

### 2.5 `rg`（ripgrep）：禁止会调用外部命令/解压工具的选项
`rg` 允许条件：
- 参数中不出现：
  - 无参数危险 flag：`--search-zip`、`-z`
  - 需要参数的危险 flag（split 与 `=` 形式都算危险）：
    - `--pre` / `--pre=<...>`
    - `--hostname-bin` / `--hostname-bin=<...>`

实现策略：
- 若 arg 在 `UNSAFE_RIPGREP_OPTIONS_WITHOUT_ARGS` 直接拒绝
- 若 arg 等于某 `opt` 或 `arg.starts_with("{opt}=")` 则拒绝

### 2.6 `git`：仅允许明确只读的子命令与安全 flags

#### 2.6.1 全局 config override 一律不安全
如果命令 token 中出现以下任一形式，则不安全（直接返回 false）：
- `-c` 或 `--config-env`
- 或 `-c<...>`（`-c` 内联）
- 或 `--config-env=<...>`

原因：这些选项可能强制 git 执行外部 pager/工具。

#### 2.6.2 子命令发现（避免 global option 绕过）
安全判定共享 `find_git_subcommand`（实现在 `is_dangerous_command.rs`，见 §3.2）：
- 在 `git` 后扫描 token，跳过已知 global options（例如 `-C`, `-c`, `--git-dir` 等及其参数）
- 第一个非 option token 视为 subcommand；若不是期望列表中的 subcommand，则立即返回 None（避免把后续 positional args 误判为 subcommand）

#### 2.6.3 允许的 git subcommands
仅允许以下子命令：
- `status`
- `log`
- `diff`
- `show`
- `branch`（但必须是只读查询，见下一小节）

其余一律不安全（例如 `git fetch`、`git checkout` 等）。

#### 2.6.4 子命令参数“只读”判定（禁止写文件/执行外部工具）
对于 `status|log|diff|show|branch` 这些子命令：
- 若 args 中出现以下任一 flag（含 `=` 形式），则不安全：
  - `--output` / `--output=<...>`
  - `--ext-diff`
  - `--textconv`
  - `--exec` / `--exec=<...>`
  - `--paginate`

#### 2.6.5 `git branch` 额外只读判定
`git branch` 被视为安全仅当满足：
1. 参数为空（列分支） → 安全
2. 或参数全部来自“只读 flags 集合”，且至少出现过一个只读 flag

只读 flags（出现任一则 `saw_read_only_flag = true`）：
- `--list`, `-l`
- `--show-current`
- `-a`, `--all`
- `-r`, `--remotes`
- `-v`, `-vv`, `--verbose`
- `--format=<...>`

任何其它 flag 或 positional arg（例如 `new-branch`、`-d`, `-D`）一律不安全。

### 2.7 `sed`：仅允许 `sed -n {N|M,N}p` 的 3/4 token 形式
特殊允许条件：
- `command.len() <= 4`
- `command[1] == "-n"`
- `command[2]` 满足正则：`^(\d+,)?\d+p$`
  - 例：`1,5p` 或 `10p`
- 这类命令常用于“只读打印行范围”

其它 `sed` 使用方式一律不安全（例如 `sed -i`、或 `-n xp`）。

---

## 3. 可能危险：`command_might_be_dangerous(command: &[String]) -> bool`

实现文件：`codex-rs/core/src/command_safety/is_dangerous_command.rs`

### 3.1 总体算法
1. Windows 特判（仅在 windows 编译目标下）：
   - 若 `is_dangerous_command_windows(command)` 为 true → true
2. 若 `is_dangerous_to_call_with_exec(command)` 为 true → true
3. 若 `parse_shell_lc_plain_commands(command)` 返回 `all_commands`，并且其中任意 inner 命令 `cmd_i` 满足 `is_dangerous_to_call_with_exec(cmd_i)` → true
4. 否则 false

关键点：
- 危险判定同样支持 `bash -lc "..."` 的“可拆解子集”；只要脚本内任何一条 inner 命令危险，则整体危险。

### 3.2 `find_git_subcommand`（安全/危险共享）
`find_git_subcommand(command, subcommands)`：
- 仅当 `cmd0.ends_with("git")` 才考虑（支持 `/usr/bin/git` 等）
- 从第 2 个 token 开始扫描：
  - 跳过：
    - inline-value global options（如 `--git-dir=<...>`, `-C<...>`, `-c<...>` 等）
    - value-taking global options（如 `-C <path>`, `--git-dir <path>`），并跳过其后一个 token
    - `--` 与其它 `-` 开头选项
  - 遇到第一个“非 option token”：
    - 如果在 `subcommands` 列表中：返回 `(idx, token)`
    - 否则：立即返回 None（不要继续扫描；避免误判 branch name 等）

### 3.3 `is_dangerous_to_call_with_exec`：危险命令集合
危险判定目前只覆盖以下几类：

#### 3.3.1 `git` 的危险子命令
当 `cmd0.ends_with("git")`：
- 若子命令是：
  - `reset` → 危险
  - `rm` → 危险
  - `branch` → 仅当“删除分支”语义（见下一条）才危险
  - `push` → 仅当包含 force/delete/dangerous refspec（见下一条）才危险
  - `clean` → 仅当包含 force（见下一条）才危险

##### a) `git branch` 删除分支判定
危险条件：branch args 中任意 token 满足：
- `-d` / `-D` / `--delete`
- 或 `--delete=<...>`
- 或短 flag group 包含 `d` 或 `D`（例如 `-dv`, `-vD`, `-Dvv`）

##### b) `git push` 危险判定
危险条件：push args 中任意 token 满足：
- force / delete flags：
  - `--force`, `--force-with-lease`, `--force-if-includes`, `--delete`
  - `-f`, `-d`
  - 以及 `--force-with-lease=<...>`, `--force-if-includes=<...>`, `--delete=<...>`
  - 或短 flag group 包含 `f` 或 `d`（例如 `-fdx`）
- 危险 refspec：
  - 以 `+` 开头且长度>1（强制更新）
  - 或以 `:` 开头且长度>1（删除远程 ref）

##### c) `git clean` force 判定
危险条件：clean args 中任意 token 满足：
- `--force` 或 `-f`
- 或 `--force=<...>`
- 或短 flag group 包含 `f`（例如 `-fdx`、`-xdf`）

#### 3.3.2 `rm` 的危险判定
当 `cmd0 == "rm"`：
- 若第 2 个 token 精确等于 `-f` 或 `-rf` 则危险
- 其它 `rm` 形式（例如 `rm -r`）不会被该启发式标记为危险

#### 3.3.3 `sudo`：递归检查被 sudo 的子命令
当 `cmd0 == "sudo"`：
- 直接对 `command[1..]` 递归调用 `is_dangerous_to_call_with_exec`

---

## 4. 与 execpolicy 的关系（定位）
- `is_known_safe_command`：在 `render_decision_for_unmatched_command` 最优先返回 allow（“无需审批即可执行”）
- `command_might_be_dangerous`：在 `render_decision_for_unmatched_command` 中强制转为 prompt/forbidden（取决于 `AskForApproval`）

详见：`docs/workdocjcl/spec/07_Infrastructure/EXEC_POLICY.md` §3。

