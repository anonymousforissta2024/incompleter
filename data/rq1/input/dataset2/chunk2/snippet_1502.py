#Source: https://stackoverflow.com/questions/72690805/python-inheriting-generic-type-typeerror-object-init-takes-exactly-one-a
# text.py
class Text(Object):
    # ignored properties...
    def __init__(self, text="placeholder text", **kwargs):
        super().__init__(object_type=Text.object_type, text=text, **kwargs)