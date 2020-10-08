# 21:00 ~ 21:19

n = int(input())

a = list(map(int, input().split()))

def binary_search(start, end):
    if start > end:
        return None
    if a[start] < 0:
        return binary_search(start+1, end)
    mid = (start + end) //2
    if a[mid] == mid:
        return mid
    elif a[mid] < mid:
        return binary_search(mid +1, end)
    else:
        return binary_search(start, mid -1)

l = len(a)
print(binary_search(0,l))
