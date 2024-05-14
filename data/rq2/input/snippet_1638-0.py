def swapPositions(list, pos1, pos2):
    list[pos1], list[pos2] = (list[pos2], list[pos1])
    return list
pos1, pos2 = (1, 3)
print(swapPositions(List, pos1 - 1, pos2 - 1))