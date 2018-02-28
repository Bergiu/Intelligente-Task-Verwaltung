from server_task import ServerTask
from interfaces import ExecutorManager
from .task_status import LifeCicle, TaskStatus


class TimeSetting(object):
    """
    TimeSetting triggers the execute function on the task manager
    """

    def __init__(self, task_id: int, executor_manager: ExecutorManager):
        """Initial function."""
        self.task_id = task_id
        self.executor_manager = executor_manager

    def execute(self):
        self.executor_manager.execute()

    def trigger_status (self, status) :
            """ true if task can be removed. also should restart the task if needed """
            # returns bool
            pass


class Manual(TimeSetting):
    """Can only be executed manual"""

    def __init__(self, server_task: ServerTask, executor_manager: ExecutorManager):
        """Initial function"""
        TimeSetting.__init__(self, server_task, executor_manager)


class Always(TimeSetting):
    """Takes care that the task is always running"""

    def __init__(self, server_task: ServerTask, executor_manager: ExecutorManager):
        """Initial function"""
        TimeSetting.__init__(self, server_task, executor_manager)


class Cron(TimeSetting):
    """Is executed with a cron task"""

    def __init__(self, server_task: ServerTask, executor_manager: ExecutorManager):
        """Initial function"""
        TimeSetting.__init__(self, server_task, executor_manager)
