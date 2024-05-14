#Source: https://stackoverflow.com/questions/73786094/error-attributeerror-connection-object-has-no-attribute-fetchall
db_engine = extrac_db.create_engine(Config.db_uri)
db_connection = db_engine.connect()