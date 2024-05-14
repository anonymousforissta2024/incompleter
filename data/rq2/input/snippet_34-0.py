def test(students):
    return {value: key for key, value in students.items()}
print(test(students))