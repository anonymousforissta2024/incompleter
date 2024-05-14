#Source: https://stackoverflow.com/questions/70787649/python3-9-i-am-trying-to-write-an-exception-but-get-this-errortypeerror-catch
class Error(BaseException):
    """something"""
    pass

class MailMessage(Error):
    def __init__(self):
        self.connection = None
c = MailMessage()
c.set_recs_for_mail_box() #just for connection
command_to_db = "SELECT *"
try:
    recs = c.execute_query(c.connection, command_to_db)
except Error():
    pass