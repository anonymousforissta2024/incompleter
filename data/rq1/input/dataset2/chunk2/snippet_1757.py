#Source: https://stackoverflow.com/questions/58580274/typeerror-metaclass-takes-no-arguments
class StateMeta:
    def __call__(*args, **kwargs):
        pass
    # end __call__
# end StateMeta

class State(metaclass=StateMeta):
    pass