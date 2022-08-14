from flask import Flask
from config import Config


def create_app(config_class=Config):
    print('SA')
    app = Flask(__name__)
    app.config.from_object(config_class)
    with app.app_context():
        import main
    return app
