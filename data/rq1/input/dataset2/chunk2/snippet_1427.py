#Source: https://stackoverflow.com/questions/40892848/attributeerror-connection-object-has-no-attribute-fetchall
engine_str = 'mysql+mysqlconnector://my_username:my_pass@localhost/my_db'
engine = sqlalchemy.create_engine(engine_str, echo=False, encoding='utf-8')
connection = engine.connect()
query = "SELECT * from history_table"

connection.execute(query)
rows = connection.fetchall()