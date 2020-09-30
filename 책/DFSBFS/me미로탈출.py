n, m = 3, 3
graph = [[1, 1, 0], [0, 1, 0], [0, 1, 1]]
from collections import deque

result = 0
que = deque()
que.append([0, 0])
visited = [[False for i in range(n)] for k in range(m)]
visited[0][0] = True
print(visited)
while que:
    x, y = que.popleft()
    if graph[x][y] == 1:
        result += 1
    if x + 1 < n and not visited[x + 1][y]:
        que.append([x + 1, y])
        visited[x + 1][y] = True
    if x - 1 >= 0 and not visited[x - 1][y]:
        que.append([x - 1, y])
        visited[x - 1][y] = True
    if y + 1 < m and not visited[x][y + 1]:
        que.append([x, y + 1])
        visited[x][y + 1] = True
    if y - 1 >= 0 and not visited[x][y - 1]:
        que.append([x, y - 1])
        visited[x][y - 1] = True

print(result)
