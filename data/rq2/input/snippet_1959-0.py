print('The original tuple : ' + str(test_tuple))
res = [{'key': sub[0], 'value': sub[1], 'id': sub[2]} for sub in test_tuple]
print('The converted dictionary : ' + str(res))