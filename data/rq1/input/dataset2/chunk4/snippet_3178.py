#Source: https://stackoverflow.com/questions/17909954/python-ddl-program-if-statement-causing-name-error-when-using-y-n-instead-of-1
import sqlite3
#
def create_table(db_name,table_name,sql):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        cursor.execute('select name from sqlite_master where name=?',(table_name,))
        result = cursor.fetchall()
        keep_table = True
        if len(result) == 1:
#Problem area
            response = input('The table {0} already exists, do you wish to overide? (y/n): '.format(table_name))
            if response == 'y':
#Problem area end
                keep_table = False
                cursor.execute('drop table if exists {0}'.format(table_name))
                print('Table overwritten')
                db.commit()
            else:
                print('Table kept')
        else:
            keep_table = False
        if not keep_table:
            cursor.execute(sql)
            db.commit()
#
if __name__ == '__main__':
    db_name = 'coffee_shop.db'
    sql = '''create table Product
             (ProductID integer,
             Name varchar(30),
             Price real,
             primary key(ProductID))'''
    create_table(db_name,'Product',sql)