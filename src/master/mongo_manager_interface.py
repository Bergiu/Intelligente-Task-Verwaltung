# imports
# parent module imports
from mongo_items import Task
# module imports
from .task_status import LifeCicle, TaskStatus


class ITaskManager(object):
    """
    Interface for TaskManager.

    A TaskManager should manage all tasks. That means, it is a
    container like class where tasks could be added, removed,
    changed and updated.
    """

    def add_task(self, task: Task):
        raise NotImplemented

    def remove_task(self, task_id: int):
        raise NotImplemented

    def update_task(self, task: Task):
        raise NotImplemented

    def get_task(self, task_id: int):
        raise NotImplemented

    def add_task_to_server_list (self) :
            # returns 
            pass
    def get_server_tasks_lists (self) :
            # returns List[(Server, List[Tasks])]
            pass
    def get_server_task_amount_list (self) :
            # returns List[(int, Server)]
            pass
    def trigger_task_status (self, task, status) :
            # returns 
            pass

class IServerManager :
    def __init__(self) :
            pass
    def get_servers (self) :
            # returns 
            pass
    def get_server (self, ip) :
            # returns 
            pass
    def add_or_update_server (self, server) :
            # returns 
            pass
    def remove_server (self, server) :
            # returns 
            pass
    def remove_server_by_ip (self, server_ip) :
            # returns 
            pass


class IServerSettingManager :
    def __init__(self) :
            pass
    def get_server_settings (self) :
            # returns List[ServerSetting]
            pass
    def get_server_setting (self, id) :
            # returns ServerSetting
            pass
    def add_or_update_server_setting (self, server_setting) :
            # returns 
            pass
    def activate_new_settings (self) :
            """ Maybe needs to restart the system """
            # returns 
            pass

