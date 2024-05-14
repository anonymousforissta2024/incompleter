#Source: https://stackoverflow.com/questions/47422466/type-error-in-pymysql-cursor
connection = pymysql.connect(host = "localhost",
                     user = "root",
                     passwd = "",
                     db = "bugs",
                     charset = "utf8mb4",
                     cursorclass = "pymysql.cursors.Dictcursor")

try:
    with connection.cursor() as cur:
        cur.execute('''SELECT COUNT(*) FROM tbl_firefox''')

        for row in cur.fetchall():
            print("Number of rows in firefox table:", row)
    connection.commit()
finally:
    connection.close()