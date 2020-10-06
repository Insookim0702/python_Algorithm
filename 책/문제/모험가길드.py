# 10:38~ 11시 16분(38뷴)
n = 5
arr = [2, 3, 1, 2, 2]

#arr = [3, 3, 3]
#arr = [1] #1
#arr = [2] #0
#arr = [3] #0
#arr = [1, 2, 3, 3]  # 2

arr.sort(reverse=True)
group = 0
from collections import deque
que = deque(arr)
print(que)
while que:
    max_fear = que.popleft()
    if max_fear ==1:
        group +=1
        break
    if (max_fear-1) > (len(que)):
        break
    group += 1
    for i in range(max_fear-1):
        que.popleft()

print(group)