arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 4


def binary_search(start, end):
    while start <= end:
        mid = (start + end) //2

        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            end = mid -1
        else:
            start = mid +1
    return None

search = binary_search(0, len(arr)-1)
if search == None:
    print('없음')
else:
    print(search)
