# import boto3
from flask import render_template
import boto.utils
import boto.ec2
from . import diag
import requests

@diag.route('/diag')
def diagnose_metrics():
    data = boto.utils.get_instance_identity()
    region_name = data['document']['region']
    conn = boto.ec2.connect_to_region(region_name)
    count = 0
    server_list = []
    for instance in conn.get_only_instances():
        count += 1
        server_list.append(instance)


    # nginx version


    return render_template('diag.html',
                           region = region_name,
                           instance_count=count,
                           instance_ids=server_list,
                           nginx_version=get_nginx_version()
                           )


def get_nginx_version():
    r = requests.get('http://flaskapp.thebetterengineers.com')
    val = r.headers
    return val.get('Server')


