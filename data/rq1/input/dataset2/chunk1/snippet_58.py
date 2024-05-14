#Source: https://stackoverflow.com/questions/61665661/how-to-solve-attribute-error-cursor-object-has-no-attribute-nocursortimeout
from pymongo import MongoClient as Connection
from datetime import datetime

conn = Connection(get_uri())
with conn as conn:
  collection = conn['db_name']['my_collection']
  documents_cursor = collection.find(query).noCursorTimeout() # same with .maxTimeMS()