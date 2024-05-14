#Source: https://stackoverflow.com/questions/69183938/python3-apache-mod-wsgi-filenotfounderror-is-not-defined
from flask import Flask


def create_app():
    app = Flask(__name__, instance_relative_config=False)

    @app.route("/")
    def home():
        import sys
        string = f"Python version {sys.version} Version info {sys.version_info}"
        return string

    return app