#Source: https://stackoverflow.com/questions/55708257/flask-attributeerror-module-object-has-no-attribute-app
import flask_lab.app

print(flask_lab.app.db)


def demo():
    print('yeah!')