#Source: https://stackoverflow.com/questions/60975722/attributeerror-bytes-object-has-no-attribute-encode-in-python-3
email = 'aashita9317@gmail.com'
send_email('Happy Hour Update',message,
            from_addr=GMAIL_LOGIN, to_addr=email)