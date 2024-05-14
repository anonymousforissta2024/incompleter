#Source: https://stackoverflow.com/questions/50805607/python-3-name-error-from-input-within-a-function
def multiply(num_1, num_2):
    num_1 = input("enter a whole number:")
    num_2 = input("enter another whole number:")
    result = int(num_1)*int(num_2)
    return(num_1 + " * " + num_2 + " = " + str(result))

multiply(num_1, num_2)