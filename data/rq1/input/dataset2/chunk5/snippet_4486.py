#Source: https://stackoverflow.com/questions/61303661/typeerror-list-indices-must-be-integers-or-slices-not-str-error-while-iterati
list1 = ['Ganga', 'Narmada', 'Kaveri', 'Tapi', 'Yamuna']
sum1 = 0
for i in list1:
  for j in list1[i]:
    sum1 += ord(int(j))
    list1.replace(i, sum1)
print(list1)