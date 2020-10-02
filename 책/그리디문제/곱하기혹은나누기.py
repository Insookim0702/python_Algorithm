# 11:22~ 11:52

n = '02984'
n = '567'
n = '12302984'
n = '102984'
n ='00000'
n ='11'
n ='1'
n ='0'
from collections import deque

que = deque(list(map(int, n)))
print(que)
result = que.popleft()
while que:
    value1 = que.popleft()
    add = result + value1
    mult = result * value1

    if add > mult:
        if add != 0:
            result = add
    else :
        if mult != 0:
            result = mult
print(result)
