#Source: https://stackoverflow.com/questions/60043979/how-to-resolve-typeerror-when-migrating-code-to-python3
found_qr = None
while not found_qr:
    keep_alive(1,5)
    time.sleep(4)
    process = None
    stdout_list = None
    process = subprocess.Popen('grep -E -o ".Source QR CODE :.{0,65}" ' + latest_file + ' | tail -1', shell=True, stdout=subprocess.PIPE,)
    stdout_list = process.communicate()
    stdout_list = stdout_list[0]
    if stdout_list.find("Source QR CODE") == -1:
        found_qr = None
    else:
        found_qr = 'found!'