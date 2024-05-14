#Source: https://stackoverflow.com/questions/52841747/create-dictionary-from-mysql-attributeerror-tuple-object-has-no-attribute-na
cursor = conn.cursor()

cursor.execute("select server_id, name from servers")

dict = {}
for row in cursor:
    dict[row.server_id] = row.name

    print(dict)