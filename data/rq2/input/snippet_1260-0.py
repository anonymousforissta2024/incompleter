import sqlite3
import io
with io.open('clientes_dump.sql', 'w') as f:
    for linha in conn.iterdump():
        f.write('%s\n' % linha)
print('Backup performed successfully.')
print('Saved as mydatabase_dump.sql')
conn.close()