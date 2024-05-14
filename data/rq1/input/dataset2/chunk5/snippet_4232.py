#Source: https://stackoverflow.com/questions/62016881/python-flask-sqlalchemy-attributeerror-table-object-has-no-attribute-added
from datetime import datetime
from TasMar import  db, login_manager
from flask import  current_app
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    __tablename__ = 'tm_user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20),unique=True, nullable=False)
    email = db.Column(db.String(120),unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password=  db.Column(db.String(120), nullable=False)

    #foreign keys accessing this table's primary keys
    added = db.relationship('Tasks', lazy=True, foreign_keys='tm_task.added_by')
    assigned = db.relationship('Tasks', lazy=True, foreign_keys='tm_task.assigned_to')

    def __repr__(self):
            return "User('{}','{}','{}')".format(self.username,self.email,self.image_file)


class Tasks(db.Model):
    __tablename__ = 'tm_task'
    task_id = db.Column(db.Integer, primary_key=True)
    parent_id = db.Column(db.Integer, db.ForeignKey('tm_task.task_id'),nullable=True)
    descr = db.Column(db.String(500), nullable=False)
    added_on = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    added_by = db.Column(db.Integer, db.ForeignKey('tm_user.id'),nullable=False)
    assigned_to = db.Column(db.Integer, db.ForeignKey('tm_user.id'),nullable=False)
    last_updated = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    remark = db.Column(db.Text)


    parent = db.relationship('Tasks', remote_side=[task_id]) #self referential
    status = db.Column(db.Integer, db.ForeignKey('tm_status.id'),nullable=False)
    type = db.Column(db.Integer, db.ForeignKey('tm_type.id'),nullable=False)
    urgency = db.Column(db.Integer, db.ForeignKey('tm_urgency.id'),nullable=False)

    def __repr__(self):
            return "Tasks('{}','{}','{}','{}')".format(self.descr,self.added_on,self.added_by,self.assigned_to)

class tm_status(db.Model):
    __tablename__ = 'tm_status'
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(20),unique=True,nullable=False)
    status_f = db.relationship('Tasks', lazy=True, foreign_keys='tm_task.status')

    def __repr__(self):
            return "tm_status('{}')".format(self.status)

class tm_type(db.Model):
    __tablename__ = 'tm_type'
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(20),unique=True,nullable=False)
    type_f = db.relationship('Tasks', lazy=True, foreign_keys='tm_task.type')

    def __repr__(self):
            return "tm_type('{}')".format(self.type)

class tm_urgency(db.Model):
    __tablename__ = 'tm_urgency'
    id = db.Column(db.Integer, primary_key=True)
    urgency = db.Column(db.String(20),unique=True,nullable=False)
    urgency_f = db.relationship('Tasks', lazy=True, foreign_keys='tm_task.urgency')

    def __repr__(self):
            return "tm_urgency('{}')".format(self.urgency)