arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 4


def binary_search(start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if arr[mid] == target:
        return mid

    elif arr[mid] > target:
        end = mid - 1
        return binary_search(start, end)
    else:
        start = mid + 1
        return binary_search(start, end)


search = binary_search(0, len(arr))

if search == None:
    print('없음')
else:
    print(search)
