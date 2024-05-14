#Source: https://stackoverflow.com/questions/44712996/typeerror-on-method-on-function-classes-attributes
num = Foo()
num.set_turnNum(13)
if num.get_turnNum % 2 == 0:
    print('Not works after all...')
    ...