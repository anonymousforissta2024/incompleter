#Source: https://stackoverflow.com/questions/67089815/flask-image-cant-upload-filenotfounderror-errno-2-no-such-file-or-directory
@app.route('/upload',methods=['POST'])
def upload():
    title = request.form['title']
    context = request.form['text']
    author = request.form['author']
    img=request.files['img']
    path = os.path.join(app.root_path,'/images',img.filename)
    img.save(path)

    new=Posts(title=title,context=context,image=path,author=author)
    db.session.add(new)
    db.session.commit()

    return redirect(url_for('blog'))