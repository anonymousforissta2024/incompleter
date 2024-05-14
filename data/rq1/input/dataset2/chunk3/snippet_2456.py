#Source: https://stackoverflow.com/questions/61911606/typeerror-int-object-is-not-iterable-when-executin-sql-with-set-in-python3
cursor = connection.cursor()
sql="SELECT id, name, state FROM domain WHERE state='2'"
cursor.execute(sql)
records = cursor.fetchall()
print("Total number of records for deleting is: ", cursor.rowcount)

deleted = set(cursor.execute("select distinct name from domain where state = 2"))
active = set(cursor.execute("select distinct name from domain where state != 2"))

to_delete = deleted - active

print('Printing each domain record', "\n")
for row in records:

    print("id = ", row["id"], )
    print("name = ", row["name"])
    print("state  = ", row["state"], "\n")

    id = row["id"]
    name = row["name"]
    state = row["state"]

    if to_delete == 2:
        try:
            if os.path.exists('/data/sa/' + name):
                print('found records for deleting: ' + name, "\n")
                print("Total number of records for deleting is: ", cursor.rowcount)
                input("Press Enter to continue...")
                shutil.rmtree('/data/sa/' + name)
                print('records deleted')            
            else:
                print('no Directory found')
        #    pass
        except Exception as error:
            print("Directory already deleted or never existed")
    else:
        print('no records for deleting found')
        print('domain', name)
        print('hast state', state, "\n")

quit()
connection.close()