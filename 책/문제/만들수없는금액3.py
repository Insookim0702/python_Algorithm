n = int(input())
arr = list(map(int, input().split()))

arr.sort()
target = 1
for i in arr:
    if target < i: break
    target+=i


print(target)
