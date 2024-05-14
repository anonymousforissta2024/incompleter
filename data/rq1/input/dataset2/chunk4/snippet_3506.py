#Source: https://stackoverflow.com/questions/63977672/filenotfounderror-errno-2-no-such-file-or-directory-python-writer-py
from subprocess import Popen, PIPE


p1 = Popen('python writer.py', stdout=PIPE)
p2 = Popen('python reader.py', stdin=p1.stdout, stdout=PIPE)
output = p2.communicate()[0]
print(output)