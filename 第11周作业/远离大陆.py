def maxDistance(grid):
    deque = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                deque.append((i, j))
    if len(deque) == len(grid) * len(grid[0]):
        return -1
    if len(deque) == 0:
        return -1
    step = 0
    while deque != []:
        layer = range(len(deque))
        # print(deque, step)
        for _ in layer:
            currVertex = deque.pop(0)
            allNeighbers = validNeighbers(currVertex, grid)
            for neighber in allNeighbers:
                if grid[neighber[0]][neighber[1]] == 0:
                    deque.append(neighber)
                    grid[neighber[0]][neighber[1]] = -1
        step += 1
    return step - 1


#某一个顶点距离为1的所有顶点
def validNeighbers(vertex, grid):
    res = []
    for vtx in [(vertex[0], vertex[1] + 1), (vertex[0] + 1, vertex[1]),
                (vertex[0] - 1, vertex[1]), (vertex[0], vertex[1] - 1)]:
        if isValid(vtx, grid):
            res.append(vtx)
    return res


#某顶点是否在网格内
def isValid(vertex, grid):
    return vertex[0] in range(len(grid)) and vertex[1] in range(len(grid[0]))


grid = eval(input())
print(maxDistance(grid))