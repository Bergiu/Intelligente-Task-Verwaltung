from enum import IntEnum


# TODO: documentation
class LifeCycle(IntEnum):
    NOT_STARTED = 0
    RUNNING = 1
    WAITING = 2
    PAUSED = 3
    EXITED = 4
    NO_RESPONSE = 5


class TaskStatus (object):
    def __init__(self, message: str, exit_code: int, life_cycle: LifeCycle) :
        self.message = message
        self.exit_code = exit_code
        self.life_cycle = life_cycle

