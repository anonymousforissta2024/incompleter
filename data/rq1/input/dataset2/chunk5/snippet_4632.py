#Source: https://stackoverflow.com/questions/61524254/what-is-wrong-here-why-is-it-showing-type-error-when-it-shouldnt-be
class student :
    def __init__(self,name,age,grade):
        self.name = name
        self.age = age
        self.grade = grade   # 0 - 100

    def get_grade(self):
        return self.grade

class Course :
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []

    def add_student(self, student):
        if len(self.students) < self.max_students :
            self.students.append(student)
            return True
        return False
    def get_average_grade(self):
        value = 0
        for i in self.students :
            value += student.get_grade() # this part had the error

        return value / len(self.students)

s1 = student('Bob', 12, 50)
s2 = student('Joe', 12, 60)
s3 = student('Sadie', 12, 100)

Course1 = Course('Chemistry', 5)
Course1.add_student(s1)
Course1.add_student(s2)
Course1.add_student(s3)
print(Course1.students[0].name)
print(Course1.get_average_grade())