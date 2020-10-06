# 14:30 ~ 15:21 품!

n, k = map(int, input().split())
print(n, k)
flask = [[]]
for i in range(1, n + 1):
    flask.append(list(map(int, input().split())))
    flask[i].insert(0, 0)
print(flask)
limit_time, result_x, result_y = map(int, input().split())
print(limit_time, result_x, result_y)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def virus_position():
    virus_position = []
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if flask[i][j] != 0:
                virus_position.append([flask[i][j], (i, j)])
    virus_position.sort()
    print(virus_position)
    return virus_position


def dfs(limit_time):
    time = 0
    if time == limit_time:
        return flask[result_x, result_y]
    from collections import deque
    while limit_time != time:
        que = deque(virus_position())
        while que:
            virus, position = que.popleft()
            for i in range(4):
                nx = position[0] + dx[i]
                ny = position[1] + dy[i]
                if nx >= 1 and nx <= n and ny >= 1 and ny <= n:
                    if flask[nx][ny] == 0:
                        flask[nx][ny] = virus
        i = 0
        time += 1


dfs(limit_time)
print(flask[result_x][result_y])
