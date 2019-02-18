import boto3
from . import diag


@diag.route('/diag')
def diagnose_metrics():

    ec2 = boto3.client('ec2')
    instance_information = ec2.describe_instances()

    for reservation in instance_information['Reservations']:
        for instance in reservation['Instances']:
            print(instance['InstanceId'])
