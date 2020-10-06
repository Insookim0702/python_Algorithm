# 11:54 ~ 12:32(18분 초과)
s = '0001100'
#s ='1010100'
zero = s.count('0')
one = s.count('1')
zero_result =0
one_result = 0
from collections import deque
que = deque(list(s))
fir_v = que.popleft()
if fir_v =='1': one_result +=1
if fir_v =='0': zero_result +=1
arr = [fir_v]
while que:
    v = que.popleft()
    if arr[len(arr) - 1] != '0' and v == '0':
        arr.append(v)
        zero_result += 1
    if arr[len(arr)-1] !='1' and v =='1':
        arr.append(v)
        one_result +=1

arr = [one_result, zero_result]
print(min(arr))




