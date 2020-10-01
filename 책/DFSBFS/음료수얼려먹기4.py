graph = [
    [0, 0, 1],
    [0, 1, 0],
    [1, 0, 1]
]
n, m = 3, 3
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

#내가푼
def dfs(t):
    x, y = t
    if graph[x][y] == 1:
        return False
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx <= -1 or nx >= n or ny <= -1 or ny >= m:
            return False
        if graph[nx][ny] != 1:
            dfs((nx, ny))
            graph[nx][ny] = 1
        return True
    return False

#책
def dfs(x,y):
    if x <=-1 or x >= n or y <= -1 or y >=m:
        return False
    if graph[x][y] ==0:
        graph[x][y] =1
        dfs(x -1, y)
        dfs(x +1, y)
        dfs(x, y+1)
        dfs(x, y-1)
        return True
    return False

result = 0
for i in range(n):
    for j in range(m):
        if dfs((i, j)) == True:
            result += 1

print(result)
