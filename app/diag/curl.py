import requests

def get_nginx_version():
    r = requests.get('http://flaskapp.thebetterengineers.com')
    val = r.headers
    nginx_version = val.get('Server')


