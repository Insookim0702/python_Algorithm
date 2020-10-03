#6:05

from collections import deque


def solution(land, height):
    result = 0
    size = len(land)
    #visited =[False for _ in range(x*x)]
    visited =[[False for _ in range(size)] for _ in range(size)]
    groups =[]
    all_visited =[False for _ in range(size)]
    px,py =0,0
    # 그룹 짓기
    while not all(all_visited):
        groups.append(bfs(px, py, land, size, visited, height))
        for i in range(size):
            all_visited[i] = all(visited[i])
            if not all(visited[i]):
                px = i
                for j in range(size):
                    if not visited[i][j]:
                        py = j
                        break
                break
    print(visited)
    print(groups)
    parent = parent = [i for i in range(0, len(groups))]

    re_groups = [[0 for _ in range(size)] for _ in range(size)]
    for i in range(len(groups)):
        for j in groups[i]:
            x,y = j
            re_groups[x][y] = i
    print(re_groups)
    edges = set()
    #edge구하기
    for i in range(len(re_groups)):
        for j in range(len(re_groups)):
            group_num = re_groups[i][j]
            for d in range(4):
                nx = i + dx[d]
                ny = j + dy[d]
                if nx <= -1 or nx >= size or ny <= -1 or ny >= size:
                    continue
                group_num2 = re_groups[nx][ny]
                if group_num != group_num2:
                    cost = abs(land[nx][ny] - land[i][j])
                    if cost > height:
                        if group_num > group_num2:
                            group_num, group_num2 = group_num2, group_num
                        edges.add((cost, (group_num, group_num2)))
    edges = list(edges)
    edges.sort()
    print(edges)

    for edge in edges:
        cost = edge[0]
        a, b = edge[1]
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a,b)
            result += cost

    # 사다리 올릴 곳 찾기
    return result


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def bfs(px, py, graph, size, visited, k):
    que = deque()
    que.append((px, py))
    group = []
    while que:
        x, y = que.popleft()
        group.append((x,y))
        visited[x][y] = True
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx <= -1 or nx >= size or ny <= -1 or ny >= size:
                continue
            if visited[nx][ny]:
                continue
            if abs(graph[x][y] - graph[nx][ny]) > k:
                continue
            que.append((nx, ny))
            visited[nx][ny] =True
    return group

def find_parent(parent, a):
    if parent[a] !=a:
        parent[a] = find_parent(parent, parent[a])
    return parent[a]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b



print(solution([[1, 4, 8, 10], [5, 5, 5, 5], [10, 10, 10, 10], [10, 10, 10, 20]], 3))