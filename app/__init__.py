from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import Config
from app.models import db
from flask_migrate import Migrate

# # Creating an instance of the Flask(kind of module)
# app = Flask(__name__)

# # Passing configs from Json file
# app.config.from_object(Config)

# pass db instance
# db = SQLAlchemy()


def create_app(confi_class=Config):
    app = Flask(__name__)

    app.config.from_object(Config)

    # DB Settings

    from app.models import db
    db.init_app(app)

    migrate = Migrate(app, db)


    from app.hello.hello import hello
    from app.health.health import health
    from app.diag.diag import diag

    app.register_blueprint(hello)
    app.register_blueprint(health)
    app.register_blueprint(diag)

    return app




