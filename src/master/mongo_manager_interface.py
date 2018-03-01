# imports
# parent module imports
from mongo_items import Task
# module imports
from .task_status import LifeCycle, TaskStatus


class ITaskManager(object):
    """
    Interface for TaskManager.

    A TaskManager should manage all tasks. That means, it is a
    container like class where tasks could be added, removed,
    changed and updated.
    """

    def get_task(self, task_id: int) -> Task:
        """
        Searches for an task with the same id and returns this task.

        :returns Task: the task with the same id
        :returns None: if there is no task with this id
        """
        raise NotImplementedError("Not implemented")

    def add_or_update_task(self, task: Task) -> bool:
        """
        Adds a task and saves it.

        If the task is already added, it updates the task

        :task Task: task to add
        """
        raise NotImplementedError("Not implemented")

    def remove_task(self, task_id: int):
        """
        Removes a task and deletes it

        :task_id int: id of the task
        """
        raise NotImplementedError("Not implemented")

    def add_task_to_server_list (self) :
        raise NotImplementedError("Not implemented")

    def get_server_tasks_lists (self) :
        raise NotImplementedError("Not implemented")

    def get_server_task_amount_list (self) :
        raise NotImplementedError("Not implemented")

    def trigger_task_status (self, task, status) :
        raise NotImplementedError("Not implemented")


class IServerManager(object):
    def get_servers (self) :
        raise NotImplementedError("Not implemented")

    def get_server (self, ip) :
        raise NotImplementedError("Not implemented")

    def add_or_update_server (self, server) :
        raise NotImplementedError("Not implemented")

    def remove_server (self, server) :
        raise NotImplementedError("Not implemented")

    def remove_server_by_ip (self, server_ip) :
        raise NotImplementedError("Not implemented")


class IServerSettingManager :
    def get_server_settings (self) :
        raise NotImplementedError("Not implemented")

    def get_server_setting (self, id) :
        raise NotImplementedError("Not implemented")

    def add_or_update_server_setting (self, server_setting) :
        raise NotImplementedError("Not implemented")

    def activate_new_settings (self) :
        """ Maybe needs to restart the system """
        raise NotImplementedError("Not implemented")
