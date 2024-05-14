#Source: https://stackoverflow.com/questions/73149936/pexpect-interact-typeerror-write-argument-must-be-str-not-bytes
child = pexpect.spawn('npm login', timeout=40, encoding='utf-8')
child.logfile_read = sys.stdout
child.expect('Username:')
child.sendline('qiulang2000')
child.expect('Password:')
child.sendline('xxxx')
...
child.interact()