#Source: https://stackoverflow.com/questions/65269486/attributeerror-float-object-has-no-attribute-append-when-trying-to-append-v
from collection import defaultdict

new_dict= defaultdict(list)

for row in list_dict:
    acct=row[acct]
    time_spent= float(row[time_spent])

    if (acct not in new_dict):
        new_dict[acct] = time_spent
    else:
        new_dict[acct].append(time_spent)