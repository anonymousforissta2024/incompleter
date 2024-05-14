#Source: https://stackoverflow.com/questions/73402817/typeerror-googleauth-localwebserverauth-missing-1-required-positional-argumen
from pydrive.drive import GoogleDrive

gauth = GoogleAuth
gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)