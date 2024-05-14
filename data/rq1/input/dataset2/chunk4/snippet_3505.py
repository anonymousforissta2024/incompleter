#Source: https://stackoverflow.com/questions/64090848/flask-and-wtforms-typeerror-unsupported-operand-types-for-nonetype-and
from flask import Flask, url_for, render_template, make_response, request, redirect, session
from forms import DecimalField, BooleanField 
import body_calculator  



app = Flask(__name__, static_folder='static',template_folder='templates')

@app.route('/', methods = ['GET','POST'])
def index():
    
    form = DecimalField()
    
    sex = request.form.get('sex')
    age = request.form.get('age')
    height = request.form.get('height')
    weight = request.form.get('weight')
    waist = request.form.get('waist')
    
    body = body_calculator.Parameters(height, weight, age, sex, waist)

    LBM = body.Body_Lean_Mass()
    BMR = body.Basal_Metabolic_Rate()
    BFP = body.Body_Fat_Percentage()
    BMI = body.Body_Mass_Index()

        
    context = {
        'int_form' : form,
        'LBM' : LBM,
        'BMR' : BMR,
        'BMI' : BMI
        }
    
    if request.method == 'POST' and form.validate():
        return render_template('index.html', **context)


if __name__ == "__main__":
    app.run(debug=True) 