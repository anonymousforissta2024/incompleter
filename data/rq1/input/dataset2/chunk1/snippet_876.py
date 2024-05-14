#Source: https://stackoverflow.com/questions/64404150/python3-replace-yielding-typeerror-a-bytes-like-object-is-required-not-str
s = paramiko.SSHClient()
s.load_system_host_keys()
s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
s.connect(hostname, port, username, password)
command = 'xe vm-list'
(stdin, stdout, stderr) = s.exec_command(command)

output = stdout.read()
x = output.replace("\n", ",").strip()
print(x)
s.close()