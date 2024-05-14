#Source: https://stackoverflow.com/questions/56044891/typeerror-module-object-is-not-callable-flask-jwt
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token, create_refresh_token, get_jwt_identity, jwt_refresh_token_required
)

@app.route('/api/users/validate', methods=['POST'])
def validate_user():

    if not request.json:
        abort(400)

    data = request.get_json()

    if ('id_token' not in data):
        abort(400, "id_token must be a parameter in the JSON")

    decoded_token = auth.verify_id_token(data['id_token'])

    if ('uid' not in decoded_token):
        return json.dumps({'verified': False}), 200
    else:
        user = mongo.db.users.find_one({'_id': decoded_token['uid']})

        if user:
            access_token = create_access_token(identity=user['_id'])
            refresh_token = create_refresh_token(identity=user['_id'])
            return json.dumps({'verified': True, 'access_token': access_token, 'refresh_token': refresh_token}), 200
        else:
            return json.dumps({'verified': False, 'message': 'unable to locate user'}), 401