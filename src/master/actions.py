from .task_status import LifeCicle, TaskStatus


class ExitCodeAction :
    def __init__(self, exit_code) :
        self.exit_code = exit_code

    def trigger_if_exit_code(self, status: TaskStatus, task: Task) -> bool:
        """
        :returns bool: false if it was restarted
        """
        if status.exit_code == self.exit_code:
            return self.trigger(status, task)
        return True

    def trigger (self, status: TaskStatus, task: Task) -> bool:
        """
        Is triggered if the task has exited with the given exit code.

        :status TaskStatus: The TaskStatus that is returned by the server that has execute this task
        :task Task: The task object

        :returns bool: false if it was restarted
        """
        raise NotImplementedError("Not implemented")


class TgBot (ExitCodeAction) :
    def __init__(self, exit_code) :
        ExitCodeAction.__init__(self, exit_code)

    def trigger (self, status: TaskStatus, task: Task) -> bool:
        """
        Is triggered if the task has exited with the given exit code.

        :status TaskStatus: The TaskStatus that is returned by the server that has execute this task
        :task Task: The task object

        :returns bool: false if it was restarted
        """
        print("Telegram Nachricht wird gesendet:")
        msg = "TaskMan: " + str(self.exit_code)
        msg += " - " + str(status.message)
        msg += " (LifeCycleCode " + str(status.life_cycle) + ")"
        print(msg)


class SlackBot (ExitCodeAction) :
    def __init__(self) :
        pass

    def trigger (self, status: TaskStatus, task: Task) -> bool:
        """
        Is triggered if the task has exited with the given exit code.

        :status TaskStatus: The TaskStatus that is returned by the server that has execute this task
        :task Task: The task object

        :returns bool: false if it was restarted
        """
        print("Slack Nachricht wird gesendet:")
        msg = "TaskMan: " + str(self.exit_code)
        msg += " - " + str(status.message)
        msg += " (LifeCycleCode " + str(status.life_cycle) + ")"
        print(msg)


class EMail (ExitCodeAction) :
    def __init__(self) :
        pass

    def trigger (self, status: TaskStatus, task: Task) -> bool:
        """
        Is triggered if the task has exited with the given exit code.

        :status TaskStatus: The TaskStatus that is returned by the server that has execute this task
        :task Task: The task object

        :returns bool: false if it was restarted
        """
        print("EMail wird gesendet:")
        msg = "TaskMan: " + str(self.exit_code)
        msg += " - " + str(status.message)
        msg += " (LifeCycleCode " + str(status.life_cycle) + ")"
        print(msg)


class ExitCodeActionHandler (object):
    """
    An Exit Code Action Handler handles the actions, that be executed on some exit codes

    It belongs to one task, and can use its data inside of the actions.

    :task Task: the task that this exit code action handler belongs to
    :exit_code_action_classes List[class]: A list of classes that inherits from ExitCodeAction
    """

    def __init__(self, task: Task) :
        self.task = task
        self.exit_code_action_classes = [TgBot, SlackBot, EMail]
        self.actions = []

    def create_exit_code_actions(self, actions: List[dict]):
        for action in actions:
            for ecacl in self.exit_code_action_classes:
                if ecacl.__name__ == action["action_name"]:
                    eca = ecacl(action["exit_code"])
                    self.actions.append(eca)

    def trigger_status (self, status: TaskStatus) -> bool:
        """
        :returns bool: false if it was restarted by one action
        """
        out = True
        for exit_code_action in self.exit_code_actions:
            if not exit_code_action.trigger_if_exit_code(status):
                out = False
        return out

