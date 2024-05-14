#Source: https://stackoverflow.com/questions/61298742/why-am-i-getting-a-typeerror-string-indices-must-be-integers-error-on-strings
cursor.execute("SELECT id, name FROM playlists")
lists = cursor.fetchall()

for index, list in lists:
    print("{0} - {1}".format(list['id'], list['name']))