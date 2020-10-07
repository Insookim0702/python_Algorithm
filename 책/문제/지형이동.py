# 21:00 ~ 22:54
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def dfs(land, x, y, group, height, visited):
    n = len(land)
    group.append((land[x][y], x, y))
    visited[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx <= -1 or nx >= n or ny <= -1 or ny >= n:
            continue
        if visited[nx][ny]:
            continue
        if abs(land[x][y] - land[nx][ny]) <= height:
            dfs(land, nx, ny, group, height, visited)
    return group


# 특정 원소가 속한 집합을 찾기
def find_parent(parents, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parents[x] != x:
        parents[x] = find_parent(parents, parents[x])
    return parents[x]


# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def solution(land, height):
    answer = 0
    n = len(land)
    visited = [[False] * n for _ in range(n)]
    groups = []
    groups_count = 0
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                groups.append((groups_count, dfs(land, i, j, [], height, visited)))
                groups_count += 1
    print(groups)
    re_groups = [[0] * n for _ in range(n)]
    parents = [i for i in range(0, len(groups))]
    # 부모테이블 구하기
    for i in groups:
        group_num, group = i
        for j in group:
            v, x, y = j
            re_groups[x][y] = group_num
    print('parents :', re_groups)

    # edges(=모든 간선에 대한 비용 구하기) 구하기
    edges = set()
    result = 0
    for i in range(n):
        for j in range(n):
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if nx <= -1 or nx >= n or ny <= -1 or ny >= n:
                    continue
                if re_groups[i][j] == re_groups[nx][ny]:
                    continue
                diff = abs(land[i][j] - land[nx][ny])

                if diff > height:
                    if re_groups[i][j] < re_groups[nx][ny]:
                        edges.add((diff, re_groups[i][j], re_groups[nx][ny]))
                    else:
                        edges.add((diff, re_groups[nx][ny], re_groups[i][j]))

    edges = list(edges)
    edges.sort()
    print('edges :', edges)

    # 간선 코스트 확인
    for edge in edges:
        cost, a, b = edge
        #사이클이 발생하지 않는 경우에만 집합에 포함
        if find_parent(parents, a) != find_parent(parents, b):
            union_parent(parents, a, b)
            answer += cost
    return answer


#print(solution([[1, 4, 8, 10], [5, 5, 5, 5], [10, 10, 10, 10], [10, 10, 10, 20]], 3))  # 15
print(solution([[10, 11, 10, 11], [2, 21, 20, 10], [1, 20, 21, 11], [2, 1, 2, 1]], 1)) #18
