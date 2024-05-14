#Source: https://stackoverflow.com/questions/74975991/shutil-copyfile-permissionerror-or-filenotfounderror-error
dst = Path.cwd() / 'destFolder/nameOfFile'
shutil.copyfile(os.path.join('sourceFolder', files[0]), dst)