#Source: https://stackoverflow.com/questions/56838221/filenotfounderror-when-trying-to-use-os-rename
import os
n = 2000

folder = r"Z:/AAA/BBB/"
os.chdir(folder)

saved_path = os.getcwd()
print("CWD is" + saved_path)

for i in range(1,n):
    old_file = os.path.join(folder, "xxx_(" + str(i) + ").bmp")
    new_file = os.path.join(folder, "xxx_" +str(i)+ ".bmp")
    os.rename(old_file, new_file)
print('renamed files')