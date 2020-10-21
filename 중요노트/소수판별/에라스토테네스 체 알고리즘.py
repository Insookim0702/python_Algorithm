# 시간복잡도 O(NloglogN)

import math

n = 1000
# 모든 원소가 소수인 것으로 True 초기화
a = [True for _ in range(n+1)]
#에라토스테네스 체 알고리즘 수행
for i in range(2, int(math.sqrt(n))+1):
    if a[i] == True:
        j = 2
        while i * j <= n:
            a[i * j] = False
            j += 1
for i in range(1, n+1):
    if a[i] == True:
        print(i, end=' ')






