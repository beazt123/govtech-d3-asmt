from flask import Flask
from .lib.utils import serverResponse

def create_app():
    app = Flask(__name__)



    @app.route('/', methods=["GET", "POST"])
    def hello_world():
        return serverResponse(None, 200, "Yes this endpoint is working")

    return app
    


