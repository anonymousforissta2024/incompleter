#Source: https://stackoverflow.com/questions/12518594/get-typeerror-when-trying-to-get-all-rows-from-mysql
query = conn.cursor()
query.execute("SELECT * FROM wp_options")
for row in query:
    print(row)
query.close()