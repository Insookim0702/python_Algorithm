n = list(map(int, input()))
g0 = 0
g1 = 0

for i in range(1, len(n)):
    if n[i-1] != n[i]:
        if n[i] == 1:
            g0 +=1
        else:
            g1 +=1


if n[-1] == 0:
    g0+=1
else:
    g1+=1


print(min(g0,g1))