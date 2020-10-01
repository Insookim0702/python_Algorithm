# 16:00~ #16:07
n = 5
arr = [8, 3, 7, 9, 2]
request = [5, 7, 9]


def binary_search(start, end, target):
    while start <= end:
        mid = (start + end) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None
arr.sort()
request.sort()
for i in request:
    search = binary_search(0, len(arr)-1, i)
    if search == None:
        print('no', end=' ')
    else:
        print('yes', end=' ')