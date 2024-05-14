#Source: https://stackoverflow.com/questions/62016881/python-flask-sqlalchemy-attributeerror-table-object-has-no-attribute-added
from TasMar import db,create_app
from TasMar.models import User,Tasks,tm_status, tm_urgency,tm_type
app=create_app()
app.app_context().push()
#db.create_all()   #<<works perfectly but not below !
user = User.query.filter_by(email='dummy@email.com').first()
print(user)