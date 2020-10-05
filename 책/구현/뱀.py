# 16:42 ~ 17:56 못품 ... 1시간 14
# 보트크기
n = 6
# 사과 개수
k = 3
# 사과 위치
p = [(3, 4), (2, 5), (5, 3)]

# 뱀의 방향 전환 횟수
l = 3

l_p = [(3, 'D'), (15, 'L'), (17, 'D')]


# l_p = [(8,'D'), (10,'D'), (11, 'D'), (13, 'L')]
def solution(n, p, l):
    board = [[0] * n for _ in range(n)]
    for i in p:
        x, y = i
        board[x][y] = 1
    print(board)
    now_position = [0, 0, 'D']
    dx = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    lx = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    d_idx = 0
    l_idx = 0
    time = 0
    from collections import deque
    occupy = deque()
    occupy.append((now_position[0], now_position[1]))
    for i in l_p:
        move, left_or_right = i
        for j in range(move):
            if now_position[2] == 'D':
                x, y = dx[d_idx % 4]
            else:
                x, y = lx[l_idx % 4]
            now_position[0] += x
            now_position[1] += y
            now_x = now_position[0]
            now_y = now_position[1]
            time += 1
            if now_x >= n or now_x <= -1 or now_y >= n or now_y <= -1:
                print(now_position)
                return time
            if occupy.count((now_x, now_y)) > 0:
                return time
            occupy.append((now_x, now_y))
            print(occupy)
            if board[now_x][now_y] != 1:
                occupy.popleft()
                print(occupy)
        now_position[2] = left_or_right
        d_idx += 1
        l_idx += 1
        print(occupy)
        print(now_position)
    return time


print(solution(n, p, l))
