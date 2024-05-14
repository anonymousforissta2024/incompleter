#Source: https://stackoverflow.com/questions/58791891/what-does-this-error-mean-typeerror-parameters-to-generic-types-must-be-types
def in_matrix(matr: List[List:int], cell: List[int]) -> bool:
    b = cell.pop()
    a = cell.pop()
    print(a)
    print(b)
    for y in range(len(matr)):
        for x in range(len(matr[y])):
            if matr[a][b] == True:
                return True
            else:
                return False