#Source: https://stackoverflow.com/questions/25491328/typeerror-when-creating-a-wtform-with-mongoengine-and-flask
@app.route('/blog/new')
def new():
    form = model_form(Post)
    return render_template('new_blog.html', form=form)