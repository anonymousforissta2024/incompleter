import re
for item in items:
    print(re.sub(' ?\\([^)]+\\)', '', item))