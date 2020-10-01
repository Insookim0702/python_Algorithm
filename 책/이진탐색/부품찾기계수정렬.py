# 16:10~ #16:15
n = 5
arr = [8, 3, 7, 9, 2]
request = [5, 7, 9]

array = [0] * 1000000

for i in arr:
    array[int(i)] = 1

for i in request:
    if array[i] == 1:
        print('yes', end=' ')
    else:
        print('no', end=' ')
