#Source: https://stackoverflow.com/questions/60950088/typeerror-sequence-item-0-expected-str-instance-tuple-found
import smtplib

from email.mime.multipart import MIMEMultipart

from email.mime.text import MIMEText


MY_ADDRESS = input('your email: ')

PASSWORD = input('your password: ')

emailadd = input('text file email addresses: ')

subject = input('text file containing subject  ')

body = input('text file containing body: ')


def getcontacts(filename):
    emails = []
    with open(filename, mode='r', encoding='utf-8') as contacts_file:
        for a_contact in contacts_file:
            emails.append(a_contact)
    return emails


def readtemplate(filename):
    with open(filename, 'r', encoding='utf-8') as template_file:
        return template_file.read()


def main():
    global contents, msg
    emails = getcontacts(emailadd)
    message_template = readtemplate(body)


    s = smtplib.SMTP(host='smtp.gmail.com', port=587)
    s.starttls()
    s.login(MY_ADDRESS, PASSWORD)


    for email in zip(emails):
        msg = MIMEMultipart()

        f = open(subject, 'r')
        if f.mode == 'r':
            contents = f.read()
        f.close()

        msg['From'] = MY_ADDRESS
        msg['To'] = email
        msg['Subject'] = contents

        msg.attach(MIMEText(message_template, 'plain'))

        s.send_message(msg)
        del msg

    s.quit()


if __name__ == '__main__':
    main()