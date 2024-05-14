#Source: https://stackoverflow.com/questions/62856777/deploying-flask-app-with-postgresql-and-getting-attributeerror-nonetype-objec
app = Flask(__name__)

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


##where to find the database and initialize SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app) 


##option to tell SQLALchemy that for every model it should just 
#look at the columns that already exist in the table. This is called reflecting
db.Model.metadata.reflect(db.engine)

class Congress(db.Model):
    __tablename__ = 'sen'
    __table_args__ = { 'extend_existing': True }
    id = db.Column(db.Text, primary_key=True) 