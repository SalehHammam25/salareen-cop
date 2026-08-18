"""Deterministic client failure-boundary tests."""

import asyncio

from salareen_cop.mcp_transport import client as client_module
from salareen_cop.mcp_transport.results import TransportError


def test_disconnect_returns_typed_failure_without_message_leak(monkeypatch) -> None:
    class DisconnectedClient:
        def __init__(self, url: str) -> None:
            self.url = url

        async def __aenter__(self):
            raise ConnectionError("private-endpoint-token")

        async def __aexit__(self, *args: object) -> None:
            return None

    monkeypatch.setattr(client_module, "Client", DisconnectedClient)
    result = asyncio.run(client_module.send_geometry("http://peer/mcp", {}))
    assert result == {
        "accepted": False,
        "code": TransportError.REMOTE_ERROR,
        "detail": "ConnectionError",
    }
    assert "private-endpoint-token" not in str(result)


def test_unstructured_response_returns_typed_local_failure(monkeypatch) -> None:
    class Result:
        structured_content = None

    class UnstructuredClient:
        def __init__(self, url: str) -> None:
            self.url = url

        async def __aenter__(self):
            return self

        async def __aexit__(self, *args: object) -> None:
            return None

        async def call_tool(self, name: str, arguments: dict[str, object]) -> Result:
            return Result()

    monkeypatch.setattr(client_module, "Client", UnstructuredClient)
    result = asyncio.run(client_module.send_geometry("http://peer/mcp", {}))
    assert result["accepted"] is False
    assert result["code"] is TransportError.REMOTE_ERROR
    assert result["detail"] == "missing structured response"
