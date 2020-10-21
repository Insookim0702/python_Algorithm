n = int(input())
arr = list(map(int, input().split()))
arr.sort()
group_count = 0;
result = 0;
for i in range(n):
    group_count += 1
    if group_count == arr[i]:
        group_count = 0
        result += 1
print(result)
