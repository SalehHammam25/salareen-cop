import asyncio

from fastmcp import Client

from salareen_cop.official.mailbox import OfficialMailboxes
from salareen_cop.official.server import build_unified_server
from salareen_cop.official.terms import greeting


def test_unified_server_declares_exact_four_tools_and_argument_names():
    async def scenario():
        boxes = OfficialMailboxes()
        boxes.set_offer(greeting("police", 1, "1" * 40, "amireman"))
        server = build_unified_server(boxes)
        async with Client(server) as client:
            tools = {tool.name: tool for tool in await client.list_tools()}
            assert set(tools) == {
                "negotiate",
                "receive_turn",
                "submit_audit",
                "receive_control",
            }
            assert set(tools["negotiate"].inputSchema["properties"]) == {"message"}
            assert set(tools["submit_audit"].inputSchema["properties"]) == {"payload"}

    asyncio.run(scenario())
