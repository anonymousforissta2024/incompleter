#Source: https://stackoverflow.com/questions/41058857/python-list-comprehension-causes-nameerror-when-assigned-to-static-varible
class Foo:
    x = 5
    y = [x for i in range(1)]