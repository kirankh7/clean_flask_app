from flask import render_template,request, current_app


from . import health

@health.route("/health")
def check_rds_conn():
    return "Ok"



