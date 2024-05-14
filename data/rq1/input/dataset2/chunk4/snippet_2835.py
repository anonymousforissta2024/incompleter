#Source: https://stackoverflow.com/questions/74975991/shutil-copyfile-permissionerror-or-filenotfounderror-error
import os
import shutil
from pathlib import Path

DATA_DIR = Path.cwd() / 'sourceFolder'
files = os.listdir(DATA_DIR)
shutil.copyfile(os.path.join('sourceFolder', files[0]), '/destFolder')