from collections import deque

ROW = 5
COL = 5

class Cell:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

class queueNode:
    def __init__(self, pt: Cell, dist: int):
        self.pt = pt
        self.dist = dist


def checkValid(row: int, col: int):
    return (row >= 0) and (row < ROW) and (col >= 0) and (col < COL)


rowNum = [-1, 0, 0, 1]
colNum = [0, -1, 1, 0]


def bfsLee(mat, src: Cell, dest: Cell):
    if mat[src.x][src.y] != 1 or mat[dest.x][dest.y] != 1:
        return -1

    visited = [[False for i in range(COL)]
               for j in range(ROW)]

    visited[src.x][src.y] = True

    q = deque()

    s = queueNode(src, 0)
    q.append(s)

    while q:

        curr = q.popleft()

        pt = curr.pt
        if pt.x == dest.x and pt.y == dest.y:
            return curr.dist

        for i in range(4):
            row = pt.x + rowNum[i]
            col = pt.y + colNum[i]

            if checkValid(row, col) and mat[row][col] == 1 and not visited[row][col]:
                visited[row][col] = True
                Adjcell = queueNode(Cell(row, col),curr.dist + 1)
                q.append(Adjcell)

    # Return -1 if destination cannot be reached
    return -1


# Driver code
mat = [[1, 0, 1, 1, 1],
       [1, 0, 1, 0, 1],
       [1, 1, 1, 0, 1],
       [0, 0, 0, 0, 1],
       [1, 1, 1, 0, 1]]
source = Cell(0, 0)
dest = Cell(2, 1)

dist = bfsLee(mat, source, dest)

if dist != -1:
    print("Length of the Shortest Path is", dist)
else:
    print("Shortest Path doesn't exist")