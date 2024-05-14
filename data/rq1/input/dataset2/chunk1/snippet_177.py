#Source: https://stackoverflow.com/questions/15328728/getting-typeerror-can-only-concatenate-tuple-not-int-to-tuple-even-thou
num_1 = 3
num_2 = 5
num_3 = 15
div_1 = 1000/3
div_2 = 1000/5
div_3 = 1000/15
sum_1 = 0
sum_2 = 0
sum_3 = 0
i = 0
while (i<300):
    sum_1 = sum_1 + i*3,
    i = i + 1
    print (sum_1)
i = 0
while (i<div_2):
    sum_2 = sum_2 + i*5,
    i += 1
i = 0
while (i<div_1):
    sum_3 = sum_3 + i*5,
    i += 1
print (sum_1)