# imports
# parent module imports
from mongo_items import load_servers
from mongo_items import load_server_settings
# module imports
from .interfaces import IExecutor
from .manager import ExecutorManager
from .manager import TaskManager
from .manager import WebserverManager


    def __init__(self) :
            pass

class Master (IServerManager, IServerSettingManager) :
    """
    Manages the server.

    Contains a task manager, the config, the webserver, the watcher and the executor
    """

    def __init__(self, amount_executors: int=1):
        """Initial function"""
        # load config
        server_settings = load_server_settings()
        if len(server_settings) <= 0:
            # TODO
            raise Exception("not enough settings")
        self.config = server_settings[0]
        # load servers
        self.servers = load_servers()
        # create managers
        self.create_managers(amount_executors=amount_executors)

    def create_managers(self, amount_executors: int=1):
        """
        Loads the webserver/executor and watcher manager
        """
        self.executor_manager = ExecutorManager()
        self.executor_manager.create_executors(self.servers, self.amount_executors)
        self.task_manager = TaskManager(self.executor_manager)
        # TODO
        self.watcher_manager = None
        self.webserver_manager = WebserverManager(self.task_manager)

    def start_threads(self):
        """
        Starts the webserver, executor and watcher threads
        """
        self.webserver.start()
        self.executor_manager.start()
        # self.watcher_manager.start()


def main():
    task_man = TaskManager()
    master = Master(task_man)
    task_man.master = master
    print("All tasks:")
    for task in task_man.tasks:
        print(task.task.dict())
    print("Settings:")
    print(master.config.dict())
    master.startWebserver()

