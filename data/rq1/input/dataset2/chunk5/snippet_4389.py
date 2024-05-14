#Source: https://stackoverflow.com/questions/28692702/attributeerror-type-object-x-has-no-attribute-y-and-some-other-inconsistencies
# metaclass methods

class Meta(type):
    def show(cls):
        return 'I am a Meta class method'

class Mistake(object):
    __metaclass__ = Meta