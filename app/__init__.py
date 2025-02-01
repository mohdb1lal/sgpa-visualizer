from flask import Flask
from config import Config
import os

def create_app(config_class=Config):
    app = Flask(__name__, template_folder=os.path.abspath('templates'))
    app.config.from_object(config_class)

    from app.routes import bp
    app.register_blueprint(bp)

    return app