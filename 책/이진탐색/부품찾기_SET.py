# 16:15~ #16:
n = 5
arr = [8, 3, 7, 9, 2,8,5]
request = [5, 7, 9]

qwr = '123123123'
print(list(map(str,qwr)))
print(list(map(int,qwr)))
print(set(list(map(int,qwr))))
s = set()

for i in arr:
    s.add(i)

for i in request:
    if i in s:
        print('yes',end=' ')
    else:
        print('no',end=' ')