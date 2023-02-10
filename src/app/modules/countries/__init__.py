from flask import Blueprint

bp = Blueprint("countries", __name__)

from app.modules.countries import routes