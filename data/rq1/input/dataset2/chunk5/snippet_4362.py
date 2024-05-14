#Source: https://stackoverflow.com/questions/74135982/python-calling-mutiple-my-own-functions-nameerror-not-defined-on-passing-ou
import pymongo
import datetime
import json
def init_db(ip, db, coll):
    myclient = pymongo.MongoClient('mongodb://' + ip + '/')
    mydb = myclient[db]
    mycol = mydb[coll]

    return mydb, mycol


def change_db_data(myquery_json, newvalues_json, one_or_many_bool):
    
    if one_or_many_bool == True:
        x = mycol.update_many(myquery_json, newvalues_json)
    else:
        x = mycol.update_one(myquery_json, newvalues_json)
    return x