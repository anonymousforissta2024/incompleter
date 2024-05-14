#Source: https://stackoverflow.com/questions/65012433/identifying-location-of-error-typeerror-nonetype-object-is-not-subscriptable
from flask import Flask, request, jsonify

from Service import ToDoService
from models import Schema

app = Flask(__name__)

@app.route("/todo", methods=["GET", "POST"])
def create_todo():
    return jsonify(ToDoService().create(request.get_json()))

if __name__ == "__main__":
    Schema()
    app.run(debug=True)