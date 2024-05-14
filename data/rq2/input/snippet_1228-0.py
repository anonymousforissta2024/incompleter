import os
print('Iterate over a root level path:')
for root, dirs, files in os.walk(path):
    print(root)