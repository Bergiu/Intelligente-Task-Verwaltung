# import
from typing import List
# parent module import
from mongo_items import Server
from mongo_items import get_test_servers
from mongo_items import ServerRole
import my_curl
# module import
from .interfaces import IExecutor


class Executor(IExecutor):
    """Executes a task on a server"""

    def __init__(self, servers: List[Server]):
        """TODO: to be defined1. """
        self.servers = servers
        self.blocked = False

    def execute(self, task_id: int):
        self.blocked = True
        if len(self.servers) <= 0:
            # TODO: make an exception class
            raise Exception("Not enough servers")
        # get a server
        server = None
        for i_server in self.servers[1:]:
            if i_server.get("role") == ServerRole.slave:
                if server == None\
                        or len(i_server.get("tasks")) < len(server.get("tasks")):
                    server = i_server
        server.get("tasks").append(task_id)
        # TODO: CURL
        url = server.get("ip") + "/execute/" + str(task_id)
        response = my_curl.GET(url)
        if response["response"]["successful"] == 1:
            return True
        else:
            server.tasks.remove(task_id)
        self.blocked = False


def test_executor():
    print("### Test Executor")
    servers = get_test_servers(4)
    executor = Executor(servers)
    print(executor.__dict__)
    executor.execute(2)
