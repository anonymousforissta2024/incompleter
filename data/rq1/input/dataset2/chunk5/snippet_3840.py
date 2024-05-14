#Source: https://stackoverflow.com/questions/60849950/typeerror-tuple-indices-must-be-integers-or-slices-not-str-python-flask
from app import app
if __name__ == '__main__':
    app.run(debug=True, port=5000)