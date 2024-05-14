#Source: https://stackoverflow.com/questions/50053995/attributeerror-mysql-connection-object-has-no-attribute-cursor
import _mysql as mc

db = mc.connect (host = "localhost", user = "root", passwd = "password1234")
cursor = db.cursor()