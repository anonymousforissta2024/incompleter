#Source: https://stackoverflow.com/questions/51720526/how-to-remove-the-type-error-associated-with-elements-of-a-list
pyramidlist = [[int(x) for x in y.split(' ')] for y in number.split('\n')]

for i in range(len(pyramidlist) - 2, -1, -1):
    for j in range(i+1):
        pyramidlist[i][j] += max(pyramidlist[i+1][j], pyramidlist[i+1][j+1])