""" Website init file """
import os
from flask import Flask
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
API_KEY = os.environ.get('API_KEY')

def create_app():
    """ Create app function """
    app = Flask(__name__)

    from .views import views
    app.register_blueprint(views)

    if API_KEY is None:
        raise Exception(f'API_KEY not found, value: {API_KEY}')
    return app
