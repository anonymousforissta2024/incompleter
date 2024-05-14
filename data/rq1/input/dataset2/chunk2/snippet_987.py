#Source: https://stackoverflow.com/questions/58090214/im-receiving-a-typeerror-can-only-concatenate-str-not-int-to-str
def play():
        grid,grid_height,grid_width,p1_name,p1_char,p2_name,p2_char=getGameSettings()
        displayGrid(grid,grid_height,grid_width)
        updateGrid(grid,grid_height,grid_width,p1_char,p2_char)
        displayGrid(grid,grid_height,grid_width)
        updateGrid(grid,grid_height,grid_width,p1_char,p2_char)
        displayGrid(grid,grid_height,grid_width)


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
        p1_char=input("Enter p1_character: ")
        if len(p1_char) != 1 or p1_char=='' : #Validation of input p1_character
            print("1 character only.")
            p1_char=input("Enter p1_character: ")
        else:
            break

    #PLAYER 2 NAME
    while True:
        p2_name=input("Enter p2_name: ")
        if len(p2_name) > 15 or p2_name == p1_name or p2_name == '': #Validation of input p2_name
            print("Max of 15 characters only or choose a different name.")
            p2_name=input("Enter p2_name: ")
        else:
            break

    #PLAYER 2 CHARACTER
    while  True:
        p2_char=input("Enter p2_character: ")
        if len(p2_char) != 1 or p2_char == p1_char or p2_char == '': #Validation  of input p2_char
            print("1 character only or choose a different character from player 1")
            p2_char=input("Enter p2_character: ")
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
    for row in range(grid_height):
        for col in range(grid_width+1):
            print("|" + grid[row-1][col-1],end = "")
        print()
    print(" "+" ".join([str(i) for i in range(1, grid_width+1)]))
    return grid

def updateGrid(grid,p1_char,p2_char,p1_name,p2_name):
    while True:
        try:
            move= int(input('Enter your move: '))
        except ValueError:
            print('Plese enter a valid  input.')
        if move < 1:
            print('Please  enter a valid input.')
            continue
        break

    for i in range(1,grid_height+1):
        if grid[grid_height-i][move-2]== " ":
            grid[grid_height-i][move-2]= p1_char
        else:
            if grid[0][move-2] != " ":
                updateGrid(grid,grid_height,grid_width,p1_char,p2_char)
            else:
                continue
        break

    return grid


#def get_input(player, grids, )
#def isWin():

#def isDraw():

#def play():
#displayGrid()
#updateGrid(grid)

if __name__ == '__main__':
    play()