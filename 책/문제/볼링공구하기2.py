
#12:07 ~12:20
from itertools import combinations

n,m = input().split()
arr = list(map(int, input().split()))
ar = []
for idx, v in enumerate(arr):
    ar.append((idx+1, v))

result =0
a = combinations(ar, 2)
for i in a:
    x, y = i
    if x[1] != y[1]:
        print(x, y)
        result+=1

print(result)
