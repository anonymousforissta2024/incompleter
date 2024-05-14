#Source: https://stackoverflow.com/questions/75774322/file-not-found-while-creating-file-in-python3-in-a-cron-job-filenotfounderror
with open(lock_file, 'x'):
    print("Lockfile " + lock_file + " created")