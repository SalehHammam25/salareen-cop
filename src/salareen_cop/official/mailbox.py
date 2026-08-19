"""Bounded mailboxes shared by the unified server and series worker."""

import queue
import threading


class OfficialMailboxes:
    def __init__(self, maxsize: int = 256) -> None:
        self.agreements: queue.Queue = queue.Queue(maxsize)
        self.turns: queue.Queue = queue.Queue(maxsize)
        self.audits: queue.Queue = queue.Queue(maxsize)
        self.controls: queue.Queue = queue.Queue(maxsize)
        self._offer: dict | None = None
        self._lock = threading.Lock()

    def set_offer(self, offer: dict | None) -> None:
        with self._lock:
            self._offer = None if offer is None else dict(offer)

    def offer_for(self, sub_game: int | None) -> dict | None:
        with self._lock:
            offer = None if self._offer is None else dict(self._offer)
        if offer is None or offer.get("sub_game_number") not in (None, sub_game):
            return None
        return offer


def enqueue(target: queue.Queue, value: dict) -> dict:
    try:
        target.put_nowait(value)
    except queue.Full:
        return {"accepted": False, "reason": "queue_full"}
    return {"accepted": True}
