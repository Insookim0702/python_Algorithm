# 11:08 ~ 12 08 1시간 10분 풀었는데 못 품
# dfs 재귀 구현을 못함
n = int(input())
data = []
temp =[['X'] * n for _ in range(n)]
teacher_position = []
for i in range(n):
    data.append(list(input().split()))
    for j in range(n):
        if data[i][j] == 'T':
            teacher_position.append((i, j))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def get_count(temp):
    count = 0
    for i in teacher_position:
        x, y = i
        for j in range(4):
            nx = x + dx[j]
            ny = y + dy[j]
            while nx >= 0 and nx < n and ny >= 0 and ny < n:
                if temp[nx][ny] == 'S':
                    count +=1
                    return count
                elif temp[nx][ny] == 'O':
                    break
                nx = nx + dx[j]
                ny = ny + dy[j]
    return count


result = False

def dfs(count):
    global result
    if count == 3:
        for i in range(n):
            for j in range(n):
                temp[i][j] = data[i][j]
        t = temp
        check(temp)
        t = temp
        count1 = get_count(temp)
        if count1 == 0:
            result = True
            return
        return
    for i in range(n):
        for j in range(n):
            te1 = data
            if data[i][j] == 'X':
                data[i][j] = 'O'
                count += 1
                dfs(count)
                data[i][j] = 'X'
                count -= 1



def check(temp):
    for i in teacher_position:
        x, y = i
        for j in range(4):
            nx = x + dx[j]
            ny = y + dy[j]
            while nx >= 0 and nx < n and ny >= 0 and ny < n:
                if temp[nx][ny] == 'X':
                    temp[nx][ny] = 'T'
                nx = nx + dx[j]
                ny = ny + dy[j]
dfs(0)
print(result)
# [
# ['T', 'S', 'T', 'T', 'T'],
# ['T', 'T', 'S', 'T', 'T'],
# ['T', 'T', 'T', 'X', 'T'],
# ['T', 'T', 'T', 'T', 'T'],
# ['T', 'T', 'T', 'T', 'T']
# ]
