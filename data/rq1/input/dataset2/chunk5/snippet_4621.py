#Source: https://stackoverflow.com/questions/59291245/flask-login-attributeerror-int-object-has-no-attribute-is-authenticated
@login_manager.user_loader
def load_user(user_id):
    return int(user_id)