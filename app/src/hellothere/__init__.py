from flask import Flask
from hellothere.config import Config


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    from hellothere.health.routes import health
    from hellothere.errors.handlers import errors
    from hellothere.main.routes import main

    app.register_blueprint(main)
    app.register_blueprint(errors)
    app.register_blueprint(health)

    return app
