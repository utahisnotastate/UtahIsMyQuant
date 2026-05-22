"""
CORE ARCHITECTURE: TICK_OBSERVER
High-speed, non-blocking tick ingestion via asyncio + WebSocket push (Sentinel Architecture).
While one tick is processed, the next is already queued — zero-wait I/O.
"""
from __future__ import annotations

import asyncio
import json
import logging
import time
from collections import deque
from dataclasses import dataclass, field
from typing import Any, Awaitable, Callable

try:
    import websockets
except ImportError:  # pragma: no cover
    websockets = None  # type: ignore[assignment]

logger = logging.getLogger(__name__)


@dataclass(frozen=True, slots=True)
class Tick:
    symbol: str
    price: float
    volume: float = 0.0
    timestamp_ns: int = field(default_factory=time.time_ns)

    @classmethod
    def from_payload(cls, data: dict[str, Any]) -> Tick:
        """Parse exchange JSON tick into a normalized Tick."""
        symbol = str(data.get("symbol") or data.get("s") or "UNKNOWN")
        price = float(data.get("price") or data.get("p") or 0.0)
        volume = float(data.get("volume") or data.get("v") or 0.0)
        ts = data.get("timestamp_ns") or data.get("t")
        timestamp_ns = int(ts) if ts is not None else time.time_ns()
        return cls(symbol=symbol, price=price, volume=volume, timestamp_ns=timestamp_ns)


TickHandler = Callable[[Tick], Awaitable[None] | None]


class TickObserver:
    """
    Asynchronous listener for market tick events.
    WebSocket listen + internal queue + O(1) dispatch to subscribers.
    """

    def __init__(self, uri: str | None = None, buffer_size: int = 10_000):
        self.uri = uri
        self.queue: asyncio.Queue[dict[str, Any] | Tick] = asyncio.Queue(maxsize=buffer_size)
        self._handlers: list[TickHandler] = []
        self._buffer: deque[Tick] = deque(maxlen=buffer_size)
        self._running = False
        self._listen_task: asyncio.Task[None] | None = None
        self._process_task: asyncio.Task[None] | None = None
        self._legacy_task: asyncio.Task[None] | None = None
        self.ticks_processed = 0

    def subscribe(self, handler: TickHandler) -> None:
        self._handlers.append(handler)

    def unsubscribe(self, handler: TickHandler) -> None:
        self._handlers = [h for h in self._handlers if h is not handler]

    @property
    def recent_ticks(self) -> list[Tick]:
        return list(self._buffer)

    async def emit(self, tick: Tick) -> None:
        """Push a single tick through the observer pipeline."""
        self._buffer.append(tick)
        await self._dispatch(tick)
        self.ticks_processed += 1

    async def _dispatch(self, tick: Tick) -> None:
        for handler in self._handlers:
            result = handler(tick)
            if asyncio.iscoroutine(result):
                await result

    async def listen(self) -> None:
        """
        Asynchronously stream market ticks from WebSocket into the internal queue.
        Non-blocking: recv loop only enqueues; processing happens in process().
        """
        if not self.uri:
            raise ValueError("TickObserver.listen() requires uri to be set")
        if websockets is None:
            raise ImportError("websockets package required for live listen — pip install websockets")

        self._running = True
        async with websockets.connect(self.uri) as websocket:
            while self._running:
                tick_data = await websocket.recv()
                payload = json.loads(tick_data) if isinstance(tick_data, str) else tick_data
                await self.queue.put(payload)

    async def process(self) -> None:
        """Drain the queue and dispatch ticks with minimal latency."""
        while self._running:
            raw = await self.queue.get()
            try:
                tick = raw if isinstance(raw, Tick) else Tick.from_payload(raw)
                await self.emit(tick)
            finally:
                self.queue.task_done()

    async def run(self) -> None:
        """Start WebSocket ingestion and queue processing concurrently."""
        if not self.uri:
            raise ValueError("TickObserver.run() requires uri to be set")
        self._running = True
        self._listen_task = asyncio.create_task(self.listen(), name="tick-listen")
        self._process_task = asyncio.create_task(self.process(), name="tick-process")
        await asyncio.gather(self._listen_task, self._process_task)

    def start_sentinel(self) -> tuple[asyncio.Task[None], asyncio.Task[None]]:
        """Background WebSocket listener + processor (Sentinel mode)."""
        if not self.uri:
            raise ValueError("TickObserver.start_sentinel() requires uri to be set")
        self._running = True
        self._listen_task = asyncio.create_task(self.listen(), name="tick-listen")
        self._process_task = asyncio.create_task(self.process(), name="tick-process")
        return self._listen_task, self._process_task

    async def ingest(self, payload: dict[str, Any] | Tick) -> None:
        """Push a tick into the queue without blocking callers (sim/replay friendly)."""
        await self.queue.put(payload)

    async def listen_queue(self, source: asyncio.Queue[Tick]) -> None:
        """Legacy path: bridge an external Tick queue into this observer."""
        self._running = True
        try:
            while self._running:
                tick = await source.get()
                await self.emit(tick)
        finally:
            self._running = False

    def start_background(self, source: asyncio.Queue[Tick]) -> asyncio.Task[None]:
        self._legacy_task = asyncio.create_task(self.listen_queue(source))
        return self._legacy_task

    async def stop(self) -> None:
        self._running = False
        for task in (self._listen_task, self._process_task, self._legacy_task):
            if task is not None:
                task.cancel()
                try:
                    await task
                except asyncio.CancelledError:
                    pass
        self._listen_task = None
        self._process_task = None
        self._legacy_task = None

    @staticmethod
    def latency_us(tick: Tick) -> float:
        """Microseconds between tick timestamp and now."""
        return (time.time_ns() - tick.timestamp_ns) / 1_000.0
