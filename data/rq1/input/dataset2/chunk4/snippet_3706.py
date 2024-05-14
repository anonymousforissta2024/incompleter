#Source: https://stackoverflow.com/questions/49249504/typeerror-argument-of-type-datetime-date-is-not-iterable
connection = MySQLdb.connect(host = "192.168.1.50", user = "root", 
password = "root", db = "mydb", port = 32768)
cursor = connection.cursor()
cursor.execute("select * from licenses")
data = cursor.fetchall()