# import
from typing import List
# parent module import
from mongo_items import Server
from mongo_items import ServerRole
from mongo_items import get_test_servers
import my_curl
from my_curl import get_url
# module import
from .mongo_manager_interface import ITaskManager


class IExecutor(object):
    def execute(task_id: int):
        raise NotImplemented


class Executor(IExecutor):
    '''Executes a task on the next free server'''

    def __init__(self, servers: List[Server]):
        """TODO: to be defined1. """
        self.servers = servers
        self.blocked = False

    def execute(self, task_id: int) -> bool:
        """
        Executes a task
        """
        self.blocked = True
        if len(self.servers) <= 0:
            # TODO: make an exception class
            raise Exception("Not enough servers")
        # sort server, less tasks first
        sorted_servers = sorted(self.servers, key=lambda server: len(server.get("tasks")))
        # try executing until it's executed
        executed = False
        server = None
        for i_server in sorted_servers:
            if i_server.get("role") == ServerRole.SLAVE:
                server = i_server
                route = "/execute/" + str(task_id)
                url = get_url(server.get("ip"), route, server.get("port"))
                response = my_curl.GET(url)
                if response["valid_response"] \
                        and response["response"]["successful"] == 1:
                    executed = True
                else:
                    print("not working")
            if executed:
                break
        if not executed:
            server = None
        else:
            server.get("tasks").append(task_id)
        self.blocked = False
        out = (executed, server)
        return out


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


def get_test_executor_manager() -> ExecutorManager:
    """Return an Executor that can be used for tests."""
    servers = get_test_servers()
    executor_manager = ExecutorManager()
    executor_manager.create_executors(servers)
    return executor_manager


def test_executor():
    print("### Test Executor")
    servers = get_test_servers(4)
    d = dict()
    d["ip"] = "0.0.0.0"
    s = Server(d)
    servers.insert(0, s)
    executor = Executor(servers)
    executor.execute(2)


def test_executor_manager():
    print("### Test ExecutorManager")
    exe_man = ExecutorManager()
    servers = get_test_servers(2)
    exe_man.create_executors(servers, 2)
    exe_man.execute(3)
