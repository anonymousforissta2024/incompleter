from collections import defaultdict
class_rollno = defaultdict(list)
for class_name, roll_id in classes:
    class_rollno[class_name].append(roll_id)
print(class_rollno)