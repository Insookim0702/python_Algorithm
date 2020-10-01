target = 10
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
start = 0
end = len(arr) - 1
def binary_search(start, end):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None


search = binary_search(start, end)
if search ==None:
    print('없음')
else:
    print(search+1)
