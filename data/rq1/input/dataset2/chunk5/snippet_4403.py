#Source: https://stackoverflow.com/questions/55641918/how-to-fix-a-nonetype-error-in-append-function
some_list = []
for i in range(10):
    if i % 2 == 0:
        i = abs(i)
        some_list = some_list.append(i)
    elif i % 2 == 1:
        some_list = some_list.append(i)
    else:
        pass
some_list