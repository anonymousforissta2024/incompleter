#Source: https://stackoverflow.com/questions/58297823/attributeerror-enter-during-connection-to-mysql-database
with _connect() as conn, conn as cursor:
 AttributeError: __enter__