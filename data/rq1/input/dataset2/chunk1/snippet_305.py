#Source: https://stackoverflow.com/questions/40511900/python-3-5-typeerror-a-bytes-like-object-is-required-not-str-using-truncate
@app.route("/")
def main():
    pages = db.session.query(Pages).all()
    return render_template('index.html', title='Dashboard', pages=pages)