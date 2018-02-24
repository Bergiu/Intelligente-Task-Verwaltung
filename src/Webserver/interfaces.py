from mongo_items import Task

class ITaskManager(object):
    def execute(task: Task=None, task_id: int=None):
        pass

    def add_task(task: Task):
        pass

    def remove_task(task_id: int):
        pass

    def get_task(task_id: int):
        pass
