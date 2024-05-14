#Source: https://stackoverflow.com/questions/47405131/flask-type-error-list-object-not-callable
@app.route('/DeleteRow', methods=['POST'])
def signUpUser():
    if request.method == "POST":
        clicked=request.form.getlist('id[]')
    print(clicked[0])