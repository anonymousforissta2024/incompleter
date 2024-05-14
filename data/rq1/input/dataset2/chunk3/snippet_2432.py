#Source: https://stackoverflow.com/questions/69692529/typeerror-object-of-type-foo-is-not-json-serializable-in-array
import flask
from flask import request, jsonify
import uuid

app = flask.Flask(__name__)
app.config["DEBUG"] = True

class Pet:
    def __init__(self,id, name, dateOfBirth):
      self.id = id.hex
      self.name = name
      self.dateOfBirth = dateOfBirth
#    def to_json(obj):
#        return json.dumps(obj, default=lambda obj: obj.__dict__)

# Create some test data for our catalog in the form of a list of dictionaries.
pets = [ Pet(uuid.uuid4(),'Hamster', '02.12.2019' )]
pets.append( Pet(uuid.uuid4(),'Fish', '07.03.1985' ))
pets.append( Pet(uuid.uuid4(),'Dog', '26.11.2000' ))
pets.append( Pet(uuid.uuid4(),'Cat', '17.05.2021' ))

@app.route('/', methods=['GET'])
def home():
    return "<h1>Petshop Archive</h1><p>This site is a prototype API for the petshop archive.</p>"

# A route to return all of the available entries in our catalog.
@app.route('/api/v1/resources/pets/all', methods=['GET'])
def api_all():
    return jsonify(pets)

if __name__ == '__main__':
    app.run(host='0.0.0.0')