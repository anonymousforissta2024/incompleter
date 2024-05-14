#Source: https://stackoverflow.com/questions/32288466/python-attributeerror-str-object-has-no-attribute
__author__ = 'Goldsmitd'

class Rook:
    def __init__(self,x,y,sl,team):
        self.name = 'Rook'
        self.x = x
        self.y = y
        self.sl = sl
        self.team = team


class Knight:
    def __init__(self,x,y,sl,team):
        self.name = 'Knight'
        self.x = x
        self.y = y
        self.sl = sl
        self.team = team


class Bishop:
    def __init__(self,x,y,sl,team):
        self.name = 'Bishop'
        self.x = x
        self.y = y
        self.sl = sl
        self.team = team


class Queen:
    def __init__(self,x,y,sl,team):
        self.name = 'Queen'
        self.x = x
        self.y = y
        self.sl = sl
        self.team = team


class King:
    def __init__(self,x,y,sl,team):
        self.name = 'King'
        self.x = x
        self.y = y
        self.sl = sl
        self.team = team


class Pawn:
    def __init__(self,x,y,sl,team):
        self.name = 'Pawn'
        self.x = x
        self.y = y
        self.sl = sl
        self.team = team


class Chess_Board:
    def __init__(self):
        self.board = [['.']*8 for _ in range(8)]
        self.board[7][0] = Rook(x=7,y=0,sl='R',team='white')
        self.board[7][1] = Knight(x=7,y=1,sl='N',team='white')
        self.board[7][2] = Bishop(x=7,y=2,sl='B',team='white')
        self.board[7][3] = Queen(x=7,y=3,sl='Q',team='white')
        self.board[7][4] = King(x=7,y=4,sl='K',team='white')
        self.board[7][5] = Bishop(x=7,y=5,sl='B',team='white')
        self.board[7][6] = Knight(x=7,y=6,sl='N',team='white')
        self.board[7][7] = Rook(x=7,y=7,sl='R',team='white')
        self.board[6][0] = Pawn(x=6,y=0,sl='P',team='white')
        self.board[6][0] = Pawn(x=6,y=1,sl='P',team='white')
        self.board[6][0] = Pawn(x=6,y=2,sl='P',team='white')
        self.board[6][0] = Pawn(x=6,y=3,sl='P',team='white')
        self.board[6][0] = Pawn(x=6,y=4,sl='P',team='white')
        self.board[6][0] = Pawn(x=6,y=5,sl='P',team='white')
        self.board[6][0] = Pawn(x=6,y=6,sl='P',team='white')
        self.board[6][0] = Pawn(x=6,y=7,sl='P',team='white')

    def display(self):
        for i in range(8):
            for j in range(8):
                if self.board[i][j].sl=='R':
                    print('R',end=' ')
                elif self.board[i][j].sl=='N':
                    print('N',end=' ')
                elif self.board[i][j].sl=='B':
                    print('B',end=' ')
                elif self.board[i][j].sl=='Q':
                    print('Q',end=' ')
                elif self.board[i][j].sl=='K':
                    print('K',end=' ')
                elif self.board[i][j].sl=='P':
                    print('P',end=' ')
                else:
                    print(self.board[i][j],end=' ')
            print()

    def figure_choice(self):
        while True:
            try:
                print('please give a position of figure which you chose')
                sx=int(input())
                sy=int(input())
                return sx,sy
            except:
                print('ERROR. Your choice is valid. Please choose only integers')

    def move_king(self):

        while True:
            try:
                print('please give a position of figure which you chose')
                sx=int(input())
                sy=int(input())
                return sx,sy
            except:
                print('ERROR. Your choice is valid. Please choose only integers')
            try:
                print('please give a position of king')
                sx=int(input())
                sy=int(input())
            except:
                print('ERROR. Your choice is valid. Please choose only integers')
            try:
                print('please choose a destination for king')
                dx=int(input())
                dy=int(input())
            except:
                print('ERROR. Your choice is valid. Please choose only integers')
            if self.board[dx][dy] == '.' :
                    if ( abs(sx-dx) <2 and abs(sx-dy) < 2 ):
                        self.board[dx][dy]=King(x=dx,y=dy,sl='K',team='white')
                        self.board[sx][sy] = '.'
                        return self.board
                        break


a=Chess_Board()

a.display()
print(a.board[7][0].sl)