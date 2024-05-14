#Source: https://stackoverflow.com/questions/61214984/interger-list-reversal-producing-a-nonetype-error
some_numbers = [1,2,3,4,5,6,7,8,9,11,22,33,44,55,66,77]

reversed_numbers = []

i = 0

while some_numbers:
    reversed_numbers = reversed_numbers.insert(i, some_numbers.pop())
    i = i + 1


print(reversed_numbers)