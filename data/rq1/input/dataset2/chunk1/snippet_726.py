#Source: https://stackoverflow.com/questions/73915176/why-do-i-get-a-nameerror-when-i-run-this-list-comprehension-inside-a-class
class Game:
    row_num = 7
    column_num = 6
    board = [['[]' for i in range(row_num)] for x in range(column_num)]