# 12:55~1:11(16분)
#공 개수, 공 최대 무게
n,m = 5, 3
arr = [1,3,2,3,2]
n,m = 8, 5
arr = [1,5,4,3,2,4,5,2]
n,m = 5, 2
arr = [1,1,1,1,1]
l =[]
for idx, v in enumerate(arr):
    l.append(((idx+1), v))
print(l)
from itertools import combinations
com = combinations(l,2)
s = set()
for i in com:
    if i[0][1] != i[1][1]:
        s.add(i)
        print(i)

print(len(s))