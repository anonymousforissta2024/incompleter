#Source: https://stackoverflow.com/questions/55063427/flask-blueprint-returns-nameerror-when-trying-to-register-blueprint-on-the-app-i
from app.i_statement import i_statement_bp
app.register_blueprint(i_statement_bp) 