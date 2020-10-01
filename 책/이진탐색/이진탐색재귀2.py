target = 10
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def binary_search(start,end):
    if start > end:
        return None
    mid = (start+end)//2

    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(start, mid-1)
    else:
        return binary_search(mid+1, end)


search = binary_search(0, 9)
if search ==None:
    print('없음')
else:
    print(search+1)