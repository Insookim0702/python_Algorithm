# 16:06 ~

n = list(input())

print(n)
a = []
b = 0
for i in n:
    if i.isalpha():
        a.append(i)
    else:
        b += int(i)

a.sort()

print(''.join(a) + str(b))



