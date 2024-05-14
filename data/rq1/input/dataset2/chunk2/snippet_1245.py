#Source: https://stackoverflow.com/questions/55292116/python-imap-typeerror-nonetype-object-is-not-subscriptable
import imaplib, time, email, mailbox, datetime
server = "imap.gmail.com"
port = 993
user = "Redacted"
password = "Redacted"

def main():
    while True:            
        conn = imaplib.IMAP4_SSL(server, port)
        conn.login(user, password)
        conn.list()
        conn.select('inbox', readonly=True)
        result, data = conn.search(None, '(UNSEEN SUBJECT "Alert: Storage Almost At Max Capacity")')
        i = len(data[0].split())

        for x in range (i):
            latest_email_uid = data[0].split()[x]
            result, email_data = conn.uid('fetch', latest_email_uid, '(RFC822)')
            raw_email = email_data[0][1] #This is where it throws the error
            raw_email_string = raw_email.decode('utf-8')
            email_message = email.message_from_string(raw_email_string)
            date_tuple = email.utils.parsedate_tz(email_message['Date'])
            local_date = datetime.datetime.fromtimestamp(email.utils.mktime_tz(date_tuple))
            local_message_date = "%s" %(str(local_date.strftime("%a, %d %b %Y %H:%M:%S")))
            for part in email_message.walk():
                if part.get_content_type() == "text/plain":
                    body = part.get_payload(decode=True)
                    body = body.decode('utf-8')
                    body = body.split()
                    #Do some stuff
        conn.close()

if __name__ == "__main__":
    main()