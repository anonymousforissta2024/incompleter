#Source: https://stackoverflow.com/questions/41401417/with-os-scandir-raises-attributeerror-exit
with os.scandir(path) as it:
    for entry in it:
        if not entry.name.startswith('.') and entry.is_file():
            print(entry.name)