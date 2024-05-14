#Source: https://stackoverflow.com/questions/60108174/typeerror-only-takes-2-positional-arguments-but-3-were-given
from flask import *
from flask_cqlalchemy import CQLAlchemy

app = Flask(__name__)
app.config['CASSANDRA_HOSTS'] = ['127.0.0.1']
app.config['CASSANDRA_KEYSPACE'] = "emp"

db = CQLAlchemy(app)

class Student(db.Model):
    uid = db.columns.Integer(primary_key=True)
    marks = db.columns.Integer(primary_key=True)
    username = db.columns.Text(required=True)
    password = db.columns.Text()

    @app.route('/meriting')
    def show_meritlist():
        ob = Student.objects().filter().only(Student.marks, Student.username)
        ob = ob.filter(Student.marks >= 65).allow_filtering()
        return render_template('merit.html', ml = ob)

db.sync_db()
if __name__ == '__main__':
    app.run(debug = True)