from vulcan import data
import time
import datetime
import asyncio
import vulcan

import webhook
import lesson
import display

global client


async def waitUntil(timestamp: int) -> None:
    """waits until given timestamp"""

    print("Waiting untill", timestamp)
    await asyncio.sleep(timestamp - time.time())


async def printLesson(block: list[data._lesson.Lesson]) -> None:

    # next lesson start
    dt = time.mktime(datetime.datetime.combine(
        block[0].date.date, block[0].time.from_).timetuple()) - 1200  # 20 mins earlier

    # wait until next lesson starts
    await waitUntil(dt)

    block = await lesson.SwapChangedLessons(block)

    message = display.displayBlock(block)

    # send discord message
    print(message)
    webhook.send(message)


async def todayLoop(c: vulcan.Vulcan) -> None:
    """single day loop menager"""

    client = c

    # get toodays lessons
    lessons = await lesson.getTodaysLessons(client)

    for block in lessons:
        # skip if there is no lesson lessons
        if len(block) == 0:
            continue

        # print lesson
        await printLesson(block)

    # today, 01,00AM
    tomorow = datetime.datetime.combine(
        datetime.date.today(), datetime.time(0, 0)) + datetime.timedelta(days=1, minutes=1)

    # wait until tomorow
    await waitUntil(time.mktime(tomorow.timetuple()))
