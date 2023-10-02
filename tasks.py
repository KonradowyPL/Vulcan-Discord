import asyncio
import time


async def runAt(timestamp: int, func, params: dict = {}) -> None:
    """Waits until given timestamp and then executes function with given params"""

    print(f"New Corrutine: {round(timestamp,2)}")
    # wait until timestamp
    # need to do this 2 times to prevent doing task before timestamp
    await asyncio.sleep(timestamp-time.time())
    await asyncio.sleep(timestamp-time.time())

    # run
    await func(**params)
