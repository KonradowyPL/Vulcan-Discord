from vulcan import data


def displayBlock(block: list[data._lesson.Lesson]) -> str:
    """returns formated lesson block"""
    message = ""
    for Lesson in block:
        message += displayLesson(Lesson) + "\n"

    # removes ending enter from string
    message = message[:-1]

    return message


def displayLesson(Lesson: data._lesson.Lesson) -> str:
    """formats single lesson"""

    # none skip
    if Lesson == None:
        return 0

    # custom display names
    groupNames = {
        "N 1": "n1",
        "N 2": "n2",
        "N 3": "n3",
        "1/2": "a1",
        "2/2": "a2",
        "": ""
    }

    # is there is other name
    group = "None"
    if Lesson.group.shortcut in groupNames:
        group = groupNames[Lesson.group.shortcut]

    # religia
    if Lesson.subject.name == "Religia":
        group = "r0"

    # formating
    return f"{Lesson.time.displayed_time} '{Lesson.room.code.replace(' ','').lower() } {Lesson.subject.name} {group}"