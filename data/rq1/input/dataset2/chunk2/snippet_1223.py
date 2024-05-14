#Source: https://stackoverflow.com/questions/61715302/i-get-the-following-error-attributeerror-enter-when-only-using-one-with-blo
with filename as file_object:
    lines=file_object.readlines()

for line in lines:
    print(line.strip())