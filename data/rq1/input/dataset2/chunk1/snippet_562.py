#Source: https://stackoverflow.com/questions/62523278/typeerror-field-classroom-expected-a-number-but-got-4
students = [
    ["James", "Smith", 4, 10],
    # more students here
]

for s in students:
    student = Student()
    student.first_name = s[0],
    student.last_name = s[1],
    student.classroom = s[2],
    student.grade1 = s[3],
    student.save()