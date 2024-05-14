#Source: https://stackoverflow.com/questions/30032078/typeerror-init-takes-1-positional-argument-but-3-were-given
from app import app, db
from flask import render_template, request, url_for
from forms import CreateForm
from models import Post


@app.route('/')
def homepage():
    return render_template('base.html')


@app.route('/create', methods=['GET', 'POST'])
def create():
    form = CreateForm(csrf_enabled=False)
    if request.method == 'GET':
        return render_template('create.html', form=form)
    if request.method == 'POST':
        if form.validate_on_submit():
            create_post = Post(form.title.data, form.text.data)
            db.session.add(create_post)
            db.session.commit()
    return redirect(url_for('homepage'))