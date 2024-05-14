#Source: https://stackoverflow.com/questions/77438731/fixing-datatype-error-in-oracledb-from-python-ora-01790
data = [1,2,None,4,5,6]
sql = """
SELECT :1 AS ID, :2 AS pkey, :3 AS issuenum FROM dual  UNION ALL
SELECT :4 AS ID, :5 AS pkey, :6 AS issuenum FROM dual 
"""

cur = con.cursor()
cur.execute(sql, data)
data = cur.fetchall()