graph = [[],[1,1],[1,2],[1,3],[2,1],[2,2],[2,3],[3,1],[3,2],[3,3]]

visited=[False] *10

def dfs(graph, v, visited):
    visited[v] =True
    print(v, end=' ')
    for i in graph[v]:
        if graph[v][0] == graph[v][1]:
            dfs(graph, i+1, visited)
        if not visited[i]:
            dfs(graph, i, visited)

dfs(graph, 1, visited)