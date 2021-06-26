from flask import Flask
from .utils import serverResponse

def create_app():
    app = Flask(__name__)



    @app.route('/', methods=["GET", "POST"])
    def hello_world():
        return serverResponse(None, 200, "Yes this endpoint is working")

    return app
    


# if __name__ == '__main__':
#     # port = int(os.getenv('PORT', 5000))
#     # app.run(host='0.0.0.0', port=port, load_dotenv=".env")
#     app.run()
