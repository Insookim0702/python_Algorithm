n, m = 3, 3
graph = [[1, 1, 0], [0, 1, 0], [0, 1, 1]]

from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def bfs(graph):
    que = deque()
    que.append((0, 0))
    while que:
        v = que.popleft()
        x = v[0]
        y = v[1]
        for i in range(4):
            xidx = x + dx[i]
            yidx = y + dy[i]
            if xidx <= -1 or xidx >=n or yidx <= -1 or yidx >= n:
                continue
            if graph[xidx][yidx] == 1:
                que.append((xidx, yidx))
                graph[xidx][yidx] = graph[x][y] +1
    return graph[n-1][m-1]

print(bfs(graph))