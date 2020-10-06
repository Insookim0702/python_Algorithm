n, m = map(int, input().split())
# 11:41 ~
data = []
temp = []
for i in range(n):
    data.append(list(map(int, input().split())))
result = 0

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def dfs(count):
    global result
    if count == 3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = data[i][j]
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus(i, j)
        max(result, get_count_0())
        return
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                temp[i][j] = 1
                count += 1
                dfs(count)
                temp[i][j] = 0
                count -= 1


def get_count_0():
    count = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                count += 1
    return count


def virus(x, y):
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if nx >= 0 or nx < n or ny >= 0 or ny < m:
            if temp[nx][ny] == 0:
                temp[nx][ny] = 2
                virus(nx, ny)


dfs(0)
print(result)
