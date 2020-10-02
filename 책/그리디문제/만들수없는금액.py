# 13:34 ~ 14:54(20분)

n = 5
arr = [3,2,1,1,9]
arr = [9,123,12]
arr = [3,5,7]
arr = [1,1,1,1,1,1]
arr = [1]
s = set()
a = []
from itertools import combinations
for i in range(1, len(arr)+1):
    one = combinations(arr,i)
    for j in one:
        s.add(sum(j))

a = list(s)
a.sort()
print(a)
for i in range(1, a[len(a)-1]+1):
    if i != a[i-1]:
        print(i)
        break
if i == a[len(a)-1]:
    print(i+1)

