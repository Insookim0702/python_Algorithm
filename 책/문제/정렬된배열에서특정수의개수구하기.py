# 16:44 ~ 17:25 41분
n, x = map(int, input().split())
a = list(map(int, input().split()))


result = 0
def binary_search(start_idx, end_idx, a):
    global result
    if start_idx >= end_idx:
        return
    mid_idx = (start_idx + end_idx) // 2
    if mid_idx >= len(a):
        return
    if x > a[mid_idx]:
        start_idx = mid_idx + 1
        return binary_search(start_idx, end_idx, a)
    elif x < a[mid_idx]:
        end_idx = mid_idx -1
        return binary_search(start_idx, end_idx, a)
    else:
        a.pop(mid_idx)
        leng = len(a)
        result += 1
        binary_search(0, leng, a)
    return result

result = binary_search(0, len(a), a)
if result == None:
    print(-1)
else:
    print(result)
