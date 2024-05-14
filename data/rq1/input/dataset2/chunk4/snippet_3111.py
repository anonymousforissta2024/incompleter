#Source: https://stackoverflow.com/questions/66471225/sqlalchemypython-typeerror-can-only-concatenate-tuple-not-rowproxy-to-tu
with sqlalchemy_engine.connect() as conn:
    ids = sum(tuple(conn.execute('select id from some_database.some_table')), ())   # statement causing error
    print(ids)