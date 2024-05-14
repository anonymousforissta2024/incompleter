#Source: https://stackoverflow.com/questions/74107311/attributeerror-legacycursorresult-object-has-no-attribute-user-name
from dataclasses import fields
import datetime
import json
from typing_extensions import Required
from unittest import result
from sqlalchemy import DateTime
from email.policy import default, strict
from flask import Flask, jsonify, request, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy.sql import text, func
from flask_marshmallow import Marshmallow
from marshmallow import Schema, fields, validates, ValidationError, validate
from sqlalchemy.sql import select, insert, bindparam
from sqlalchemy.dialects.postgresql import UUID
import uuid
from werkzeug.security import generate_password_hash,check_password_hash
from sqlalchemy import create_engine
import logging
# from flask_jwt_extended import get_jwt_identity,JWTManager, jwt_required, create_access_token, create_refresh_token
from functools import wraps
import jwt

engine = create_engine('mysql://root:admin@172.17.0.2:3306/flask')


app = Flask(_name_)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:admin@172.17.0.2:3306/flask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['SECRET_KEY'] = 'thisissecret'
app.config['SECRET_KEY'] = 'super-secret' 
db = SQLAlchemy(app)
ma= Marshmallow(app)
migrate = Migrate(app, db)
# jwt = JWTManager(app)









class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    email_address = db.Column(db.String(80), unique=True, nullable=False)
    dob = db.Column(db.DateTime, nullable=True)
    address = db.Column(db.String(200))
    uid = db.Column(db.Text(length=16), nullable = False)

    def _init_(self, user_name, password, email_address, dob, address, uid):
        self.user_name = user_name
        self.password = password
        self.email_address = email_address
        self.dob = dob
        self.address = address
        self.uid = uid

# User Schema
class UserSchema(Schema):
    print("Scehma")

    user_name = fields.String(required=True, validate=validate.Length(min=5))
    password = fields.String()
    # email_address = fields.String(required=True, error_messages={"required": " email_address is required. "})
    email_address = fields.String()
    dob = fields.DateTime()
    address = fields.String()
    uid = fields.UUID( error_messages={'null': 'Sorry, Id field cannot be null', 'invalid_uuid': 'Sorry, Id field must be a valid UUID'})

    print("access")

    @validates('dob')
    def is_not_in_future(self,value):
        """'value' is the datetime parsed from time_created by marshmallow"""
        now = datetime.datetime.now()
        if value > now:
            raise ValidationError("Can't create notes in the future!")
        # if the function doesn't raise an error, the check is considered passed

    class Meta:
        # Fields to show when sending data
        fields = ('id','user_name', 'password', 'email_address', 'dob', 'address', 'uid')   


#init Schema

user_schema = UserSchema()
users_scehma = UserSchema(many=True)

@app.route('/login', methods=['POST'])
def login():
    # print("login") 
    # # request_data= user_schema.load(request.get_json()) 
    request_data = request.get_json()
    user_name=request_data['user_name']
    password=request_data['password']
    # conn = engine.connect()
    # data=conn.execute("""SELECT user_name, password, uid FROM user WHERE user_name = user_name""",{"user_name": user_name})
    # user = data.mappings().all()
    # print(user)
    #   return jsonify({'Message':'login user'})

    auth= user_schema.load(request.get_json())
    if not auth or not auth.get('user_name') or not auth.get('password'):
        return make_response('Could not verify!', 401, {'WWW-Authenticate': 'Basic-realm= "Login required!"'})

    conn = engine.connect()
    # sql= text(f"SELECT id, user_name, email_address, dob, uid FROM user WHERE user_name = '{auth['user_name']}' and password = '{auth['password']}'")
    result = conn.execute(text("SELECT id, user_name, email_address, dob, uid FROM user WHERE user_name = :user_name and password = :password"), [{"user_name": user_name, "password": password}],)
    print(result.all())
    for row in result:
        print(f"id: {row.id}  user_name: {row.user_name} email_address: {row.email_address} dob: {row.dob} uid: {row.uid}")
    # rows= conn.execute(sql)
    # for result in rows:
    #     print(f"result : {result} ")
    

   
    
    if user_name != result.user_name  :
        return make_response('Could not verify user, Please signup!', 401, {'WWW-Authenticate': 'Basic-realm= "No user found!"'})

    if check_password_hash(result.password, auth.get('password')):
        token = jwt.encode({'uid': result.uid}, app.config['SECRET_KEY'], 'HS256')
        return make_response(jsonify({'token': token}), 201)

    return make_response('Could not verify password!', 403, {'WWW-Authenticate': 'Basic-realm= "Wrong Password!"'})


if _name_ == '_main_':
    app.run(debug=True)