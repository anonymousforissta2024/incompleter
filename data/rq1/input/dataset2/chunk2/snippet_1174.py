#Source: https://stackoverflow.com/questions/58389828/typeerror-unhashable-type-list-in-python-chess-program
king=(5,1)
opponentmoves={'ksknight': [(8, 3), (5, 2), (6, 3)],
 'ksbishop': [(3, 6), (4, 7), (5, 8), (1, 4), (1, 6), (3, 4), (4, 3), (5, 1), (6, 1)],
 'king': [(6, 1), (5, 2), (4, 1)],
 'queen': [(4, 5), (2, 4), (1, 3), (2, 6), (1, 7), (4, 4)],
 'qsknight': [(3, 3), (1, 3)]}
opponentposition={'ksknight': (1, 3), 
 'ksbishop': (1, 6), 
 'king': (6, 1), 
 'queen': (4, 5), 
 'qsknight': (3, 3)}
if king in [z for v in opponentmoves.values() for z in v]:
    piece=[key for key in opponentmoves if king in opponentmoves[key]]
    opponentpieceposition=opponentposition.get(piece)
    print(opponentpieceposition)