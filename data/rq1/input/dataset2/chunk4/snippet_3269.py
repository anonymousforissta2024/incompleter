#Source: https://stackoverflow.com/questions/67992681/typeerror-not-all-arguments-converted-during-string-formatting-when-pymysql-c
sql = 'create table if not exists currency(t integer primary key, prediction real default null, realVal real default null)'
cursor.execute(sql)