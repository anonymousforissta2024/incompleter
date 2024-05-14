#Source: https://stackoverflow.com/questions/38380270/python3-ftp-file-upload-throws-typeerror-type-str-doesnt-support-the-buffer-a
import ftplib

ftp = ftplib.FTP(url)
ftp.login(name, password)
ftp.storlines("STOR " + "mylog.log", open("log/mylog.log"))
ftp.close()