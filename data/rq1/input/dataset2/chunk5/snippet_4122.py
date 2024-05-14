#Source: https://stackoverflow.com/questions/51418152/python-error-when-inserting-data-typeerror-object-of-type-int64-is-not-jso
if len(acct) > 0:
    list = []
    for i in range(len(acct)):
        update = {'Id': acct['Id'].iloc[i],
              'name': acct['user_count'].iloc[i]}

        list.append(update)
    sf_data_cursor.bulk.Account.update(list)