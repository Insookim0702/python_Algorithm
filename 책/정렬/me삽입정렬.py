l = [7,5,9,0,3,1,6,2,4,8]

for i in range(1,len(l)):
    for k in range(0,i):
        if l[i] < l[k]:
            l[i],l[k] = l[k],l[i]

print(l)