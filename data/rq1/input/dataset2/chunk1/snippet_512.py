#Source: https://stackoverflow.com/questions/52140811/overwriting-class-raises-typeerror
class Derived(Base):
    @classmethod
    def cast(cls, obj: Base):
        obj.__class__ = cls