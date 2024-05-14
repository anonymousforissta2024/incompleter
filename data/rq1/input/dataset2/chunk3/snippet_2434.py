#Source: https://stackoverflow.com/questions/55331164/typeerror-object-of-type-int-has-no-len-subtraction
number_1_raw = random.randrange(1, 1000)
number_1_len = len(number_1_raw)
number_of_zeros = 4 - number_1_len
print("0" * number_of_zeros + number_1_raw)