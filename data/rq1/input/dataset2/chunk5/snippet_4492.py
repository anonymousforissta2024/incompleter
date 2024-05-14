#Source: https://stackoverflow.com/questions/63198481/os-rename-does-not-succeed-in-renaming-in-subdirectories-throws-filenotfounderr
cwd = os.getcwd()
fileListOld = glob.glob(f"{cwd}/**/{old_name}", recursive=True)