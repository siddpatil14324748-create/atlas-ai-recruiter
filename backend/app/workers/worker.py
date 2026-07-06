import asyncio
import logging
from collections.abc import Awaitable, Callable

logger = logging.getLogger(__name__)


class Worker:
    def __init__(self, name: str, handler: Callable[[], Awaitable[None]]) -> None:
        self.name = name
        self.handler = handler

    async def run(self) -> None:
        logger.info("worker_started", extra={"worker": self.name})
        await self.handler()


async def run_worker(worker: Worker) -> None:
    await worker.run()


async def main() -> None:
    await asyncio.sleep(0)
