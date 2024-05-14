#Source: https://stackoverflow.com/questions/57162695/typeerror-in-python-for-loop
pair_1 = []
for num1 in range(2,10):
    for num2 in range(3,11):
        pair_1.append(num1, num2)

print(pair_1)