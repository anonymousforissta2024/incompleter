#Source: https://stackoverflow.com/questions/64775607/typo-in-pymongo-set-update-causes-typeerror-unhashable-type-dict
find_query = {'_id': doc['_id']}
upd_statement = {'$set:',
                 {'subdivision_name': new_name}
                 }
dbCollection.update_one(find_query, upd_statement, upsert=False)