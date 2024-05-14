#Source: https://stackoverflow.com/questions/56580094/attributeerror-float-object-has-no-attribute-write
for x in range(0, 500):

    t1 = timeit.default_timer()
    x=x+1
    t.write(str(t1) + '\n')

    t = timeit.default_timer() - t1
    print("Pretecen cas: ", t)

    break