#Source: https://stackoverflow.com/questions/61870153/typeerror-supertype-obj-obj-must-be-an-instance-or-subtype-of-type-error-w
class MetaDemo(type):
    def __new__(mcs, class_name: str, bases: Tuple[Type, ...], class_dict: Dict[str, Any]):
        basis = bases[0]
        c_attrs = dict(basis.__dict__)
        prior_c_process_bases = basis.__base__
        c_attrs["__init__"] = lambda self, settings: prior_c_process_bases.__init__(self, settings)
        new_bases = types.new_class(basis.__qualname__, basis.__bases__,
                                    exec_body=lambda np: MetaDemo.populate_class_dict(np, c_attrs))
        return super(MetaDemo, mcs).__new__(mcs, class_name, (new_bases,), class_dict)

    @staticmethod
    def populate_class_dict(namespace: Dict[str, Any], attr: Dict[str, Any]) -> None:
        for key, value in attr.items():
            namespace[key] = value

class CustomLibraryDemo(LibraryDemo, metaclass=MetaDemo):
    def __init__(self, test: Optional[str] = None) -> None:
        super(CustomLibraryDemo, self).__init__(test)
        print("At CustomDemo __init__ method: This message should appear")

    def test(self) -> None:
        print("In test method at CustomLibraryDemo class: %s" % self.test)