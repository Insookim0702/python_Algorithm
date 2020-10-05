#21:00 ~ 21:40
n = 4
m = 4
k = 2
x = 1
street = [(1, 2), (1, 3), (2, 3), (2, 4)]
n = 4
m = 3
k = 2
x = 1
street = [(1, 2), (1, 3), (1, 4)]
# n = 4
# m = 4
# k = 1
# x = 1
# street = [(1, 2), (1, 3), (2, 3), (2, 4)]
visited = [False] * (n + 1)

def bfs(street, x, k):
    answer = ''
    from collections import deque
    que = deque()
    que.append(x)
    count = 1
    while que:
        v = que.popleft()
        for i in street:
            ix, iy = i
            if ix == v:
                if not visited[iy]:
                    if count == k:
                        answer += str(iy) + ' '
                    que.append(iy)
                    visited[iy] = True
        count += 1
        if answer == '' :
            return -1
        else :
            return answer



print(bfs(street, x, k))
