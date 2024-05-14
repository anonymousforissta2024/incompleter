#Source: https://stackoverflow.com/questions/73786094/error-attributeerror-connection-object-has-no-attribute-fetchall
import sqlalchemy as sch
from config import Config

db_uri = os.environ["SQLALCHEMY_DATABASE_URI"] + os.environ["DB_NAME"]