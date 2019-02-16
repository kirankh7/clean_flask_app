from flask import Flask
from flask_sqlalchemy import SQLAlchemy




# Creating an instance of the Flask(kind of module)
app = Flask(__name__)


#DB_URL = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(user=POSTGRES_USER,pw=POSTGRES_PW,url=POSTGRES_URL,db=POSTGRES_DB)
#database settings
app.config.update(
    SECRET_KEY= 'Avankia1',
    SQLALCHEMY_DATABASE_URI='postgresql://rooter:Avankia1@kiran-db.c09ylvqoqhhn.eu-west-1.rds.amazonaws.com/flaskdb',
    SQLALCHEMY_TRACK_MODIFICATIONS=True
)

# pass db instance
db = SQLAlchemy(app)

from app import routes