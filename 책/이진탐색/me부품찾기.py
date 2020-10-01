# 15:53~ #16:00
n = 5
arr = [8, 3, 7, 9, 2]
request = [5, 7, 9]

def binary_search(start, end, target):
    if start > end:
        return None
    mid = (start + end) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(start, mid - 1, target)
    else:
        return binary_search(mid + 1, end, target)
request.sort()
arr.sort()
for target in request:
    search = binary_search(0, len(arr) - 1, target)
    if search == None:
        print('no', end=' ')
    else:
        print('yes', end=' ')
