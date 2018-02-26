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


class ServerTaskManager(ITaskManager):
    def __init__(self, executor_manager: ExecutorManager):
        """Initial function"""
        self.executor_manager = executor_manager
        self.tasks = load_tasks()

    def execute(self, task_id: int):
        self.executor_manager.execute(task_id)

    def add_task(self, task: Task):
        id = task.get("id")
        for i_task in self.tasks:
            if i_task.get("id") == id:
                raise Exception("duplicate task id")
        server_task = ServerTask(task, self.executor_manager)
        self.tasks.append(server_task)

    def remove_task(self, task_id: int):
        raise NotImplemented

    def update_task(self, task: Task):
        raise NotImplemented

    def get_task(self, task_id: int):
        raise NotImplemented
