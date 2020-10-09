# 14:47 ~ 14:59 12분

n,m = map(int,input().split())
w = [i for i in range(1, n+1)]
data = list(map(int, input().split()))
from itertools import combinations
b = combinations(w,2)
s = []
for i in b:
    x, y = i
    if data[x-1] != data[y-1]:
        s.append(i)


print(len(s))