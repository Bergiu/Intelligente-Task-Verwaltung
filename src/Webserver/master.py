# imports
import json
# module imports
from mongo_items import Task
from mongo_items import ServerSettings
from mongo_items import Server


class MongoConnector(object):
    def load_tasks():
        """"Loads the tasks from the mongodb and returns them as json string"""
        return '[{"id": 1, "name": "task1", "dependencies":[{"dependency": "linux"},{"dependency": "python", "version": "3.6.8"}]}, {"id": 2, "name": "task2"}]'

    def load_server_settings():
        """"Loads the server settings from the mongodb and returns them as json string"""
        return '[{"id": 0, "client_ips": ["192.168.178.4", "192.168.178.5"], "log_settings": {}}]'


class ServerTask(object):
    """
    A Wrapper around the Task class.

    Gives access to necessary functions for the TaskManager
    """

    def __init__(self, task: Task):
        """Initial function"""
        self.task = task


class TaskManager(object):
    """Manages all Tasks."""

    def __init__(self):
        """Initial function"""
        self.loadConfig()
        self.loadTasks()

    def loadConfig(self):
        """Loads the first server settings"""
        configs_j = json.loads(MongoConnector.load_server_settings())
        if len(configs_j) >= 1:
            self.config = ServerSettings(configs_j[0])

    def loadTasks(self):
        """Loads all tasks"""
        self.tasks = []
        tasks_j = json.loads(MongoConnector.load_tasks())
        for task_j in tasks_j:
            task = Task(task_j)
            s_task = ServerTask(task)
            self.tasks.append(s_task)

tm = TaskManager()
print("All tasks:")
for task in tm.tasks:
    print(task.task.dict())
print("Settings:")
print(tm.config.dict())
