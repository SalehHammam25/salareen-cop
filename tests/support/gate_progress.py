"""Flushed progress records for long-running gate cases."""

import time
from collections.abc import Callable


def run_case[T](name: str, repeat: int, operation: Callable[[], T]) -> T:
    started = time.monotonic()
    print(f"repeat={repeat + 1} scenario={name} START", flush=True)
    try:
        result = operation()
    except BaseException:
        elapsed = time.monotonic() - started
        print(
            f"repeat={repeat + 1} scenario={name} FAIL elapsed={elapsed:.3f}s",
            flush=True,
        )
        raise
    elapsed = time.monotonic() - started
    print(
        f"repeat={repeat + 1} scenario={name} PASS elapsed={elapsed:.3f}s", flush=True
    )
    return result
