from flask import Blueprint

diag = Blueprint("diag", __name__)

# ^^^^ coming
from . import diag
