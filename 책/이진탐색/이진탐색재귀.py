arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 4
def binary_search(start, end):
    if start > end:
        return None
    middle = (start + end) // 2
    if target == arr[middle]:
        return middle
    elif arr[middle] > target:
        return binary_search(start, middle-1)
    else:
        return binary_search(middle + 1, end)


search = binary_search(0, len(arr) - 1)
if search == None:
    print('없음')
else:
    print(search+1)


def binary_search(arr, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr, target, start, mid - 1)
    else:
        return binary_search(arr, target, mid + 1, end)


n, target = 10, 4
result = binary_search(arr, target, 0, 9)

if result == None:
    print("원소가 존재하지 않음")
else:
    print(result + 1)
