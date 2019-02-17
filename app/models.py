from flask_sqlalchemy import SQLAlchemy
from flask import current_app

db = SQLAlchemy()

#
# db.config.update(
#     SECRET_KEY= 'Avankia1',
#     SQLALCHEMY_DATABASE_URI='postgresql://rooter:Avankia1@kiran-db.c09ylvqoqhhn.eu-west-1.rds.amazonaws.com/flaskdb',
#     SQLALCHEMY_TRACK_MODIFICATIONS=True
# )

class DBProfile(db.Model):
    __tablename__ = 'flask_app'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __repr__(self):
        return 'The id is {}, Name is is {}'.format(self.id, self.name)
