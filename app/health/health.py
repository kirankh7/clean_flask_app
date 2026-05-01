import time
from flask import Blueprint, jsonify

health = Blueprint('health', __name__)
_START = time.time()


@health.route('/health')
def health_check():
    return jsonify(status='ok', uptime_seconds=round(time.time() - _START))
