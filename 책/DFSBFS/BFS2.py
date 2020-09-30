graph =[[],[2,3,8],[1,7],[1,4,5],[3,5],[3,4],[7],[2,6,8],[1,7]]
visited = [False] * 9
from collections import deque
def bfs(graph,v,visited):
    que = deque()
    que.append(v)
    visited[v] = True
    while que:
        v = que.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                que.append(i)
                visited[i] = True


bfs(graph, 1, visited)
