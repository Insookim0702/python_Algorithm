# 14:20 ~
n = int(input())

a = list(map(int, input().split()))
a.sort()

target = 1
for i in a:
    if target < i:
        break
    target += i


print(target)

