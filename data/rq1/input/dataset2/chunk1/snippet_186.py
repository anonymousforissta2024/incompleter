#Source: https://stackoverflow.com/questions/61919865/typeerror-parameters-to-generic-types-must-be-types-got-ellipsis
def get_list_from_tuple(board: Tuple[Tuple[Optional[int], ...], ...]) -> List[List[Optional[int], ...], ...]:
    return list(list(x) for x in board)