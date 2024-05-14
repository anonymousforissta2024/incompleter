#Source: https://stackoverflow.com/questions/54564772/renaming-files-in-python-getting-filenotfounderror
import os

old_dir = '/Users/User/Desktop/MyFolder'

for f in os.listdir(old_dir):
    file_name, file_ext = os.path.splitext(f)
    file_name.split('-')

    split_file_name = file_name.split('-')

    new_dir = os.path.join(old_dir,
                           '-'.join(split_file_name[:3]),
                           split_file_name[5],
                           f)

    os.rename(os.path.join(old_dir, f), new_dir)