#6:05

from collections import deque


def solution(land, height):
    print(land)
    answer = 0
    x = len(land)
    visited =[False for _ in range(x*x)]
    #visited =[[False for _ in range(x)] for _ in range(x)]
    while not all(visited):
        bfs(land, x)
    return answer


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def bfs(graph,x):
    que = deque()
    que.append((0, 0))
    while que:
        x, y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx <= -1 or nx >= x or ny <= -1 or ny >= x:
                continue
            if graph[nx][ny] == 1:
                que.append((nx, ny))
                graph[nx][ny] = graph[x][y] + 1

                
solution([[1, 4, 8, 10], [5, 5, 5, 5], [10, 10, 10, 10], [10, 10, 10, 20]], 3)