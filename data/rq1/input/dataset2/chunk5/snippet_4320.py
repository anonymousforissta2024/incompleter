#Source: https://stackoverflow.com/questions/61779471/i-kept-getting-typeerror-can-only-concatenate-str-not-nonetype-to-str
@app.route("/search", methods = ["GET", "POST"])
def search():
    if "user_email" not in session:
        return render_template("sign.html", error="Please Login First", work="Failed")

    if request.method == 'GET':
        title = request.form.get('title')
        isbn = request.form.get('isbn')
        author = request.form.get('author')     
        searchs = db.execute("SELECT * FROM books WHERE author iLIKE '%"+author+"%' OR title iLIKE '%"+title+"%' OR isbn iLIKE '%"+isbn+"%'").fetchall()
        return render_template('search.html', work = 'Success', searchs = searchs )