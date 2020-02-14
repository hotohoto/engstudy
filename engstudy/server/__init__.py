# pylint: disable=import-outside-toplevel, unused-import

from flask import Flask

app = None  # pylint: disable=invalid-name


def init_server():
    global app  # pylint: disable=global-statement, invalid-name
    app = Flask(__name__)

    # load controllers
    import engstudy.controllers.index
    import engstudy.controllers.login


init_server()
