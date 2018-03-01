# parent module imports
from mongo_items import Task
# modules imports
from .task_status import TaskStatus, LifeCycle
from .executor import ExecutorManager
from .executor import get_test_executor_manager


class TimeSetting(object):
    """TimeSetting triggers the execute function on the task manager."""

    def __init__(self, task: Task, executor_manager: ExecutorManager):
        """Initialize function."""
        self.task = task
        self.executor_manager = executor_manager

    def execute(self):
        """Execute the task."""
        self.executor_manager.execute(self.task.get("id"))

    def trigger_status(self, status: TaskStatus) -> bool:
        """
        Use to handle TaskStatuses (Stati?).

        Should restart the Task if necessary.

        :returns bool: True if task can be removed. Also should restart the task if needed.
        """
        if status.life_cycle == LifeCycle.NO_RESPONSE:
            self.execute()
            return False
        else:
            return True


class Manual(TimeSetting):
    """Can only be executed manual."""

    def __init__(self, task: Task, executor_manager: ExecutorManager):
        """Initialize function."""
        TimeSetting.__init__(self, task, executor_manager)


class Always(TimeSetting):
    """Takes care that the task is always running."""

    def __init__(self, task: Task, executor_manager: ExecutorManager):
        """Initialize function."""
        TimeSetting.__init__(self, task, executor_manager)

    def trigger_status(self, status: TaskStatus) -> bool:
        """
        Restart the task always if it exited

        :returns bool: True if task can be removed. Also should restart the task if needed.
        """
        if status.life_cycle == LifeCycle.EXITED:
            self.execute()
            return False
        else:
            return super().trigger_status(status)


class Cron(TimeSetting):
    """Is executed with a cron task."""

    def __init__(self, task: Task, executor_manager: ExecutorManager):
        """Initialize function."""
        TimeSetting.__init__(self, task, executor_manager)

    def trigger_status(self, status: TaskStatus) -> bool:
        """
        Use to handle TaskStatuses (Stati?).

        Should restart the Task if necessary.

        :returns bool: True if task can be removed. Also should restart the task if needed.
        """
        raise NotImplementedError("Not implemented")


CLASSES = [Manual, Always, Cron]


def create_time_setting(task: Task, executor_manager: ExecutorManager) -> TimeSetting:
    """Create the related TimeSetting object."""
    for CLASS in CLASSES:
        if CLASS.__name__.lower() == task.get("time")["type"].name.lower():
            return CLASS(task, executor_manager)


def test_create_time_setting():
    print("### Test create_time_setting")
    executor_manager = get_test_executor_manager()
    task_manual = Task({"id": 5, "time": {"type": 0}})
    time_manual = create_time_setting(task_manual, executor_manager)
    time_manual.execute()
    print("Should be 'manual': " + str(time_manual.__class__))
    task_always = Task({"id": 6, "time": {"type": 1}})
    time_always = create_time_setting(task_always, executor_manager)
    time_always.execute()
    status = TaskStatus("MemoryError", 1, LifeCycle.EXITED)
    time_always.trigger_status(status)
    status = TaskStatus("No response", 2, LifeCycle.NO_RESPONSE)
    time_always.trigger_status(status)
    print("Should be 'always': " + str(time_always.__class__))
    task_cron = Task({"id": 7, "time": {"type": 2}})
    time_cron = create_time_setting(task_cron, executor_manager)
    time_cron.execute()
    print("Should be 'cron': " + str(time_cron.__class__))
