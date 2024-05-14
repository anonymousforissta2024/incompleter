#Source: https://stackoverflow.com/questions/55592445/how-to-resolve-nameerror-when-importing-class-with-class-variables-that-depend-o
class foo:
    A = 5
    B = [i*A for A in range(3)]