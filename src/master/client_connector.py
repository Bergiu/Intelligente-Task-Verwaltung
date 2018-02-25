class Executor(object):

    """Executes tasks"""

    def __init__(self, server_manager: ServerManager):
        """TODO: to be defined1.

        :server_manager: ServerManager: TODO

        """
        self._server_manager: ServerManager = server_manager: ServerManager

    def execute(self, task: Task)
