#Source: https://stackoverflow.com/questions/63729685/how-to-differentiate-between-unexpected-keyword-argument-and-missing-positional
def test_method(a):
    print(a)

test_method(a=1) # 'a'
test_method() # TypeError: test_method() missing 1 required positional argument: 'a'
test_method(a=1, b=2) # TypeError: test_method() got an unexpected keyword argument 'b'