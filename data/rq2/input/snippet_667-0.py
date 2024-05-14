from collections import defaultdict

def test(students):
    obj = defaultdict(list)
    for key, value in students.items():
        obj[value].append(key)
    return dict(obj)
print(test(students))