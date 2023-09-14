from vulcan import Vulcan
from vulcan import data, model
import datetime

global client


def fixLesson(Lesson: data._lesson.Lesson) -> data._lesson.Lesson:
    """replaces None values with empty dataclasses. This prevents error later"""

    id = Lesson.id
    date = Lesson.date
    time = Lesson.time
    room = Lesson.room
    teacher = Lesson.teacher
    second_teacher = Lesson.second_teacher
    subject = Lesson.subject
    event = Lesson.event
    changes = Lesson.changes
    team_class = Lesson.team_class
    pupil_alias = Lesson.pupil_alias
    group = Lesson.group
    visible = Lesson.visible

    if Lesson.group == None:
        group = model.TeamVirtual(0, "0", "", "", "")

    if Lesson.subject == None:
        subject = model.Subject(0, "0", "", "", 0)

    # remake class
    return data._lesson.Lesson(id, date, time, room, teacher, second_teacher, subject,
                               event, changes, team_class, pupil_alias, group, visible)


async def getTodaysLessons(c: Vulcan) -> list[list[data._lesson.Lesson]]:
    """returns toodays lesson blocks"""

    global client
    client = c

    current_date = datetime.date.today()
    # today, 00,00AM
    midnight = datetime.datetime.combine(
        current_date, datetime.time(0, 0)).date() + datetime.timedelta(days=0)
    getlessons = await client.data.get_lessons(date_from=midnight,)

    # empty array len = 13
    lessons: list[list[data._lesson.Lesson]] = [[] for _ in range(13)]

    # fix
    async for Lesson in getlessons:
        lessons[Lesson.time.position].append(fixLesson(Lesson))

    return lessons