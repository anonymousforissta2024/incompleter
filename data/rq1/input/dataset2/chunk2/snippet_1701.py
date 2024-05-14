#Source: https://stackoverflow.com/questions/22961897/why-do-i-get-and-error-when-my-loop-runs-the-2nd-time-typeerror-int-object-h
import numpy

board = numpy.array([[0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 1, 2, 0, 0, 0],
                     [0, 0, 0, 2, 1, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0]])



boardlist0 = [board]*2

boardlist1 = []
ind = 0
move = [[0,0], [7,4]]


for k in move:
    move = move[ind]

    boardlist0[ind][move[0]][move[1]] = 1

    boardlist1.append(boardlist0)
    ind += 1