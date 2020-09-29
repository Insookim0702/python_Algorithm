from collections import deque

n, m = 3, 3
graph = [[1, 1, 0], [0, 1, 0], [0, 1, 1]]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    result = 0
    que = deque()
    que.append((x, y))
    while que:
        x, y = que.popleft()
        # 현재 위치에서 네방향으로의 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로 찾기 공간을 벗어난 경우 무시
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                que.append((nx, ny))
    return graph[n - 1][m - 1]


print(bfs(0, 0))
