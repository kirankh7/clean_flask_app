import os
from flask import Blueprint, jsonify

diag = Blueprint('diag', __name__)


@diag.route('/diag')
def diag_check():
    return jsonify(
        status='ok',
        service='clean_flask_app',
        version='2.0.0',
        env=os.environ.get('FLASK_ENV', 'unknown'),
    )
