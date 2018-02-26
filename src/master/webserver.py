# imports
from flask import Flask
from flask import redirect, url_for, request, render_template
# this module imports
from .task_manager_interface import ITaskManager
from .executor import IExecutor


class Webserver(object):
    """
    TaskManger Webserver

    Can access functions on the task_manager, for Example to execute tasks or add new one.
    """

    def routes(self):
        @self.app.route('/')
        def index():
            return render_template('index.html')
        @self.app.route('/hello/<string:name>')
        def hello_world(name: str):
            return render_template('hello.html', name=name)

    def __init__(self, task_manager: ITaskManager, host: str="0.0.0.0", port: int=5000, debug: bool=False):
        """Initial function"""
        self.task_manager = task_manager
        self.host = host
        self.port = port
        self.debug = debug
        self.app = Flask(__name__)

    def start(self):
        self.routes()
        self.app.run(self.host, self.port, self.debug)


class WebserverManager(object):
    pass
