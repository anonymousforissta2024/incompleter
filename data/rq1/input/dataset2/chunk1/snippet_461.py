#Source: https://stackoverflow.com/questions/69656383/typeerror-cannot-use-a-string-pattern-on-a-bytes-like-object-pyexpect-in-pyth
buff = BytesIO()
child = pexpect.spawn(path, args, logfile=buff, timeout=self.PASSPHRASE_TIMEOUT, **kwargs)
while True:
     idx = child.expect([self.PASSPHRASE_RE,pexpect.EOF])
     if idx == 0:
        child.sendline(passphrase)
     elif idx == 1:
          child.wait()
          break