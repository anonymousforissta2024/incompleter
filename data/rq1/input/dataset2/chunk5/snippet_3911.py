#Source: https://stackoverflow.com/questions/59296980/attributeerror-blueprint-object-has-no-attribute-teardown-appcontext-in-goo
#!/home/kimdev/Documents/pythonwebapp/flask_v1/bin/python3

import os
import yaml
import datetime

from flask         import Flask, session, make_response, request, url_for, redirect
from flask_mysqldb import MySQL
from functools     import wraps

def _directory():
    return os.path.dirname(os.path.abspath(__file__))

def _file(fileTarget):
    return os.path.join(_directory(), fileTarget)

def isFileExists(fileTarget):
    return os.path.exists(_file(fileTarget))

def cookieCheckActive(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        _active = request.cookies.get('_active', '')
        _u      = request.cookies.get('_u', '')

        if _active != '' and _active == '1' and 'login' not in session:
            session['login']  = '1'
            session['userID'] = _u

            return redirect(url_for('business_dashboard.dashboard'))
        else:
            return f(*args, **kwargs)
    return wrapper

def ifLogin(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if 'login' in session and session['login'] == '1':
            return redirect(url_for('business_dashboard.dashboard'))
        else:
            return f(*args, **kwargs)
    return wrapper

def ifNotLogin(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        cookieUserID = request.cookies.get('_u', '') if '_u' in request.cookies else None

        if 'login' not in session:
            return redirect(url_for('business_login.login'))
        # elif cookieUserID == None:
        #     '''
        #         I'm so confuse with this block of code; cause if i will not
        #         remember my session eventhough it must equals to NONE it return
        #         to true and store the cookie but when i reverse it, then the trouble
        #         comes in when you are logging in.
        #     '''
        #     if cookieUserID != session['userID']:
        #         session.clear()
        #
        #         today   = datetime.datetime.now()
        #         expires = datetime.timedelta(days=1)
        #         expires = today - expires
        #
        #         response = make_response(redirect(url_for('business_login.login')))
        #
        #         response.set_cookie('_u', '', expires = expires)
        #         response.set_cookie('_active', '', expires = expires)
        #
        #         return response
        else:
            return f(*args, **kwargs)
    return wrapper

app = Flask(__name__)

app.secret_key = b'\x0c\xcd\xc4\x95ri\xb9\xb2O\xea\xd9\xea\x87&*\xb3'

_dbconfig = yaml.load(open(_file('config/dbconnection.yaml')), Loader = yaml.FullLoader)

app.config['MYSQL_HOST']        = _dbconfig['DB_HOST']
app.config['MYSQL_USER']        = _dbconfig['DB_USERNAME']
app.config['MYSQL_PASSWORD']    = _dbconfig['DB_PASSWORD']
app.config['MYSQL_DB']          = _dbconfig['DB_NAME']
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

_mysql = MySQL(app)

from blueprints import *

@app.errorhandler(404)
def page_not_found(error):
    return 'page not found', 404

@app.context_processor
def inject_dateYear():
    return {'dateYear': datetime.datetime.now().strftime('%Y')}

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080, debug=True)