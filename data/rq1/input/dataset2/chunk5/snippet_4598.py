#Source: https://stackoverflow.com/questions/63442808/typeerror-list-indices-must-be-integers-or-slices-not-nonetype-on-a-connect-4
def main():
    board = [
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None],
    ]

    board_list = []
    while len(board[0]) > len(board_list):
        board_list.append(str(len(board_list) + 1))

    header()

    active_player_index = 0
    players = ["Vasco", "PC"]
    symbols = ["O", "X"]
    player = players[active_player_index]

    while not find_winner(board):
        # show the board
        player = players[active_player_index]
        symbol = symbols[active_player_index]

        announce_turn(player)
        show_board(board)
        if not choose_location(board, symbol):
            print()
            print("You're an UBER IDIOT!")
            print("That spot was already used!")
            print()
            continue

        #   toggle active player
        active_player_index = (active_player_index + 1) % len(player)

    footer()


def header():
    print()
    print("-----------------------------")
    print("----------WHALECUM-----------")
    print("-----------------------------")
    print("----------CONNECT 4----------")
    print("-----------------------------")


def footer():
    print()
    print("-----------------------------")
    print("-----------THE END-----------")
    print("-----------------------------")


def show_board(board):
    print()
    for row in board:
        print("| ", end='')
        for cell in row:
            symbol = cell if cell is not None else " "
            print(symbol, end=" | ")
        print()
    for index, r in enumerate(board[0], start=1):
        print(f"  {index} ", end="")
    print()


def announce_turn(player):
    print()
    print(f"It's {player} turn!")
    print()
    print("Pick your column...")
    print()
    print("Here's the Board:")
    print()


def choose_location(board, symbol, board_list):
    column = input("Choose a column: ")
    while column not in board_list:
        print(f"{column} is not an option, try again")
        column = input("Choose a column: ")
    column = int(column) - 1
    row = None

    while board[row][column] is None:
        row += 1
    row = row - 1
    cell = board[row][column]
    if cell is not None:
        return False

    board[row][column] = symbol
    return True


def find_winner(board):
    sequences = get_winning_sequences(board)

    for cells in sequences:
        symbol1 = cells[0]
        if symbol1 and all(symbol1 == cell for cell in cells):
            return True

    return False


def get_winning_sequences(board):
    sequences = []

    # win by row
    rows = board
    sequences.extend(rows)

    # win by columns
    for col_idx in range(0, 3):
        col = [
            board[0][col_idx],
            board[1][col_idx],
            board[2][col_idx],
        ]
        sequences.append(col)

    # win by diagonals
    diagonals = [
        [board[0][0], board[1][1], board[2][2]],
        [board[0][2], board[1][1], board[2][0]],
    ]
    sequences.extend(diagonals)

    return sequences


if __name__ == '__main__':
    main()