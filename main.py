
import asyncio

import load
import loop

# asycio throws error when loop gets closed (?)
# This prevents throwing error
from asyncio import base_events
base_events.BaseEventLoop._check_closed = lambda x: None


global client


def getClient():
    global client
    return client


async def main():
    # try:
    global client
    client = await load.load()

    # init all
    loop.init(client)

    # this runs each day
    while True:
        await loop.todayLoop()
        break


if __name__ == "__main__":

    asyncio.set_event_loop(asyncio.ProactorEventLoop())
    asyncioLoop = asyncio.new_event_loop()
    asyncioLoop.run_until_complete(main())
