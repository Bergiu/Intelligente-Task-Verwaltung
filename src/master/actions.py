from .task_status import LifeCicle, TaskStatus



class ExitCodeActionHandler (object):
    def __init__(self, exit_code: int, task_id: int) :
        self.exit_code = exit_code
        self.task_id = task_id
        pass

    def trigger_status (self, status) -> bool:
            """ true if task can be removed """
            # returns bool
            pass

class ExitCodeAction :
    def __init__(self) :
            pass
    def trigger (self) :
            # returns 
            pass

class TgBot (ExitCodeAction) :
    def __init__(self) :
            pass

class SlackBot (ExitCodeAction) :
    def __init__(self) :
        pass

class EMail (ExitCodeAction) :
    def __init__(self) :
        pass

