# parent module imports
from mongo_items import Task


class ITaskManager(object):
    """
    Interface for TaskManager.

    A TaskManager should manage all tasks. That means, it is a
    container like class where tasks could be added, removed,
    changed and updated.
    """

    def add_task(self, task: Task):
        raise NotImplemented

    def remove_task(self, task_id: int):
        raise NotImplemented

    def update_task(self, task: Task):
        raise NotImplemented

    def get_task(self, task_id: int):
        raise NotImplemented
