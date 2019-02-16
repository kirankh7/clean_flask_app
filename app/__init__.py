from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import Config

#
#
# # Creating an instance of the Flask(kind of module)
# app = Flask(__name__)
#
# # Passing configs from Json file
# app.config.from_object(Config)
#
# app.config.update(
#     SECRET_KEY= 'Avankia1',
#     SQLALCHEMY_DATABASE_URI='postgresql://rooter:Avankia1@kiran-db.c09ylvqoqhhn.eu-west-1.rds.amazonaws.com/flaskdb',
#     SQLALCHEMY_TRACK_MODIFICATIONS=True
# )

# pass db instance
db = SQLAlchemy()




def create_app(confi_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    from app.hello.hello import hello
    from app.health.health import health
    from app.diag.diag import diag

    app.register_blueprint(hello)

    return app




