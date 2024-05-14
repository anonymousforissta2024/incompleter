#Source: https://stackoverflow.com/questions/64755775/python-marshmallow-attributeerror-list-object-has-no-attribute-get
data = UserSchema(many=True).load(input_data)