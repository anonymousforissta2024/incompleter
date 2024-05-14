#Source: https://stackoverflow.com/questions/75473452/why-is-python-throwing-a-nameerror-when-doing-nested-exceptions-with-same-variab
try:
    1 / 0
except ZeroDivisionError as error:
    try:
        [1, 2, 3][3]
    except IndexError as error:
        pass
    print("The last error was:", error)