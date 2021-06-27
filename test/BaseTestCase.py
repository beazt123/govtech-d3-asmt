import sys
sys.path.append("..\\")

from flask import Flask
from flask_testing import TestCase
import backend.database
from unittest.mock import patch, Mock
from backend.routes.urlshortener import bp


class BaseTestCase(TestCase):
    @patch.object(backend.database,"db", side_effect=Mock)
    def create_app(self, mockSQL):

        app = Flask(__name__)
        app.config['TESTING'] = True
        app.config["FLASK_ENV"] = "development"
        app.register_blueprint(bp)
        self.sqlite = mockSQL
        
        return app