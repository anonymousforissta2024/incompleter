#Source: https://stackoverflow.com/questions/67601549/trying-to-rename-files-with-os-rename-throws-a-filenotfounderror-errno-2
import sys
import os

path = os.listdir("/home/user/Downloads/student-02-c3f0f7fe19ef/data/")
for i in path:
        print(i)
        if "jane" in i:
                os.rename(i, i.replace("jane", "jdoe"))