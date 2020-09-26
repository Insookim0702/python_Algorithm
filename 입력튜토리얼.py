
#n = input()
#list = list(map(int,input().split()))
#print(n)
#list.sort(reverse=False)
#print(list)


#import sys
##data = sys.stdin.readline().rstrip()
#print(data)


result = sum([1,2,3,4])
result = min([1,2,3,4,5])
result = max([1,2,3,4,5,6])
result = eval("(1+4)*8")

i = [4,324,432,2,2,1,23,21,3,23,12]
i.sort(reverse=True)
print(i)
result = sorted([5,23,34,4,23,32,1,43,2,23], reverse= True)
print(result)


result = [('홍길동', 2),('김아무개', 23),('무리수', 12),('무리수', 12),('가자', 123),('라아', 12)]
result.append(('mdm',3))
result = sorted(result, key=lambda x: x[1], reverse=True)
result = sorted(result, key=lambda x: x[0])
print('@@@@@@@',result)

from itertools import permutations
data = ['A','B','C']
result = list(permutations(data,3))
arr = []
m=""
for i in result:
    for k in i:
        m+=k
    arr.append(m)
    m ="";
print('arr : ', arr)

print(result)


import math
print(math.factorial(5))

from collections import deque, Counter

data = deque([3,4,5])
data.append(6)
data.appendleft(2)
data.appendleft(1)
print(list(data))

data = Counter(['blue','red','blue'])

print(data['red'])



