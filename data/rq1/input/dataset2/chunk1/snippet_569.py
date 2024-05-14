#Source: https://stackoverflow.com/questions/46111203/flask-dynamo-connection-issueattributeerror-dynamo-object-has-no-attribute
@app.route('/', methods=['GET'])
def hello_world():
    with app.app_context():
        dynamo.create_all()
    return 'table created!'