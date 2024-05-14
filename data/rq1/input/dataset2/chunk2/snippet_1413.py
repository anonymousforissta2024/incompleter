#Source: https://stackoverflow.com/questions/54003962/typeerror-nonetype-object-is-not-iterable-when-applying-decorator-to-generato
def decor(func):
    def wrapper(*args, **kwargs):
        func_name = func.__name__
        is_generator = "_generator" in func_name
        if is_generator:
            for item in func(*args, **kwargs):
                print(item)
        else:
            res = func(*args, **kwargs)
            print(res)
    return wrapper

@decor            
def f():
    return "a"

@decor    
def f_generator():
    for i in range(2):
        yield "b"

f()

""" Output: a """

for item in f_generator():
    print ("Processing item ", item)

"""
Output:
b
b
Traceback (most recent call last):
  File "test.py", line 27, in <module>
      for item in f_generator():
TypeError: 'NoneType' object is not iterable
"""