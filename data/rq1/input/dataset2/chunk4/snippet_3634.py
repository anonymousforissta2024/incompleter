#Source: https://stackoverflow.com/questions/59822759/python-import-random-issue-attributeerror-builtin-function-or-method-object
characters = string.ascii_letters + string.digits
passwordGen =  "".join(choice(characters) for x in range(randint(12, 20)))