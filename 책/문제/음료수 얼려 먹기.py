# 17:13 ~ 17:47
n ,m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

dx = [1,-1,0,0]
dy = [0,0,1,0-1]

def dfs(x,y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return 0
    if graph[x][y] == 1:
        return 0
    g =graph
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x+1, y)
        dfs(x-1, y)
        dfs(x, y+1)
        dfs(x, y-1)
        return 1
    return 0
result = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] != 1:
            result += dfs(i,j)

print(result)