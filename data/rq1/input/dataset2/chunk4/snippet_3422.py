#Source: https://stackoverflow.com/questions/67992681/typeerror-not-all-arguments-converted-during-string-formatting-when-pymysql-c
data = [(1, 12.5), (2, 10.2)]
sql = 'insert into currency(t, prediction) values(%s, %s) on duplicate key update values prediction=values(prediction)'
cursor.execute(sql, data)