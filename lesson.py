from vulcan import Vulcan
from vulcan import data, model
import datetime

global client


def changeLessonData(Lesson: data._lesson.Lesson, override: dict = {}) -> data._lesson.Lesson:
    lesson_info = {
        "id": Lesson.id,
        "date": Lesson.date,
        "time": Lesson.time,
        "room": Lesson.room,
        "teacher": Lesson.teacher,
        "second_teacher": Lesson.second_teacher,
        "subject": Lesson.subject,
        "event": Lesson.event,
        "changes": Lesson.changes,
        "team_class": Lesson.team_class,
        "pupil_alias": Lesson.pupil_alias,
        "group": Lesson.group,
        "visible": Lesson.visible
    }

    lesson_info |= override

    return data._lesson.Lesson(**lesson_info)


def fixLesson(Lesson: data._lesson.Lesson) -> data._lesson.Lesson:
    """replaces None values with empty dataclasses. This prevents error later"""

    override = {}

    if Lesson.group == None:
        override["group"] = model.TeamVirtual(0, "0", "", "", "")

    if Lesson.subject == None:
        override["subject"] = model.Subject(0, "0", "", "", 0)

    # remake class
    return changeLessonData(Lesson, override)


async def getTodaysLessons(c: Vulcan) -> list[list[data._lesson.Lesson]]:
    """returns toodays lesson blocks"""

    global client
    global midnight

    client = c

    current_date = datetime.date.today()
    # today, 00,00AM
    midnight = datetime.datetime.combine(
        current_date, datetime.time(0, 0)).date() + datetime.timedelta(days=-3)
    getlessons = await client.data.get_lessons(date_from=midnight,)

    # empty array len = 13
    lessons: list[list[data._lesson.Lesson]] = [[] for _ in range(13)]

    # fix
    async for Lesson in getlessons:
        lessons[Lesson.time.position].append(fixLesson(Lesson))

    return lessons


async def SwapChangedLessons(block):
    global midnight

    changedLessons = await client.data.get_changed_lessons(date_from=midnight)

    async for changedLesson in changedLessons:

        for idx, Lesson in enumerate(block):
            if Lesson.changes != None and Lesson.changes.id == changedLesson.id:

                override = {}

                if changedLesson.room != None:
                    override["room"] = changedLesson.room

                if changedLesson.subject != None:
                    override["subject"] = changedLesson.subject

                if changedLesson.group != None:
                    override["group"] = changedLesson.group

                block[idx] = changeLessonData(Lesson, override)

                # canceled
                if changedLesson.changes.type == 1:
                    block.pop(idx)

    return block
