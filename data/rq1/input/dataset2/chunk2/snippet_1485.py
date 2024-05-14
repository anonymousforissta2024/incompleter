#Source: https://stackoverflow.com/questions/66824172/python-classmethod-type-hint-for-static-builder-returns-nameerror-name
class Options(object):
    def __init__(self, path: str):
        self._path = path

    @property
    def path(self):
        return self._path

class Config(object):
    def __init__(self, path: str):
        self._path = path

    @classmethod
    def from_options(cls, options: Options) -> Config:
        return cls(options.path)