#Source: https://stackoverflow.com/questions/56867560/nameerror-name-paramiko-is-not-defined
import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
print(ssh)