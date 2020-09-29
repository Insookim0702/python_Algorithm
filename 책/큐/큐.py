que = []

from collections import deque

que = deque()

que.append(1)
que.append(2)
que.append(3)
que.popleft()
print(list(que))