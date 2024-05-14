#Source: https://stackoverflow.com/questions/66104884/unsupported-operand-type-error-when-trying-to-multiply-function-parameter-by-an
def user_input(x):
    print(x)


def repeat(y):
    return 5*y


repeat(user_input(input('Get input ')))