#Source: https://stackoverflow.com/questions/32972393/python-attributeerror-list-object-has-no-attribute-after-using-queue
import collections
import queue

class Node:

    def __init__(self, Puzzle, last=None):
        self.puzzle = Puzzle
        self.last = last

    def getPuzzle(self):
        return self.puzzle

    def getLast(self):
        return self.last

class Puzzle:

    def __init__(self, startState, goalState):
        self.state = startState
        self.goal = goalState

    def getState():
        return self.state

    def getMoves(self):

        currentState = self.state

        possibleNewStates = []

        zeroPos = currentState.index(0)

        if zeroPos == 0:
            possibleNewStates.append(move(0,1))
            possibleNewStates.append(move(0,3))
        elif zeroPos == 1:
            possibleNewStates.append(move(1,0))
            possibleNewStates.append(move(1,2))
            possibleNewStates.append(move(1,4))
        elif zeroPos == 2:
            possibleNewStates.append(move(2,1))
            possibleNewStates.append(move(2,5))
        elif zeroPos == 3:
            possibleNewStates.append(move(3,0))
            possibleNewStates.append(move(3,4))
            possibleNewStates.append(move(3,6))
        elif zeroPos == 4:
            possibleNewStates.append(self.move(4,1))
            possibleNewStates.append(self.move(4,3))
            possibleNewStates.append(self.move(4,5))
            possibleNewStates.append(self.move(4,7))
        elif zeroPos == 5:
            possibleNewStates.append(move(5,2))
            possibleNewStates.append(move(5,4))
            possibleNewStates.append(move(5,8))
        elif zeroPos == 6:
            possibleNewStates.append(move(6,3))
            possibleNewStates.append(move(6,7))
        elif zeroPos == 7:
            possibleNewStates.append(move(7,4))
            possibleNewStates.append(move(7,6))
            possibleNewStates.append(move(7,8))
        else:
            possibleNewStates.append(move(8,5))
            possibleNewStates.append(move(8,7))

        return possibleNewStates

    def move(self, current, to):

        changeState = self.state

        save = changeState[to]
        changeState[to] = changeState[current]
        changeState[current] = save

        return changeState

    def printPuzzle(self):

        copyState = self.state
        print(copyState)
        '''
        for i in range(9):
            if i == 2 or i == 5:
                print((str)(copyState[i]))
            else:
                print((str)(copyState[i])+" ", end="")
            print()
        '''

    def isSolved(self):
        return self.state == self.goal

class Solver:

    def __init__(self, Puzzle):
        self.puzzle = Puzzle

    def solveBFS(self):
        puzzle = self.puzzle
        startNode = Node(puzzle)
        myQueue = queue.Queue(0)
        myQueue.put(startNode)
        myPuzzle = startNode.getPuzzle()
        print(myPuzzle.isSolved())
        while myQueue:
            currentNode = myQueue.get()
            currentPuzzle = currentNode.puzzle

            if currentPuzzle == [0,1,2,3,4,5,6,7,8]:
                return currentNode

            nextMoves = currentPuzzle.getMoves() # << ERROR HERE
            for state in nextMoves:
                nextNode = Node(state, currentNode)
                myQueue.put(nextNode)

    startingState = [7,2,4,5,0,6,8,3,1]
    goalState = [0,1,2,3,4,5,6,7,8]
    myPuzzle = Puzzle(startingState, goalState)
    mySolver = Solver(myPuzzle)
    goalNode = mySolver.solveBFS()
    goalPuzzle = goalNode.getPuzzle()
    goalPuzzle.printPuzzle()