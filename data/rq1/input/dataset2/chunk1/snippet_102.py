#Source: https://stackoverflow.com/questions/59181118/os-mkdir-returns-error-filenotfounderror-errno-2-no-such-file-or-directory
ssh_path = f"{os.getenv('HOME')}/temp/.ssh"
print(ssh_path)
os.mkdir(ssh_path)