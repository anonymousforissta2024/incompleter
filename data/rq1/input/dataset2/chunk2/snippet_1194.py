#Source: https://stackoverflow.com/questions/68263163/attributeerror-set-object-has-no-attribute-sa-instance-state-sqlalchemy
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

schema_name = 'Traffic'

engine = create_engine('postgresql://xxx:xxx@localhost:5432/xxx')

if not engine.dialect.has_schema(engine, schema_name):
    engine.execute(sqlalchemy.schema.CreateSchema(schema_name))

Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()