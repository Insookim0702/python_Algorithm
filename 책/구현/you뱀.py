n = int(input())
k = int(input())
data = [[0] * n for _ in range(n)]
info = []
for _ in range(k):
    a,b = map(int, input().split())
    data[a][b] = 1

l = int(input())
for _ in range(1):
    x, c = input().split()
    info.append((int(x), c))


dx = [0,1,0,-1]
dy = [1,0,-1,0]

def turn(direction, c):
    if c == 'L':
        direction = (direction -1) %4
    else:
        direction = (direction +1) % 4
def simulate():
    x, y = 1, 1
    data[x][y] = 2
    direction = 0
    time = 0
    index = 0
    q = [(x, y)]
    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]
        if 1 <= nx and nx <= n and 1 <= ny and ny <=n and data[nx][ny] !=2:
            #사과가 없다면 이동 후 꼬리 제거
            if data[nx][ny] ==  0:
                data[nx][ny] = 2
                q.append((nx, ny))
                px, py = q.pop(0)
                data[px][py] = 0
            # 사과가 있다면 이동 후에 꼬리를 그대로 두기
            if data[nx][ny] == 1:
                data[nx][ny] = 2
                q.append((nx, ny))
        else:
            time +=1
            break
        x, y = nx, ny
        time +=1
        if index < 1 and time ==info[index][0]:
            direction = turn(direction, info[index][1])
            index += 1
    return time


print(simulate())