# imports
# parent module imports
from mongo_items import Server
from mongo_items import Task
import my_curl
from my_curl import get_url
# module imports
from .task_manager_interface import ITaskManager
from .executor import IExecutor
from .task_status import LifeCycle, TaskStatus

class Watcher :
    '''Watches the tasks of a server. For each server there is a watcher'''
    def __init__(self) :
            self.server = None # Server
            pass
    def __init__ (self, server) :
            # returns 
            pass

class WatcherManager :
    def __init__(self) :
            self.watchers = None # List[Watcher]
            self.task_manager = None # ITaskManager
            pass
    def create_watchers (self, servers) :
            # returns 
            pass

