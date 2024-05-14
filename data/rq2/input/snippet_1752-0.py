import re
for file in filenames:
    match = re.search('\\.xml$', file)
    if match:
        print('The file ending with .xml is:', file)