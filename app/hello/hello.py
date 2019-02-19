from flask import render_template,request, current_app
from datetime import datetime
import pytz



from . import hello
from ..models import DatabaseTables,db



# First / root of the flask app
@hello.route('/')
def hello_world():
    message = "Hello World!  {}".format(get_pst_time())
    image_src = "https://s3.amazonaws.com/kiran-test-2/cruiser80.jpg"

    # Database
    db_string = DatabaseTables.query.all
    me = DatabaseTables(2, 'Kiran Haridas')
    db.session.add(me)
    db.session.commit()


    return render_template("hello.html",
                           src_hello=message,
                           image_name=image_src,
                           db_message=db_string
                           )
def get_pst_time():
    # date_format = '%m/%d/%Y %H:%M:%S %Z'
    date = datetime.now(tz=pytz.utc)
    date = date.astimezone(pytz.timezone('US/Pacific'))
    return str(date) + " PST"

def string_from_db():
    pass
