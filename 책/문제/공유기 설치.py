# 21:20 ~
n, c = map(int, input().split())
a = []
for _ in range(n):
    a.append(int(input()))

visited = [False * n]
a.sort()
min_value = 1e9
c = c - 2
def binary_search(start, end, min_value, c):
    if c == 0:
        return min_value
    if start > end:
        return None
    mid = (start + end) //2
    min_value = a[mid] - a[start]
    c -= 1
    if min(abs(a[mid] - a[mid - 1]), abs(a[mid -1] - a[start])) > min(abs(a[end] - a[mid + 1]), abs(a[mid+1] - a[mid])) :
        return binary_search(start, mid - 1, min_value, c)
    else:
        return binary_search(mid + 1, end, min_value, c)



i = len(a)
print(binary_search(0,i-1, min_value, c))


