
n = input()
num = list(map(int, input().split()))
cal = list(map(int, input().split()))
calulator = []
for _ in range(cal[0]):
    calulator.append('+')
for _ in range(cal[1]):
    calulator.append('-')
for _ in range(cal[2]):
    calulator.append('*')
for _ in range(cal[3]):
    calulator.append('//')

print(n)
print(num)
print(calulator)
from itertools import permutations

perm = permutations(calulator)
max_answer = 0
min_answer = 0

for i in perm:
    k = []
    for n in num:
        k.append(n)
    sum = k.pop(0)
    for j in i:
        v = k.pop(0)
        if j == '//' and sum  < 0 and v > 0 :
            sum = sum * -1
            sum = eval(str(sum) + j + str(v))
            sum = sum * -1
        else:
            sum = eval(str(sum) + j + str(v))

    max_answer = max(max_answer, sum)

    min_answer = min(min_answer, sum)
    if min_answer == 0:
        min_answer = sum

print(max_answer)
print(min_answer)

