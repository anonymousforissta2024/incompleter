#Source: https://stackoverflow.com/questions/72754431/python-list-attribute-error-without-a-list
receiver_email = open(subscribers.txt, 'r').readlines()
for i in receiver_email:
    current_mail = i.removesuffix("\n")
    print(type(current_mail))
    print(type(smtp_data[2]))
    print(type(message))
    smtp.sendmail(smtp_data[2], current_mail, message.as_string())