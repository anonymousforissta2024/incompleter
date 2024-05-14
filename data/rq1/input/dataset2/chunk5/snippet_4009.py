#Source: https://stackoverflow.com/questions/62877328/typeerror-object-of-type-bool-has-no-len
store_id = 1
acc_id = str(store_id)
print("type of acc_id is ", type(acc_id))

x = len(acc_id)
print(x)

if len(acc_id == 1):
    acc_id += '000' + acc_id