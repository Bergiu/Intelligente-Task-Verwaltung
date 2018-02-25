# parent module imports
from mongo_items import Task
# module imports
from .interfaces import IExecutor

class ServerTask(object):
    """
    A Wrapper around the Task class.

    Gives access to necessary functions for the TaskManager
    """

    def __init__(self, task: Task, executor: IExecutor):
        """Initial function"""
        self.task = task

    def get(self, key: str):
        """
        returns the value of the key
        """
        return self.task.get(key)

