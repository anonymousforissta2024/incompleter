#Source: https://stackoverflow.com/questions/73786094/error-attributeerror-connection-object-has-no-attribute-fetchall
db_connection.execute("select count(*) from table")
query_result = db_connection.fetchall()