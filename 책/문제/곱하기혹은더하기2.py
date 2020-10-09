# 13:55 ~ 14:04 9뷴
n = list(map(int,input()))
print(n)
sum = 0
if n[0] == 0 or n[1] == 0 or n[0] == 1or n[1] == 1:
    sum = n[0] + n[1]
else:
    sum = n[0] * n[1]
for i in range(2, len(n)):
    if i == 0 or i ==1:
        sum = sum + n[i]
    else:
        sum = sum * n[i]

print(sum)





# 02984