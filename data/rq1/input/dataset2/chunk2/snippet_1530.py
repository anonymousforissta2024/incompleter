#Source: https://stackoverflow.com/questions/55468914/how-to-fix-filenotfounderror-winerror-2-the-system-cannot-find-the-file-speci
import os
os.chdir(directory)
for f in os.listdir():
    f_name, f_ext = os.path.splitext(f)
    os.rename(f_name,f_name.translate(str.maketrans("","","ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")))