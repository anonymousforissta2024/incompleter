#Source: https://stackoverflow.com/questions/49852919/python-used-the-decorator-typeerror-bilolgy-missing-1-required-positional-arg
class Base(object):
    """
    base class
    """
    def bilolgy(self, pre):
        def animal(func):
            def color(a):
                print(pre)
                print("Today is a good day")
                func(a)

            return color

        return animal


class Sub(Base):
    """
    subclass
    """
    @Base.bilolgy(pre="Cats")
    def cat(self, name):
        print("This is a " + name)


if __name__ == '__main__':
    sub = Sub()
    sub.cat("cat")