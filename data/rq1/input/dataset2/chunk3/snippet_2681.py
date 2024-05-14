#Source: https://stackoverflow.com/questions/55814099/flask-sqlalchemy-attributeerror-user-query-attribute-is-none
user = db_user.find_user(username=username, password=password)
# it raises: `AttributeError: 'NoneType' object has no attribute 'filter_by'`

user = User.query.filter_by(username=username, password=password).all()
# it raises: `AttributeError: 'NoneType' object has no attribute 'filter_by'`

user = User.query.filter(username=username, password=password).all()
# it raises: `AttributeError: 'NoneType' object has no attribute 'filter'`