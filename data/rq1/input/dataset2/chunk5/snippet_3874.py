#Source: https://stackoverflow.com/questions/57566737/attributeerror-module-rethinkdb-has-no-attribute-connect
import rethinkdb as rdb
r = rdb.RethinkDB()
self.conn = r.connect('localhost', 28015)