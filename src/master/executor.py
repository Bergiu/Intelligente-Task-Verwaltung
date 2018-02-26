# import
from typing import List
# parent module import
from mongo_items import Server
from mongo_items import get_test_servers
from mongo_items import ServerRole
import my_curl
from my_curl import get_url
# module import
from .interfaces import IExecutor


class Executor(IExecutor):
    """Executes a task on a server"""

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
        for i_server in sorted_servers:
            if i_server.get("role") == ServerRole.slave:
                server = i_server
                server.get("tasks").append(task_id)
                route = "/execute/" + str(task_id)
                url = get_url(server.get("ip"), route, server.get("port"))
                response = my_curl.GET(url)
                if response["valid_response"] \
                        and response["response"]["successful"] == 1:
                    executed = True
                else:
                    print("not working")
                    server.tasks.remove(task_id)
            if executed:
                break
        self.blocked = False
        out = (executed, server)
        return out



def test_executor():
    print("### Test Executor")
    servers = get_test_servers(4)
    d = dict()
    d["ip"] = "0.0.0.0"
    s = Server(d)
    servers.insert(0, s)
    executor = Executor(servers)
    executor.execute(2)
