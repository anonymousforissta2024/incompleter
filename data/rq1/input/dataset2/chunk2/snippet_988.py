#Source: https://stackoverflow.com/questions/60917020/dictionary-with-lists-typeerror-unhashable-type-list
def satisfied(self, assignment: Dict[str, List[str]]) -> bool:
        row: str = self.variables[0]
        column: str = self.variables[1]

        # If either variable is not in the assignment then it is not
        # yet possible for them to conflict
        if row not in assignment or column not in assignment:
            return True

        row_num: int = int(row[3:])
        col_num: int = int(column[3:])

        return assignment[row][col_num] == assignment[col][row_num] # here is this error