# 15:40 ~ 16:57 1시간 17분 못품
n, l, r = map(int, input().split())
popul = []
for i in range(n):
    popul.append(list(map(int, input().split())))

groups = []
visited = [[False] * n for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def dfs(popul, x, y, visited, group):
    if visited[x][y] == True:
        return
    group.append([popul[x][y],x, y])
    visited[x][y] = True
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if nx <= -1 or nx >= n or ny <= -1 or ny >= n:
            continue
        if abs(popul[x][y] - popul[nx][ny]) >= l and abs(popul[x][y] - popul[nx][ny]) <= r:
            dfs(popul, nx, ny, visited, group)
    return group

def check_all_true():
    for i in visited:
        if not all(i):
            return False
    return True

def find_false():
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                return i, j

def make_groups(popul):
    while not check_all_true():
        x, y = find_false()
        g = dfs(popul, x, y, visited, [])
        groups.append(g)

def move_pop(groups):
    for group in groups:
        s = 0
        for i in group:
            v,x,y = i
            s += v
        general_pop = s // len(group)
        for i in range(len(group)):
            group[i][0] = general_pop
    for group in groups:
        for g in group:
            v, x, y = g
            popul[x][y] = v

count = 0
def sol(popul):
    global count
    make_groups(popul)
    print(groups)
    move_pop(groups)
    print(popul)
    count += 1
    sol(popul)




sol()




