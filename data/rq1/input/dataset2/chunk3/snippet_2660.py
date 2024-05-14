#Source: https://stackoverflow.com/questions/52000635/typeerror-nonetype-object-is-not-callable-but-object-is-not-nonetype
def winner(board):
    WAYS_TOWIN = ((0, 1, 2),
                  (3, 4, 5),
                  (6, 7, 8),
                  (0, 4, 8),
                  (2, 4, 6),
                  (0, 3, 6),
                  (1, 4, 7),
                  (2, 5, 8))
    for row in WAYS_TOWIN:
        if board[row[0]] == board[row[1]] == board[row[2]] != " ":
            winner = board[row[0]]
            return winner
    if " " not in board:
            return TIE
    else:
        return None



#Main
instructions()
human = input("Enter your name: "); print("\n")
pieces = who_first(human, computer); print("\n")#pieces becomes a list with human piece first and computer piece second
board = new_board(); print("\n")
winner = winner(board)



while winner == None and winner != TIE:
    if turn == pieces[0]:#if human is first
        winner = winner(board)