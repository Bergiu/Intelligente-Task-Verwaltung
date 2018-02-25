# parent module imports
from mongo_items import Task

class ITaskManager(object):
    """
    Interface for TaskManager.

    A TaskManager should manage all tasks. That means, it is a
    container like class where tasks could be added, removed,
    changed and updated.
    """

    def add_task(task: Task):
        raise NotImplemented

    def remove_task(task_id: int):
        raise NotImplemented

    def update_task(task: Task):
        raise NotImplemented

    def get_task(task_id: int):
        raise NotImplemented
