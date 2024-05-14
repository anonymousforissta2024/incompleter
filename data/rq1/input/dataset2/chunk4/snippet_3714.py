#Source: https://stackoverflow.com/questions/59872286/typeerror-unsupported-operand-typ
def cel_to_fahr(c):
    f = c * 9/5 + 32
    return f

c = input("enter the temperature in celcius:")
print(cel_to_fahr(c))