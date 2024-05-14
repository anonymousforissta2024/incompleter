#Source: https://stackoverflow.com/questions/74135982/python-calling-mutiple-my-own-functions-nameerror-not-defined-on-passing-ou
from Iser_upd_qur_del_function import *

ip_input = input("Enter the ip: ")
exist_DB_name = input("Enter exist DB name: ")
exist_coll_name = input("Enter exist collection name: ")
mydb, mycol  = init_db(ip_input, exist_DB_name, exist_coll_name)

myquery_str = input("Enter ur query: ")
update_one_or_many = input("U are update one or many values? (ex:1 for many , 0 for one): ")
newvalues_str = input("Enter new values: ")

one_or_many_bool = bool(int(update_one_or_many))

myquery_json =json.loads(myquery_str)
newvalues_json =json.loads(newvalues_str)
x = change_db_data(myquery_json, newvalues_json, one_or_many_bool)
print(x)
print(x.modified_count, "documents updated.")