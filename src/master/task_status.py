from typing import IntEnum


# TODO: documentation
class LifeCicle(IntEnum):
    NOT_STARTED = 0
    RUNNING = 1
    WAITING = 2
    PAUSED = 3
    EXITED = 4
    NO_RESPONSE = 5


class TaskStatus(object):
    pass
