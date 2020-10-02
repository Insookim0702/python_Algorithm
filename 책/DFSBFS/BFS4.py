graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited=[False] *9
def bfs(x):
    from collections import deque
    que = deque()
    que.append(x)
    while que:
        x = que.popleft()
        print(x, end=' ')
        for i in graph[x]:
            if not visited[i]:
                que.append(i)
                visited[i] = True


bfs(1)









