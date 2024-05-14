#Source: https://stackoverflow.com/questions/67916291/pd-dataframe-resulting-in-typeerror-when-a-metaclass-is-defined-before-it
class MappingMeta(type, collections.abc.Mapping):
    def __setattr__(self, *args, **kwargs):
        raise RuntimeError("Can not set attributes of Mapping type")

    def __call__(self, *args, **kwargs):
        raise RuntimeError("Can not directly instantiate Mapping type")

    def __getitem__(self, value):
        return getattr(self, value)

    def __iter__(self):
        return (k for k in vars(self) if not k.startswith("_"))

    def __len__(self):
        return sum(1 for _ in self)


class Mapping(metaclass=MappingMeta):
    pass


class Test(Mapping):
    x = 1
    y = 2