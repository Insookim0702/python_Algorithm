import math

def is_prim_num(n):
    arr = [True for _ in range(n+1)]
    print(arr)
    for i in range(2, n+1):
        if arr[i]:
            j = 2
            while i*j <=n:
                arr[i*j] = False
                j+=1

    for i in range(2, n+1):
        if arr[i]:
            print(i, end=' ')


print(is_prim_num(100))