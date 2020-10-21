n = list(map(int, input()))
sum = 0
for i in n:
    if i == 0 or i == 1 or sum ==0:
        sum +=i
    else:
        sum *= i


print(sum)