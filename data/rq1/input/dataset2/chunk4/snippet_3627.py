#Source: https://stackoverflow.com/questions/71359706/flask-login-attributeerror-str-object-has-no-attribute-is-active
@admin.route('/', methods=['GET'])
def index():
    form = admin_login()
    return render_template('login.html', form=form)

@admin.route('/', methods=['POST'])
def index_post():
    form = admin_login()
    user = form.name.data
    password = form.password.data
    remember = form.remember.data
    user_check = Admin.query.filter_by(username=user).first()
    if user_check:
        password_check = check_password_hash(user_check.password, password)
        if password_check:
            login_user(user)
            return redirect(url_for('admin.search'))