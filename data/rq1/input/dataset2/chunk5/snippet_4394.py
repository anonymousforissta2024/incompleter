#Source: https://stackoverflow.com/questions/75028036/flask-attributeerror-mysql-object-has-no-attribute-model
# msql_connector.py

from application import mysql


print(mysql)


conn = mysql.connect()
cursor = conn.cursor()


cursor.execute('''SHOW SCHEMAS;''')
rv = cursor.fetchall()

for db in rv:
    print(db)