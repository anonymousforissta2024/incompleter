result = {}
for key, value in student_data.items():
    if value not in result.values():
        result[key] = value
print(result)