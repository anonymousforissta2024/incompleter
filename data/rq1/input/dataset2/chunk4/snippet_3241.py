#Source: https://stackoverflow.com/questions/76844263/flaskapi-attributeerror-module-app-routers-api-has-no-attribute-register
from flask import Blueprint, request
from app.models import User
from app.db import get_db


bp = Blueprint('api', __name__, url_prefix = '/api')

@bp.route('/users', methods = ['POST'])
def signup():
    data = request.get_json()
    print(data)
    return ''