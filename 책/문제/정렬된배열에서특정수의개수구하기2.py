
def count_by_value(arr, x):
    n = len(arr)
    a = start(arr, x, 0, n)
    if a == None:
        return 0
    b = last(arr, x, 0, n)

    return b - a + 1

def last(arr, target, start, end):
    if start >end:
        return None
    mid = (start + end) // 2
    if (mid == n -1 or target < arr[mid + 1]) and arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return last(arr, target, start, mid -1)
    else:
        return last(arr, target, mid+1, end)

def start(arr, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if (mid == 0 or target > arr[mid -1]) and arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return start(arr, target, start, mid -1)
    else:
        return start(arr, target, mid+1, end)



n, x = map(int, input().split())
arr = list(map(int, input().split()))

count = count_by_value(arr, x)

if count == 0:
    print(-1)
else:
    print(count)