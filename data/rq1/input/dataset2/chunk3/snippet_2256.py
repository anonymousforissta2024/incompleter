#Source: https://stackoverflow.com/questions/67042983/typeerror-init-missing-1-required-positional-argument-sage
from Studentclass import Student
from Courseclass import Course

class Marks(Student, Course):
    def __init__(self, Sid,Cid, Mark):
        super().__init__(Sid,Cid)#Error line 7, in __init__ super().__init__(Sid,Cid) TypeError: __init__() missing 1 required positional argument: 'Sage'#
        self.Mark = Mark

    def __repr__(self):
        return '({},{},{})'.format(self.Sid, self.Cid, self.Mark)