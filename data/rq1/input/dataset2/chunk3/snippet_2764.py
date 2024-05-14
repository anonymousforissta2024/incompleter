#Source: https://stackoverflow.com/questions/74975991/shutil-copyfile-permissionerror-or-filenotfounderror-error
DATA_DIR = Path.cwd() / 'sourceFolder'
files = os.listdir(DATA_DIR)
des = os.path.join('/destFolder', files[0])
shutil.copyfile(os.path.join('sourceFolder', files[0]), des)