#Source: https://stackoverflow.com/questions/70147078/attributeerror-type-object-student-has-no-attribute-name
class Student:
    
    def __init__(self, name, uci_name, semester):
        self.name = name
        self.uci_name = uci_name
        self.semester = semester
    
    def get_name(self) -> str:
        return self.name
    
    def get_uci_name(self) -> str:
        return self.uci_name
    
    def get_semester(self) -> int:
        return self.semester
    
    def __str__(self):
        return f"{self.name} [{self.uci_name}] in Semester {self.semester}"

student_tom = Student("Tom", "tom55", 3)
    
assert isinstance(getattr(Student, "name"), property)
assert isinstance(getattr(Student, "uci_name"), property)
assert isinstance(getattr(Student, "semester"), property)