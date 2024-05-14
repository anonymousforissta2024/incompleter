#Source: https://stackoverflow.com/questions/51401920/name-error-with-f-strings-in-python3
path = f'{PROJECT_PATH["raw_data"]}/cashValues'
print("PATH", path)
filenames = [f'{path}/{i}' for i in filenames]