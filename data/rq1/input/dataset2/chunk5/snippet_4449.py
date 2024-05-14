#Source: https://stackoverflow.com/questions/59291245/flask-login-attributeerror-int-object-has-no-attribute-is-authenticated
class UserData(UserMixin):
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self._authenticated = False

    def is_authenticated(self):
        return self._authenticated

    def is_active(self):
            return True
        # return true if user is activte and authenticated

    def is_annonymous(self):
        return False
        # return true if annon, actual user return false

    def get_id(self):
        global connection
        user_id = get_user_id(self.username, connection)
        unicode_user_id = load_user(user_id)
        if unicode_user_id != 0:
            self._authenticated = True

        print("userid:" , unicode_user_id)
        return unicode_user_id