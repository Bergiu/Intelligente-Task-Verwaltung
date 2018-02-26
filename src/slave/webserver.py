# imports
import json
from flask import Flask
from flask import redirect, url_for, request, render_template
# this module imports

class Webserver(object):
    """
    TaskManger slave Webserver
    """

    def routes(self):
        @self.app.route('/')
        def index():
            return render_template('index.html')
        @self.app.route('/execute/<int:task_id>')
        def execute(task_id: int):
            j = dict()
            j["successful"] = True
            return json.dumps(j)

    def __init__(self, host: str="0.0.0.0", port: int=5000, debug: bool=False):
        """Initial function"""
        self.host = host
        self.port = port
        self.debug = debug
        self.app = Flask(__name__)

    def start(self):
        self.routes()
        self.app.run(self.host, self.port, self.debug)


def run():
    webserver = Webserver(debug=True)
    webserver.start()

