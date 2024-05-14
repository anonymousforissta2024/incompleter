#Source: https://stackoverflow.com/questions/60043979/how-to-resolve-typeerror-when-migrating-code-to-python3
keep_alive(1,1)
process = subprocess.Popen('grep -E -o ".Source QR CODE :.{0,65}" ' + latest_file + ' | tail -1', shell=True, stdout=subprocess.PIPE,)
stdout_list = process.communicate()
qr_code = stdout_list[0].replace('Source QR CODE : ','')
qr_code = qr_code.replace(' ','')
qr_code = qr_code.replace('\n', '')
qr_code = str(qr_code)