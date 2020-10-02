arr = ['hanneul','jonggu','Dongbin','taeil','sangwook']

def sequential_search(n, target, arr):
    for i in range(n):
        if arr[i] == target:
            return i



n = 5
target = 'Dongbin'
print(sequential_search(n, target, arr))