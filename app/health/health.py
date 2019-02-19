from flask import render_template,request, current_app
from ..models import DatabaseTables,db


from . import health

@health.route("/health")
def check_rds_conn():
    validation = ""
    try:
        db.session.query("1").from_statement("SELECT 1").all()
        validation = 'OK'
    except:
        validation = 'ERROR'
    return render_template("health.html", validation_msg=validation)



