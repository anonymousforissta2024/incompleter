print('Original List: ', L)
u_value = set((val for dic in L for val in dic.values()))
print('Unique Values: ', u_value)