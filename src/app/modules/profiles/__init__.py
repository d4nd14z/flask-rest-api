from flask import Blueprint

bp = Blueprint("profiles", __name__)

from app.modules.profiles import routes
