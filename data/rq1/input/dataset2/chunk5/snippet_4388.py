#Source: https://stackoverflow.com/questions/51236398/typeerror-zip-argument-1-must-support-iteration-in-python
data = [0, 2, 4, 8, 0, 2, 8, 0, 0, 0, 0, 2, 4, 2, 2, 0]
def drawBoard(): # Making the board into a 2d array
    count = 0
    for i in range(16):
        print(data[i], end = ' ')
        count += 1
        if count == 4:
            print("")
            count = 0
drawBoard()
data = zip(*data[::-1])
data = data[::-1]
for col in range(4):
    count = 0  
    for row in range(4): 
        if data[row*4+col] != 0:
            data[count*4+col] = data[row*4+col]
    for row in range(count, 4):
        data[row*4+col] = 0
data = data[::-1]
data = list(zip(*reversed(data)))
drawBoard()