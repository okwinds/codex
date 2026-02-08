# `scripts/mock_responses_websocket_server.py`

## Identity
- kind: `source`
- ext: `.py`
- size_bytes: `5882`
- sha256: `c28540e27248b84de020e40fb9f68eee3909c98d15a1e6f0e5a1cd461ddc5a5d`
- generated_utc: `2026-02-08T10:45:42Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `scripts/mock_responses_websocket_server.py` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `def _utc_iso() -> str:`
- `def _default_usage() -> dict[str, Any]:`
- `def _event_response_created(response_id: str) -> dict[str, Any]:`
- `def _event_response_done() -> dict[str, Any]:`
- `def _event_response_completed(response_id: str) -> dict[str, Any]:`
- `def _event_function_call(call_id: str, name: str, arguments_json: str) -> dict[str, Any]:`
- `def _event_assistant_message(message_id: str, text: str) -> dict[str, Any]:`
- `def _dump_json(payload: Any) -> str:`
- `def _print_request(prefix: str, payload: Any) -> None:`
- `def main() -> int:`
- `if __name__ == "__main__":`

## Definitions (auto, per-file)
- `import` `scripts/mock_responses_websocket_server.py:3` `import argparse`
- `import` `scripts/mock_responses_websocket_server.py:4` `import asyncio`
- `import` `scripts/mock_responses_websocket_server.py:5` `import datetime as dt`
- `import` `scripts/mock_responses_websocket_server.py:6` `import json`
- `import` `scripts/mock_responses_websocket_server.py:7` `import sys`
- `import` `scripts/mock_responses_websocket_server.py:8` `from typing import Any`
- `import` `scripts/mock_responses_websocket_server.py:10` `import websockets`
- `def` `scripts/mock_responses_websocket_server.py:24` `def _utc_iso() -> str:`
- `def` `scripts/mock_responses_websocket_server.py:28` `def _default_usage() -> dict[str, Any]:`
- `def` `scripts/mock_responses_websocket_server.py:38` `def _event_response_created(response_id: str) -> dict[str, Any]:`
- `def` `scripts/mock_responses_websocket_server.py:42` `def _event_response_done() -> dict[str, Any]:`
- `def` `scripts/mock_responses_websocket_server.py:46` `def _event_response_completed(response_id: str) -> dict[str, Any]:`
- `def` `scripts/mock_responses_websocket_server.py:50` `def _event_function_call(call_id: str, name: str, arguments_json: str) -> dict[str, Any]:`
- `def` `scripts/mock_responses_websocket_server.py:57` `def _event_assistant_message(message_id: str, text: str) -> dict[str, Any]:`
- `def` `scripts/mock_responses_websocket_server.py:69` `def _dump_json(payload: Any) -> str:`
- `def` `scripts/mock_responses_websocket_server.py:73` `def _print_request(prefix: str, payload: Any) -> None:`
- `def` `scripts/mock_responses_websocket_server.py:172` `def main() -> int:`
- `main` `scripts/mock_responses_websocket_server.py:194` `if __name__ == "__main__":`

## Dependencies (auto sample)
### Imports / Includes
- `import argparse`
- `import asyncio`
- `import datetime as dt`
- `import json`
- `import sys`
- `from typing import Any`
- `import websockets`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
