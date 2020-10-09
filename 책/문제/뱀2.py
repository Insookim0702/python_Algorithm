# 20:21 ~
n = int(input())
apple_num = int(input())
a = []
map = [[0]* n for i in range(n)]
print(map)
for _ in range(apple_num):
    x = input().split()
    a.append(x)

print(a)

for i in a:
    x, y = i
    map[int(x) - 1][int(y) - 1] = 1

print(map)

m = int(input())
move_command = []
for _ in range(m):
    move_command.append((input().split()))

occupy_area = [[0, 0, 'D']]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
time = 0


def process(time):
    global i, x, count
    mm = move_command
    idx = 0
    for i in move_command:
        go = i[0]
        direct_command = i[1]
        count = len(move_command)


        now_x, now_y, direct = occupy_area[0]
        if direct == 'D':
            for _ in range(int(go)):
                occupy_area.append((now_x, now_y))
                o = occupy_area
                now_x += dx[idx]
                now_y += dy[idx]
                time += 1
                if now_x <= -1 or now_y <= -1 or now_x >= n or now_y >= n or (now_x, now_y) in occupy_area:
                    return time
                occupy_area[0][0] = now_x
                occupy_area[0][1] = now_y
                occupy_area[0][2] = direct_command
                if map[now_x][now_y] != 1:
                    occupy_area.pop(len(occupy_area) - 1)
            idx += 1


print(process(0))


def check_true():

    return True

