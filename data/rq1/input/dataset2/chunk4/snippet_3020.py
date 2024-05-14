#Source: https://stackoverflow.com/questions/65194399/how-to-fix-attributeerror-partially-initialized-module-sendemail-has-no-attr
import Main
import smtplib
import time
from email.message import EmailMessage


# send function
def send_email():
    try:
        msg = EmailMessage()

        emailText = Main.email_str.get()
        passwordText = Main.password_str.get()
        receiverText = Main.receiver_str.get()
        subjectText = Main.subject_str.get()
        bodyText = Main.bodyEntry.get("1.0", "end-1c")

        msg['Subject'] = subjectText
        msg['From'] = emailText
        msg['To'] = receiverText
        msg.set_content(bodyText)

        if emailText == "" or passwordText == "" or receiverText == "" or subjectText == "" or bodyText == "":
            Main.notif.config(text="All fields are required!", fg="red")

            Main.root.update()
            time.sleep(2.5)

            Main.notif.config(text="")
            return
        else:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(emailText, passwordText)
            server.send_message(msg)

            Main.emailEntry.delete(0, 'end')
            Main.passwordEntry.delete(0, 'end')
            Main.receiverEntry.delete(0, 'end')
            Main.subjectEntry.delete(0, 'end')
            Main.bodyEntry.delete("1.0", "end-1c")

            Main.notif.config(text="Email Sent!", fg="green")

            Main.root.update()
            time.sleep(2.5)

            Main.notif.config(text="")
    except:
        Main.notif.config(text="There was a error please try again", fg="red")

        Main.root.update()
        time.sleep(2.5)

        Main.notif.config(text="")