
n = int(input())

a = []
for _ in range(n):
    a.append(list(input().split()))


a.sort(key = lambda x : (-int(x[1]), x[2],-int(x[3]),x[0]))

for i in a:
    print(i[0])