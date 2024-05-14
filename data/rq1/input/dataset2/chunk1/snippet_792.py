#Source: https://stackoverflow.com/questions/45132645/list-comprehension-in-exec-with-empty-locals-nameerror
def bar():
    return 1
print([bar() for _ in range(5)])