# parent module imports
from mongo_items import Task
# module imports
from .actions import ExitCodeActionHandler
from .task_status import TaskStatus, LifeCicle
from .time_setting import TimeSetting
import mongo_items

class ServerTask(object):
    """
    A Wrapper around the Task class.

    Gives access to necessary functions for the TaskManager
    """

    def __init__(self, task: Task, exit_code_action_handler: ExitCodeActionHandler, time_setting: TimeSetting):
        """Initial function"""
        self.task = task
        self.exit_code_action_handler = exit_code_action_handler
        # self.exit_code_action_handler = ExitCodeActionHandler(task)
        # self.exit_code_action_handler.create_exit_code_actions(task.get("actions"))
        self.time_setting = time_setting

    def get(self, key: str):
        """
        returns the value of the key
        """
        return self.task.get(key)

    def trigger_status (self, task_status: TaskStatus) :
        """
        :returns bool: false if restarted
        """
        eca_restarted = not self.exit_code_action_handler.trigger_status(task_status)
        time_restarted = not self.time_setting.trigger_status(task_status)
        return not (eca_restarted or time_restarted)


class ServerTaskManager(ITaskManager):
    def __init__(self, settings: ServerSettings, executor_manager: ExecutorManager):
        """Initial function"""
        self.settings = settings
        self.executor_manager = executor_manager
        self.tasks = mongo_items.load_tasks()
        self.server_tasks = []
        self.create_server_tasks()

    def create_server_tasks(tasks: List[Task], #TODO):
        for task in tasks:
            server_task = ServerTask(task, )

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

    def trigger_task_status(self, task: Task, status: TaskStatus):
        st = self.get_server_task(task.get("id"))
        restarted = 
        # if task stopped
        if task_status.life_cycle == LifeCicle.EXITED \
                or task_status.life_cycle == LifeCicle.NO_RESPONSE:
            # and if task is not restarted
            if restarted
