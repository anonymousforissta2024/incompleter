#Source: https://stackoverflow.com/questions/73149936/pexpect-interact-typeerror-write-argument-must-be-str-not-bytes
child = pexpect.spawn('npm login', timeout=40)
child.logfile_read = sys.stdout.buffer
...