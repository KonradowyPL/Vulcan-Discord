from vulcan import data
import datetime
import asyncio
import webhook
import vulcan
import time

import display
import lesson
import tasks

global client

# forces lesson to be sent to user even if it already happen. remove after debugging
force = True


async def printLesson(block: "list[data._lesson.Lesson]") -> None:

    message = display.displayBlock(block)

    # send discord message
    webhook.send(message)


def dtToTimestamp(date: datetime.date, time_: datetime.time):
    """converts dateitme.date & datetime.time to timestamp"""
    return time.mktime(datetime.datetime.combine(
        date, time_).timetuple())


def init(c: "vulcan.vulcan"):
    global client
    client = c


async def todayLoop():

    global client
    lessons = await lesson.getTodaysLessons(client)

    timeNow = time.time()

    for block in lessons:
        if len(block) == 0:
            continue

        block = await lesson.SwapChangedLessons(block)

        if len(block) == 0:
            continue

        params = {
            "block": block
        }

        date = dtToTimestamp(
            block[0].date.date, block[0].time.from_) - 1200  # 20 mins earlier

        if timeNow < date or force:
            await tasks.runAt(date, printLesson, params)
        else:
            print("Skipped lesson: already after")

    # wait until tomorow 00:01 AM
    tomorow = dtToTimestamp(datetime.date.today(), datetime.time(0, 0)) + 86460

    print("Day loop done.")
    await asyncio.sleep(tomorow - time.time())
