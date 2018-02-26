# imports
from typing import List
# parent module imports
import mongo_items
from mongo_items import Server
from mongo_items import Task
from mongo_items import load_tasks
# module imports
from .executor import Executor
from .interfaces import IExecutor
from .interfaces import ITaskManager
from .server_task import ServerTask


class WebserverManager(object):
    pass


class WatcherManager(object):
    pass


class ExecutorManager(IExecutor):
    """Handles a list of executors"""

    def __init__(self):
        """Initial function"""
        self.executors = []

    def create_executors(self, servers: List[Server], amount: int=1):
        for i in range(amount):
            executor = Executor(servers)
            self.executors.append(executor)

    def execute(self, task_id: int):
        executor = None
        for i_executor in self.executors:
            if not i_executor.blocked:
                executor = i_executor
                break
        if executor == None:
            # wait until one is free
            executor = None  # free one
            pass
        executor.execute(task_id)

    def start(self):
        print("Not implemented now")


class TaskManager(ITaskManager, IExecutor):
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

def test_executor_manager():
    print("### Test ExecutorManager")
    exe_man = ExecutorManager()
    servers = mongo_items.get_test_servers(2)
    exe_man.create_executors(servers, 2)
    # test
    exe_man.execute(3)
