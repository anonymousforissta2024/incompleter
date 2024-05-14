#Source: https://stackoverflow.com/questions/65010286/typeerror-sqlite3-cursor-object-is-not-subscriptable-how-to-print-sql-select
import sqlite3
con=sqlite3.connect("aditi")
con.execute('''CREATE TABLE IF NOT EXISTS LOGIN
                   (ID         INTEGER PRIMARY KEY AUTOINCREMENT,
                    NAME       TEXT NOT NULL,
                    ROLL       INT NOT NULL,
                    PASS       TEXT NOT NULL);''')
quer=f'''INSERT INTO LOGIN(NAME,ROLL,PASS) VALUES('ADMIN','0','ADMIN123')'''
con.execute(quer)
con.commit()

cursor=con.execute('''SELECT NAME FROM LOGIN''')
print(cursor[0])   
con.close()