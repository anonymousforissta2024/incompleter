from os import popen
output = popen(f'fsutil file queryfileid {file}').read()
print(output)