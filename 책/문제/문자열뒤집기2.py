# 14:07 ~ 14:17

n = list(map(int,input()))

gr_1 = 0
gr_0 = 0
v = n[0]
if v == 0:
    gr_0 += 1
else:
    gr_1 += 1
for i in range(1, len(n)):
    if v != n[i]:
        if n[i] == 0:
            gr_0 += 1
            v = 0
        else:
            gr_1 += 1
            v = 1

print(min(gr_0,gr_1))