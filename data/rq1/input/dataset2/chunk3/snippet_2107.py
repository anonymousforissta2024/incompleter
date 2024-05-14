#Source: https://stackoverflow.com/questions/61396892/python-cant-use-base-abstract-calass-property-from-subclass-gettig-attributeerr
from abc import abstractmethod, ABC
class Base(ABC):

    @property
    def is_ver0(self):
        return None

    @abstractmethod
    def execute_sql(self):
        print("Base execute_sql")

    def print_and_exit(self):
        print("Base")