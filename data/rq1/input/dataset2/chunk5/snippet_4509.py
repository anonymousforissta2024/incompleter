#Source: https://stackoverflow.com/questions/74596527/nameerror-name-alltodos-is-not-defined-unboundlocalerror-local-variable-a
from flask import Flask, render_template ,request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
db = SQLAlchemy(app)


class Todo(db.Model):
    SNumber = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(200),nullable=False)
    desc = db.Column(db.String(500),nullable=False)
    data_created = db.Column(db.DateTime, default = datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.SNumber} - {self.title}"


@app.route('/' , methods=['GET','POST'])
def hello_world():
    if request.method == 'POST':
        title = request.form['title']
        desc = request.form['desc']
        todo = Todo(title = title, desc = desc)
        db.session.add(todo)
        db.session.commit()
        
        allTodos = Todo.query.all()
        
    return render_template('index.html',allTodo=allTodos)
        
    

@app.route('/show')
def products():
    #allTodo = Todo.query.all()
    #print(allTodo)
    return "this is a product page"    

if __name__ == "__main__":
    app.run(debug=True)