graph = [
    [1, 1, 0],
    [0, 1, 0],
    [0, 1, 1]
]
n, m = 3, 3
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):
    from collections import deque
    que = deque()
    que.append((x, y))
    while que:
        x, y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx <= -1 or nx >= n or ny <= -1 or ny >= m:
                continue
            if graph[nx][ny] == 1:
                que.append((nx, ny))
                graph[nx][ny] = graph[x][y] +1
    return graph[n-1][m-1]


print(bfs(0,0))