#Source: https://stackoverflow.com/questions/55805086/python-postgres-insert-error-typeerror-not-all-arguments-converted-during-stri
data1 = json.load(response)

volume = (len(data1['data']))


data = (data1["data"])

jsonstr = (json.dumps(data, indent=4))

print(jsonstr)

connection = psycopg2.connect("host=localhost dbname=xxx user=xxx password=xxx")

cur = connection.cursor()

connection.autocommit = True

query =  "INSERT INTO xxx.xxx (xxx) VALUES (%s);"
sql = "INSERT INTO xxx.xxx VALUES (%s)"
cur.execute(sql, jsonstr)