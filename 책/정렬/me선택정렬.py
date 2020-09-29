
l = [7,5,9,0,3,1,6,2,4,8]

for i in range(len(l)):
    min = l[i]
    for k in l[i : len(l)]:
        if min > k:
            min = k
    l.remove(min)
    l.insert(i, min)
print(l)