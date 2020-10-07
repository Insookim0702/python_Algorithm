# 10:22 ~ 11:48 1시간 26분 풀어도 못품.,
# 0 빈칸
# 1 벽
# 2 바이러스 있는 곳

n, m = map(int, input().split())
lab = []

data = []

for j in range(m):
    lab.append(list(map(int, input().split())))

print(lab)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def dfs(lab, x, y, wall, count):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx <= -1 or nx >= n or ny <= -1 or ny >= m:
            continue
        if lab[nx][ny] == 0:
            if wall > 0:
                lab[nx][ny] = 1
                wall -= 1
            else:
                break
    if count_0(infection_lab(lab,x, y)) ==0:
        return
    if count < new_count:
        return new_count
    else:
        dfs(lab, )
temp = [[0] * m for _ in range(n)]


def dfs(count):
    global result
    if count == 3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = data[i][j]
        # 각 바이러스 위치에서 전염 진행
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    infection_lab(i,j)
        result = max(result, count_0())
        return
    for i in range(n):
        for j in range(m):
            if data[i][j] == 0:
                data[i][j] = 1
                count +=1
                dfs(count)
                data[i][j] = 0
                count -= 1

def count_0():
    count = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                count +=1
    return count


def infection_lab(x, y):
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if nx >= 0 or nx < n or ny >= 0 or ny < m:
            if temp[nx][ny] == 0:
                temp[nx][ny] = 2
                infection_lab(nx, ny)

for i in range(len(lab)):
    for j in range(len(lab)):
        if lab[i][j] == 2:
            dfs(lab, i, j, 3, 0)
