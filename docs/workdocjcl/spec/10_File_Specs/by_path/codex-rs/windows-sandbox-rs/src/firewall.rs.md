# `codex-rs/windows-sandbox-rs/src/firewall.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `8457`
- sha256: `19d0a5efd3495a43007e69cc53775f14ab55203a668de1b647322d8dd1ecb583`
- generated_utc: `2026-02-03T16:08:31Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/windows-sandbox-rs/src/firewall.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub fn ensure_offline_outbound_block(offline_sid: &str, log: &mut File) -> Result<()> {`

## Definitions (auto, per-file)
- `use` `codex-rs/windows-sandbox-rs/src/firewall.rs:3` `use anyhow::Result;`
- `use` `codex-rs/windows-sandbox-rs/src/firewall.rs:4` `use std::fs::File;`
- `use` `codex-rs/windows-sandbox-rs/src/firewall.rs:5` `use std::io::Write;`
- `use` `codex-rs/windows-sandbox-rs/src/firewall.rs:7` `use windows::core::Interface;`
- `use` `codex-rs/windows-sandbox-rs/src/firewall.rs:8` `use windows::core::BSTR;`
- `use` `codex-rs/windows-sandbox-rs/src/firewall.rs:9` `use windows::Win32::Foundation::VARIANT_TRUE;`
- `use` `codex-rs/windows-sandbox-rs/src/firewall.rs:10` `use windows::Win32::NetworkManagement::WindowsFirewall::INetFwPolicy2;`
- `use` `codex-rs/windows-sandbox-rs/src/firewall.rs:11` `use windows::Win32::NetworkManagement::WindowsFirewall::INetFwRule3;`
- `use` `codex-rs/windows-sandbox-rs/src/firewall.rs:12` `use windows::Win32::NetworkManagement::WindowsFirewall::NetFwPolicy2;`
- `use` `codex-rs/windows-sandbox-rs/src/firewall.rs:13` `use windows::Win32::NetworkManagement::WindowsFirewall::NetFwRule;`
- `use` `codex-rs/windows-sandbox-rs/src/firewall.rs:14` `use windows::Win32::NetworkManagement::WindowsFirewall::NET_FW_ACTION_BLOCK;`
- `use` `codex-rs/windows-sandbox-rs/src/firewall.rs:15` `use windows::Win32::NetworkManagement::WindowsFirewall::NET_FW_IP_PROTOCOL_ANY;`
- `use` `codex-rs/windows-sandbox-rs/src/firewall.rs:16` `use windows::Win32::NetworkManagement::WindowsFirewall::NET_FW_PROFILE2_ALL;`
- `use` `codex-rs/windows-sandbox-rs/src/firewall.rs:17` `use windows::Win32::NetworkManagement::WindowsFirewall::NET_FW_RULE_DIR_OUT;`
- `use` `codex-rs/windows-sandbox-rs/src/firewall.rs:18` `use windows::Win32::System::Com::CoCreateInstance;`
- `use` `codex-rs/windows-sandbox-rs/src/firewall.rs:19` `use windows::Win32::System::Com::CoInitializeEx;`
- `use` `codex-rs/windows-sandbox-rs/src/firewall.rs:20` `use windows::Win32::System::Com::CoUninitialize;`
- `use` `codex-rs/windows-sandbox-rs/src/firewall.rs:21` `use windows::Win32::System::Com::CLSCTX_INPROC_SERVER;`
- `use` `codex-rs/windows-sandbox-rs/src/firewall.rs:22` `use windows::Win32::System::Com::COINIT_APARTMENTTHREADED;`
- `use` `codex-rs/windows-sandbox-rs/src/firewall.rs:24` `use codex_windows_sandbox::SetupErrorCode;`
- `use` `codex-rs/windows-sandbox-rs/src/firewall.rs:25` `use codex_windows_sandbox::SetupFailure;`
- `const` `codex-rs/windows-sandbox-rs/src/firewall.rs:29` `const OFFLINE_BLOCK_RULE_NAME: &str = "codex_sandbox_offline_block_outbound";`
- `const` `codex-rs/windows-sandbox-rs/src/firewall.rs:32` `const OFFLINE_BLOCK_RULE_FRIENDLY: &str = "Codex Sandbox Offline - Block Outbound";`
- `fn` `codex-rs/windows-sandbox-rs/src/firewall.rs:34` `pub fn ensure_offline_outbound_block(offline_sid: &str, log: &mut File) -> Result<()> {`
- `fn` `codex-rs/windows-sandbox-rs/src/firewall.rs:81` `fn ensure_block_rule(`
- `fn` `codex-rs/windows-sandbox-rs/src/firewall.rs:144` `fn configure_rule(`
- `fn` `codex-rs/windows-sandbox-rs/src/firewall.rs:217` `fn log_line(log: &mut File, msg: &str) -> Result<()> {`

## Dependencies (auto sample)
### Imports / Includes
- `use anyhow::Result;`
- `use std::fs::File;`
- `use std::io::Write;`
- `use windows::core::Interface;`
- `use windows::core::BSTR;`
- `use windows::Win32::Foundation::VARIANT_TRUE;`
- `use windows::Win32::NetworkManagement::WindowsFirewall::INetFwPolicy2;`
- `use windows::Win32::NetworkManagement::WindowsFirewall::INetFwRule3;`
- `use windows::Win32::NetworkManagement::WindowsFirewall::NetFwPolicy2;`
- `use windows::Win32::NetworkManagement::WindowsFirewall::NetFwRule;`
- `use windows::Win32::NetworkManagement::WindowsFirewall::NET_FW_ACTION_BLOCK;`
- `use windows::Win32::NetworkManagement::WindowsFirewall::NET_FW_IP_PROTOCOL_ANY;`
- `use windows::Win32::NetworkManagement::WindowsFirewall::NET_FW_PROFILE2_ALL;`
- `use windows::Win32::NetworkManagement::WindowsFirewall::NET_FW_RULE_DIR_OUT;`
- `use windows::Win32::System::Com::CoCreateInstance;`
- `use windows::Win32::System::Com::CoInitializeEx;`
- `use windows::Win32::System::Com::CoUninitialize;`
- `use windows::Win32::System::Com::CLSCTX_INPROC_SERVER;`
- `use windows::Win32::System::Com::COINIT_APARTMENTTHREADED;`
- `use codex_windows_sandbox::SetupErrorCode;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
