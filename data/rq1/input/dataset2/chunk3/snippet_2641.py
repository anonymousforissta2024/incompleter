#Source: https://stackoverflow.com/questions/58096497/im-getting-a-typeerror-unsupported-operand-types-for-str-and-int
PLAYING = "PLAYING"
WAITING = "WAITING"

class User:
    state = ""
    name = ""
    def __init__(self,name, stateParam):
        self.name = name
        self.state = stateParam

    def userInfo(self):
        return self.name

    def getState(self):
        return self.state
    def setState(self, stateParam):
        self.state = stateParam

def play():
    grid,grid_height,grid_width,p1_name,p1_char,p2_name,p2_char=getGameSettings()
    displayGrid(grid,grid_height,grid_width)
    updateGrid(grid,grid_height,grid_width,p1_char,p2_char)
   # while True:
        #count=0
        #if count < 5:
            #displayGrid(grid,grid_height,grid_width)
            #updateGrid(grid,grid_height,grid_width,p1_char,p2_char)
            #count =+1
    userA = User(p1_name, PLAYING)
    userB = User(p2_name, WAITING)  

    turn = 0
    while True:
        user = userA
        if turn % 2 == 0 :
            p_char= p1_char
            user = userA
            userA.setState(PLAYING)
            userB.setState(WAITING)
        else :
            user = userB
            userB.setState(PLAYING)
            userA.setState(WAITING)

        print(".................................................. ")
        print("User to play : ", user.userInfo() , " SEQ : ", str(turn + 1))
        print(".................................................. ")

        try:
            move= int(input('Enter your move: '))
        except ValueError:
            print('Plese enter a valid  input.')
        if move < 1 or move > grid_width:
            print('Please  enter a valid input.')
            continue
        break

        updateGrid(grid,move,p_char,grid_height,grid_width)
        turn += 1


def getGameSettings(): 

    #PLAYER 1 NAME
    while True:
        p1_name=input("Enter p1_name: ")
        if len(p1_name) > 15 or p1_name == '': #Validation of input p1_name
            print("Input a valid name. Max of 15 characters only.")
            p1_name=input("Enter p1_name: ")
        else:
            break

    #PLAYER 1 CHARACTER
    while True:
        p1_char=str(input("Enter p1_character: "))
        if len(p1_char) != 1 or p1_char=='' : #Validation of input p1_character
            print("1 character only.")
            p1_char=input("Enter p1_character: ")
        else:
            break

    #PLAYER 2 NAME
    while True:
        p2_name=str(input("Enter p2_name: "))
        if len(p2_name) > 15 or p2_name == p1_name or p2_name == '': #Validation of input p2_name
            print("Max of 15 characters only or choose a different name.")
            p2_name=input("Enter p2_name: ")
        else:
            break

    #PLAYER 2 CHARACTER
    while  True:
        p2_char=str(input("Enter p2_character: "))
        if len(p2_char) != 1 or p2_char == p1_char or p2_char == '': #Validation  of input p2_char
            print("1 character only or choose a different character from player 1")
            p2_char=str(input("Enter p2_character: "))
        else:
            break

    while True: #VALIDATION OF INPUT OF GRID_WIDTH
        try:
            global grid_height
            grid_height=int(input("Enter grid_height(6-10): "))
        except ValueError: #if input is not the right type()
            print('Ivalid input type. Enter an integer')
            continue
        if grid_height > 10 or grid_height < 6: #to check if input is within accepted values
            print('Height must be less than 11 and greater than 5.')
            continue  
        break


    while True: #VALIDATION OF INPUT OF GRID_WIDTH
        try:
            global grid_width
            grid_width=int(input("Enter grid_width: "))
        except ValueError: #if input is not the right type()
            print('Ivalid input type. Enter an integer')
            continue
        if grid_width > 9 or grid_width < 7: #to check if input is within accepted values
            print('Width must be less than 10 and greater than 6.')
            continue  
        break

    #SETTING UP THE GRID
    grid=[]
    for row in range(grid_height): # FOR ROW
        z =[]
        for col in range(grid_width): # FOR COLUMN
            z.append(" ")
        grid.append(z)

    return grid,grid_width,grid_width,p1_name,p1_char,p2_name,p2_char


def displayGrid(grid,grid_height,grid_width):
    for row in range(1,grid_height):
        #print(row) #for checking
        for col in range(grid_width):
            print("|", end="")
            print(str(grid[row-1][col-1]),end = "")
        print("|")
    print(" "+" ".join([str(i) for i in range(1, grid_width+1)]))
    return grid

def updateGrid(grid,move,p_char,grid_height,grid_width):
    for i in range(1, grid_height-1):
        if grid[grid_height-i][move-2] == " ":
            grid[grid_height-i][move-2]= p_char
        else:
            if grid[0][move-1] != " ":
                updateGrid(grid,move,p_char,grid_height,grid_width)
            else:
                continue
        break

    return grid


#def isWin():

#def isDraw():


if __name__ == '__main__':
    play()