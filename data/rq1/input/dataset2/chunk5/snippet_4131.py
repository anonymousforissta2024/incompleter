#Source: https://stackoverflow.com/questions/60849950/typeerror-tuple-indices-must-be-integers-or-slices-not-str-python-flask
from app import app, conn, bcrypt
from flask import request, jsonify
from flask_bcrypt import Bcrypt, check_password_hash
from datetime import datetime
import logging
from flask_jwt_extended import create_access_token

# registration api #################################################33


@app.route('/users/register', methods=['POST'])
def register():

    try:
        cur = conn.cursor()
        first_name = request.get_json()['first_name']
        last_name = request.get_json()['last_name']
        email = request.get_json()['email']
        password = bcrypt.generate_password_hash(
            request.get_json()['password']).decode('utf-8')
        created = datetime.utcnow()

        cur.execute("INSERT INTO admin.admin(first_name,last_name,email,password,created) VALUES('" +
                    str(first_name) + "','" +
                    str(last_name) + "','" +
                    str(email) + "','" +
                    str(password) + "','" +
                    str(created) + "')")
        conn.commit()
        result = {
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "password": password,
            "created": created
        }
        return jsonify({"result": result})
    except Exception as e:
        conn.rollback()
        logging.error("db error:{}".format(e))

##########################LOGIN API#######################################


@app.route('/users/login', methods=['POST'])
def login():


        cur = conn.cursor()
        email = request.get_json()['email']
        password = request.get_json()['password']
        result = ""
        cur.execute("SELECT * FROM admin.admin WHERE email='" +
                    str(email) + "'")
        rv = cur.fetchone()

        if bcrypt.check_password_hash(rv['password'], password):

            access_token = create_access_token(identity={'first_name': rv['first_name'], 'last_name': rv['last_name'], 'email': rv['email']})
            result = jsonify({"token": access_token})
        else:
            result = jsonify({"error": "invalid username and password"})
            return result