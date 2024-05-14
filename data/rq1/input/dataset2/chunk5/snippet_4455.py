#Source: https://stackoverflow.com/questions/43924311/typeerror-unsupported-operand-types-for-str-and-int-program-to-change
x = input("Enter the Celsius Temparature:")
print("Its", u"x\u00B0", "out there")
y = (((9*x)/5)+32)
print("The Fahrenheit Equivalent is:{0:0.3f}" .format(y))