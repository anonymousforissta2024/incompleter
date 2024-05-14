#Source: https://stackoverflow.com/questions/72181000/attribute-error-module-teradatasql-has-no-attribute-connect-please-solve-th
cursor.execute ("insert into voltab (?, ?)", [
        [1, "abc"],
        [2, "def"],
        [3, "ghi"]])

cursor.execute ("select * from voltab order by 1")
[ print (row) for row in cur.fetchall () ]
connect.commit()