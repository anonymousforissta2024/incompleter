#Source: https://stackoverflow.com/questions/50647042/typeerror-object-supporting-the-buffer-api-required-in-flask-api
class UserLogin(Resource):
    def post(self):

            # Parse the arguments

            parser = reqparse.RequestParser()
            parser.add_argument('username')
            parser.add_argument('password')
            args = parser.parse_args()

            _user = args['username']
            _userPassword = args['password']
            _h = hashlib.md5(_userPassword.encode())
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute('''select * from user where username = %s && password = %s''', (_user, _h))
            data = cursor.fetchall()

            return jsonify(data)