#Source: https://stackoverflow.com/questions/64607460/what-am-i-missing-because-i-keep-getting-a-typeerror-list-indices-must-be-int
def add_rows(sq_list):
    rowNum = [[0, 0, 0],
              [0, 0, 0],
              [0, 0, 0]]
    
    for row in rowNum:
        total = 0
        for column in sq_list[row]:
            total += column
            
        print("Row total is:", total)
    
add_rows([[1, 3, 8],
          [2, 4, 6],
          [7, 9, 0]])