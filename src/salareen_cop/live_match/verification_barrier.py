"""Opt-in lifecycle barrier used only by the local verification runner."""

import asyncio
from pathlib import Path

from .session import LiveMatchSession


async def block_strategy(session: LiveMatchSession) -> None:
    turn = getattr(session, "verification_barrier_turn", -1)
    if turn != session.turn_index:
        return
    session.events.emit(
        "strategy_blocked",
        turn=turn,
        phase=session.phase,
        correlation_id=f"action-{turn}",
    )
    release = Path(session.verification_barrier_release)
    while not release.exists():
        await asyncio.sleep(0.02)
