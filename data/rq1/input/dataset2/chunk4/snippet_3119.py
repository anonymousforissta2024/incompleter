#Source: https://stackoverflow.com/questions/63885766/python-error-typeerror-module-object-is-notcallable
import pyAesCrypt
        
#get FTP pwd
user = db.session.query(User).filter_by(username="ita_itf").first()
p_decrypt = pyAesCrypt(encoding=False)
DICP_FTP_DESTINATION_PSW = p_decrypt.decrypt("password",user.pwd)
        