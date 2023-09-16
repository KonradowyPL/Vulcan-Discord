import asyncio


# project files
import load
import loop


async def main():

    global client
    client = await load.load()

    # this runs each day
    while True:
        await loop.todayLoop(client)

    # this never runs lol
    await client.close()


if __name__ == "__main__":
    asyncio.set_event_loop(asyncio.ProactorEventLoop())
    asyncioLoop = asyncio.new_event_loop()
    asyncioLoop.run_until_complete(main())
