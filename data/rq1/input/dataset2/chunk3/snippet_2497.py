#Source: https://stackoverflow.com/questions/69692529/typeerror-object-of-type-foo-is-not-json-serializable-in-array
import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Create some test data for our catalog in the form of a list of dictionaries.
books = [
    {'id': 0,
     'title': 'A Fire Upon the Deep'},
    {'id': 1,
     'title': 'The Ones Who Walk Away From Omelas'},
    {'id': 2,
     'title': 'Dhalgren'}
]

@app.route('/', methods=['GET'])
def home():
    return '''<h1>Distant Reading Archive</h1>
<p>A prototype API for distant reading of science fiction novels.</p>'''

# A route to return all of the available entries in our catalog.
@app.route('/api/v1/resources/books/all', methods=['GET'])
def api_all():
    return jsonify(books)

app.run()