#Source: https://stackoverflow.com/questions/50176436/type-error-unsupported-operand
def sum_dig_pow(a, b):
    dict1 = {}
    for k in range(a,b+1):
        if k < 10:
            dict1[k] = k**1

        else:
            num_len = int(len(str(k))) + 1

            def dig_pow(k):
                nonlocal num_len
                num_len -= 1
                if k < 10:
                    return k
                else:
                    var = (k%10)**num_len + dig_pow(k//10)
                    dict1[k] = var

            dig_pow(k)
    return dict1
print(sum_dig_pow(98, 100))