import json
from typing import List


class TimeType:
    """
    TimeType Enum

    It doesn't inherit from Enum, because than it isn't JSON serializable

    :manual: A Task is only executed manually
    :always: A Task will be restarted after exiting
    :cron: A Task will be started with a crontab entry
    """
    manual = 1
    always = 2
    cron = 3


class ServerRole:
    """
    ServerRole Enum

    It doesn't inherit from Enum, because than it isn't JSON serializable

    :task_manager: The Task Manager distributes the Tasks to the clients
    :client: The client executes the tasks
    """
    task_manager = 1
    client = 2


class DictWrapper(object):
    """
    Wraps an dict object that should contain only JSON serializable objects.
    """

    def __init__(self, d: dict):
        """
        Initial function

        :d dict: the dict object
        """
        self.d = d

    def dict(self) -> dict:
        """
        Returns the dict object
        """
        return self.d


class Task(DictWrapper):
    """
    A Task is a program that is executed to a given time.
    """

    def __init__(self, d: dict):
        """
        Initial method

        :d dict: dictionary
        :d["id"] int: task id
        :d["name"] str: task name
        :d["priority"] int: priority
        :d["dependencies"] List[dict["dependency": str, "version": str]]: list of dependencies
        :d["executable"] dict: executable options
        :d["executable"]["archivefile"] str: archivefile that contains the program
        :d["executable"]["command"] str: command that is executed in the root of the archivefile
        :d["time"] dict: time settings
        :d["time"]["type"] int: type is the integer value of TimeType
        :d["time"]["cron_entry"] str: the cron entry in the crontab
        :d["actions"] List[dict["exit_code": int, "action_name": string]]: list of exit code actions
        """
        # id
        id = int(d["id"])
        # task name
        if "name" not in d.keys():
            name = "No Name"
        else:
            name = str(d["name"])
        # priority
        if "priority" not in d.keys():
            priority = 0
        else:
            priority = int(d["priority"])
        # dependencies
        dependencies = []
        if "dependencies" in d.keys():
            for dependency in d["dependencies"]:
                # dependency name
                if "dependency" in dependency.keys():
                    dependency_name = str(dependency["dependency"])
                else:
                    continue
                # dependency version
                if "version" in dependency.keys():
                    version = str(dependency["version"])
                else:
                    version = ""
                # append dependency
                dependencies.append({"dependency": dependency_name, "version": version})
        # executable
        e_archivefile = ""
        e_command = ""
        if "executable" in d.keys():
            # archivefile that contains the program
            if "archivefile" in d["executable"]:
                # TODO: how to work with files
                e_archivefile = str(d["executable"]["archivefile"])
            # command that should be executed
            if "command" in d["executable"]:
                e_command = str(d["executable"]["command"])
        executable = {"archivefile": e_archivefile, "command": e_command}
        # time
        t_time_type = TimeType.manual
        t_cron_entry = ""
        if "time" in d.keys():
            # time type
            if "type" in d["executable"]:
                time_type_raw = int(d["executable"]["type"])
                t_time_type = TimeType(time_type_raw)
            # cron entry
            if "cron_entry" in d["executable"]:
                t_cron_entry = str(d["executable"]["cron_entry"])
        time = {"type": t_time_type, "cron_entry": t_cron_entry}
        # actions
        actions = []
        if "actions" in d.keys():
            for action in d["actions"]:
                # exit code
                if "exit_code" in action.keys():
                    exit_code = int(action["exit_code"])
                else:
                    exit_code = 0
                # action_name
                if "action_name" in action.keys():
                    action_name = str(action["action_name"])
                else:
                    continue
                # append dependency
                actions.append({"exit_code": exit_code, "action_name": action_name})
        # create new json
        n = { \
                "id": id, \
                "name": name, \
                "priority": priority, \
                "dependencies": dependencies, \
                "executable": executable, \
                "time": time, \
                "actions": actions \
            }
        super(Task, self).__init__(n)

    def add_dependency(self, dependency: str, version: str):
        """
        Creates and adds a dependency to the task
        """
        self.d["dependencies"].append({"dependency": dependency, "version": version})

    def set_executable(self, archivefile: str, command: str):
        """
        Sets the executable options of the task
        """
        self.d["executable"] = {"archivefile": str, "command": str}

    def set_time(self, time_type: TimeType, cron_entry: str):
        """
        Sets the time settings of the task
        """
        self.d["time"] = {"time": time_type, "cron_entry": cron_entry}

    def add_action(self, exit_code: int, action_name: str):
        """
        Creates and adds an action to the task
        """
        self.d["actions"].append({"exit_code": exit_code, "action_name": action_name})

    def __str__(self) -> str:
        return str(self.dict())


class Server(DictWrapper):
    """
    A server that runs the intelligent task manager.

    A server runs the clients or task manager.
    """

    def __init__(self, d: dict):
        """
        Initial method

        :d dict:
        :d["ip"] str: ip of the server
        :d["role"] int: role is the integer value of ServerRole
        :d["task"] List[int]: list of task ids that are executed currently on this server
        :d["dependencies"] List[dict["dependency": str, "version": str]]: list of dependencies
        """
        # ip
        ip = str(d["ip"])
        # role
        if "role" in d.keys():
            role = ServerRole(d["role"])
        else:
            role = ServerRole.client
        # tasks
        tasks = []
        if "tasks" in d.keys():
            for task_ in d["tasks"]:
                tasks.append(int(task_))
        # dependencies
        dependencies = []
        if "dependencies" in d.keys():
            for dependency in d["dependencies"]:
                # dependency name
                if "dependency" in dependency.keys():
                    dependency_name = str(dependency["dependency"])
                else:
                    continue
                # dependency version
                if "version" in dependency.keys():
                    version = str(dependency["version"])
                else:
                    version = ""
                # append dependency
                dependencies.append({"dependency": dependency_name, "version": version})
        n = {"ip": ip, "role": role, "tasks": tasks, "dependencies": dependencies}
        super(Server, self).__init__(n)

    def add_dependency(self, dependency: str, version: str):
        """
        Creates and adds a dependency to the task
        """
        self.d["dependencies"].append({"dependency": dependency, "version": version})

    def add_task(self, task_id: int):
        """
        Adds a task to the list
        """
        self.d["dependencies"].append(task_id)

    def __str__(self) -> str:
        return str(self.dict())


class ServerSettings(DictWrapper):
    """
    Server Settings
    """

    def __init__(self, d: dict):
        """
        Initial method

        :d dict:
        :d["id"] int: id
        :d["client_ips"] List[str]: ips of all clients/servers
        :d["log_settings"] dict: settings about logging
        :d["log_settings"]["save_path"] str: path to save the logs
        :d["log_settings"]["amount_days_till_delition"] int: amount of days till deletion of the logs
        :d["log_settings"]["log_std_out_daily"] bool: if the logs should be saved daily
        """
        # id
        id = int(id)
        # client ips
        client_ips = []
        if "client_ips" in d.keys():
            for client_ip in d["client_ips"]:
                client_ips.append(str(client_ip))
        # log settings
        l_save_path = "logs/"
        l_amount_days_till_delition = 14
        l_log_std_out_daily = True
        if "log_settings" in d.keys():
            if "save_path" in d.keys():
                l_save_path = str(d["save_path"])
            if "amount_days_till_delition" in d.keys():
                l_amount_days_till_delition = int(d["amount_days_till_delition"])
            if "log_std_out_daily" in d.keys():
                l_log_std_out_daily = bool(d["log_std_out_daily"])
        log_settings = { \
                "save_path": l_save_path, \
                "amount_days_till_delition": l_amount_days_till_delition, \
                "log_std_out_daily": l_log_std_out_daily \
            }
        n = {"id": id, "client_ips": client_ips, "log_settings": log_settings}
        super(ServerSettings, self).__init__(n)

    def add_client_ip(self, client_ip: str):
        """
        Adds a client ip to the system
        """
        self.d["dependencies"].append(client_ip)

    def __str__(self) -> str:
        return str(self.dict())


def print_tasks(tasks:List[Task]):
    for task in tasks:
        print(task)


class Main:
    def run(self):
        # main
        # load db
        tasks_j = json.loads('[{"id": 1, "name": "task1", "dependencies":[{"dependency": "linux"},{"dependency": "python", "version": "3.6.8"}]}, {"id": 2, "name": "task2"}]')
        print(type(tasks_j[0]))

        # initialize objects
        tasks = []
        for task_j in tasks_j:
            tasks.append(Task(task_j))

        # del(tasks_j)
        tasks_j[0]["name"] = "blau"

        # work
        # ...
        print_tasks(tasks)

        print(json.dumps(tasks[0].dict()))


if __name__ == "__main__":
    main = Main()
    main.run()
