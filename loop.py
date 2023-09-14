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


async def printLesson() -> None:
    """gets lesson and messages it on discord"""

    # get toodays lessons
    lessons: list[list[data._lesson.Lesson]] = await lesson.getTodaysLessons(client)

    # loop for all lessons
    # block becouse sometimes lessons are split into groups
    for block in lessons:
        # skip if there is no lesson lessons
        if len(block) == 0:
            continue

        # next lesson start
        dt = time.mktime(datetime.datetime.combine(
            block[0].date.date, block[0].time.from_).timetuple()) - 1200  # 20 mins earlier

        # wait until next lesson starts
        await waitUntil(dt)

        message = display.displayBlock(block)

        # send discord message
        print(message)
        webhook.send(message)


async def todayLoop(c: vulcan.Vulcan) -> None:
    """single day loop menager"""
    global client

    client = c

    # print lessons
    await printLesson()

    # today, 01,00AM
    current_date = datetime.date.today()
    tomorow = datetime.datetime.combine(
        current_date, datetime.time(0, 0)) + datetime.timedelta(days=1, minutes=1)

    # wait until tomorow
    await waitUntil(time.mktime(tomorow.timetuple()))
