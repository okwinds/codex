# Python Symbol Index

- generated_utc: `2026-02-08T10:45:45Z`
- symbol_count: `108`

| Kind | Location | Signature |
|---|---|---|
| `def` | `codex-cli/scripts/build_npm_package.py:35` | `def parse_args() -> argparse.Namespace:` |
| `def` | `codex-cli/scripts/build_npm_package.py:80` | `def main() -> int:` |
| `def` | `codex-cli/scripts/build_npm_package.py:150` | `def prepare_staging_dir(staging_dir: Path | None) -> tuple[Path, bool]:` |
| `def` | `codex-cli/scripts/build_npm_package.py:162` | `def stage_sources(staging_dir: Path, version: str, package: str) -> None:` |
| `def` | `codex-cli/scripts/build_npm_package.py:214` | `def run_command(cmd: list[str], cwd: Path | None = None) -> None:` |
| `def` | `codex-cli/scripts/build_npm_package.py:219` | `def stage_codex_sdk_sources(staging_dir: Path) -> None:` |
| `def` | `codex-cli/scripts/build_npm_package.py:240` | `def copy_native_binaries(` |
| `def` | `codex-cli/scripts/build_npm_package.py:286` | `def run_npm_pack(staging_dir: Path, output_path: Path) -> Path:` |
| `class` | `codex-cli/scripts/install_native_deps.py:37` | `class BinaryComponent:` |
| `def` | `codex-cli/scripts/install_native_deps.py:86` | `def _gha_enabled() -> bool:` |
| `def` | `codex-cli/scripts/install_native_deps.py:93` | `def _gha_escape(value: str) -> str:` |
| `def` | `codex-cli/scripts/install_native_deps.py:98` | `def _gha_error(*, title: str, message: str) -> None:` |
| `def` | `codex-cli/scripts/install_native_deps.py:110` | `def _gha_group(title: str):` |
| `def` | `codex-cli/scripts/install_native_deps.py:122` | `def parse_args() -> argparse.Namespace:` |
| `def` | `codex-cli/scripts/install_native_deps.py:154` | `def main() -> int:` |
| `def` | `codex-cli/scripts/install_native_deps.py:194` | `def fetch_rg(` |
| `def` | `codex-cli/scripts/install_native_deps.py:262` | `def _download_artifacts(workflow_id: str, dest_dir: Path) -> None:` |
| `def` | `codex-cli/scripts/install_native_deps.py:276` | `def install_binary_components(` |
| `def` | `codex-cli/scripts/install_native_deps.py:308` | `def _install_single_binary(` |
| `def` | `codex-cli/scripts/install_native_deps.py:334` | `def _archive_name_for_target(artifact_prefix: str, target: str) -> str:` |
| `def` | `codex-cli/scripts/install_native_deps.py:340` | `def _fetch_single_rg(` |
| `def` | `codex-cli/scripts/install_native_deps.py:401` | `def _download_file(url: str, dest: Path) -> None:` |
| `def` | `codex-cli/scripts/install_native_deps.py:409` | `def extract_archive(` |
| `def` | `codex-cli/scripts/install_native_deps.py:456` | `def _load_manifest(manifest_path: Path) -> dict:` |
| `def` | `codex-rs/core/src/skills/assets/samples/skill-creator/scripts/generate_openai_yaml.py:52` | `def yaml_quote(value):` |
| `def` | `codex-rs/core/src/skills/assets/samples/skill-creator/scripts/generate_openai_yaml.py:57` | `def format_display_name(skill_name):` |
| `def` | `codex-rs/core/src/skills/assets/samples/skill-creator/scripts/generate_openai_yaml.py:76` | `def generate_short_description(display_name):` |
| `def` | `codex-rs/core/src/skills/assets/samples/skill-creator/scripts/generate_openai_yaml.py:106` | `def read_frontmatter_name(skill_dir):` |
| `def` | `codex-rs/core/src/skills/assets/samples/skill-creator/scripts/generate_openai_yaml.py:132` | `def parse_interface_overrides(raw_overrides):` |
| `def` | `codex-rs/core/src/skills/assets/samples/skill-creator/scripts/generate_openai_yaml.py:155` | `def write_openai_yaml(skill_dir, skill_name, raw_overrides):` |
| `def` | `codex-rs/core/src/skills/assets/samples/skill-creator/scripts/generate_openai_yaml.py:189` | `def main():` |
| `def` | `codex-rs/core/src/skills/assets/samples/skill-creator/scripts/init_skill.py:125` | `def main():` |
| `def` | `codex-rs/core/src/skills/assets/samples/skill-creator/scripts/init_skill.py:197` | `def normalize_skill_name(skill_name):` |
| `def` | `codex-rs/core/src/skills/assets/samples/skill-creator/scripts/init_skill.py:206` | `def title_case_skill_name(skill_name):` |
| `def` | `codex-rs/core/src/skills/assets/samples/skill-creator/scripts/init_skill.py:211` | `def parse_resources(raw_resources):` |
| `def` | `codex-rs/core/src/skills/assets/samples/skill-creator/scripts/init_skill.py:230` | `def create_resource_dirs(skill_dir, skill_name, skill_title, resources, include_examples):` |
| `def` | `codex-rs/core/src/skills/assets/samples/skill-creator/scripts/init_skill.py:258` | `def init_skill(skill_name, path, resources, include_examples, interface_overrides):` |
| `def` | `codex-rs/core/src/skills/assets/samples/skill-creator/scripts/init_skill.py:333` | `def main():` |
| `def` | `codex-rs/core/src/skills/assets/samples/skill-creator/scripts/quick_validate.py:15` | `def validate_skill(skill_path):` |
| `def` | `codex-rs/core/src/skills/assets/samples/skill-installer/scripts/github_utils.py:10` | `def github_request(url: str, user_agent: str) -> bytes:` |
| `def` | `codex-rs/core/src/skills/assets/samples/skill-installer/scripts/github_utils.py:20` | `def github_api_contents_url(repo: str, path: str, ref: str) -> str:` |
| `class` | `codex-rs/core/src/skills/assets/samples/skill-installer/scripts/install-skill-from-github.py:22` | `class Args:` |
| `class` | `codex-rs/core/src/skills/assets/samples/skill-installer/scripts/install-skill-from-github.py:33` | `class Source:` |
| `class` | `codex-rs/core/src/skills/assets/samples/skill-installer/scripts/install-skill-from-github.py:41` | `class InstallError(Exception):` |
| `def` | `codex-rs/core/src/skills/assets/samples/skill-installer/scripts/install-skill-from-github.py:45` | `def _codex_home() -> str:` |
| `def` | `codex-rs/core/src/skills/assets/samples/skill-installer/scripts/install-skill-from-github.py:49` | `def _tmp_root() -> str:` |
| `def` | `codex-rs/core/src/skills/assets/samples/skill-installer/scripts/install-skill-from-github.py:55` | `def _request(url: str) -> bytes:` |
| `def` | `codex-rs/core/src/skills/assets/samples/skill-installer/scripts/install-skill-from-github.py:59` | `def _parse_github_url(url: str, default_ref: str) -> tuple[str, str, str, str | None]:` |
| `def` | `codex-rs/core/src/skills/assets/samples/skill-installer/scripts/install-skill-from-github.py:80` | `def _download_repo_zip(owner: str, repo: str, ref: str, dest_dir: str) -> str:` |
| `def` | `codex-rs/core/src/skills/assets/samples/skill-installer/scripts/install-skill-from-github.py:99` | `def _run_git(args: list[str]) -> None:` |
| `def` | `codex-rs/core/src/skills/assets/samples/skill-installer/scripts/install-skill-from-github.py:105` | `def _safe_extract_zip(zip_file: zipfile.ZipFile, dest_dir: str) -> None:` |
| `def` | `codex-rs/core/src/skills/assets/samples/skill-installer/scripts/install-skill-from-github.py:115` | `def _validate_relative_path(path: str) -> None:` |
| `def` | `codex-rs/core/src/skills/assets/samples/skill-installer/scripts/install-skill-from-github.py:120` | `def _validate_skill_name(name: str) -> None:` |
| `def` | `codex-rs/core/src/skills/assets/samples/skill-installer/scripts/install-skill-from-github.py:128` | `def _git_sparse_checkout(repo_url: str, ref: str, paths: list[str], dest_dir: str) -> str:` |
| `def` | `codex-rs/core/src/skills/assets/samples/skill-installer/scripts/install-skill-from-github.py:164` | `def _validate_skill(path: str) -> None:` |
| `def` | `codex-rs/core/src/skills/assets/samples/skill-installer/scripts/install-skill-from-github.py:172` | `def _copy_skill(src: str, dest_dir: str) -> None:` |
| `def` | `codex-rs/core/src/skills/assets/samples/skill-installer/scripts/install-skill-from-github.py:179` | `def _build_repo_url(owner: str, repo: str) -> str:` |
| `def` | `codex-rs/core/src/skills/assets/samples/skill-installer/scripts/install-skill-from-github.py:183` | `def _build_repo_ssh(owner: str, repo: str) -> str:` |
| `def` | `codex-rs/core/src/skills/assets/samples/skill-installer/scripts/install-skill-from-github.py:187` | `def _prepare_repo(source: Source, method: str, tmp_dir: str) -> str:` |
| `def` | `codex-rs/core/src/skills/assets/samples/skill-installer/scripts/install-skill-from-github.py:209` | `def _resolve_source(args: Args) -> Source:` |
| `def` | `codex-rs/core/src/skills/assets/samples/skill-installer/scripts/install-skill-from-github.py:243` | `def _default_dest() -> str:` |
| `def` | `codex-rs/core/src/skills/assets/samples/skill-installer/scripts/install-skill-from-github.py:247` | `def _parse_args(argv: list[str]) -> Args:` |
| `def` | `codex-rs/core/src/skills/assets/samples/skill-installer/scripts/install-skill-from-github.py:269` | `def main(argv: list[str]) -> int:` |
| `class` | `codex-rs/core/src/skills/assets/samples/skill-installer/scripts/list-skills.py:19` | `class ListError(Exception):` |
| `class` | `codex-rs/core/src/skills/assets/samples/skill-installer/scripts/list-skills.py:23` | `class Args(argparse.Namespace):` |
| `def` | `codex-rs/core/src/skills/assets/samples/skill-installer/scripts/list-skills.py:30` | `def _request(url: str) -> bytes:` |
| `def` | `codex-rs/core/src/skills/assets/samples/skill-installer/scripts/list-skills.py:34` | `def _codex_home() -> str:` |
| `def` | `codex-rs/core/src/skills/assets/samples/skill-installer/scripts/list-skills.py:38` | `def _installed_skills() -> set[str]:` |
| `def` | `codex-rs/core/src/skills/assets/samples/skill-installer/scripts/list-skills.py:50` | `def _list_skills(repo: str, path: str, ref: str) -> list[str]:` |
| `def` | `codex-rs/core/src/skills/assets/samples/skill-installer/scripts/list-skills.py:68` | `def _parse_args(argv: list[str]) -> Args:` |
| `def` | `codex-rs/core/src/skills/assets/samples/skill-installer/scripts/list-skills.py:86` | `def main(argv: list[str]) -> int:` |
| `class` | `codex-rs/vendor/bubblewrap/tests/test-seccomp.py:209` | `class Test(unittest.TestCase):` |
| `def` | `codex-rs/vendor/bubblewrap/tests/test-seccomp.py:612` | `def main():` |
| `def` | `codex-rs/windows-sandbox-rs/sandbox_smoketests.py:12` | `def _resolve_codex_cmd() -> List[str]:` |
| `class` | `codex-rs/windows-sandbox-rs/sandbox_smoketests.py:57` | `class CaseResult:` |
| `def` | `codex-rs/windows-sandbox-rs/sandbox_smoketests.py:61` | `def run_sbx(` |
| `def` | `codex-rs/windows-sandbox-rs/sandbox_smoketests.py:93` | `def have(cmd: str) -> bool:` |
| `def` | `codex-rs/windows-sandbox-rs/sandbox_smoketests.py:96` | `def make_dir_clean(p: Path) -> None:` |
| `def` | `codex-rs/windows-sandbox-rs/sandbox_smoketests.py:101` | `def write_file(p: Path, content: str = "x") -> None:` |
| `def` | `codex-rs/windows-sandbox-rs/sandbox_smoketests.py:105` | `def remove_if_exists(p: Path) -> None:` |
| `def` | `codex-rs/windows-sandbox-rs/sandbox_smoketests.py:112` | `def assert_exists(p: Path) -> bool:` |
| `def` | `codex-rs/windows-sandbox-rs/sandbox_smoketests.py:115` | `def assert_not_exists(p: Path) -> bool:` |
| `def` | `codex-rs/windows-sandbox-rs/sandbox_smoketests.py:118` | `def make_junction(link: Path, target: Path) -> bool:` |
| `def` | `codex-rs/windows-sandbox-rs/sandbox_smoketests.py:126` | `def make_symlink(link: Path, target: Path) -> bool:` |
| `def` | `codex-rs/windows-sandbox-rs/sandbox_smoketests.py:138` | `def summarize(results: List[CaseResult]) -> int:` |
| `def` | `codex-rs/windows-sandbox-rs/sandbox_smoketests.py:148` | `def main() -> int:` |
| `def` | `scripts/asciicheck.py:49` | `def main() -> int:` |
| `def` | `scripts/asciicheck.py:72` | `def lint_utf8_ascii(filename: Path, fix: bool) -> bool:` |
| `def` | `scripts/mock_responses_websocket_server.py:24` | `def _utc_iso() -> str:` |
| `def` | `scripts/mock_responses_websocket_server.py:28` | `def _default_usage() -> dict[str, Any]:` |
| `def` | `scripts/mock_responses_websocket_server.py:38` | `def _event_response_created(response_id: str) -> dict[str, Any]:` |
| `def` | `scripts/mock_responses_websocket_server.py:42` | `def _event_response_done() -> dict[str, Any]:` |
| `def` | `scripts/mock_responses_websocket_server.py:46` | `def _event_response_completed(response_id: str) -> dict[str, Any]:` |
| `def` | `scripts/mock_responses_websocket_server.py:50` | `def _event_function_call(call_id: str, name: str, arguments_json: str) -> dict[str, Any]:` |
| `def` | `scripts/mock_responses_websocket_server.py:57` | `def _event_assistant_message(message_id: str, text: str) -> dict[str, Any]:` |
| `def` | `scripts/mock_responses_websocket_server.py:69` | `def _dump_json(payload: Any) -> str:` |
| `def` | `scripts/mock_responses_websocket_server.py:73` | `def _print_request(prefix: str, payload: Any) -> None:` |
| `def` | `scripts/mock_responses_websocket_server.py:172` | `def main() -> int:` |
| `def` | `scripts/readme_toc.py:22` | `def main() -> int:` |
| `def` | `scripts/readme_toc.py:37` | `def generate_toc_lines(content: str) -> List[str]:` |
| `def` | `scripts/readme_toc.py:71` | `def check_or_fix(readme_path: Path, fix: bool) -> int:` |
| `def` | `scripts/stage_npm_packages.py:31` | `def parse_args() -> argparse.Namespace:` |
| `def` | `scripts/stage_npm_packages.py:63` | `def collect_native_components(packages: list[str]) -> set[str]:` |
| `def` | `scripts/stage_npm_packages.py:71` | `def resolve_release_workflow(version: str) -> dict:` |
| `def` | `scripts/stage_npm_packages.py:95` | `def resolve_workflow_url(version: str, override: str | None) -> tuple[str, str | None]:` |
| `def` | `scripts/stage_npm_packages.py:103` | `def install_native_components(` |
| `def` | `scripts/stage_npm_packages.py:118` | `def run_command(cmd: list[str]) -> None:` |
| `def` | `scripts/stage_npm_packages.py:123` | `def main() -> int:` |
