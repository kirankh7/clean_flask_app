import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .config import config

db = SQLAlchemy()
migrate = Migrate()


def create_app(config_name=None):
    if config_name is None:
        config_name = os.environ.get('FLASK_ENV', 'default')
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    db.init_app(app)
    migrate.init_app(app, db)

    from .hello.hello import hello
    from .health.health import health
    from .diag.diag import diag
    from .ai.ai import ai
    app.register_blueprint(hello)
    app.register_blueprint(health)
    app.register_blueprint(diag)
    app.register_blueprint(ai)

    return app
