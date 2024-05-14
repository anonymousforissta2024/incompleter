#Source: https://stackoverflow.com/questions/58138056/summing-a-list-of-floatstypeerror-int-object-is-not-callable
range_list = range(1, 97)


for p in range_list:

    p_numerator = 4*((-1)**(p+1))
    p_denominator = 2*p - 1

    function_ofK = float(p_numerator)/float(p_denominator)


    total = sum(function_ofK)
    print(total)