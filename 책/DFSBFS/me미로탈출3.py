n, m = 3, 3
graph = [[1, 1, 0], [0, 1, 0], [0, 1, 1]]
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(x, y):
    que = deque()
    que.append((x, y))
    while que:
        xi, yi = que.popleft()
        for i in range(4):
            nx = xi + dx[i]
            ny = yi + dy[i]
            if nx <= -1 or nx >= n or ny <= -1 or ny >=m:
                continue
            if graph[nx][ny] == 1:
                que.append((nx, ny))
                graph[nx][ny] = graph[xi][yi] + 1


bfs(0, 0)
print(graph[n - 1][m - 1])
