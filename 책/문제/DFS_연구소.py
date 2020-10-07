n, m = map(int, input().split())
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
data = []
temp = [[0] * m for _ in range(n)]
vp = []
space = []
for i in range(n):
    data.append(list(map(int, input().split())))
    for j in range(m):
        if data[i][j] == 2:
            vp.append((i, j))
        if data[i][j] == 0:
            space.append((i, j))


def count_0():
    count = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                count += 1
    return count


def virus_infection_field(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            if temp[nx][ny] == 0:
                temp[nx][ny] = 2
                virus_infection_field(nx, ny)


result = 0


def dfs(count):
    global result
    if count == 3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = data[i][j]
        for i in vp:
            x, y = i
            virus_infection_field(x, y)
        result = max(result, count_0())
        return
    for i in range(n):
        for j in range(m):
            if data[i][j] ==0:
                data[i][j] = 1
                count += 1
                dfs(count)
                data[i][j] = 0
                count -= 1


dfs(0)
print(result)
