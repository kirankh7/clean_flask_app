from flask import Flask,render_template,request, current_app
from app import db
from datetime import datetime
import pytz


# First / root of the flask app
@app.route('/hello.html') # same hello_world
@app.route('/')
def hello_world():
    message = "Hello World!  {}".format(get_pst_time())
    image_src = "https://s3.amazonaws.com/kiran-test-2/cruiser80.jpg"

    return render_template("hello.html",
                           src_hello=message,
                           image_name=image_src
                           )
    # return message



# pass some values
@app.route('/surnames/')
def get_surname(surname="Enter Name=Some Name"):
    query_val = request.args.get("Name", surname)
    get_surname = query_val.split()
    return '<p>Name Is : {}<p/>'.format("".join(get_surname[1:]))

# This route must print database connetion
# Check Connection Auth in infinete While loop & sleep for 5 minute
# Configure db config using chef
# SQLAlchemy
@app.route('/hello')
def health_rds():
    return "OK"

# '/diag' must print
# 1. Number of instance in the region
# 2. Version from the Nginx(Configure something into setting with using chef)
# 3. Health of each instance name: try to get instance IP get /hello


@app.route('/diag')
def status_cheker():
    return "OK"

class Publication(db.Model):
    __tablename__ = 'publication'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __repr__(self):
        return 'The id is {}, Name is is {}'.format(self.id, self.name)
