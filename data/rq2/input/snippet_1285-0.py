print('Original dictionary: ', student_list)
student_dict = {x.translate({32: None}): y for x, y in student_list.items()}
print('New dictionary: ', student_dict)