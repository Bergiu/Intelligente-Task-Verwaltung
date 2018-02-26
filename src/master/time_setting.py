from server_task import ServerTask
from interfaces import ExecutorManager

class TimeSetting(object):
    """
    TimeSetting triggers the execute function on the task manager
    """

    def __init__(self, server_task: ServerTask, executor_manager: ExecutorManager):
        """Initial function."""
        self.server_task = server_task
        self.executor_manager = executor_manager

    def execute(self):
        self.executor_manager.execute()


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
