#Source: https://stackoverflow.com/questions/63840413/typeerror-method-object-is-not-subscriptable-flask-sql
@app.route('/<string:autor>')
def iniciarSesion(autor):
    autor_id = db.execute("SELECT id FROM autores WHERE autor = :autor", {"autor":autor}).fetchone[0]
    return autor_id