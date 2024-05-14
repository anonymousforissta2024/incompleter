#Source: https://stackoverflow.com/questions/57786570/typeerror-list-indices-must-be-integers-or-slices-not-str-using-python-3-7
from operator import itemgetter
balance = 1000
name = "Charles De."
acc_no = "1235621234"

print("Name: ",name,   "Account: ", acc_no, "Original Balance: ", "$" + 
str(balance))
charges_list = []
charges_dict = []
for charge_string in open("market.txt"):
    charge_info_list = charge_string.strip().split(',')

charge_info = dict()
charge_info['vendor'] = charge_info_list[0]
charge_info['date'] = charge_info_list[1]
charge_info['charge'] = charge_info_list[2]

charges_list.append(charge_info)

if charge_info['vendor'] not in charges_dict:
    charges_dict[charge_info['vendor']] = list()

charges_dict[charge_info['vendor']].append(charge_info)
charges_sorted_by_date = sorted(charges_list, key=itemgetter('date'))