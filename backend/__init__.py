from flask import Flask
from flask_cors import CORS
from .database import db
from .lib.utils import serverResponse
from .routes.urlshortener import bp
from .commands import create_tables


def create_app(config_file):
    app = Flask(__name__)
    app.config.from_pyfile(config_file)

    
    db.init_app(app)
    CORS(app)



    @app.route('/health', methods=["GET"])
    def hello_world():
        return serverResponse(
            None, 
            200, 
            "Yes this server is alive"
            )


    app.register_blueprint(bp)

    app.cli.add_command(create_tables)
    return app
    


