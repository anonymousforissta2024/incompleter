#Source: https://stackoverflow.com/questions/60807377/why-is-python-giving-attributeerror-even-when-the-attribute-does-exist
"""
Shortest distance between two cells in a matrix or grid

"""

class Tile:
  def __init__(self, row, col, dist):  
    self.row = row
    self.col = col
    self.dist = dist

def min_path(rows, cols, lot):
  start_node = Tile(0, 0, 0)
  q = []
  q.append(start_node)
  visited = [[False]*cols for i in range(rows)]

  for i in range(rows):
    for j in range(cols):
      if lot[i][j] == 0:
        visited[i][j] = True

  while q:
    new_tile = q.pop(0)

    print(new_tile.row)

    if lot[new_tile.row][new_tile.col] == 9:
      return new_tile.dist

    if new_tile.row - 1 >= 0 and visited[new_tile.row - 1][new_tile.col] == False:
      Tile(new_tile.row - 1, new_tile.col, new_tile.dist + 1)
      q.append(Tile)
      visited[new_tile.row - 1][new_tile.col] = True

    if new_tile.row + 1 < rows and visited[new_tile.row + 1][new_tile.col] == False:
      Tile(new_tile.row + 1, new_tile.col, new_tile.dist + 1)
      q.append(Tile)
      visited[new_tile.row + 1][new_tile.col] = True

    if new_tile.col - 1 >= 0 and visited[new_tile.row][new_tile.col - 1] == False:
      Tile(new_tile.row, new_tile.col - 1, new_tile.dist + 1)
      q.append(Tile)
      visited[new_tile.row][new_tile.col - 1] = True

    if new_tile.col + 1 < cols and visited[new_tile.row][new_tile.col + 1] == False:
      Tile(new_tile.row, new_tile.col + 1, new_tile.dist + 1)
      q.append(Tile)
      visited[new_tile.row][new_tile.col + 1] = True

  return -1


if __name__ == "__main__":
  lot = [
    [1, 0, 0, 0],
    [1, 0, 1, 0],
    [1, 1, 0, 0],
    [0, 1, 9, 0],
  ]
  result = min_path(4, 4, lot)
  print(result)